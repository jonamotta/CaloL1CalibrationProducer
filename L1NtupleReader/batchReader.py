from optparse import OptionParser
from caloParamsOnTheFly import *
from itertools import chain
from TowerGeometry import *
import pandas as pd
import numpy as np
import uproot3
import math
import os,sys
import warnings
warnings.simplefilter(action='ignore')

n_jets = 0
n_mismatch = 0

def chunker(seq, size):
    for pos in range(0, len(seq), size):
        yield seq.iloc[pos:pos + size] 

def deltarSelect( df, dRcut ):
    deta = np.abs(df['jetEta'] - df['jetEta_joined'])
    dphi = np.abs(df['jetPhi'] - df['jetPhi_joined'])
    sel = dphi > np.pi
    dphi = np.abs(sel*(2*np.pi) - dphi)
    return (np.sqrt(dphi*dphi+deta*deta) > dRcut) | ((deta == 0) & (dphi == 0))


# returns an array with 81 entries, for each entry we have [eta,phi] number of the tower belonging to the chunky donut
def ChunkyDonutTowers(jetIeta, jetIphi):

    CD = []
    iphi_start = jetIphi
    # define the top position of the chunky donut
    for i in range(0,4):
        iphi_start = PrevPhiTower(iphi_start)
    
    if jetIeta < 0:
        ieta_start = jetIeta
        # define the top right position of the chunky donut
        for i in range(0,4):
            ieta_start = NextEtaTower(ieta_start)
        
        ieta = ieta_start
        iphi = iphi_start 

        for i in range(0,9): # scan eta direction towards left
            if i > 0:
                ieta = PrevEtaTower(ieta)
            iphi = iphi_start # for every row in eta we restart from the first iphi
            for j in range(0,9): # scan phi direction
                if j > 0:
                    iphi = NextPhiTower(iphi)
                CD.append([ieta,iphi])
    
    elif jetIeta > 0:
        ieta_start = jetIeta
        # define the top left position of the chunky donut
        for i in range(0,4):
            ieta_start = PrevEtaTower(ieta_start)

        ieta = ieta_start
        iphi = iphi_start

        for i in range(0,9): # scan eta direction towards right
            if i > 0:
                ieta = NextEtaTower(ieta)
            iphi = iphi_start # for every row in eta we restart from the first iphi
            for j in range(0,9): # scan phi direction
                if j > 0:
                    iphi = NextPhiTower(iphi)
                CD.append([ieta,iphi])
    return CD

def NextPhiTower(iphi):
    if iphi == 72: return 1
    else:          return iphi + 1
def PrevPhiTower(iphi):
    if iphi == 1: return 72
    else:         return iphi - 1
def NextEtaTower(ieta):
    if ieta == -1: return 1
    else:          return ieta + 1
def PrevEtaTower(ieta):
    if ieta == 1: return -1
    else:         return ieta - 1

def FindClusterCoordinates(iEta, iPhi, egShape, direction):

    # define snake coordinates for left or right cluster
    SnakeCoords = []
    if direction == +1: iEtaShift = NextEtaTower(iEta) #right = EAST = eta+1
    if direction == -1: iEtaShift = PrevEtaTower(iEta) #left  = WEST = eta-1 

    SnakeCoords.append((iEta, PrevPhiTower(iPhi)))                  # bit 1 = N = phi-1
    SnakeCoords.append((iEta, NextPhiTower(iPhi)))                  # bit 2 = S = phi+1
    SnakeCoords.append((iEtaShift, iPhi))                           # bit 3 = E/W = eta+/-1
    SnakeCoords.append((iEtaShift, PrevPhiTower(iPhi)))             # bit 4 = NE/NW = eta+/-1,phi-1
    SnakeCoords.append((iEtaShift, NextPhiTower(iPhi)))             # bit 5 = SE/SW = eta+/-1,phi+1
    SnakeCoords.append((iEta, PrevPhiTower(PrevPhiTower(iPhi))))    # bit 6 = NN = phi-2
    SnakeCoords.append((iEta, NextPhiTower(NextPhiTower(iPhi))))    # bit 7 = SS = phi+2
    
    # decode the shape to bits and revert the order so that: 
    # bit 1 (position 0) corresponds to the first entry of SnakeCoords
    # bit 2 (position 1) corresponds to the second entry of SnakeCoords
    padded_num = str(bin(egShape)[2:]).rjust(9, '0')[::-1]
    
    # keep only the eta, phi coordinates belonging to the cluster
    ClusterCoords = [(iEta, iPhi)] #seed is always in the cluster
    for i, coord in enumerate(SnakeCoords):
        if padded_num[i] != '0':
            ClusterCoords.append(coord)
    
    return ClusterCoords

def FindDirection(iEta, iPhi, df):
    # define the 3 neighbour towers on the right
    RigthTowers = []
    RigthTowers.append((NextEtaTower(iEta), PrevPhiTower(iPhi)))
    RigthTowers.append((NextEtaTower(iEta), iPhi))
    RigthTowers.append((NextEtaTower(iEta), NextPhiTower(iPhi)))
    # define the 3 neighbour towers on the left
    LeftTowers = []
    LeftTowers.append((PrevEtaTower(iEta), PrevPhiTower(iPhi)))
    LeftTowers.append((PrevEtaTower(iEta), iPhi))
    LeftTowers.append((PrevEtaTower(iEta), NextPhiTower(iPhi)))
    # compute the energy sum of ECAL and HCAL deposit in the left and right towers
    EtRight = df[df[['ieta', 'iphi']].apply(tuple, axis=1).isin(RigthTowers)].iesum.sum()
    EtLeft = df[df[['ieta', 'iphi']].apply(tuple, axis=1).isin(LeftTowers)].iesum.sum()
    # decide if the cluster is left or right
    if EtRight >= EtLeft:
        return +1 # right
    else:
        return -1 # left

def padDataFrameWithZerosMaskedCluster( dfFlatEJT ):
    padded = pd.DataFrame()
    for i, uniqueIdx in enumerate(dfFlatEJT.index.unique()):
        if i%100 == 0:
            print('{:.4f}%'.format(i/len(dfFlatEJT.index.unique())*100))
        
        if len(dfFlatEJT[dfFlatEJT.index == uniqueIdx]) > 1:
            # get shape and position of the cluster
            jetIeta     = dfFlatEJT['jetIeta'][uniqueIdx].unique()[0]
            jetIphi     = dfFlatEJT['jetIphi'][uniqueIdx].unique()[0]
            trainingPt  = dfFlatEJT['trainingPt'][uniqueIdx].unique()[0]
            jetShape    = dfFlatEJT['jetShape'][uniqueIdx].unique()[0]
            jetPt       = dfFlatEJT['jetPt'][uniqueIdx].unique()[0]
            jetEta      = dfFlatEJT['jetEta'][uniqueIdx].unique()[0]
            jetPhi      = dfFlatEJT['jetPhi'][uniqueIdx].unique()[0]
            clusterIeta = dfFlatEJT['TowerIeta'][uniqueIdx].unique()[0]
            clusterIphi = dfFlatEJT['TowerIphi'][uniqueIdx].unique()[0]
        else:
            # get shape and position of the cluster
            jetIeta     = dfFlatEJT['jetIeta'][uniqueIdx]
            jetIphi     = dfFlatEJT['jetIphi'][uniqueIdx]
            trainingPt  = dfFlatEJT['trainingPt'][uniqueIdx]
            jetShape    = dfFlatEJT['jetShape'][uniqueIdx]
            jetPt       = dfFlatEJT['jetPt'][uniqueIdx]
            jetEta      = dfFlatEJT['jetEta'][uniqueIdx]
            jetPhi      = dfFlatEJT['jetPhi'][uniqueIdx]
            clusterIeta = dfFlatEJT['TowerIeta'][uniqueIdx]
            clusterIphi = dfFlatEJT['TowerIphi'][uniqueIdx]

        # get the true cluster seed coordinates (mismatch often happens between the offline and L1)
        # check if the cluster is right or left
        df_i = dfFlatEJT[dfFlatEJT.index == uniqueIdx]
        df_i['iesum'] = df_i['iem'] + df_i['hcalET']

        # mask TT outside the cluster shape
        Direction = FindDirection(clusterIeta, clusterIphi, df_i)
        ClusterCoordinates = FindClusterCoordinates(clusterIeta, clusterIphi, jetShape, Direction)
        filtered_padded = df_i[df_i[['ieta', 'iphi']].apply(tuple, axis=1).isin(ClusterCoordinates)]
        padded = pd.concat([padded, filtered_padded])

        # keep only the number of towers inside the cluster shape
        N = len(filtered_padded)

        # crosscheck for debug
        N_TT_cluster = int(str(bin(jetShape)[2:]).rjust(9, '0')[::-1].count('1')) + 1 # add one for the central tower
        if N_TT_cluster != N:
            global n_mismatch
            n_mismatch += 1
            print("\nMismatched")
            print("\nShape of the cluster is: ", jetShape) #DEBUG
            print("Direction: ", Direction) #DEBUG
            print("ClusterCoordinates: ", ClusterCoordinates) #DEBUG
            print("iEsum = ", list(df_i['iesum'].values)) #DEBUG
            print("iEta = ", list(df_i['ieta'].values)) #DEBUG
            print("iPhi = ", list(df_i['iphi'].values)) #DEBUG

        padder = pd.DataFrame(columns=dfFlatEJT.columns, index=range(0,81-N))
        padder['uniqueId'] = uniqueIdx
        padder['jetPt'] = jetPt
        padder['trainingPt'] = trainingPt
        padder['jetEta'] = jetEta
        padder['jetPhi'] = jetPhi
        padder['jetIeta'] = jetIeta
        padder['jetIphi'] = jetIphi
        padder['iem'] = 0
        padder['ihad'] = 0
        padder['iet'] = 0
        padder['hcalET'] = 0
        padder['ieta'] = 0
        padder['iphi'] = 0

        padded = pd.concat([padded, padder])
        del padder

    return padded

def padDataFrame( dfFlatEJT ):
    padded = dfFlatEJT
    for i, uniqueIdx in enumerate(dfFlatEJT.index.unique()):
        if i%100 == 0:
            print('{:.4f}%'.format(i/len(dfFlatEJT.index.unique())*100))
        try:
            len(dfFlatEJT['jetIeta'][uniqueIdx])
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx].unique()[0]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx].unique()[0]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx].unique()[0]
            trainingPt = dfFlatEJT['trainingPt'][uniqueIdx].unique()[0]
            jetEta = dfFlatEJT['jetEta'][uniqueIdx].unique()[0]
            jetPhi = dfFlatEJT['jetPhi'][uniqueIdx].unique()[0]
            # nFT = dfFlatEJT['nFT'][uniqueIdx].unique()[0]
        except TypeError:
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx]
            trainingPt = dfFlatEJT['trainingPt'][uniqueIdx]
            jetEta = dfFlatEJT['jetEta'][uniqueIdx]
            jetPhi = dfFlatEJT['jetPhi'][uniqueIdx]
            # nFT = dfFlatEJT['nFT'][uniqueIdx]

        padder = pd.DataFrame(columns=dfFlatEJT.columns, index=range(0,81))
        padder['uniqueId'] = uniqueIdx
        padder['jetPt'] = jetPt
        padder['trainingPt'] = trainingPt
        padder['jetEta'] = jetEta
        padder['jetPhi'] = jetPhi
        padder['jetIeta'] = jetIeta
        padder['jetIphi'] = jetIphi
        # padder['nFT'] = nFT
        padder['iem'] = 0
        padder['ihad'] = 0
        padder['iet'] = 0
        padder['hcalET'] = 0
        padder[['ieta','iphi']] = ChunkyDonutTowers(jetIeta,jetIphi)

        padded = padded.append(padder)
        del padder
        
    return padded

def padDataFrameWithZeros( dfFlatEJT ):

    padded = dfFlatEJT
    for i, uniqueIdx in enumerate(dfFlatEJT.index.unique()):
        if i%100 == 0:
            print('{:.4f}%'.format(i/len(dfFlatEJT.index.unique())*100))
        try:
            N = len(dfFlatEJT['jetIeta'][uniqueIdx])
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx].unique()[0]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx].unique()[0]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx].unique()[0]
            trainingPt = dfFlatEJT['trainingPt'][uniqueIdx].unique()[0]
            jetEta = dfFlatEJT['jetEta'][uniqueIdx].unique()[0]
            jetPhi = dfFlatEJT['jetPhi'][uniqueIdx].unique()[0]
            # nFT = dfFlatEJT['nFT'][uniqueIdx].unique()[0]
            # contained = dfFlatEJT['contained'][uniqueIdx].unique()[0]
        except TypeError:
            N = 1
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx]
            trainingPt = dfFlatEJT['trainingPt'][uniqueIdx]
            jetEta = dfFlatEJT['jetEta'][uniqueIdx]
            jetPhi = dfFlatEJT['jetPhi'][uniqueIdx]
            # nFT = dfFlatEJT['nFT'][uniqueIdx]
            # contained = dfFlatEJT['contained'][uniqueIdx]

        padder = pd.DataFrame(columns=dfFlatEJT.columns, index=range(0,81-N))
        padder['uniqueId'] = uniqueIdx
        padder['jetPt'] = jetPt
        padder['trainingPt'] = trainingPt
        padder['jetEta'] = jetEta
        padder['jetPhi'] = jetPhi
        padder['jetIeta'] = jetIeta
        padder['jetIphi'] = jetIphi
        # padder['nFT'] = nFT
        # padder['contained'] = contained
        padder['iem'] = 0
        padder['ihad'] = 0
        padder['iet'] = 0
        padder['hcalET'] = 0
        padder['ieta'] = 0
        padder['iphi'] = 0

        padded = padded.append(padder)
        del padder
        
    return padded

def mainReader( dfFlatET, dfFlatEJ, saveToDFs, saveToTensors, uJetPtcut, lJetPtcut, iEtacut, iEtacutMin, applyCut_3_6_9, Ecalcut, \
                Hcalcut, HoTotcut, TTNumberCut, TTNumberCutInverse, trainPtVers, whichECALcalib, whichHCALcalib, \
                flattenPtDistribution, flattenEtaDistribution, applyOnTheFly, ClusterFilter, applyZS, LooseEle):
    
    if len(dfFlatET) == 0 or len(dfFlatEJ) == 0:
        print(' ** WARNING: Zero data here --> EXITING!\n')
        return
    
    dfFlatEJ['jetId'] = dfFlatEJ.index # each jet gets an identifier based on a progressive value independent of event -> this allows further flexibility of ID on top of event

    #########################################################################
    ###################### Application of ZS to inputs ######################
    if applyZS != False:
        # print(dfFlatET[dfFlatET['ihad'] == 1]['ieta'].unique()) #DEBUG
        # apply ZS mehod to the MC inputs for ihad == 1 and |ieta| <= 15
        dfFlatET.loc[(dfFlatET['ihad'] == 1) & (dfFlatET['ieta'].abs() <= 15), 'ihad'] = 0
        # print(dfFlatET[dfFlatET['ihad'] == 1]['ieta'].unique()) #DEBUG

    #########################################################################
    ########################## Application of cuts ##########################

    print('starting cuts') # DEBUG

    if LooseEle != False:
        dfFlatEJ = dfFlatEJ[dfFlatEJ['LooseEle'] == 1]
        dfFlatEJ.drop(['LooseEle'], axis=1, inplace=True) # drop column not needed anymore

    # Apply cut on jetPt
    if uJetPtcut != False:
        dfFlatEJ = dfFlatEJ[dfFlatEJ['jetPt'] < float(uJetPtcut)]
    if lJetPtcut != False:
        dfFlatEJ = dfFlatEJ[dfFlatEJ['jetPt'] > float(lJetPtcut)]

    # Apply cut on HoTot (ony for the Private MC L1Ntuples)
    if HoTotcut != False:
        print("Applying cut HoTot > ", HoTotcut)
        dfFlatEJ = dfFlatEJ[dfFlatEJ['HoTot'] > float(HoTotcut)]

    # flatten the pT distribution of the QCD samples
    # ideally this flattening would go after the hoe cut by I was not able to make it work there :(
    if flattenPtDistribution != False:
        print('flattening pT distribution')
        dfFlatEJ.sort_values('jetPt', ascending=False) # order largest to smallest
        step = 10
        pt_bins = np.arange(math.floor(dfFlatEJ['jetPt'].min()), math.ceil(dfFlatEJ['jetPt'].max())+step, step)
        idx150 = math.ceil((150-pt_bins[0])/step)-1 # get the idx of the bin with containing the 150GeV population
        pt_bins[0] = pt_bins[0]-1
        labels = np.arange(1, len(pt_bins), 1)
        dfFlatEJ['jetPtBin'] = pd.cut(dfFlatEJ['jetPt'], bins = pt_bins, labels=labels) # bin jets by pT
        size = len(dfFlatEJ[dfFlatEJ['jetPtBin']==labels[idx150]]['jetPtBin']) # get the number of event in the last pT bin
        dfFlatEJBalanced = dfFlatEJ.groupby('jetPtBin', as_index = False, group_keys=False).apply(lambda s: s.sample( min(len(s),size))) # select the same number of events for each pT bin
        dfFlatEJ = dfFlatEJBalanced.copy(deep=True)
        del dfFlatEJBalanced

    # transform jetPt in hardware units
    dfFlatEJ['trainingPt'] = dfFlatEJ['jetPt'].copy(deep=True) * 2

    # remove jets outside L1 acceptance
    dfFlatEJ = dfFlatEJ[np.abs(dfFlatEJ['jetEta']) < 5.191]

    # Apply cut for noisy towers: ieta=26 -> iem>=6, ieta=27 -> iem>=12, ieta=28 -> iem>=18
    if applyCut_3_6_9:
        dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 26) & (dfFlatET['iem'] < 6)].index, inplace = True)
        dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 27) & (dfFlatET['iem'] < 12)].index, inplace = True)
        dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 28) & (dfFlatET['iem'] < 18)].index, inplace = True)

    # Define overall hcalET information, ihad for ieta < 29 and iet for ieta > 29
    dfFlatET['hcalET'] = dfFlatET['ihad']*(np.abs(dfFlatET['ieta'])<29) + dfFlatET['iet']*(np.abs(dfFlatET['ieta'])>29)

    # reset indeces to be the event number to be able to join the DFs later
    dfFlatET.set_index('event', inplace=True)
    dfFlatEJ.set_index('event', inplace=True)

    #########################################################################
    #########################################################################

    ## DEBUG
    # print(dfFlatET.shape[0])
    # print(dfFlatEJ.shape[0])
    # print(dfFlatEJ.shape[0])
    # dfFlatET = dfFlatET.head(100).copy(deep=True)
    # dfFlatEJ = dfFlatEJ.head(5000).copy(deep=True)
    print('starting dR rejection')

    # cerate all the possible combinations of jets per each event
    dfFlatEJ  = dfFlatEJ.join(dfFlatEJ, on='event', how='left', rsuffix='_joined', sort=False)
    # select only those jets that are at least dRcut away from each other
    dRcut = 0.5
    dfFlatEJ['dRsafe'] = deltarSelect(dfFlatEJ, dRcut)
    notSafe = list(dfFlatEJ[(dfFlatEJ['dRsafe']==False)]['jetId'])
    dfFlatEJ = dfFlatEJ[dfFlatEJ.jetId.isin(notSafe) == False]
    dfFlatEJ.drop(['jetEta_joined', 'jetPhi_joined', 'jetPt_joined', 'jetId_joined', 'dRsafe'], axis=1, inplace=True) # drop columns not needed anymore
    dfFlatEJ.drop_duplicates('jetId', keep='first', inplace=True) # drop duplicates of the jets

    ## DEBUG
    print('starting conversion eta/phi->ieta/iphi')

    # find ieta/iphi values for the jets
    FindIeta_vctd = np.vectorize(FindIeta)
    FindIphi_vctd = np.vectorize(FindIphi)
    dfFlatEJ['jetIeta'] = FindIeta_vctd(dfFlatEJ['jetEta'])
    dfFlatEJ['jetIphi'] = FindIphi_vctd(dfFlatEJ['jetPhi'])

    # For ECAL/HCAL we consider just jets having a chunky donuts completely inside the ECAL/HCAL detector
    if iEtacut != False: dfFlatEJ = dfFlatEJ[abs(dfFlatEJ['jetIeta']) <= int(iEtacut)]
    if iEtacutMin != False: dfFlatEJ = dfFlatEJ[abs(dfFlatEJ['jetIeta']) >= int(iEtacutMin)]

    # join the jet and the towers datasets -> this creates all the possible combination of towers and jets for each event
    # important that dfFlatET is joined to dfFlatEJ and not viceversa --> this because dfFlatEJ contains the safe jets to be used and the safe event numbers
    dfFlatEJT = dfFlatEJ.join(dfFlatET, on='event', how='left', rsuffix='_joined', sort=False)

    # make the unique ID for each jet across all the files
    dfFlatEJT.reset_index(inplace=True)
    dfFlatEJT['uniqueId'] = dfFlatEJT['event'].astype(str)+'_'+dfFlatEJT['jetId'].astype(str)
    dfFlatEJT['uniqueIdx'] = dfFlatEJT['uniqueId'].copy(deep=True)
    dfFlatEJT.set_index('uniqueIdx', inplace=True)

    # apply cut on saturated towers (we do not only drop the towers but we drop the full jet otherwise we train on chunky donuts with holes)
    dfFlatEJT.drop(dfFlatEJT[dfFlatEJT['iem']>255].index, inplace=True)
    dfFlatEJT.drop(dfFlatEJT[dfFlatEJT['ihad']>255].index, inplace=True)
    dfFlatEJT.drop(dfFlatEJT[dfFlatEJT['iet']>255].index, inplace=True)

    ## DEBUG
    print('starting bigORtowers')

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
    dfFlatEJT.drop(['event', 'jetId', 'deltaI29', 'deltaIm29', 'deltaI1', 'deltaIm1', 'deltaIphi', 'deltaIeta'], axis=1, inplace=True)

    if Ecalcut != "False":
        if Ecalcut == "True":
            Ecalcut_value = 0.80
        else:
            Ecalcut_value = float(Ecalcut)
        # drop all photons that have a deposit in HF
        print(" ### INFO: Apply E/Tot cut = {}".format(Ecalcut_value))
        dfFlatEJT.drop(dfFlatEJT[(dfFlatEJT['iet']>0)&(dfFlatEJT['ieta']>=30)].index, inplace=True)

        # drop all photons for which E/(E+H)<0.8
        group = dfFlatEJT.groupby('uniqueIdx')
        dfFlatEJT['eoh'] = group['iem'].sum()/(group['iem'].sum()+group['hcalET'].sum())
        dfFlatEJT = dfFlatEJT[dfFlatEJT['eoh']>float(Ecalcut_value)]

    # apply ECAL calibration on the fly
    if whichECALcalib != False:
        print("starting ECAL calibration")
        dfFlatEJT.reset_index(inplace=True)
        
        # get the correct caloParams for the calibration on the fly
        if whichECALcalib == "oldCalib":
            energy_bins = layer1ECalScaleETBins_currCalib
            labels = layer1ECalScaleETLabels_currCalib
            SFs = layer1ECalScaleFactors_currCalib
        elif whichECALcalib == "currCalib":
            energy_bins = layer1ECalScaleETBins_currCalib
            labels = layer1ECalScaleETLabels_currCalib
            SFs = layer1ECalScaleFactors_currCalib
        elif whichECALcalib == "v33_newCalib":
            energy_bins = layer1ECalScaleETBins_v33_newCalib
            labels = layer1ECalScaleETLabels_v33_newCalib
            SFs = layer1ECalScaleFactors_v33_newCalib
        elif whichECALcalib == "v33Rate0p8_newCalib":
            energy_bins = layer1ECalScaleETBins_v33Rate0p8_newCalib
            labels = layer1ECalScaleETLabels_v33Rate0p8_newCalib
            SFs = layer1ECalScaleFactors_v33Rate0p8_newCalib
        elif whichECALcalib == "v33Rate1p2_newCalib":
            energy_bins = layer1ECalScaleETBins_v33Rate1p2_newCalib
            labels = layer1ECalScaleETLabels_v33Rate1p2_newCalib
            SFs = layer1ECalScaleFactors_v33Rate1p2_newCalib
        elif whichECALcalib == "v33Rate0p8True_newCalib":
            energy_bins = layer1ECalScaleETBins_v33Rate0p8True_newCalib
            labels = layer1ECalScaleETLabels_v33Rate0p8True_newCalib
            SFs = layer1ECalScaleFactors_v33Rate0p8True_newCalib
        elif whichECALcalib == "v33Rate1p2True_newCalib":
            energy_bins = layer1ECalScaleETBins_v33Rate1p2True_newCalib
            labels = layer1ECalScaleETLabels_v33Rate1p2True_newCalib
            SFs = layer1ECalScaleFactors_v33Rate1p2True_newCalib
        
        dfFlatEJT['iemBin'] = pd.cut(dfFlatEJT['iem'], bins = energy_bins, labels=labels)
        dfFlatEJT['iem'] = dfFlatEJT.apply(lambda row: math.floor(row['iem'] * SFs[int( abs(row['ieta']) + 28*(row['iemBin']-1) ) -1]), axis=1)
        dfFlatEJT.set_index('uniqueIdx', inplace=True)

    # HCAL cuts depending on energy must come after the ECAL calibration (hoe depends on iem too!!)
    if Hcalcut != "False":
        if Hcalcut == "True":
            Hcalcut_value = 0.95
        else:
            Hcalcut_value = float(Hcalcut)
        print(" ### INFO: Apply H/Tot cut = {}".format(Hcalcut_value))
        group = dfFlatEJT.groupby('uniqueIdx')
        dfFlatEJT['hoe'] = group['hcalET'].sum()/(group['iem'].sum()+group['hcalET'].sum())
        dfFlatEJT = dfFlatEJT[dfFlatEJT['hoe']>float(Hcalcut_value)]

    # [Elena] Training with only jets formad by 10 TT maximum
    if TTNumberCut != False:
        group_jet = dfFlatEJT.groupby('uniqueIdx')
        dfFlatEJT['FiredTTs'] = group_jet['hcalET'].count()
        dfFlatEJT = dfFlatEJT[dfFlatEJT['FiredTTs'] <= 10]
        dfFlatEJT.drop(['FiredTTs'], axis=1, inplace=True)

    # [Elena] Training with only jets formad by 10 TT minimum
    if TTNumberCutInverse != False:
        group_jet = dfFlatEJT.groupby('uniqueIdx')
        dfFlatEJT['FiredTTs'] = group_jet['hcalET'].count()
        dfFlatEJT = dfFlatEJT[dfFlatEJT['FiredTTs'] > 10]
        dfFlatEJT.drop(['FiredTTs'], axis=1, inplace=True)

    # apply HCAL calibration on the fly
    if whichHCALcalib != False:
        print("starting HCAL calibration")
        dfFlatEJT.reset_index(inplace=True)
        
        # get the correct caloParams for the calibration on the fly
        if whichHCALcalib == "oldCalib":
            energy_bins = layer1HCalScaleETBins_oldCalib
            labels = layer1HCalScaleETLabels_oldCalib
            SFs = layer1HCalScaleFactors_oldCalib
        elif whichHCALcalib == "currCalib":
            energy_bins = layer1HCalScaleETBins_currCalib
            labels = layer1HCalScaleETLabels_currCalib
            SFs = layer1HCalScaleFactors_currCalib
        
        dfFlatEJT['ihadBin'] = pd.cut(dfFlatEJT['hcalET'], bins = energy_bins, labels=labels)
        dfFlatEJT['hcalET'] = dfFlatEJT.apply(lambda row: math.floor(row['hcalET'] * SFs[int( abs(row['ieta']) + 40*(row['ihadBin']-1) ) -1]), axis=1)
        dfFlatEJT.set_index('uniqueIdx', inplace=True)

    print("sorting")
    print(dfFlatEJT) # DEBUG
    # sort towers in order to have the first one as the seed (highest iet)
    dfFlatEJT = dfFlatEJT.groupby('uniqueIdx').apply(lambda x: x.sort_values('iet', ascending=False))
    print(dfFlatEJT) # DEBUG

    global n_jets
    n_jets += len(dfFlatEJT.index.unique())
    print("The followings are the first 50 jets:")
    print(dfFlatEJT.index.unique()[:50]) #DEBUG

    # store number of TT fired by the jet
    # dfFlatEJT['nFT'] = dfFlatEJT.groupby('uniqueIdx')['uniqueId'].count()

    # flag to know if the CD is fully contained in the detector or not
    #dfFlatEJT['contained'] = dfFlatEJT.apply(lambda row: 0 if row['jetIeta']<=37 else 1, axis=1)

    print('starting padding') # DEBUG

    # do the padding of the dataframe to have 81 rows for each jet        
    #paddedEJT = padDataFrame(dfFlatEJT)
    #paddedEJT.drop_duplicates(['uniqueId', 'ieta', 'iphi'], keep='first', inplace=True)
    if ClusterFilter:
        paddedEJT = padDataFrameWithZerosMaskedCluster(dfFlatEJT)
    else:
        paddedEJT = padDataFrameWithZeros(dfFlatEJT)

    # avoid problems when the dataframe is empty
    if len(paddedEJT) == 0: return False
    paddedEJT.set_index('uniqueId',inplace=True)

    # subtract iem/ihad to jetPt in oprder to get the correct training Pt to be be used for the NN
    # here the jetPt is already in hardware units so no */2 is needed
    if trainPtVers != False:
        group = paddedEJT.groupby('uniqueId')
        if trainPtVers=="ECAL": paddedEJT['trainingPt'] = group['trainingPt'].mean() - group['hcalET'].sum()
        if trainPtVers=="HCAL": paddedEJT['trainingPt'] = group['trainingPt'].mean() - group['iem'].sum()

    # keep only the jets that have a meaningful trainingPt to be used (this selection should actually be redundant with )
    paddedEJT = paddedEJT[paddedEJT['trainingPt']>=1]

    # shuffle the rows so that no order of the chunky donut gets learned
    paddedEJT.reset_index(inplace=True)
    # remove the shiffling to keep track of the seed for the HCAL rate estimate (from v40)
    # paddedEJT = paddedEJT.sample(frac=1).copy(deep=True)

    dfTowers = paddedEJT[['uniqueId','ieta','iem','hcalET']].copy(deep=True) #'contained', 'nFT'
    dfJets = paddedEJT[['uniqueId','jetPt','jetEta','jetPhi','trainingPt']].copy(deep=True)

    ## DEBUG
    # print(dfFlatEJT)
    # print(dfTowers)
    # print(len(dfTowers.event.unique()), 'events')
    # print(len(dfTowers.uniqueId.unique()), 'jets')
    # print(len(dfTowers), 'rows')
    print('storing')

    # [FIXME] To save space
    # save hdf5 files with dataframe formatted datasets
    # storeT = pd.HDFStore(saveToDFs['towers']+'.hdf5', mode='w')
    # storeT['towers'] = dfTowers
    # storeT.close()

    # storeJ = pd.HDFStore(saveToDFs['jets']+'.hdf5', mode='w')
    # storeJ['jets'] = dfJets
    # storeJ.close()

    ## DEBUG
    print('starting one hot encoding')

    # define some variables on top
    dfTowers['ieta'] = abs(dfTowers['ieta'])
    dfTowers['iesum'] = dfTowers['iem'] + dfTowers['hcalET']
    dfE = dfTowers[['uniqueId', 'ieta', 'iem', 'hcalET', 'iesum']] #'contained', 'nFT'

    # set the uniqueId indexing
    dfE.set_index('uniqueId',inplace=True)
    dfJets.drop_duplicates('uniqueId', keep='first', inplace=True)
    dfJets.set_index('uniqueId', inplace=True)

    if not applyOnTheFly:
        # do the one hot encoding of ieta
        dfEOneHotEncoded = pd.get_dummies(dfE, columns=['ieta'])
        # pad the values of ieta that might be missing from the OHE
        for i in list(TowersEta.keys()):
            if 'ieta_'+str(i) not in dfEOneHotEncoded:
                dfEOneHotEncoded['ieta_'+str(i)] = 0
        dfEOneHotEncoded = dfEOneHotEncoded[['iem', 'hcalET', 'iesum', 'ieta_1', 'ieta_2', 'ieta_3', 'ieta_4', 'ieta_5', 'ieta_6', 'ieta_7', 'ieta_8', 'ieta_9', 'ieta_10', 'ieta_11', 'ieta_12', 'ieta_13', 'ieta_14', 'ieta_15', 'ieta_16', 'ieta_17', 'ieta_18', 'ieta_19', 'ieta_20', 'ieta_21', 'ieta_22', 'ieta_23', 'ieta_24', 'ieta_25', 'ieta_26', 'ieta_27', 'ieta_28', 'ieta_30', 'ieta_31', 'ieta_32', 'ieta_33', 'ieta_34', 'ieta_35', 'ieta_36', 'ieta_37', 'ieta_38', 'ieta_39', 'ieta_40', 'ieta_41']]#, 'contained', 'nFT']]
    else:
        dfEOneHotEncoded = dfE.copy(deep=True)

    # add this not to bias input to the NN
    # print('\n### BEFORE:',dfEOneHotEncoded.loc[dfEOneHotEncoded['hcalET'] == 0, 'ieta_1':'ieta_41'].max()) #DEBUG
    if options.type == 'jet':
        dfEOneHotEncoded.loc[dfEOneHotEncoded['hcalET'] == 0, 'ieta_1':'ieta_41'] = 0
    if options.type == 'ele':
        dfEOneHotEncoded.loc[dfEOneHotEncoded['iem'] == 0, 'ieta_1':'ieta_41'] = 0
    # print('\n### AFTER:',dfEOneHotEncoded.loc[dfEOneHotEncoded['hcalET'] == 0, 'ieta_1':'ieta_41'].max()) #DEBUG


    ## DEBUG
    print('starting tensorisation')

    # convert to tensor
    Y = np.array([dfJets.loc[i].values for i in dfJets.index])
    X = np.array([dfEOneHotEncoded.loc[i].to_numpy() for i in dfE.index.drop_duplicates(keep='first')])

    if flattenEtaDistribution != False:
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

    ## DEBUG
    # if len(X != 43): 
    #     print('Different lenght!')
    print('storing')

    # save .npz files with tensor formatted datasets
    np.savez_compressed(saveToTensors['towers']+'.npz', X)
    np.savez_compressed(saveToTensors['jets']+'.npz', Y)

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

if __name__ == "__main__" :

    parser = OptionParser()
    parser.add_option("--fin",         dest="fin",         default='')
    parser.add_option("--fout",        dest="fout",        default='')
    parser.add_option("--target",      dest="target",      default='')
    parser.add_option("--type",        dest="type",        default='')
    parser.add_option("--chunk_size",  dest="chunk_size",  default=5000,  type=int)
    parser.add_option("--calibrateECAL", dest="calibrateECAL", default=False, help="oldCalib or newCalib; not specified == noCalib")
    parser.add_option("--calibrateHCAL", dest="calibrateHCAL", default=False, help="oldCalib or newCalib; not specified == noCalib")
    parser.add_option("--trainPtVers", dest="trainPtVers", default=False)
    parser.add_option("--uJetPtCut",   dest="uJetPtCut",   default=False)
    parser.add_option("--lJetPtCut",   dest="lJetPtCut",   default=False)
    parser.add_option("--etacut",      dest="etacut",      default=False)
    parser.add_option("--etacutmin",   dest="etacutmin",   default=False)
    parser.add_option("--applyCut_3_6_9",     dest="applyCut_3_6_9",     default=False)
    parser.add_option("--ecalcut",     dest="ecalcut",     default="False",  type=str)
    parser.add_option("--hcalcut",     dest="hcalcut",     default="False",  type=str)
    parser.add_option("--HoTotcut",    dest="HoTotcut",    default=False)
    parser.add_option("--TTNumberCut", dest="TTNumberCut", default=False)
    parser.add_option("--TTNumberCutInverse", dest="TTNumberCutInverse", default=False)
    parser.add_option("--flattenPtDistribution",     dest="flattenPtDistribution",     default=False)
    parser.add_option("--flattenEtaDistribution",     dest="flattenEtaDistribution",     default=False)
    parser.add_option("--applyOnTheFly", dest="applyOnTheFly", default=False)
    parser.add_option("--ClusterFilter", dest="ClusterFilter", default=False)
    parser.add_option("--applyZS",       dest="applyZS",       default=False)
    parser.add_option("--LooseEle",      dest="LooseEle", action='store_true', default=False)
    parser.add_option("--PuppiJet",      dest="PuppiJet", action='store_true', default=False)
    (options, args) = parser.parse_args()

    if (options.fin=='' or options.fout=='' or options.target=='' or options.type==''): print('** ERROR: wrong input options --> EXITING!!'); exit()

    keyEvents = "l1EventTree/L1EventTree"
    branchesEvents = ["Event/event"]

    keyTowers = "l1CaloTowerEmuTree/L1CaloTowerTree"
    branchesTowers = ["L1CaloTower/ieta", "L1CaloTower/iphi", "L1CaloTower/iem", "L1CaloTower/ihad", "L1CaloTower/iet"]

    if options.target == 'reco':
        if options.type == 'ele':
            keyTarget = "l1ElectronRecoTree/ElectronRecoTree"
            branchesTarget = ["Electron/eta", "Electron/phi", "Electron/et", "Electron/isLooseElectron"]
            energy = b'et'
            eta = b'eta'
            phi = b'phi'

        if options.type == 'jet':
            if options.PuppiJet:
                keyTarget = "l1JetRecoTree/JetRecoTree"
                branchesTarget = ["Jet/puppi_eta", "Jet/puppi_phi", "Jet/puppi_etCorr"]
                energy = b'puppi_etCorr'
                eta = b'puppi_eta'
                phi = b'puppi_phi'
            else:
                keyTarget = "l1JetRecoTree/JetRecoTree"
                branchesTarget = ["Jet/eta", "Jet/phi", "Jet/etCorr"]
                energy = b'etCorr'
                eta = b'eta'
                phi = b'phi'

    if options.target == 'gen':
        keyTarget = "l1GeneratorTree/L1GenTree"
        branchesTarget = ["Generator/jetEta", "Generator/jetPhi", "Generator/jetPt"]
        energy = b'jetPt'
        eta = b'jetEta'
        phi = b'jetPhi'

    if options.target == 'emu':
        keyTarget = "l1UpgradeEmuTree/L1UpgradeTree"
        branchesTarget = ["L1Upgrade/jetEta", "L1Upgrade/jetPhi", "L1Upgrade/jetEt"]
        energy = b'jetEt'
        eta = b'jetEta'
        phi = b'jetPhi'

    if options.target == 'reco_corr':
        if options.type == 'jet':
            keyTarget = "l1JetRecoTree/JetRecoTree"
            branchesTarget = ["Jet/eta", "Jet/phi", "Jet/PtHCAL", "Jet/HoTot"] #PtHCAL is defined as etCorr - ecalEnergy
            energy = b'PtHCAL'
            eta = b'eta'
            phi = b'phi'
        if options.type == 'ele':
            sys.exit('This is not implemented yet')

    if options.target == 'rate':
        if options.type == 'jet':
            sys.exit('This is not implemented yet')
        if options.type == 'ele':
            keyTarget = "l1UpgradeEmuTree/L1UpgradeTree"
            branchesTarget = ["L1Upgrade/egEt", "L1Upgrade/egEta", "L1Upgrade/egPhi", "L1Upgrade/egShape", "L1Upgrade/egTowerIEta", "L1Upgrade/egTowerIPhi"]
            energy = b'egEt'
            eta = b'egEta'
            phi = b'egPhi'

    InFile = uproot3.open(options.fin)

    eventsTree = InFile[keyEvents]
    towersTree = InFile[keyTowers]
    targetTree = InFile[keyTarget]

    del InFile

    arrEvents = eventsTree.arrays(branchesEvents)
    arrTowers = towersTree.arrays(branchesTowers)
    arrTarget = targetTree.arrays(branchesTarget)

    del eventsTree, towersTree, targetTree

    dfE = pd.DataFrame(arrEvents)
    dfT = pd.DataFrame(arrTowers)
    dfJ = pd.DataFrame(arrTarget)

    del arrEvents, arrTowers, arrTarget

    dfET = pd.concat([dfE, dfT], axis=1)
    dfEJ = pd.concat([dfE, dfJ], axis=1)
    dfET = dfET.dropna(axis=0)
    dfEJ = dfEJ.dropna(axis=0)

    n_events = len(dfE[b'event'].unique())

    del dfE, dfT, dfJ

    # index of rhe Ntuple as tag
    tag = '_'+options.fin.split('/Ntuple_')[1]
    tag = tag.split('.')[0]

    j = 0
    for ET, EJ in zip(chunker(dfET, options.chunk_size),chunker(dfEJ, options.chunk_size)):
        # flatten out the dataframes so that each entry of the dataframe is a number and not a vector
        dfFlatET = pd.DataFrame({
            'event': np.repeat(ET[b'event'].values, ET[b'ieta'].str.len()), # event IDs are copied to keep proper track of what is what
            'ieta': list(chain.from_iterable(ET[b'ieta'])),
            'iphi': list(chain.from_iterable(ET[b'iphi'])),
            'iem' : list(chain.from_iterable(ET[b'iem'])),
            'ihad': list(chain.from_iterable(ET[b'ihad'])),
            'iet' : list(chain.from_iterable(ET[b'iet']))
            })

        if options.target == 'reco_corr': #[FIXME] In this option the L1Ntuples contain the HoTot information for the cut
            dfFlatEJ = pd.DataFrame({
                'event': np.repeat(EJ[b'event'].values, EJ[eta].str.len()), # event IDs are copied to keep proper track of what is what
                'jetEta': list(chain.from_iterable(EJ[eta])),
                'jetPhi': list(chain.from_iterable(EJ[phi])),
                'jetPt' : list(chain.from_iterable(EJ[energy])),
                'HoTot' : list(chain.from_iterable(EJ[b'HoTot'])),
                })
            
        if options.target == 'rate':
            dfFlatEJ = pd.DataFrame({
                'event': np.repeat(EJ[b'event'].values, EJ[eta].str.len()), # event IDs are copied to keep proper track of what is what
                'jetEta': list(chain.from_iterable(EJ[eta])),
                'jetPhi': list(chain.from_iterable(EJ[phi])),
                'jetPt' : list(chain.from_iterable(EJ[energy])),
                'jetShape' : list(chain.from_iterable(EJ[b'egShape'])),
                'TowerIeta' : list(chain.from_iterable(EJ[b'egTowerIEta'])),
                'TowerIphi' : list(chain.from_iterable(EJ[b'egTowerIPhi'])),
                })
            
        if options.target == 'reco' and options.type == 'ele' and options.LooseEle:
            dfFlatEJ = pd.DataFrame({
                'event': np.repeat(EJ[b'event'].values, EJ[eta].str.len()), # event IDs are copied to keep proper track of what is what
                'jetEta': list(chain.from_iterable(EJ[eta])),
                'jetPhi': list(chain.from_iterable(EJ[phi])),
                'jetPt' : list(chain.from_iterable(EJ[energy])),
                'LooseEle' : list(chain.from_iterable(EJ[b'isLooseElectron']))
                })            
            
        else:
            dfFlatEJ = pd.DataFrame({
                'event': np.repeat(EJ[b'event'].values, EJ[eta].str.len()), # event IDs are copied to keep proper track of what is what
                'jetEta': list(chain.from_iterable(EJ[eta])),
                'jetPhi': list(chain.from_iterable(EJ[phi])),
                'jetPt' : list(chain.from_iterable(EJ[energy]))
                })

        # define the paths where to save the hdf5 files
        saveToDFs = {
            'towers'  : options.fout+'/dataframes/towers'+tag+'_'+str(j),
            'jets'    : options.fout+'/dataframes/jets'+tag+'_'+str(j)
        }
        # define the two paths where to save the hdf5 files
        saveToTensors = {
            'towers'  : options.fout+'/tensors/towers'+tag+'_'+str(j),
            'jets'    : options.fout+'/tensors/jets'+tag+'_'+str(j)
        }

        j += 1

        mainReader( dfFlatET, dfFlatEJ, saveToDFs, saveToTensors, options.uJetPtCut, options.lJetPtCut, options.etacut, options.etacutmin, options.applyCut_3_6_9, \
                    options.ecalcut, options.hcalcut, options.HoTotcut, options.TTNumberCut, options.TTNumberCutInverse, options.trainPtVers, \
                    options.calibrateECAL, options.calibrateHCAL, options.flattenPtDistribution, options.flattenEtaDistribution, options.applyOnTheFly, \
                    options.ClusterFilter, options.applyZS, options.LooseEle)

    print("\nNumber of events = ", n_events)
    print("Number of jets passing reader conditions = ", n_jets)
    print("Mismatched = ", n_mismatch)
    print("DONE!")

