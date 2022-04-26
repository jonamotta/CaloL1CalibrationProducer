from sklearn.model_selection import train_test_split
from itertools import chain
from TowerGeometry import *
import pandas as pd
import numpy as np
import argparse
import glob
import sys
import csv
import os

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 batchMerger.py --dir /data_CMS/cms/motta/CaloL1calibraton/2022_04_21_NtuplesV2 --sample train --v (ECAL or HCAL) (--jetcut 60)

if __name__ == "__main__" :

    # read the batched input tensors to the NN and merge them
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--v",        dest="v",       help="Ntuple type ('ECAL' or 'HCAL')",      default='ECAL')
    parser.add_option("--jetcut",   dest="jetcut",  help="JetPt cut in GeV",                    default=None)
    parser.add_option("--dir",      dest="dir",     help="Folder with npz files to be merged",  default='')
    parser.add_option("--sample",   dest="sample",  help="Type of sample (train or test",       default='')
    (options, args) = parser.parse_args()
    print(options)

    indir = options.dir
    if options.v == 'ECAL':
        taglists = [open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_gamma0-200.txt')]
        taglists.append(open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_gamma200-500.txt'))

        tensors_dir = [indir + '/hdf5dataframes_gamma0-200_batches/paddedAndReadyToMerge/tensors/']
        tensors_dir.append(indir + '/hdf5dataframes_gamma200-500_batches/paddedAndReadyToMerge/tensors/')

        dataframe_dir = [indir + '/hdf5dataframes_gamma0-200_batches/paddedAndReadyToMerge/dataframes/']
        dataframe_dir.append(indir + '/hdf5dataframes_gamma200-500_batches/paddedAndReadyToMerge/dataframes/')

    elif options.v == 'HCAL':
        taglists = [open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU.txt')]
        tensors_dir = [indir + '/hdf5dataframes_qcdNoPU_batches/paddedAndReadyToMerge/tensors/']
        dataframe_dir = [indir + '/hdf5dataframes_qcdNoPU_batches/paddedAndReadyToMerge/dataframes/']
    
    # dummy arrays filled with zeros
    X = np.array([[np.zeros(43) for i in range(81)]])
    Y = np.array([[0,0]])

    # define the two paths where to read the hdf5 files

    training_folder = indir + '/{}training'.format(options.v)
    os.system('mkdir -p ' + training_folder)
    os.system('mkdir -p ' + training_folder + '/dataframes')
    # define the paths where to save the hdf5 files
    saveto = {
        'X'  : training_folder+'/dataframes/X.hdf5',
        'Y'  : training_folder+'/dataframes/Y.hdf5',
    }

    dfX = pd.DataFrame()
    dfY = pd.DataFrame()

    # [FIXME] this will need to be changed in the taglist, splitting training and testing tags
    if options.sample == 'train':
        tags_range = [0,500]
    elif options.sample == 'test':
        tags_range = [501,1000]

    i_samples = 0
    for i_fold, taglist in enumerate(taglists):
        # concatenate low energy photons
        for idx,tag in enumerate(taglist):
            if idx not in range(tags_range[0],tags_range[1]):
                continue
            if not idx%10: print('reading batch', idx)
            tag = tag.strip()
            try:
                X = np.concatenate([X,np.load(tensors_dir[i_fold]+'/towers'+tag+'.npz')['arr_0']])
                Y = np.concatenate([Y,np.load(tensors_dir[i_fold]+'/jets'+tag+'.npz')['arr_0']])

                # read hdf5 files
                readT = pd.HDFStore(dataframe_dir[i_fold]+'towers'+tag+'.hdf5', mode='r')
                dfET = readT['towers']
                readT.close()

                readJ = pd.HDFStore(dataframe_dir[i_fold]+'jets'+tag+'.hdf5', mode='r')
                dfEJ = readJ['jets']
                readJ.close()

                dfX.append(dfET)
                dfY.append(dfEJ)

            except FileNotFoundError:
                print('** INFO: towers'+tag+' not found --> skipping')
                continue
            i_samples = i_samples + 1
            if i_samples == 100: break # break at the 30th file to speed up the process
        
        ## DEBUG
        print(len(X))
        print(len(Y))

    # remove the dummy array filled with zeros
    X = X[1:]
    Y = Y[1:]

    ## DEBUG
    print(len(X))
    print(len(Y))

    # We will produce one sample fot training and one for testing from different ntuples
    np.savez_compressed(training_folder+'/X_'+options.sample+'.npz', X)
    np.savez_compressed(training_folder+'/Y_'+options.sample+'.npz', Y)

    print("Saved data samples in folder: {}".format(training_folder))    

    '''
    # split train and testing datasets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

    print('Length of training sample = {}'.format(len(Y_train)))

    # Apply cut on the jetPt of the training sample
    if options.jetcut:
        X_train_cut = []
        Y_train_cut = []
        for i in range(len(Y_train)):
            if Y_train[i][0] < float(options.jetcut):
                X_train_cut.append(X_train[i])
                Y_train_cut.append(Y_train[i])
        X_train = X_train_cut
        Y_train = Y_train_cut
        print('Length of training sample for jetPt < {} GeV = {}'.format(options.jetcut, len(Y_train)))

    # save them
    np.savez_compressed(training_folder+'/X_train.npz', X_train)
    np.savez_compressed(training_folder+'/X_test.npz', X_test)
    np.savez_compressed(training_folder+'/Y_train.npz', Y_train)
    np.savez_compressed(training_folder+'/Y_test.npz', Y_test)

    print("Saved data samples in folder: {}".format(training_folder))
    '''

    # save hdf5 files with dataframe formatted datasets
    storeT = pd.HDFStore(saveto['X'], mode='w')
    storeT['X'] = dfX
    storeT.close()

    storeJ = pd.HDFStore(saveto['Y'], mode='w')
    storeJ['Y'] = dfY
    storeJ.close()
