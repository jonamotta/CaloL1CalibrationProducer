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
### python3 alternateReader.py --v (ECAL or HCAL)

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--v",    dest="v",   help="Ntuple type ('ECAL' or 'HCAL')", default='ECAL')
    parser.add_option("--outdir",    dest="outdir",   help="Ntuple version folder where to save", default='')
    parser.add_option("--applyHCALpfa1p", dest="applyHCALpfa1p", action='store_true', default=True)
    parser.add_option("--applyNoCalib", dest="applyNoCalib", action='store_true', default=False)
    parser.add_option("--applyOldCalib", dest="applyOldCalib", action='store_true', default=False)
    parser.add_option("--applyNewCalib", dest="applyNewCalib", action='store_true', default=False)
    parser.add_option("--applyNewCalibSaturAt", dest="applyNewCalibSaturAt", type=float, default=None)
    parser.add_option("--applyNewCalibECALsaturAt", dest="applyNewCalibECALsaturAt", type=float, default=None)
    parser.add_option("--applyNewCalibHCALsaturAt", dest="applyNewCalibHCALsaturAt", type=float, default=None)
    parser.add_option("--doEG0_200", dest="doEG0_200", action='store_true', default=False)
    parser.add_option("--doEG0_200pu", dest="doEG0_200pu", action='store_true', default=False)
    parser.add_option("--doEG200_500", dest="doEG200_500", action='store_true', default=False)
    parser.add_option("--doEG200_500pu", dest="doEG200_500pu", action='store_true', default=False)
    parser.add_option("--doQCD", dest="doQCD", action='store_true', default=False)
    parser.add_option("--doQCDpu", dest="doQCDpu", action='store_true', default=False)
    parser.add_option("--qcdPtBin", dest="qcdPtBin", default="")
    parser.add_option("--doPi0_200", dest="doPi0_200", action='store_true', default=False)
    parser.add_option("--doNuGun", dest="doNuGun", action='store_true', default=False)
    parser.add_option("--chunk_size", dest="chunk_size", type=int, default=5000)
    (options, args) = parser.parse_args()
    print(options)

    if options.outdir=='':
        print('** WARNING: no ntuple version output folder specified - EXITING!')
        exit()

    if options.applyNoCalib == False and options.applyOldCalib == False and options.applyNewCalib == False and options.applyNewCalibSaturAt == None and options.applyNewCalibECALsaturAt == None and options.applyNewCalibHCALsaturAt == None:
        print('** WARNING: no calibration to be used specified - EXITING!')
        exit()

    if options.doEG0_200 == False and options.doEG200_500 == False and options.doEG0_200pu == False and options.doEG200_500pu == False and options.doQCD == False and options.doQCDpu == False and options.doPi0_200 == False and options.doNuGun == False:
        print('** WARNING: no dataset to be used specified - EXITING!')
        exit()

    tagHCALpfa1p = ""
    tagCalib = ""
    if   options.applyNoCalib:                                                  tagCalib = "_uncalib"
    elif options.applyOldCalib:                                                 tagCalib = "_oldCalib"
    elif options.applyNewCalib:                                                 tagCalib = "_newCalib" 
    elif options.applyNewCalibSaturAt:                                          tagCalib = "_newCalibSatur"+str(options.applyNewCalibSaturAt).split('.')[0]+'p'+str(options.applyNewCalibSaturAt).split('.')[1]
    elif options.applyNewCalibECALsaturAt and options.applyNewCalibHCALsaturAt: tagCalib = "_newCalibECALsatur"+str(options.applyNewCalibECALsaturAt).split('.')[0]+'p'+str(options.applyNewCalibECALsaturAt).split('.')[1]+"_newCalibHCALsatur"+str(options.applyNewCalibHCALsaturAt).split('.')[0]+'p'+str(options.applyNewCalibHCALsaturAt).split('.')[1]
    if   options.applyHCALpfa1p:                                                tagHCALpfa1p = "_applyHCALpfa1p"

    ##################### DEFINE INPUTS AND OUTPUTS ####################
    indir  = '/data_CMS/cms/motta/CaloL1calibraton/L1NTuples'
    outdir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.outdir

    # choose ECAL of HCAL folder according to option v
    folder_names = []

    if options.doQCDpu:
        ## qcd with pu - backup datasets
        if options.qcdPtBin=="20To30":
            folder_names.append("QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
            outdir = outdir+'/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

        elif options.qcdPtBin=="30To50":
            folder_names.append("QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
            outdir = outdir+'/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

        elif options.qcdPtBin=="50To80":
            folder_names.append("QCD_Pt-50To80_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
            outdir = outdir+'/QCD_Pt-50To80_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

        elif options.qcdPtBin=="80To120":
            folder_names.append("QCD_Pt-80To120_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
            outdir = outdir+'/QCD_Pt-80To120_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

        elif options.qcdPtBin=="120To170":
            folder_names.append("QCD_Pt-120To170_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
            outdir = outdir+'/QCD_Pt-120To170_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'
        else:
            ## qcd flat0-80 pu
            folder_names.append("/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-FlatPU0to80FEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
            outdir = outdir+'/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-FlatPU0to80FEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

    elif options.doQCD:
        ## qcd without pu
        folder_names.append("QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
        outdir = outdir+'/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

    elif options.doEG0_200:
        ## signle photon 0-200 without pu
        folder_names.append("SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
        outdir = outdir+'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

    elif options.doEG0_200pu:
        ## signle photon 0-200 with pu
        folder_names.append("SinglePhoton_Pt-0To200-gun__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
        outdir = outdir+'/SinglePhoton_Pt-0To200-gun__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'
    
    elif options.doEG200_500:
        ## signle photon 200-500 without pu
        folder_names.append("SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
        outdir = outdir+'/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

    elif options.doEG200_500pu:
        ## signle photon 200-500 with pu
        folder_names.append("SinglePhoton_Pt-200to500-gun__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
        outdir = outdir+'/SinglePhoton_Pt-200to500-gun__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

    elif options.doPi0_200:
        folder_names.append("SinglePion_Pt-0to200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
        outdir = outdir+'/SinglePion_Pt-0to200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

    elif options.doNuGun:
        folder_names.append("SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p)
        outdir = outdir+'/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'

    os.system('mkdir -p '+outdir+'/towers')
    os.system('mkdir -p '+outdir+'/jets')
    
    # set output to go both to terminal and to file
    sys.stdout = Logger(outdir+'/info'+options.v+'.log')

    print(folder_names)

    # list Ntuples
    InFiles = []
    for folder_name in folder_names:
        subfolders = glob.glob(indir+'/'+folder_name+'/Ntuple*.root')
        for subfolder in subfolders:
            InFiles.append(subfolder)
    # print(len(InFiles))

    keyEvents = "l1EventTree/L1EventTree"
    keyTowers = "l1CaloTowerEmuTree/L1CaloTowerTree"
    keyGenjet = "l1GeneratorTree/L1GenTree"
    if options.doNuGun: keyGenjet = "l1UpgradeEmuTree/L1UpgradeTree"

    branchesEvents = ["Event/event"]
    branchesTowers = ["L1CaloTower/ieta", "L1CaloTower/iphi", "L1CaloTower/iem", "L1CaloTower/ihad", "L1CaloTower/iet"]
    branchesGenjet = ["Generator/jetEta", "Generator/jetPhi", "Generator/jetPt", "Generator/nJet"]
    if options.doNuGun: branchesGenjet = ["L1Upgrade/jetEta", "L1Upgrade/jetPhi", "L1Upgrade/jetEt", "L1Upgrade/nJets"]

    InFiles.sort()

    for i, testInfile in enumerate(InFiles[:]):

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

        chunk_size = options.chunk_size
        j = 0
        for ET,EJ in zip(chunker(dfET, chunk_size),chunker(dfEJ, chunk_size)):
            print('runnning on batch '+str(j)+' of Ntuple'+tag)

            dfTowers = pd.DataFrame(ET)
            dfJets = pd.DataFrame(EJ)

            # flatten out the dataframes so that ech entry of the dataframe is a number and not a vector
            dfFlatET = pd.DataFrame({
                'event': np.repeat(dfTowers[b'event'].values, dfTowers[b'ieta'].str.len()), # event IDs are copied to keep proper track of what is what
                'ieta': list(chain.from_iterable(dfTowers[b'ieta'])),
                'iphi': list(chain.from_iterable(dfTowers[b'iphi'])),
                'iem' : list(chain.from_iterable(dfTowers[b'iem'])),
                'ihad': list(chain.from_iterable(dfTowers[b'ihad'])),
                'iet' : list(chain.from_iterable(dfTowers[b'iet']))
                })

            dfFlatEJ = pd.DataFrame({
                'event': np.repeat(dfJets[b'event'].values, dfJets[b'jetEta'].str.len()), # event IDs are copied to keep proper track of what is what
                'jetEta': list(chain.from_iterable(dfJets[b'jetEta'])),
                'jetPhi': list(chain.from_iterable(dfJets[b'jetPhi'])),
                # 'jetPt' : list(chain.from_iterable(dfJets[b'jetEt']))
                'jetPt' : list(chain.from_iterable(dfJets[b'jetPt']))
                })

            # save hdf5 files
            storeT = pd.HDFStore(saveTo['towers']+tag+'_'+str(j)+'.hdf5', mode='w')
            storeT['towers'] = dfFlatET
            storeT.close()

            storeJ = pd.HDFStore(saveTo['jets']+tag+'_'+str(j)+'.hdf5', mode='w')
            storeJ['jets'] = dfFlatEJ
            storeJ.close()

            j+=1

        # break

    print('** INFO: ALL DONE!')

