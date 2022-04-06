import os
import sys
import numpy as np
import uproot3
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split

class Logger(object):
    def __init__(self, file):
        self.terminal = sys.stdout
        self.log = open(file, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

if __name__ == "__main__" :

    ##################### DEFINE INPUTS AND OUTPUTS ####################
    indir  = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0'
    outdir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes'
    os.system('mkdir -p '+outdir)

    # set output to go both to terminal and to file
    sys.stdout = Logger('/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes/info.log')

    testInfile  = indir+'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_9.root'
    testOutfile = outdir+'/test.hdf5'


    ##################### READ TTREES AND MATCH EVENTS ####################
    keyEvents="l1EventTree/L1EventTree"
    keyTowers="l1CaloTowerEmuTree/L1CaloTowerTree"
    keyGenjet="l1GeneratorTree/L1GenTree"

    branchesEvents = ["Event/event"]
    branchesTowers = ["L1CaloTower/ieta", "L1CaloTower/iphi", "L1CaloTower/iem", "L1CaloTower/ihad", "L1CaloTower/iet"]
    branchesGenjet = ["Generator/jetEta", "Generator/jetPhi", "Generator/jetPt", "Generator/nJet"]

    eventsTree = uproot3.open(testInfile)[keyEvents]
    towersTree = uproot3.open(testInfile)[keyTowers]
    genjetTree = uproot3.open(testInfile)[keyGenjet]

    arrEvents = eventsTree.arrays(branchesEvents)
    arrTowers = towersTree.arrays(branchesTowers)
    arrGenjet = genjetTree.arrays(branchesGenjet)

    dfE = pd.DataFrame(arrEvents)
    dfT = pd.DataFrame(arrTowers)
    dfJ = pd.DataFrame(arrGenjet)

    dfET = pd.concat([dfE, dfT], axis=1)
    dfEJ = pd.concat([dfE, dfJ], axis=1)
    dfET.set_index(b"event", inplace=True)
    dfEJ.set_index(b"event", inplace=True)

    print(dfET.shape[0])
    print(dfEJ.shape[0])

