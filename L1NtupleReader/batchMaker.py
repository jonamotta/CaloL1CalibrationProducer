# from mainReader import mainReader
from itertools import chain
import pandas as pd
import numpy as np
import argparse
import uproot3
import glob
import sys
import os

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

### To run:
### python3 batchMaker.py --v (ECAL or HCAL)

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--v",    dest="v",   help="Ntuple type ('ECAL' or 'HCAL')", default='ECAL')
    (options, args) = parser.parse_args()
    print(options)

    ##################### DEFINE INPUTS AND OUTPUTS ####################
    indir  = '/data_CMS/cms/motta/CaloL1calibraton/'
    if options.v == 'ECAL': outdir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_ECAL_batches'
    else:                   outdir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_HCAL_batches'
    os.system('mkdir -p '+outdir+'/towers')
    os.system('mkdir -p '+outdir+'/jets')

    # set output to go both to terminal and to file
    sys.stdout = Logger(outdir+'/info.log')

    # choose ECAL of HCAL folder according to option v
    folder_names = []
    if options.v == 'HCAL':
        folder_names.append('QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__reEmulated_appliedHCALpfa1p')
    elif options.v == 'ECAL':
        folder_names.append('SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p')
        folder_names.append('SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p')
    else:
        sys.exit('basicReader.py: [ERROR] Wrong argument, choose ECAL or HCAL.'.format(os.getcwd()))

    # list Ntuples
    InFiles = []
    for folder_name in folder_names:
        subfolders = glob.glob(indir+'/'+folder_name+'/Ntuple*.root')
        for subfolder in subfolders:
            InFiles.append(subfolder)
    #print(len(InFiles))

    keyEvents="l1EventTree/L1EventTree"
    keyTowers="l1CaloTowerEmuTree/L1CaloTowerTree"
    keyGenjet="l1GeneratorTree/L1GenTree"

    branchesEvents = ["Event/event"]
    branchesTowers = ["L1CaloTower/ieta", "L1CaloTower/iphi", "L1CaloTower/iem", "L1CaloTower/ihad", "L1CaloTower/iet"]
    branchesGenjet = ["Generator/jetEta", "Generator/jetPhi", "Generator/jetPt", "Generator/nJet"]

    InFiles.sort()

    for i, testInfile in enumerate(InFiles[:]):

        if testInfile in ['/data_CMS/cms/motta/CaloL1calibraton//SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_131.root',
                          '/data_CMS/cms/motta/CaloL1calibraton//SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_160.root']:
            continue

        try:
            # see progress
            if i%1 == 0:
                print(testInfile)

            tag = testInfile.split('/Ntuple')[1].split('.r')[0]

            # define the two paths where to store the hdf5 files
            saveTo = {
                'towers'  : outdir+'/towers/towers',
                'jets'    : outdir+'/jets/jets'
            }

            ##################### READ TTREES AND MATCH EVENTS ####################

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

            ## DEBUG
            #dfET = dfET.head(553)
            #dfEJ = dfEJ.head(553)


            def chunker(seq, size):
                for pos in range(0, len(seq), size):
                    yield seq.iloc[pos:pos + size] 

            chunk_size = 100
            j = 0
            for ET,JT in zip(chunker(dfET, chunk_size),chunker(dfEJ, chunk_size)):
                print('runnning on batch '+str(j)+' of Ntuple'+tag)

                dfTowers = pd.DataFrame(ET)
                dfJets = pd.DataFrame(JT)

                # save hdf5 files
                storeT = pd.HDFStore(saveTo['towers']+tag+'_'+str(j)+'.hdf5', mode='w')
                storeT['towers'] = dfTowers
                storeT.close()

                storeJ = pd.HDFStore(saveTo['jets']+tag+'_'+str(j)+'.hdf5', mode='w')
                storeJ['jets'] = dfJets
                storeJ.close()

                # make the produced files accessible to the other people otherwise we cannot work together
                os.system('chmod 774 '+saveTo['towers']+tag+'_'+str(j)+'.hdf5')
                os.system('chmod 774 '+saveTo['jets']+tag+'_'+str(j)+'.hdf5')


                #mainReader(ET, JT, outdir, tag+'_'+str(j))
                j+=1

        except:
            print('Bad file : {}'.format(testInfile))

    print('** INFO: ALL DONE!')


