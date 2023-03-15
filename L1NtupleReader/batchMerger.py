# from L1Calibrator.NNModelTraining_FullyCustom_GPUdistributed_batchedRate import Fgrad
from sklearn.model_selection import train_test_split
from optparse import OptionParser
from TowerGeometry import *
import tensorflow as tf
import pandas as pd
import numpy as np
import zipfile
import pickle
import glob
import os

# split list l in sublists of length n each
def splitInBlocks (l, n):
    r = len(l) % n

    i = 0
    blocks = []
    while i < len(l):
        if len(blocks)<r:
            blocks.append(l[i:i+n+1])
            i += n+1
        else:
            blocks.append(l[i:i+n])
            i += n

    return blocks

# convert training sample to have correct shape and order of tensor entries
def convert_train_samples(X, Y, version):
    # Y vector columns: jetPt, jetEta, jetPhi, trainingPt
    # keep only the trainingPt
    Y = Y[:,3]

    # X vector columns: iem, ihad, iesum, ieta
    if version == 'ECAL':
        X = np.delete(X, 2, axis=2) # delete iesum column (always start deleting from right columns)
        X[:,:,[0,1]] = X[:,:,[1,0]] # order iem and ihad to have iem on the right

    elif version == 'HCAL' or version == 'HF':
        X = np.delete(X, 2, axis=2) # delete iesum column (always start deleting from right columns)
        
    return X, Y

# convert rate sample to have correct shape and order of tensor entries
def convert_rate_samples(Z, version):
    # Z vector columns: iem, ihad, iesum, ieta
    if version == 'ECAL':
        Z = np.delete(Z, 2, axis=2) # delete iesum column (always start deleting from right columns)
        Z = Z[ Z[:,:,0] >= 29 ] # remove TTs that have iEM<=29 : 29 = (50-(50*0.12))/1.5 = (egThr-(egThr*hoeThrEB))/bigSF [this already reshapes so that every TT becomes an event]
        Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have iem on the right

    elif version == 'HCAL' or version == 'HF':
        Z = Z[ np.sum(Z[:,:,2], axis=1) >= 50 ] # remove JETs that have E<=50 : 50 ~ (100/n)/1.66*n = (jetThr/nActiveTT)/bigSF*nActiveTT
        Z = np.delete(Z, 2, axis=2) # delete iesum column (always start deleting from right columns)

    return Z

# application of ECAL calibration ot the HCAL rate proxy samples
def applyECALcalib(Z, TTP):
    xDim = Z.shape[0] ; yDim = 81 ; zDim = 42
    Z = Z.reshape(xDim*yDim, zDim) # reshape so that every TT becomes an event
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    TT_em_pred = TTP.predict(Z[:,1:], batch_size=2048)
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    Z[:,[0]] = TT_em_pred
    Z = Z.reshape(xDim, yDim, zDim) # reshape so that 81xTT becomes an event again
    return Z

# application of HCAL calibration ot the HCAL rate proxy samples
def applyHCALcalib(Z, TTP):
    xDim = Z.shape[0] ; yDim = 81 ; zDim = 42
    Z = Z.reshape(xDim*yDim, zDim) # reshape so that every TT becomes an event
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    TT_had_pred = TTP.predict(Z[:,1:], batch_size=2048)
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    Z[:,[0]] = TT_had_pred
    Z = Z.reshape(xDim, yDim, zDim) # reshape so that 81xTT becomes an event again
    return Z

# tf.train.example serialization function to store in TFRecord
def serialize_example(x, y):
    # create feature dictionary
    feature = {
      'chuncky_donut': tf.train.Feature(bytes_list=tf.train.BytesList(value=[tf.io.serialize_tensor(x).numpy()])),
      'trainingPt'   : tf.train.Feature(float_list=tf.train.FloatList(value=[y]))
    }

    # create example protocol buffer
    example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
    return example_proto.SerializeToString()

# dataset serialization function to store in TFRecord
def tf_serialize_example(x, y):
    tf_string = tf.py_function( serialize_example, (x, y), tf.string )
    return tf.reshape(tf_string, ()) # The result is a scalar.

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

if __name__ == "__main__" :

    # read the batched input tensors to the NN and merge them
    parser = OptionParser()
    parser.add_option("--indir",                  dest="indir",                  default=None,                         help="Base-folder with files to be merged")
    parser.add_option("--batchdir",               dest="batchdir",               default=None,                         help="Sub-folder with npz files to be merged")
    parser.add_option("--ratedir",                dest="ratedir",                default=None,                         help="Sub-folder with npz files for the rate")
    parser.add_option("--odir",                   dest="odir",                   default=None,                         help="Output tag of the output folder")
    parser.add_option("--v",                      dest="v",                      default=None,                         help="Ntuple type (ECAL, HCAL, or HF)")
    parser.add_option("--rate_only",              dest="rate_only",              default=False,   action='store_true', help="Make only rate datasets")
    parser.add_option("--filesLim",               dest="filesLim",               default=1000000, type=int,            help="Maximum number of npz files to use")
    parser.add_option("--filesPerRecord",         dest="filesPerRecord",         default=500,     type=int,            help="Maximum number of npz files per TFRecord")
    parser.add_option("--validation_split",       dest="validation_split",       default=0.20,    type=float,          help="Fraction of events to be used for testing")
    parser.add_option("--flattenEtaDistribution", dest="flattenEtaDistribution", default=False,   action='store_true', help="Flatten eta distribution")
    parser.add_option("--ECALcalib4rate",         dest="ECALcalib4rate",         default=None,                         help="Model for ECAL calibration in HCAL rate proxy dataset ('/data_CMS/cms/motta/CaloL1calibraton/'+options.ECALcalib4rate+'/model_ECAL/TTP')")
    parser.add_option("--HCALcalib4rate",         dest="HCALcalib4rate",         default=None,                         help="Model for HCAL calibration in ECAL rate proxy dataset ('/data_CMS/cms/motta/CaloL1calibraton/'+options.HCALcalib4rate+'/model_HCAL/TTP')")
    (options, args) = parser.parse_args()
    print(options)

    filedir = '/data_CMS/cms/motta/CaloL1calibraton/'+options.indir
    training_folder = filedir + '/{0}training{1}'.format(options.v, options.odir)
    os.system('mkdir -p ' + training_folder + '/trainTFRecords/')
    os.system('mkdir -p ' + training_folder + '/testTFRecords/')
    os.system('mkdir -p ' + training_folder + '/rateTFRecords/')

    if not options.rate_only:
        # read inputs and split them in blocks
        InFilesTrain = glob.glob(filedir+'/'+options.batchdir+'/tensors/towers_*.npz')[:options.filesLim]
        InFilesTrainBlocks = splitInBlocks(InFilesTrain, options.filesPerRecord)

    InFilesRate = glob.glob(filedir+'/'+options.ratedir+'/tensors/towers_*.npz')[:options.filesLim]
    InFilesRateBlocks = splitInBlocks(InFilesRate, options.filesPerRecord)

    with tf.device('/CPU:0'):
        if not options.rate_only:
            print('********************************************')
            print('********************************************')
            print('CREATING TRAIN/TEST TFRecords')

            print('\nUsing', len(InFilesTrain), 'files batched in', len(InFilesTrainBlocks), 'blocks\n')

            train_total_dimension = 0

            # for each block create a TFRecordDataset
            for blockIdx, block in enumerate(InFilesTrainBlocks):
                print('--------------------------------------')
                print('reading block', blockIdx)
                XsToConcatenate = []
                YsToConcatenate = []

                for fileIdx, file in enumerate(block):
                    if not fileIdx%10: print('    reading batch', fileIdx)
                    try:
                        filex = np.load(file, allow_pickle=True)['arr_0']
                        filey = np.load(file.replace('towers_', 'jets_'), allow_pickle=True)['arr_0']

                    except FileNotFoundError:
                        # DEBUG
                        print('** INFO: file idx '+str(fileIdx)+' not found --> skipping')
                        continue

                    except pickle.UnpicklingError:
                        # DEBUG
                        print('** INFO: file idx '+str(fileIdx)+' unpickling error --> skipping')
                        continue

                    except zipfile.BadZipFile:
                        # DEBUG
                        print('** INFO: file idx '+str(fileIdx)+' unzipping error --> skipping')
                        continue

                    except OSError:
                        # DEBUG
                        print('** INFO: file idx '+str(fileIdx)+' Failed to interpret file as a pickle --> skipping')
                        continue

                    if filex.shape[1:] != (81,43) or filey.shape[1:] != (4,):
                        # DEBUG
                        print('** INFO: file idx '+str(fileIdx)+' corrupted --> skipping')
                        continue

                    XsToConcatenate.append(filex)
                    YsToConcatenate.append(filey)

                X = np.concatenate(XsToConcatenate)
                Y = np.concatenate(YsToConcatenate)
                del XsToConcatenate, YsToConcatenate

                # store eta of the targets to compute sample weights
                Ynrg = Y[:,0]
                Yeta = Y[:,1]

                # pre-process to have correct shape and entires
                X, Y = convert_train_samples(X, Y, options.v)

                # clean from the events that are completely outside of a 'regular' resposne
                uncalibResp = Y / np.sum(X[:,:,1], axis=1)
                selection = (uncalibResp < 3) & (uncalibResp > 0.3)
                X = X[selection]
                Y = Y[selection]
                # apply the same selection aslo to the energy and eta vectors for weight computation
                Ynrg = Ynrg[selection]
                Yeta = Yeta[selection]
                del uncalibResp, selection

                # start implementing sample weights
                if False:
                    # compute weights to balance pT distribution
                    dfweights = pd.DataFrame(columns=['E'])
                    dfweights['E']  = Ynrg
                    total_jets = len(Ynrg)

                    # compress in ieta and pt binning
                    iEbins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 2000] ; labelsE = np.arange(1, len(iEbins), 1)
                    dfweights['compressedIE'] = pd.cut(dfweights['E'], bins=iEbins, labels=labelsE)
                    del dfweights['E']

                    # compute weights
                    dfweights['weight'] = total_jets / dfweights.groupby(['compressedIE'])['compressedIE'].transform('count')

                    import matplotlib.pyplot as plt
                    plt.hist(dfweights['weight'])#, bins=np.linspace(-5.191,5.191,200))
                    plt.yscale('log')
                    plt.savefig('./test.pdf')
                    plt.close()

                    import matplotlib.pyplot as plt
                    plt.hist(Ynrg, bins=iEbins)#, bins=np.linspace(-5.191,5.191,200))
                    # plt.yscale('log')
                    plt.xlim(0,250)
                    plt.savefig('./test0.pdf')
                    plt.close()

                    import matplotlib.pyplot as plt
                    plt.hist(Ynrg, weights=dfweights['weight'], bins=iEbins)#, bins=np.linspace(-5.191,5.191,200))
                    # plt.yscale('log')
                    plt.xlim(0,250)
                    plt.savefig('./test1.pdf')
                    plt.close()

                    import matplotlib.pyplot as plt
                    plt.hist(Yeta, weights=dfweights['weight'], bins=np.linspace(-3,3,60))#, bins=np.linspace(-5.191,5.191,200))
                    # plt.yscale('log')
                    plt.savefig('./test2.pdf')
                    plt.close()

                # # select the region for the objects
                # if options.v == 'ECAL': regSel = Y[:,1] < 2.9
                # if options.v == 'HCAL': regSel = Y[:,1] < 2.9
                # if options.v == 'HF':   regSel = Y[:,1] > 3.1
                # X = X[regSel]
                # Y = Y[regSel]

                ## DEBUG
                print('    block dimensions', len(X))
                print('    block dimensions', len(Y))

                # split train and testing
                x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=options.validation_split, random_state=7)
                del X, Y

                # update total dimension
                train_total_dimension += len(y_train)

                # make tensorflow datasets
                Xtrain = tf.convert_to_tensor(x_train, dtype=tf.float32)
                Ytrain = tf.convert_to_tensor(y_train, dtype=tf.float32)
                del  x_train, y_train
                train_dataset = tf.data.Dataset.from_tensor_slices((Xtrain, Ytrain))
                del Xtrain, Ytrain

                Xtest  = tf.convert_to_tensor(x_test, dtype=tf.float32)
                Ytest  = tf.convert_to_tensor(y_test, dtype=tf.float32)
                del x_test, y_test
                test_dataset  = tf.data.Dataset.from_tensor_slices((Xtest, Ytest))
                del Xtest, Ytest

                # serialize the datasets
                serialized_train_dataset = train_dataset.map(tf_serialize_example)
                serialized_test_dataset  = test_dataset.map(tf_serialize_example)
                del train_dataset, test_dataset

                # store TFRecords
                train_filename = training_folder+'/trainTFRecords/record_'+str(blockIdx)+'.tfrecord'
                train_writer = tf.data.experimental.TFRecordWriter(train_filename)
                train_writer.write(serialized_train_dataset)
                del serialized_train_dataset

                test_filename  = training_folder+'/testTFRecords/record_'+str(blockIdx)+'.tfrecord'
                test_writer = tf.data.experimental.TFRecordWriter(test_filename)
                test_writer.write(serialized_test_dataset)
                del serialized_test_dataset

            print('training sample total domension =', train_total_dimension)

        print('********************************************')
        print('********************************************')
        print('CREATING RATE TFRecords')

        print('\nUsing', len(InFilesRate), 'files batched in', len(InFilesRateBlocks), 'blocks\n')

        rate_dimensions = []

        # for each block create a TFRecordDataset
        for blockIdx, block in enumerate(InFilesRateBlocks):
            print('--------------------------------------')
            print('reading block', blockIdx)
            ZsToConcatenate = []

            for fileIdx, file in enumerate(block):
                if not fileIdx%10: print('    reading batch', fileIdx)
                try:
                    filex = np.load(file, allow_pickle=True)['arr_0']

                except FileNotFoundError:
                    # DEBUG
                    print('** INFO: file idx '+str(fileIdx)+' not found --> skipping')
                    continue

                except pickle.UnpicklingError:
                    # DEBUG
                    print('** INFO: file idx '+str(fileIdx)+' unpickling error --> skipping')
                    continue

                except zipfile.BadZipFile:
                    # DEBUG
                    print('** INFO: file idx '+str(fileIdx)+' unzipping error --> skipping')
                    continue

                except OSError:
                    # DEBUG
                    print('** INFO: file idx '+str(fileIdx)+' Failed to interpret file as a pickle --> skipping')
                    continue

                if filex.shape[1:] != (81,43):
                    # DEBUG
                    print('** INFO: file idx '+str(fileIdx)+' corrupted --> skipping')
                    continue

                ZsToConcatenate.append(filex)

            Z = np.concatenate(ZsToConcatenate)
            del ZsToConcatenate

            # pre-process to have correct shape and entires
            Z = convert_rate_samples(Z, options.v)
            _ = np.zeros(len(Z))

            if options.ECALcalib4rate and options.v == 'HCAL':
                ECAL_TTPmodel = keras.models.load_model('/data_CMS/cms/motta/CaloL1calibraton/'+options.ECALcalib4rate+'/model_ECAL/TTP', compile=False, custom_objects={'Fgrad': Fgrad})
                Z = applyECALcalib(Z, ECAL_TTPmodel)
                del ECAL_TTPmodel

            if options.HCALcalib4rate and options.v == 'ECAL':
                HCAL_TTPmodel = keras.models.load_model('/data_CMS/cms/motta/CaloL1calibraton/'+options.HCALcalib4rate+'/model_HCAL/TTP', compile=False, custom_objects={'Fgrad': Fgrad})
                Z = applyHCALcalib(Z, HCAL_TTPmodel)
                del HCAL_TTPmodel

            ## DEBUG
            rate_dimensions.append(len(Z))
            print('    block dimensions', len(Z))

            # make tensorflow datasets
            Z = tf.convert_to_tensor(Z, dtype=tf.float32)
            _ = tf.convert_to_tensor(_, dtype=tf.float32)
            rate_dataset = tf.data.Dataset.from_tensor_slices((Z, _))
            del Z, _

            # serialize the datasets
            serialized_rate_dataset = rate_dataset.map(tf_serialize_example)
            del rate_dataset

            # store TFRecords
            rate_filename = training_folder+'/rateTFRecords/record_'+str(blockIdx)+'.tfrecord'
            rate_writer = tf.data.experimental.TFRecordWriter(rate_filename)
            rate_writer.write(serialized_rate_dataset)
            del serialized_rate_dataset

            # directly break as soon as the dimension is met
            if np.sum(rate_dimensions) > train_total_dimension: break

        rate_total_dimension = np.sum(rate_dimensions)

        if not options.rate_only:
            # generally the rate datasets are smaller than the raining datasets therefore we need to 
            # copy the rate TFRecords to have their final dimenion equal to the train sample
            repeatIdx = 0
            records = glob.glob(training_folder+'/rateTFRecords/record_*.tfrecord')
            print('--------------------------------------------')
            while rate_total_dimension < train_total_dimension:
                repeatIdx += 1
                print('Copying rate datasets '+str(repeatIdx)+'th time')
                for record, recordDim in zip(records, rate_dimensions):
                    recordCopy = record.replace('.tfrecord', '_'+str(repeatIdx)+'.tfrecord')
                    os.system('cp '+record+' '+recordCopy)

                    rate_total_dimension += recordDim
                    # directly break as soon as the dimension is met
                    if rate_total_dimension > train_total_dimension: break

        print('rate sample total domension =', rate_total_dimension)

