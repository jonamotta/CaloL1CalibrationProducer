from optparse import OptionParser
from TowerGeometry import *
import pandas as pd
import numpy as np
import zipfile
import pickle
import os

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 batchMerger.py --indir 2022_04_21_NtuplesV2 --sample train --v (ECAL or HCAL) 

if __name__ == "__main__" :

    # read the batched input tensors to the NN and merge them
    parser = OptionParser()
    parser.add_option("--indir",                  dest="indir",                  help="Folder with npz files to be merged",            default='')
    parser.add_option("--batchdir",               dest="batchdir",                                                                     default='')
    parser.add_option("--odir",                   dest="odir",                                                                         default='')
    parser.add_option("--v",                      dest="v",                      help="Ntuple type (ECAL, HCAL, or HF)",               default='ECAL')
    parser.add_option("--jetcut",                 dest="jetcut",                 help="JetPt cut in GeV",                              default=None)
    parser.add_option("--sample",                 dest="sample",                 help="Type of sample (train or test)",                default='')
    parser.add_option("--noY",                    dest="noY",                    help="Avoid saving Y",           action='store_true', default=False)
    parser.add_option("--filesLim",               dest="filesLim",               type=int,                                             default=100000)
    parser.add_option("--flattenEtaDistribution", dest="flattenEtaDistribution", help="Flatten eta distribution", action='store_true', default=False)
    (options, args) = parser.parse_args()
    print(options)

    filedir = '/data_CMS/cms/motta/CaloL1calibraton/'+options.indir

    InFiles = glob.glob(filedir+'/'+options.batchdir+'/tensors/towers_*.npz')
    InFiles.sort()

    XsToConcatenate = []
    YsToConcatenate = []

    training_folder = filedir + '/{0}training{1}'.format(options.v, options.odir)
    os.system('mkdir -p ' + training_folder)

    for idx,file in enumerate(InFiles):
        if not idx%10: print('reading batch', idx)
        try:
            # DEBUG
            # print(tag)
            # print(np.load(file, allow_pickle=True)['arr_0'])
            # exit()

            filex = np.load(file, allow_pickle=True)['arr_0']
            filey = np.load(file.replace('towers_', 'jets_'), allow_pickle=True)['arr_0']

        except FileNotFoundError:
            # DEBUG
            print('** INFO: file idx '+str(idx)+' not found --> skipping')
            continue

        except pickle.UnpicklingError:
            # DEBUG
            print('** INFO: file idx '+str(idx)+' unpickling error --> skipping')
            continue

        except zipfile.BadZipFile:
            # DEBUG
            print('** INFO: file idx '+str(idx)+' unzipping error --> skipping')
            continue

        except OSError:
            # DEBUG
            print('** INFO: file idx '+str(idx)+' Failed to interpret file as a pickle --> skipping')
            continue

        if filex.shape[1:] != (81,43) or filey.shape[1:] != (4,):
            # DEBUG
            print('** INFO: file idx '+str(idx)+' corrupted --> skipping')
            continue

        XsToConcatenate.append(filex)
        YsToConcatenate.append(filey)

        if idx == options.filesLim: break # break at the n-th file to speed up the process

    X = np.concatenate(XsToConcatenate)
    Y = np.concatenate(YsToConcatenate)

    if options.flattenEtaDistribution:
        # compute selection to flatten eta distribution
        print('applying flat eta selection')
        FindIeta_vctd = np.vectorize(FindIeta)
        dfIeta = pd.DataFrame(FindIeta_vctd(Y[:,1]), columns=['iEta'])
        nToSave = int(np.mean(dfIeta[abs(dfIeta['iEta'])<=15].groupby('iEta')['iEta'].count()))
        dfIeta['frac'] = nToSave / dfIeta.groupby('iEta')['iEta'].transform('count')
        dfIeta['random'] = np.random.uniform(0.0, 1.0, size=dfIeta.shape[0])
        flatEtaSelection = (dfIeta['random'] <= dfIeta['frac']).to_list()

        X = X[flatEtaSelection]
        Y = Y[flatEtaSelection]

    import matplotlib.pyplot as plt
    plt.hist(Y[:,1], bins=np.linspace(-5.191,5.191,200))
    plt.yscale('log')
    plt.savefig('./test.pdf')
    plt.close()

    # # select the region for the objects
    # if options.v == 'ECAL': regSel = Y[:,1] < 2.9
    # if options.v == 'HCAL': regSel = Y[:,1] < 2.9
    # if options.v == 'HF':   regSel = Y[:,1] > 3.1
    # X = X[regSel]
    # Y = Y[regSel]

    ## DEBUG
    print(len(X))
    print(len(Y))

    # We will produce one sample fot training and one for testing from different ntuples
    np.savez_compressed(training_folder+'/X_'+options.sample+'.npz', X)
    if not options.noY: np.savez_compressed(training_folder+'/Y_'+options.sample+'.npz', Y)

    print("Saved data samples in folder: {}".format(training_folder))    
