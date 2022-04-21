from sklearn.model_selection import train_test_split
from itertools import chain
from TowerGeometry import *
import pandas as pd
import numpy as np
import argparse
import uproot3
import glob
import sys
import csv
import os

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 batchMerger.py --v (ECAL or HCAL)

if __name__ == "__main__" :

    # read the batched input tensors to the NN and merge them
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--v",    dest="v",   help="Ntuple type ('ECAL' or 'HCAL')", default='ECAL')
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0'
    taglist1 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_gamma0-200.txt')
    taglist2 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_gamma200-500.txt')
    
    # dummy arrays filled with zeros
    X = np.array([[np.zeros(41) for i in range(81)]])
    Y = np.array([[0]])

    # define the two paths where to read the hdf5 files
    readfrom = {
        'towers'  : indir+'/hdf5dataframes_gamma{}_batches/paddedAndReadyToMerge/dataframes/towers',
        'jets'    : indir+'/hdf5dataframes_gamma{}_batches/paddedAndReadyToMerge/dataframes/jets'
    }

    training_folder = indir + '/{}training'.format(options.v)     
    os.system('mkdir -p ' + training_folder)
    # define the paths where to save the hdf5 files
    saveto = {
        'X'  : training_folder+'/dataframes/X.hdf5',
        'Y'  : training_folder+'/dataframes/Y.hdf5',
    }

    dfX = pd.DataFrame()
    dfY = pd.DataFrame()

    # concatenate low energy photons
    for idx,tag in enumerate(taglist1):
        if not idx%10: print('reading batch', idx)
        tag = tag.strip()
        try:
            X = np.concatenate([X,np.load(indir+'/hdf5dataframes_gamma0-200_batches/paddedAndReadyToMerge/tensors/towers'+tag+'.npz')['arr_0']])
            Y = np.concatenate([Y,np.load(indir+'/hdf5dataframes_gamma0-200_batches/paddedAndReadyToMerge/tensors/jets'+tag+'.npz')['arr_0']])

            # read hdf5 files
            readT = pd.HDFStore(readfrom['towers'].format('0-200')+tag+'.hdf5', mode='r')
            dfET = readT['towers']
            readT.close()

            readJ = pd.HDFStore(readfrom['jets'].format('0-200')+tag+'.hdf5', mode='r')
            dfEJ = readJ['jets']
            readJ.close()

            dfX.append(dfET)
            dfY.append(dfEJ)

        except FileNotFoundError:
            print('** INFO: towers'+tag+' not found --> skipping')
            continue
        if idx == 30: break # break at the 30th file to speed up the process
    
    ## DEBUG
    print(len(X))
    print(len(Y))

    # concatenate high energy photons
    for idx,tag in enumerate(taglist2):
        if not idx%10: print('reading batch', idx)
        tag = tag.strip()
        try:
            X = np.concatenate([X,np.load(indir+'/hdf5dataframes_gamma200-500_batches/paddedAndReadyToMerge/tensors/towers'+tag+'.npz')['arr_0']])
            Y = np.concatenate([Y,np.load(indir+'/hdf5dataframes_gamma200-500_batches/paddedAndReadyToMerge/tensors/jets'+tag+'.npz')['arr_0']])
        
            # read hdf5 files
            readT = pd.HDFStore(readfrom['towers'].format('200-500')+tag+'.hdf5', mode='r')
            dfET = readT['towers']
            readT.close()

            readJ = pd.HDFStore(readfrom['jets'].format('200-500')+tag+'.hdf5', mode='r')
            dfEJ = readJ['jets']
            readJ.close()

            dfX.append(dfET)
            dfY.append(dfEJ)

        except FileNotFoundError:
            print('** INFO: towers'+tag+' not found --> skipping')
            continue
        if idx == 30: break # break at the 30th file to speed up the process
    
    # remove the dummy array filled with zeros
    X = X[1:]
    Y = Y[1:]

    ## DEBUG
    print(len(X))
    print(len(Y))

    # split train and testing datasets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

    # save them
    np.savez_compressed(training_folder+'/X_train.npz', X_train)
    np.savez_compressed(training_folder+'/X_test.npz', X_test)
    np.savez_compressed(training_folder+'/Y_train.npz', Y_train)
    np.savez_compressed(training_folder+'/Y_test.npz', Y_test)

    # save hdf5 files with dataframe formatted datasets
    storeT = pd.HDFStore(saveto['X'], mode='w')
    storeT['X'] = dfX
    storeT.close()

    storeJ = pd.HDFStore(saveto['Y'], mode='w')
    storeJ['Y'] = dfY
    storeJ.close()
