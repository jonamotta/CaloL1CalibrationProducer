from sklearn.model_selection import train_test_split
from TowerGeometry import *
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

def CheckClose(etas1,etas2,phis1,phis2): 
    outs = []
    for eta1,eta2,phi1,phi2 in zip(etas1,etas2,phis1,phis2):
        match_eta = (eta1 == eta2)
        match_phi = (phi1 == phi2)
        match_phi_adj = ((NextPhiTower(phi1) == phi2) or (PrevPhiTower(phi1) == phi2))
        match_eta_adj = ((NextEtaTower(eta1) == eta2) or (PrevEtaTower(eta1) == eta2))
        if match_eta and match_phi:
            out = True
        elif match_eta and match_phi_adj:
            out = 'Phi'
        elif match_eta_adj and match_phi:
            out = 'Eta'
        elif match_eta_adj and match_phi_adj:
            out = 'EtaPhi'
        else:
            out = False
        outs.append(out)
    return outs

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
            InFiles.append(subfolder)
    #print(len(InFiles))

    # testInfile = indir+'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated_appliedHCALpfa1p/Ntuple_0.root'
    testOutHDF = outdir+'/test.hdf5'
    testOutCSV = outdir+'/test.csv'
    store = pd.HDFStore(testOutHDF, mode='w')

    keyEvents="l1EventTree/L1EventTree"
    keyTowers="l1CaloTowerEmuTree/L1CaloTowerTree"
    keyGenjet="l1GeneratorTree/L1GenTree"

    branchesEvents = ["Event/event"]
    branchesTowers = ["L1CaloTower/ieta", "L1CaloTower/iphi", "L1CaloTower/iem", "L1CaloTower/ihad", "L1CaloTower/iet"]
    branchesGenjet = ["Generator/jetEta", "Generator/jetPhi", "Generator/jetPt", "Generator/nJet"]

    InFiles.sort()

    no_match = 0
    good_match = 0
    part_match_eta = 0
    part_match_phi = 0
    part_match_etaphi = 0
    bad_match = 0
    problem_match = 0
    multiple_match = 0

    for i, testInfile in enumerate(InFiles[0:1]):

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
        if i%100 == 0:
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
        dfET = dfET.head(1)
        dfEJ = dfEJ.head(1)

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

        # reset indeces to be the event number to be able to join the SFs later
        dfFlatET.set_index('event', inplace=True)
        dfFlatEJ.set_index('event', inplace=True)

        ## DEBUG
        # print(dfET.shape[0])
        # print(dfEJ.shape[0])

        # cerate all the possible combinations of jets per each event
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

        dfFlatEJT['central'] = (CheckClose(dfFlatEJT.jetIeta,dfFlatEJT.ieta,dfFlatEJT.jetIphi,dfFlatEJT.iphi))
        if len(dfFlatEJT[dfFlatEJT['central'] == 1]) == 0:
            # print('\nNo matching found for file {}\n'.format(testInfile.split('appliedHCALpfa1p')[1]))
            no_match = no_match + 1

        elif len(dfFlatEJT[dfFlatEJT['central'] == True]) == 1:
            try:
                dfFlatEJT['itot'] = dfFlatEJT['iem'] + dfFlatEJT['ihad'] + dfFlatEJT['iet']
                if (dfFlatEJT[dfFlatEJT['central'] == True].itot == dfFlatEJT['itot'].max()).any():
                    # print('Good match for file {}\n'.format(testInfile.split('appliedHCALpfa1p')[1]))
                    good_match = good_match + 1
                elif (dfFlatEJT[dfFlatEJT['central'] == 'Eta'].itot == dfFlatEJT['itot'].max()).any():
                    # print('Partial match for file {}\n'.format(testInfile.split('appliedHCALpfa1p')[1]))
                    part_match_eta = part_match_eta + 1
                elif (dfFlatEJT[dfFlatEJT['central'] == 'Phi'].itot == dfFlatEJT['itot'].max()).any():
                    # print('Partial match for file {}\n'.format(testInfile.split('appliedHCALpfa1p')[1]))
                    part_match_phi = part_match_phi + 1
                elif (dfFlatEJT[dfFlatEJT['central'] == 'EtaPhi'].itot == dfFlatEJT['itot'].max()).any():
                    # print('Partial match for file {}\n'.format(testInfile.split('appliedHCALpfa1p')[1]))
                    part_match_etaphi = part_match_etaphi + 1
                else:
                    print('Bad match for file {}\n'.format(testInfile.split('appliedHCALpfa1p')[1]))
                    bad_match = bad_match + 1
            except:
                # print('Problem for file {}\n'.format(testInfile.split('appliedHCALpfa1p')[1]))
                problem_match = problem_match + 1
        else:
            # print('More than one match for file {}\n'.format(testInfile.split('appliedHCALpfa1p')[1]))
            multiple_match = multiple_match + 1

        # DEBUG 
        # print(dfFlatEJT)

        # this is just a sort of example of how we would like to have the dataframe looking at the end
        # we have a column per each tower in the chunky donut --> this is the meaning of one hot encoding
        # for i in range(81):
        #     dfFlatEJT['iTinCD'+str(i)] = np.zeros(dfFlatEJT.shape[0])
    
        # save hdf5 file
        store = dfFlatEJT

    print('no_match = ', no_match)
    print('good_match = ', good_match)
    print('part_match_eta = ', part_match_eta)
    print('part_match_phi = ', part_match_phi)
    print('part_match_etaphi = ', part_match_etaphi)
    print('bad_match = ', bad_match)
    print('problem_match = ', problem_match)
    print('multiple_match = ', multiple_match)

    # store.close()


