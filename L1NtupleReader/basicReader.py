import os
import sys
import glob
import csv
import numpy as np
import uproot3
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split

from TowerGeometry import FindEtaGap
from TowerGeometry import FindPhiGap


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

def InChunkyDonut(i_eta, i_phi, jet_EtaGap, jet_PhiGap):
    return np.abs(i_eta - jet_EtaGap) <= 4 and np.abs(i_phi - jet_PhiGap) <= 4

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 basicReader.py --v (ECAL or HCAL)

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--v",    dest="v",   help="Ntuple type ('ECAL' or 'HCAL')", default='ECAL')
    (options, args) = parser.parse_args()
    print(options)

    ##################### DEFINE INPUTS AND OUTPUTS ####################
    indir  = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0'
    outdir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes'
    os.system('mkdir -p '+outdir)

    # set output to go both to terminal and to file
    sys.stdout = Logger('/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes/info.log')

    # choose ECAL of HCAL folder according to option v
    folder_names = []
    if options.v == 'HCAL':
        folder_names.append('SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p')
    elif options.v == 'ECAL':
        folder_names.append('SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p')
        folder_names.append('SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p')
    else:
        sys.exit('basicReader.py: [ERROR] Wrong argument, choose ECAL or HCAL.'.format(os.getcwd()))

    # list Ntuples
    InFiles = []
    for folder_name in folder_names:
        subfolders = glob.glob(indir+'/'+folder_name+'/Ntuple*')
        for subfolder in subfolders:
            InFiles.append(indir+'/'+folder_name+'/'+subfolder)
    # print(len(InFiles))

    testInfile = indir+'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_9.root'
    # testOutfile = outdir+'/test.hdf5'
    testOutfile = outdir+'/test.csv'

    fieldnames = ['ev','i_eta','i_phi','i_em','i_had','i_et']
    with open(testOutfile, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

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

# Is it too much to have everything compressed in one pandas? In this way we can easily connect each jet with its towers
    dfETJ = pd.concat([dfE, dfT, dfJ], axis=1)
    dfETJ.set_index(b"event", inplace=True)
    dfETJ = dfETJ.sort_values(by=[b'event'])
    dfETJ.reset_index(level=0,drop=False)

    for i in range(dfETJ.shape[0]):
        jet_EtaGap = FindEtaGap(dfETJ[b'jetEta'].iloc[i])
        jet_PhiGap = FindPhiGap(dfETJ[b'jetPhi'].iloc[i])
        for i_eta, i_phi, i_em, i_had, i_et in zip(dfETJ[b'ieta'].iloc[i], dfETJ[b'iphi'].iloc[i],dfETJ[b'iem'].iloc[i],dfETJ[b'ihad'].iloc[i],dfETJ[b'iet'].iloc[i]):
            if InChunkyDonut(i_eta, i_phi, jet_EtaGap, jet_PhiGap):
                print(i,i_eta,i_phi,i_em,i_had,i_et)
                with open(testOutfile, 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'ev':i, 'i_eta':i_eta, 'i_phi':i_phi, 'i_em':i_em, 'i_had':i_had, 'i_et':i_et})
