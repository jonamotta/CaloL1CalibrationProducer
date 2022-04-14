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


def deltarSelect( df, dRcut ):
    deta = np.abs(df['jetEta'] - df['jetEta_joined'])
    dphi = np.abs(df['jetPhi'] - df['jetPhi_joined'])
    sel = dphi > np.pi
    dphi = np.abs(sel*(2*np.pi) - dphi)
    return (np.sqrt(dphi*dphi+deta*deta) > dRcut) | ((deta == 0) & (dphi == 0))

# returns an array with 81 entries, for each entry we have [eta,phi] number of the tower belonging to the chunky donut
def ChunkyDonutTowers(jetIeta, jetIphi):

    ieta_start = jetIeta
    iphi_start = jetIphi

    # define the top left position of the chunky donut
    for i in range(0,4):
        ieta_start = PrevEtaTower(ieta_start)
    for i in range(0,4):
        iphi_start = PrevPhiTower(iphi_start)

    ieta = ieta_start
    iphi = iphi_start

    CD = []
    for i in range(0,9): # scan eta direction
        if i > 0:
            ieta = NextEtaTower(ieta)
        iphi = iphi_start # for every row in eta we restart from the iphi on the left
        for j in range(0,9): # scan phi direction
            if j > 0:
                iphi = NextPhiTower(iphi)
            CD.append([ieta,iphi])
    return CD


def padDataFrame( dfFlatEJT ):
    padded = dfFlatEJT
    for uniqueIdx in dfFlatEJT.index.unique():
        #print(dfFlatEJT['jetIeta'][uniqueIdx])
        try:
            len(dfFlatEJT['jetIeta'][uniqueIdx])
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx].unique()[0]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx].unique()[0]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx].unique()[0]
        except TypeError:
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx]

        padder = pd.DataFrame(columns=dfFlatEJT.columns, index=range(0,81))
        padder['uniqueId'] = uniqueIdx
        padder['jetPt'] = jetPt
        padder['jetIeta'] = jetIeta
        padder['jetIphi'] = jetIphi
        padder['iem'] = 0
        padder['ihad'] = 0
        padder['iet'] = 0
        padder[['ieta','iphi']] = ChunkyDonutTowers(jetIeta,jetIphi)

        padded = padded.append(padder)
        #padded.sort_values('iet', inplace=True)
        padded.drop_duplicates(['uniqueId', 'ieta', 'iphi'], keep='first', inplace=True)
        
    return padded

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 alternateReader.py --v (ECAL or HCAL)

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--v",    dest="v",   help="Ntuple type ('ECAL' or 'HCAL')", default='ECAL')
    (options, args) = parser.parse_args()
    print(options)

    ##################### DEFINE INPUTS AND OUTPUTS ####################
    indir  = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0'
    outdir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_alternate'
    os.system('mkdir -p '+outdir)

    # set output to go both to terminal and to file
    sys.stdout = Logger('/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_alternate/info.log')

    # define the two paths where to store the hdf5 files
    saveTo = {
        'towers'  : outdir+'/test_towers.hdf5',
        'jets'    : outdir+'/test_jets.hdf5'
    }

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

    dfJets = pd.DataFrame()
    dfTowers = pd.DataFrame()

    for i, testInfile in enumerate(InFiles[0:10]):

        if testInfile in ['/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_175.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_256.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_278.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_31.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_363.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_371.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_38.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_388.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_407.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_41.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_430.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_433.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_453.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_459.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_462.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_466.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_470.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_478.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_491.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_498.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_51.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_84.root',
                          '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_240.root']:
            continue

        # see progress
        if i%1 == 0:
            print(testInfile)

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
        dfET = dfET.head(1000)
        dfEJ = dfEJ.head(1000)

        if len(dfET) == 0 or len(dfEJ) == 0:
            print('\nZero data for file {}\n'.format(testInfile))
        
        # flatten out the dataframes so that ech entry of the dataframe is a number and not a vector
        dfFlatET = pd.DataFrame({
            'event': np.repeat(dfET[b'event'].values, dfET[b'ieta'].str.len()), # event IDs are copied to keep proper track of what is what
            'ieta': list(chain.from_iterable(dfET[b'ieta'])),
            'iphi': list(chain.from_iterable(dfET[b'iphi'])),
            'iem' : list(chain.from_iterable(dfET[b'iem'])),
            'ihad': list(chain.from_iterable(dfET[b'ihad'])),
            'iet' : list(chain.from_iterable(dfET[b'iet']))
            })

        dfFlatEJ = pd.DataFrame({
            'event': np.repeat(dfEJ[b'event'].values, dfEJ[b'jetEta'].str.len()), # event IDs are copied to keep proper track of what is what
            'jetEta': list(chain.from_iterable(dfEJ[b'jetEta'])),
            'jetPhi': list(chain.from_iterable(dfEJ[b'jetPhi'])),
            'jetPt' : list(chain.from_iterable(dfEJ[b'jetPt']))
            })
        dfFlatEJ['jetId'] = dfFlatEJ.index # each jet gets an identifier based on a progressive value independent of event -> this allows further flexibility of ID on top of event

        # reset indeces to be the event number to be able to join the DFs later
        dfFlatET.set_index('event', inplace=True)
        dfFlatEJ.set_index('event', inplace=True)

        ## DEBUG
        # print(dfET.shape[0])
        # print(dfEJ.shape[0])

        # cerate all the possible combinations of jets per each event
        dfFlatEJ  = dfFlatEJ.join(dfFlatEJ, on='event', how='left', rsuffix='_joined', sort=False)
        # select only those jets that are at least dRcut away from each other
        dRcut = 0.5
        dfFlatEJ['dRsafe'] = deltarSelect(dfFlatEJ, dRcut)
        notSafe = list(dfFlatEJ[(dfFlatEJ['dRsafe']==False)]['jetId'])
        dfFlatEJ = dfFlatEJ[dfFlatEJ.jetId.isin(notSafe) == False]
        dfFlatEJ.drop(['jetEta_joined', 'jetPhi_joined', 'jetPt_joined', 'jetId_joined', 'dRsafe'], axis=1, inplace=True) # drop columns not needed anymore
        dfFlatEJ.drop_duplicates('jetId', keep='first', inplace=True) # drop duplicates of teh jets

        # find ieta/iphi values for the jets
        FindIeta_vctd = np.vectorize(FindIeta)
        FindIphi_vctd = np.vectorize(FindIphi)
        dfFlatEJ['jetIeta'] = FindIeta_vctd(dfFlatEJ['jetEta'])
        dfFlatEJ['jetIphi'] = FindIphi_vctd(dfFlatEJ['jetPhi'])
        dfFlatEJ.drop(['jetEta', 'jetPhi'], axis=1, inplace=True) # drop columns not needed anymore

        # join the jet and the towers datasets -> this creates all the possible combination of towers and jets for each event
        dfFlatEJT = dfFlatEJ.join(dfFlatET, on='event', how='left', rsuffix='_joined', sort=False)

        # select only towers that are inside the +-4 range from jetIphi
        # since on phi the range is wrapped around 72 we need to take into account the cases with |deltaIphi|>68
        dfFlatEJT['deltaIphi'] = dfFlatEJT['iphi'] - dfFlatEJT['jetIphi']
        dfFlatEJT = dfFlatEJT[((dfFlatEJT['deltaIphi']<=4)&(dfFlatEJT['deltaIphi']>=-4))|(dfFlatEJT['deltaIphi']<=-68)|(dfFlatEJT['deltaIphi']>=68)]

        # select only towers that are inside the +-5 range from jetIphi
        # since towers 0/29 do not exist we need to take a range larger by 1 tower on each side compared to the actual chunky donut
        dfFlatEJT['deltaIeta'] = dfFlatEJT['ieta'] - dfFlatEJT['jetIeta']
        dfFlatEJT = dfFlatEJT[(dfFlatEJT['deltaIeta']<=5)&(dfFlatEJT['deltaIeta']>=-5)]

        # compute the distances from towers +-29 and +-1
        # this gives us the possibility to define some specific conditions to select the correct towers of a cunky donut
        dfFlatEJT['deltaI29'] = 29 - dfFlatEJT['jetIeta']
        dfFlatEJT['deltaIm29'] = -29 - dfFlatEJT['jetIeta']
        dfFlatEJT['deltaI1'] = 1 - dfFlatEJT['jetIeta']
        dfFlatEJT['deltaIm1'] = -1 - dfFlatEJT['jetIeta']
        # define full OR condition in order to select the correct towers for each jet
        # the onditions (in coordinates wrt the jetIeta) are summarized in teh file bigORtowers.txt
        dfFlatEJT = dfFlatEJT[( ((dfFlatEJT['deltaI29']<5)&(dfFlatEJT['deltaI29']>0)&(dfFlatEJT['deltaIeta']>=-4)&(dfFlatEJT['deltaIeta']<=5)) | ((dfFlatEJT['deltaI29']>-5)&(dfFlatEJT['deltaI29']<0)&(dfFlatEJT['deltaIeta']>=-5)&(dfFlatEJT['deltaIeta']<=4)) | (((dfFlatEJT['deltaI29']<-5)|(dfFlatEJT['deltaI29']>5))&(dfFlatEJT['deltaIeta']>=-4)&(dfFlatEJT['deltaIeta']<=4)) | ((dfFlatEJT['deltaIm29']<5)&(dfFlatEJT['deltaIm29']>0)&(dfFlatEJT['deltaIeta']>=-4)&(dfFlatEJT['deltaIeta']<=5)) | ((dfFlatEJT['deltaIm29']>-5)&(dfFlatEJT['deltaIm29']<0)&(dfFlatEJT['deltaIeta']>=-5)&(dfFlatEJT['deltaIeta']<=4)) | (((dfFlatEJT['deltaIm29']<-5)|(dfFlatEJT['deltaIm29']>5))&(dfFlatEJT['deltaIeta']>=-4)&(dfFlatEJT['deltaIeta']<=4)) )]
        dfFlatEJT = dfFlatEJT[( ((dfFlatEJT['deltaI1']<5)&(dfFlatEJT['deltaI1']>0)&(dfFlatEJT['deltaIeta']>=-4)&(dfFlatEJT['deltaIeta']<=5)) | ((dfFlatEJT['deltaI1']>-5)&(dfFlatEJT['deltaI1']<0)&(dfFlatEJT['deltaIeta']>=-5)&(dfFlatEJT['deltaIeta']<=4)) | (((dfFlatEJT['deltaI1']<-5)|(dfFlatEJT['deltaI1']>5))&(dfFlatEJT['deltaIeta']>=-4)&(dfFlatEJT['deltaIeta']<=4)) | ((dfFlatEJT['deltaIm1']<5)&(dfFlatEJT['deltaIm1']>0)&(dfFlatEJT['deltaIeta']>=-4)&(dfFlatEJT['deltaIeta']<=5)) | ((dfFlatEJT['deltaIm1']>-5)&(dfFlatEJT['deltaIm1']<0)&(dfFlatEJT['deltaIeta']>=-5)&(dfFlatEJT['deltaIeta']<=4)) | (((dfFlatEJT['deltaIm1']<-5)|(dfFlatEJT['deltaIm1']>5))&(dfFlatEJT['deltaIeta']>=-4)&(dfFlatEJT['deltaIeta']<=4)) )]


        # drop what is no longer needed
        dfFlatEJT.drop(['deltaI29', 'deltaIm29', 'deltaI1', 'deltaIm1', 'deltaIphi', 'deltaIeta'], axis=1, inplace=True)

        # make the unique ID for each jet across all the files
        dfFlatEJT.reset_index(inplace=True)
        dfFlatEJT['uniqueId'] = dfFlatEJT['event'].astype(str)+'_'+dfFlatEJT['jetId'].astype(str)
        dfFlatEJT['uniqueIdx'] = dfFlatEJT['uniqueId'].copy(deep=True)
        dfFlatEJT.set_index('uniqueIdx', inplace=True)

        # drop what is no longer needed
        dfFlatEJT.drop(['event', 'jetId'], axis=1, inplace=True)

        # do the padding of the dataframe to have 81 rows for each jet        
        paddedEJT = padDataFrame(dfFlatEJT)
        paddedEJT.reset_index(inplace=True)

        # append the DFs from the different files to one single big DF
        dfTowers = dfTowers.append(paddedEJT[['uniqueId','ieta','iem','ihad','iet']])
        dfJets = dfJets.append(paddedEJT[['uniqueId','jetPt']])

        ## DEBUG
        # print(dfFlatEJT)
        # print(dfTowers)
    
    ## DEBUG
    #print(dfTowers)
    #print(len(dfTowers.event.unique()), 'events')
    print(len(dfTowers.uniqueId.unique()), 'jets')
    print(len(dfTowers), 'rows')

    # save hdf5 files
    storeT = pd.HDFStore(saveTo['towers'], mode='w')
    storeT['towers'] = dfTowers
    storeT.close()

    storeJ = pd.HDFStore(saveTo['jets'], mode='w')
    storeJ['jets'] = dfJets
    storeJ.close()


    # make the produced files accessible to the other people otherwise we cannot work together
    os.system('chmod 774 '+saveTo['towers'])
    os.system('chmod 774 '+saveTo['jets'])
