from sklearn.model_selection import train_test_split
from TowerGeometry import FindIeta
from TowerGeometry import FindIphi
from itertools import chain
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

def InChunkyDonut(i_eta, i_phi, jet_EtaGap, jet_PhiGap):
    return np.abs(i_eta - jet_EtaGap) <= 4 and np.abs(i_phi - jet_PhiGap) <= 4


def deltarSelect( df, dRcut ):
    deta = np.abs(df['jetEta'] - df['jetEta_joined'])
    dphi = np.abs(df['jetPhi'] - df['jetPhi_joined'])
    sel = dphi > np.pi
    dphi = np.abs(sel*(2*np.pi) - dphi)
    return (np.sqrt(dphi*dphi+deta*deta) > dRcut) | ((deta == 0) & (dphi == 0))

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
        subfolders = glob.glob(indir+'/'+folder_name+'/Ntuple*.root')
        for subfolder in subfolders:
            InFiles.append(indir+'/'+folder_name+'/'+subfolder)
    #print(len(InFiles))


    testInfile = indir+'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_9.root'
    testOutHDF = outdir+'/test.hdf5'
    testOutCSV = outdir+'/test.csv'

    fieldnames = ['ev','i_eta','i_phi','i_em','i_had','i_et']
    with open(testOutCSV, 'w', newline='') as csvfile:
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

    ## DEBUG
    dfET = dfET.head(1)
    dfEJ = dfEJ.head(1)
    
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

    # reset indeces to be the event number to be able to join the SFs later
    dfFlatET.set_index('event', inplace=True)
    dfFlatEJ.set_index('event', inplace=True)

    ## DEBUG
    # print(dfET.shape[0])
    # print(dfEJ.shape[0])

    # cerate all teh possible combinations of jets per each event
    dfFlatEJ  = dfFlatEJ.join(dfFlatEJ, on='event', how='left', rsuffix='_joined', sort=False)
    # select only those jets that are at least dRcut away from each other
    dfFlatEJ['dRsafe'] = deltarSelect(dfFlatEJ, 0.5)
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
    dfFlatEJT  = dfFlatEJ.join(dfFlatET, on='event', how='left', rsuffix='_joined', sort=False)

    # identify the central tower for each jet by looking for the tower with the same ieta/iphi as the jet
    # FIXME - THIS NEEDS TO BE CHECKED!!! 
    #  --> in the sense that after having fixed the FindIeta/FindIphi function we need to check if it really works
    #  --> at a first look I would say that at least for ieta away from 29 it works
    dfFlatEJT['central'] = (dfFlatEJT['jetIeta']==dfFlatEJT['ieta']) & (dfFlatEJT['jetIphi']==dfFlatEJT['iphi']) 

    # DEBUG
    print(dfFlatEJT)

    # this is just a sort of example of how we would like to have the dataframe looking at the end
    # we have a column per each tower in the chunky donut --> this is the meaning of one hot encoding
    for i in range(81):
        dfFlatEJT['iTinCD'+str(i)] = np.zeros(dfFlatEJT.shape[0])

    
    # save hdf5 file
    store = pd.HDFStore(testOutHDF, mode='w')
    store = dfFlatEJT
    #store.close()


    # make the produced files accessible to the other people otherwise we cannot work together
    os.system('chmod -R 764 '+testOutHDF)
    os.system('chmod -R 764 '+testOutCSV)



    ## IM LEAVING THIS PART OF THE CODE THAT YOU WROTE ELENA, CAUSE MAYBE YOU WANT TO REUSE SOMETHING OR AT LEAST RESATRT FROM WERE YOU LEFT
    ## AS I MENTIONED IN ONE OF UR CHATS, REMEMBER THAT LOOPING OVER PANDAS DATAFRAMES IS EXTREMELY TIME CONSUMING 
    ##      --> TRY TO ONLY USE VECTORIZED OPERATIONS OR WORST CASE AN APPLY FCT
    ##      --> REMEMBRER THAT SIOMETIMES APPLY IS EVEN SLOWER THAN LOOPING CAUSE IT TAKES QUITE A BIT OF MEMORY TO CREATE SERIES INSIDE THE APPLY LOOP)

    # # Is it too much to have everything compressed in one pandas? In this way we can easily connect each jet with its towers
    # dfETJ = pd.concat([dfE, dfT, dfJ], axis=1)
    # dfETJ.set_index(b"event", inplace=True)
    # dfETJ = dfETJ.sort_values(by=[b'event'])
    # dfETJ.reset_index(level=0,drop=False)

    # for i in range(dfETJ.shape[0]):
    #     jet_EtaGap = FindEtaGap(dfETJ[b'jetEta'].iloc[i])
    #     jet_PhiGap = FindPhiGap(dfETJ[b'jetPhi'].iloc[i])
    #     for i_eta, i_phi, i_em, i_had, i_et in zip(dfETJ[b'ieta'].iloc[i], dfETJ[b'iphi'].iloc[i],dfETJ[b'iem'].iloc[i],dfETJ[b'ihad'].iloc[i],dfETJ[b'iet'].iloc[i]):
    #         if InChunkyDonut(i_eta, i_phi, jet_EtaGap, jet_PhiGap):
    #             print(i,i_eta,i_phi,i_em,i_had,i_et)
    #             with open(testOutCSV, 'a', newline='') as csvfile:
    #                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #                 writer.writerow({'ev':i, 'i_eta':i_eta, 'i_phi':i_phi, 'i_em':i_em, 'i_had':i_had, 'i_et':i_et})




























