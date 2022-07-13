from optparse import OptionParser
from caloParamsOnTheFly import *
from itertools import chain
from TowerGeometry import *
import pandas as pd
import numpy as np
import math
import os


import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import mplhep
plt.style.use(mplhep.style.CMS)

def colorbar_index(ncolors, cmap, label):
    cmap = cmap_discretize(cmap, ncolors)
    mappable = cm.ScalarMappable(cmap=cmap)
    mappable.set_array([])
    mappable.set_clim(-0.5, ncolors+0.5)
    colorbar = plt.colorbar(mappable, label=label)
    
    if ncolors > 10:
        nticks = 10
        colorbar.set_ticks(np.linspace(0, ncolors, nticks))
        colorbar.set_ticklabels(np.linspace(0, ncolors-1, nticks).astype('int64'))
        colorbar.ax.tick_params(which='minor', width=0, length=0)
    else:
        colorbar.set_ticks(np.linspace(0, ncolors, ncolors))
        colorbar.set_ticklabels(range(ncolors))
        colorbar.ax.tick_params(which='minor', width=0, length=0)

def cmap_discretize(cmap, N):
    """Return a discrete colormap from the continuous colormap cmap.

        cmap: colormap instance, eg. cm.jet. 
        N: number of colors.

    Example
        x = resize(arange(100), (5,100))
        djet = cmap_discretize(cm.jet, 5)
        imshow(x, cmap=djet)
    """

    if type(cmap) == str:
        cmap = plt.get_cmap(cmap)
    colors_i = np.concatenate((np.linspace(0, 1., N), (0.,0.,0.,0.)))
    colors_rgba = cmap(colors_i)
    indices = np.linspace(0, 1., N+1)
    cdict = {}
    for ki,key in enumerate(('red','green','blue')):
        cdict[key] = [ (indices[i], colors_rgba[i-1,ki], colors_rgba[i,ki])
                       for i in range(N+1) ]
    # Return colormap object.
    return mcolors.LinearSegmentedColormap(cmap.name + "_%d"%N, cdict, 1024)

def deltarSafeSelect( df, dRcut ):
    deta = np.abs(df['jetEta'] - df['jetEta_joined'])
    dphi = np.abs(df['jetPhi'] - df['jetPhi_joined'])
    sel = dphi > np.pi
    dphi = np.abs(sel*(2*np.pi) - dphi)
    return (np.sqrt(dphi*dphi+deta*deta) > dRcut) | ((deta == 0) & (dphi == 0))

def deltarMatchSelect( df, dRcut ):
    deta = np.abs(df['jetEta'] - df['jetEta_joined'])
    dphi = np.abs(df['jetPhi'] - df['jetPhi_joined'])
    sel = dphi > np.pi
    dphi = np.abs(sel*(2*np.pi) - dphi)
    return np.sqrt(dphi*dphi+deta*deta) < dRcut


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
            # nTT = dfFlatEJT['nTT'][uniqueIdx].unique()[0]
        except TypeError:
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx]
            trainingPt = dfFlatEJT['trainingPt'][uniqueIdx]
            jetEta = dfFlatEJT['jetEta'][uniqueIdx]
            jetPhi = dfFlatEJT['jetPhi'][uniqueIdx]
            # nTT = dfFlatEJT['nTT'][uniqueIdx]

        padder = pd.DataFrame(columns=dfFlatEJT.columns, index=range(0,81))
        padder['uniqueId'] = uniqueIdx
        padder['jetPt'] = jetPt
        padder['trainingPt'] = trainingPt
        padder['jetEta'] = jetEta
        padder['jetPhi'] = jetPhi
        padder['jetIeta'] = jetIeta
        padder['jetIphi'] = jetIphi
        # padder['nTT'] = nTT
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
            # nTT = dfFlatEJT['nTT'][uniqueIdx].unique()[0]
            # contained = dfFlatEJT['contained'][uniqueIdx].unique()[0]
        except TypeError:
            N = 1
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx]
            trainingPt = dfFlatEJT['trainingPt'][uniqueIdx]
            jetEta = dfFlatEJT['jetEta'][uniqueIdx]
            jetPhi = dfFlatEJT['jetPhi'][uniqueIdx]
            # nTT = dfFlatEJT['nTT'][uniqueIdx]
            # contained = dfFlatEJT['contained'][uniqueIdx]

        padder = pd.DataFrame(columns=dfFlatEJT.columns, index=range(0,81-N))
        padder['uniqueId'] = uniqueIdx
        padder['jetPt'] = jetPt
        padder['trainingPt'] = trainingPt
        padder['jetEta'] = jetEta
        padder['jetPhi'] = jetPhi
        padder['jetIeta'] = jetIeta
        padder['jetIphi'] = jetIphi
        # padder['nTT'] = nTT
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

def fakeJetsCreator( dfEJNew, dfFlatEJOld ):
    dfFlatEJNew = pd.DataFrame({
        'eventNew': np.repeat(dfEJNew[b'event'].values, dfEJNew[b'jetEta'].str.len()), # event IDs are copied to keep proper track of what is what
        'jetEta': list(chain.from_iterable(dfEJNew[b'jetEta'])),
        'jetPhi': list(chain.from_iterable(dfEJNew[b'jetPhi'])),
        'jetNewPt' : list(chain.from_iterable(dfEJNew[b'jetEt']))
        })

    dfFlatEJNew.sort_values(['jetEta','jetPhi'], inplace=True)
    dfFlatEJNew.set_index(['jetEta','jetPhi'], inplace=True)
    dfFlatEJOld.set_index(['jetEta','jetPhi'], inplace=True)
    dfFlatJoined  = pd.concat([dfFlatEJNew,dfFlatEJOld], axis=1, sort=False)
    dfFlatJoined.reset_index(inplace=True)

    dfFlatJoined.drop(['event', 'jetNewPt'], axis=1, inplace=True)
    dfFlatJoined.rename({'eventNew' : 'event'}, axis=1, inplace=True)
    dfFlatJoined.fillna(-99.9, inplace=True)

    return dfFlatJoined

def mainReader( dfET, dfEJ, uJetPtcut, lJetPtcut, iEtacut, applyCut_3_6_9, Ecalcut, Hcalcut, trainingPtVersion, whichECALcalib, whichHCALcalib, flattenPtDistribution, applyOnTheFly, makeNewFakes, dfEJNewForFakes):
    if len(dfET) == 0 or len(dfEJ) == 0:
        print(' ** WARNING: Zero data here --> EXITING!\n')
        return

    print('starting flattening') # DEBUG

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
        'jetPt' : list(chain.from_iterable(dfEJ[b'jetEt']))
        })

    dfFlatEJ.sort_values(['jetEta','jetPhi'], inplace=True)
    dfFlatEJ.reset_index(inplace=True)
    dfFlatEJ.drop('index', axis=1, inplace=True)

    if makeNewFakes: dfFlatEJ = fakeJetsCreator(dfEJNewForFakes, dfFlatEJ)

    dfFlatEJ['jetId'] = dfFlatEJ.index # each jet gets an identifier based on a progressive value independent of event -> this allows further flexibility of ID on top of event

    #########################################################################
    ########################## Application of cuts ##########################

    print('starting cuts') # DEBUG

    # Apply cut on jetPt
    if uJetPtcut != False:
        dfFlatEJ = dfFlatEJ[dfFlatEJ['jetPt'] < float(uJetPtcut)]
    if lJetPtcut != False:
        dfFlatEJ = dfFlatEJ[dfFlatEJ['jetPt'] > float(lJetPtcut)]

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
        dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 26) & (dfFlatET['iem'] < 3)].index, inplace = True)
        dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 27) & (dfFlatET['iem'] < 6)].index, inplace = True)
        dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 28) & (dfFlatET['iem'] < 9)].index, inplace = True)

    # Define overall hcalET information, ihad for ieta < 29 and iet for ieta > 29
    dfFlatET['hcalET'] = dfFlatET['ihad']*(np.abs(dfFlatET['ieta'])<29) + dfFlatET['iet']*(np.abs(dfFlatET['ieta'])>29)

    # reset indeces to be the event number to be able to join the DFs later
    dfFlatET.set_index('event', inplace=True)
    dfFlatEJ.set_index('event', inplace=True)

    #########################################################################
    #########################################################################

    ## DEBUG
    # print(dfET.shape[0])
    # print(dfEJ.shape[0])
    # print(dfFlatEJ.shape[0])
    # dfFlatET = dfFlatET.head(100).copy(deep=True)
    # dfFlatEJ = dfFlatEJ.head(5000).copy(deep=True)
    print('starting dR rejection')

    # cerate all the possible combinations of jets per each event
    dfFlatEJ  = dfFlatEJ.join(dfFlatEJ, on='event', how='left', rsuffix='_joined', sort=False)
    # select only those jets that are at least dRcut away from each other
    dRcut = 0.5
    dfFlatEJ['dRsafe'] = deltarSafeSelect(dfFlatEJ, dRcut)
    notSafe = list(dfFlatEJ[(dfFlatEJ['dRsafe']==False)]['jetId'])
    dfFlatEJ = dfFlatEJ[dfFlatEJ.jetId.isin(notSafe) == False]
    dfFlatEJ.drop(['jetEta_joined', 'jetPhi_joined', 'jetPt_joined', 'jetId_joined', 'dRsafe'], axis=1, inplace=True) # drop columns not needed anymore
    dfFlatEJ.drop_duplicates('jetId', keep='first', inplace=True) # drop duplicates of teh jets

    ## DEBUG
    print('starting conversion eta/phi->ieta/iphi')

    # find ieta/iphi values for the jets
    FindIeta_vctd = np.vectorize(FindIeta)
    FindIphi_vctd = np.vectorize(FindIphi)
    dfFlatEJ['jetIeta'] = FindIeta_vctd(dfFlatEJ['jetEta'])
    dfFlatEJ['jetIphi'] = FindIphi_vctd(dfFlatEJ['jetPhi'])

    # For ECAL/HCAL we consider just jets having a chunky donuts completely inside the ECAL/HCAL detector
    if iEtacut != False:
        dfFlatEJ = dfFlatEJ[abs(dfFlatEJ['jetIeta']) <= int(iEtacut)]

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

    if Ecalcut != False:
        # drop all photons that have a deposit in HF
        dfFlatEJT.drop(dfFlatEJT[(dfFlatEJT['iet']>0)&(dfFlatEJT['ieta']>=30)].index, inplace=True)

        # drop all photons for which E/(E+H)<0.8
        group = dfFlatEJT.groupby('uniqueIdx')
        dfFlatEJT['eoh'] = group['iem'].sum()/(group['iem'].sum()+group['hcalET'].sum())
        dfFlatEJT = dfFlatEJT[dfFlatEJT['eoh']>0.8]

    # apply ECAL calibration on the fly
    if whichECALcalib != False:
        print("starting ECAL calibration")
        dfFlatEJT.reset_index(inplace=True)
        
        # get the correct caloParams for the calibration on the fly
        if whichECALcalib == "oldCalib":
            energy_bins = layer1ECalScaleETBins_oldCalib
            labels = layer1ECalScaleETLabels_oldCalib
            SFs = layer1ECalScaleFactors_oldCalib
        elif whichECALcalib == "newCalib":
            energy_bins = layer1ECalScaleETBins_newCalib
            labels = layer1ECalScaleETLabels_newCalib
            SFs = layer1ECalScaleFactors_newCalib
        
        dfFlatEJT['iemBin'] = pd.cut(dfFlatEJT['iem'], bins = energy_bins, labels=labels)
        dfFlatEJT['iem'] = dfFlatEJT.apply(lambda row: math.floor(row['iem'] * SFs[int( abs(row['ieta']) + 28*(row['iemBin']-1) ) -1]), axis=1)
        dfFlatEJT.set_index('uniqueIdx', inplace=True)

    # HCAL cuts depending on energy must come after the ECAL calibration (hoe depends on iem too!!)
    if Hcalcut != False:
        group = dfFlatEJT.groupby('uniqueIdx')
        dfFlatEJT['hoe'] = group['hcalET'].sum()/(group['iem'].sum()+group['hcalET'].sum())
        dfFlatEJT = dfFlatEJT[dfFlatEJT['hoe']>0.95]

    # apply HCAL calibration on the fly
    if whichHCALcalib != False:
        print("starting HCAL calibration")
        dfFlatEJT.reset_index(inplace=True)
        
        # get the correct caloParams for the calibration on the fly
        if whichHCALcalib == "oldCalib":
            energy_bins = layer1HCalScaleETBins_oldCalib
            labels = layer1HCalScaleETLabels_oldCalib
            SFs = layer1HCalScaleFactors_oldCalib
        elif whichHCALcalib == "newCalib":
            energy_bins = layer1HCalScaleETBins_newCalib
            labels = layer1HCalScaleETLabels_newCalib
            SFs = layer1HCalScaleFactors_newCalib
        
        dfFlatEJT['ihadBin'] = pd.cut(dfFlatEJT['hcalET'], bins = energy_bins, labels=labels)
        dfFlatEJT['hcalET'] = dfFlatEJT.apply(lambda row: math.floor(row['hcalET'] * SFs[int( abs(row['ieta']) + 40*(row['ihadBin']-1) ) -1]), axis=1)
        dfFlatEJT.set_index('uniqueIdx', inplace=True)

    print('starting padding') # DEBUG
    paddedEJT = padDataFrame(dfFlatEJT)
    paddedEJT.drop_duplicates(['uniqueId', 'ieta', 'iphi'], keep='first', inplace=True)
    paddedEJT.set_index('uniqueId',inplace=True)

    return paddedEJT

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 batchReader.py --fin <fileIN_path> --tag <batch_tag> --fout <fileOUT_path> [--jetcut 60 --etacut 24]
### OR
### python batchSubmitOnTier3.py (after appropriate modifications)

if __name__ == "__main__" :

    parser = OptionParser()
    parser.add_option("--fin",         dest="fin",         default='')
    parser.add_option("--tag",         dest="tag",         default='')
    parser.add_option("--fout",        dest="fout",        default='')
    parser.add_option("--calibrateECAL", dest="calibrateECAL", default=False, help="oldCalib or newCalib; not specified == noCalib")
    parser.add_option("--calibrateHCAL", dest="calibrateHCAL", default=False, help="oldCalib or newCalib; not specified == noCalib")
    parser.add_option("--trainPtVers", dest="trainPtVers", default=False)
    parser.add_option("--uJetPtCut",   dest="uJetPtCut",   default=False)
    parser.add_option("--lJetPtCut",   dest="lJetPtCut",   default=False)
    parser.add_option("--etacut",      dest="etacut",      default=False)
    parser.add_option("--applyCut_3_6_9",     dest="applyCut_3_6_9",     default=False)
    parser.add_option("--ecalcut",     dest="ecalcut",     default=False)
    parser.add_option("--hcalcut",     dest="hcalcut",     default=False)
    parser.add_option("--flattenPtDistribution",     dest="flattenPtDistribution",     default=False)
    parser.add_option("--applyOnTheFly", dest="applyOnTheFly", default=False)
    parser.add_option("--makeNewFakes", dest="makeNewFakes", default=False)
    parser.add_option("--dfEJNewForFakes", dest="dfEJNewForFakes", default='')
    (options, args) = parser.parse_args()

    if (options.fin=='' or options.tag=='' or options.fout==''): print('** ERROR: wrong input options --> EXITING!!'); exit()

    # define the two paths where to read the hdf5 files
    readfrom = {
        'towers'  : options.fin+'/towers/towers'+options.tag,
        'jets'    : options.fin+'/jets/jets'+options.tag
    }

    readfromForFakes = {
        'towers'  : options.dfEJNewForFakes+'/towers/towers'+options.tag,
        'jets'    : options.dfEJNewForFakes+'/jets/jets'+options.tag
    }

    print(readfrom['towers']+'.hdf5')

    # read hdf5 files
    readT = pd.HDFStore(readfrom['towers']+'.hdf5', mode='r')
    dfET = readT['towers']
    readT.close()

    readJ = pd.HDFStore(readfrom['jets']+'.hdf5', mode='r')
    dfEJ = readJ['jets']
    readJ.close()

    nEvents = 1
    dfET = dfET.head(nEvents)
    dfEJ = dfEJ.head(nEvents)
    
    dfEJNewForFakes = 0
    if options.makeNewFakes:
        readJNewForFakes = pd.HDFStore(readfromForFakes['jets']+'.hdf5', mode='r')
        dfEJNewForFakes = readJNewForFakes['jets']
        readJNewForFakes.close()
        dfEJNewForFakes = dfEJNewForFakes.head(nEvents)

    dfEJT = mainReader(dfET, dfEJ, options.uJetPtCut, options.lJetPtCut, options.etacut, options.applyCut_3_6_9, options.ecalcut, options.hcalcut, options.trainPtVers, options.calibrateECAL, options.calibrateHCAL, options.flattenPtDistribution, options.applyOnTheFly, options.makeNewFakes, dfEJNewForFakes)

    # pd.set_option('display.max_rows', 81)
    # print(dfEJT)
    # exit()

    os.system('mkdir -p '+options.fout)
    for ID in dfEJT.index.unique():

        # if ID != '3807006_20': continue

        tmp = dfEJT[dfEJT.index==ID].sort_values(['ieta','iphi'])

        if ( (72 in dfEJT[dfEJT.index==ID]['iphi'].unique()) and (1 in dfEJT[dfEJT.index==ID]['iphi'].unique()) ):
            tmpA = tmp[tmp['iphi']>=65].sort_values(['ieta','iphi'])
            tmpB = tmp[tmp['iphi']<=64].sort_values(['ieta','iphi'])

            tmp = pd.concat([tmpA,tmpB], sort=False)
            tmp.sort_values('ieta', inplace=True, kind='mergesort')

        pt9x9 = tmp['iet'].sum()
        jetpt = tmp['jetPt'].unique()
        jeteta = tmp['jetEta'].unique()
        jetphi = tmp['jetPhi'].unique()

        HADdeposit = tmp['hcalET'].to_numpy().reshape(9,9)
        EMdeposit = tmp['iem'].to_numpy().reshape(9,9)

        HADcmap = cm.get_cmap('Blues')
        EMcmap = cm.get_cmap('Reds')

        HADcolorbarTicks = [0,tmp['hcalET'].max()]
        EMcolorbarTicks = [0,tmp['iem'].max()]

        etalabels = tmp['ieta'].unique()
        philabels = tmp['iphi'].unique()

        props = dict(boxstyle='square', facecolor='white')
        textstr1 = '\n'.join((
            r'$E_T^{9\times9}=%.0f$' % (pt9x9, ) ,
            r'$p_T^{L1}=%.2f$ GeV' % (jetpt, ) if jetpt!=-99.9 else r'$p_T^{L1}=Nan$ GeV',
            r'$\eta^{L1}=%.2f$' % (jeteta, ) if jetpt!=-99.9 else r'$\eta^{L1}=Nan$',
            r'$\phi^{L1}=%.2f$' % (jetphi, ) if jetpt!=-99.9 else r'$\phi^{L1}=Nan$'))

        plt.figure(figsize=(10,8))
        im = plt.pcolormesh(EMdeposit, cmap=EMcmap, edgecolor='black', vmin=0)
        
        ncolors = max(2,tmp['iem'].max()+1)
        colorbar = plt.colorbar(im, label='iem')
        plt.clim(0., ncolors+0.5)
        if ncolors > 10:
            nticks = 10
            colorbar.set_ticks(np.linspace(0, ncolors, nticks))
            colorbar.set_ticklabels(np.linspace(0, ncolors, nticks).astype('int64'))
            colorbar.ax.tick_params(which='minor', width=0, length=0)
        else:
            colorbar.set_ticks(np.linspace(0, ncolors, ncolors))
            colorbar.set_ticklabels(range(ncolors))
            colorbar.ax.tick_params(which='minor', width=0, length=0)

        # colorbar_index(ncolors=max(2,tmp['iem'].max()+1), cmap=EMcmap, label='iem') # for discretized colorbar
        for i in range(EMdeposit.shape[0]):
            for j in range(EMdeposit.shape[1]):
                if EMdeposit[i, j] > 0: plt.text(j+0.5, i+0.5, format(EMdeposit[i, j], '.0f'), ha="center", va="center", fontsize=14, color='white' if EMdeposit[i, j] > tmp['iem'].max()*0.8 else "black")
        plt.xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5], etalabels)
        plt.yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5], philabels)
        plt.tick_params(which='both', width=0, length=0)
        plt.xlabel(f'$i\eta$')
        plt.ylabel(f'$i\phi$')
        plt.text(0.2, 8.8, textstr1, fontsize=14, verticalalignment='top',  bbox=props)
        mplhep.cms.label('', data=False, rlabel='14 TeV')
        plt.savefig(options.fout+'/'+ID+'_EMdeposit.pdf')
        plt.close()
        
        plt.figure(figsize=(10,8))
        im = plt.pcolormesh(HADdeposit, cmap=HADcmap, edgecolor='black', vmin=0)
        
        ncolors = max(2,tmp['hcalET'].max()+1)
        colorbar = plt.colorbar(im, label='ihad')
        plt.clim(-0.5, ncolors+0.5)
        if ncolors > 10:
            nticks = 10
            colorbar.set_ticks(np.linspace(0, ncolors, nticks))
            colorbar.set_ticklabels(np.linspace(0, ncolors-1, nticks).astype('int64'))
            colorbar.ax.tick_params(which='minor', width=0, length=0)
        else:
            colorbar.set_ticks(np.linspace(0, ncolors, ncolors))
            colorbar.set_ticklabels(range(ncolors))
            colorbar.ax.tick_params(which='minor', width=0, length=0)

        # colorbar_index(ncolors=max(2,tmp['hcalET'].max()+1), cmap=HADcmap, label='ihad') # for discretized colorbar
        for i in range(HADdeposit.shape[0]):
            for j in range(HADdeposit.shape[1]):
                if HADdeposit[i, j] > 0: plt.text(j+0.5, i+0.5, format(HADdeposit[i, j], '.0f'), ha="center", va="center", fontsize=14, color='white' if HADdeposit[i, j] > tmp['hcalET'].max()*0.8 else "black")
        plt.xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5], etalabels)
        plt.yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5], philabels)
        plt.tick_params(which='both', width=0, length=0)
        plt.xlabel(f'$i\eta$')
        plt.ylabel(f'$i\phi$')
        plt.text(0.2, 8.8, textstr1, fontsize=14, verticalalignment='top',  bbox=props)
        mplhep.cms.label('', data=False, rlabel='14 TeV')
        plt.savefig(options.fout+'/'+ID+'_HADdeposit.pdf')
        plt.close()
       