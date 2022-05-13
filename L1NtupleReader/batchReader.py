from optparse import OptionParser
from caloParamsOnTheFly import *
from itertools import chain
from TowerGeometry import *
import pandas as pd
import numpy as np
import os


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
            jetEta = dfFlatEJT['jetEta'][uniqueIdx].unique()[0]
            jetPhi = dfFlatEJT['jetPhi'][uniqueIdx].unique()[0]
        except TypeError:
            jetIeta = dfFlatEJT['jetIeta'][uniqueIdx]
            jetIphi = dfFlatEJT['jetIphi'][uniqueIdx]
            jetPt = dfFlatEJT['jetPt'][uniqueIdx]
            jetEta = dfFlatEJT['jetEta'][uniqueIdx]
            jetPhi = dfFlatEJT['jetPhi'][uniqueIdx]

        padder = pd.DataFrame(columns=dfFlatEJT.columns, index=range(0,81))
        padder['uniqueId'] = uniqueIdx
        padder['jetPt'] = jetPt
        padder['jetEta'] = jetEta
        padder['jetPhi'] = jetPhi
        padder['jetIeta'] = jetIeta
        padder['jetIphi'] = jetIphi
        padder['iem'] = 0
        padder['ihad'] = 0
        padder['iet'] = 0
        padder['hcalET'] = 0
        padder[['ieta','iphi']] = ChunkyDonutTowers(jetIeta,jetIphi)

        padded = padded.append(padder)
        del padder
        
    return padded


def mainReader( dfET, dfEJ, saveToDFs, saveToTensors, uJetPtcut, lJetPtcut, iEtacut, Ecalcut, trainingPtVersion, whichECALcalib):
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
        'jetPt' : list(chain.from_iterable(dfEJ[b'jetPt']))
        })
    dfFlatEJ['jetId'] = dfFlatEJ.index # each jet gets an identifier based on a progressive value independent of event -> this allows further flexibility of ID on top of event

    #########################################################################
    ########################## Application of cuts ##########################

    print('starting cuts') # DEBUG

    # Apply cut on jetPt
    if uJetPtcut != False:
        dfFlatEJ = dfFlatEJ[dfFlatEJ['jetPt'] < float(uJetPtcut)]
    if lJetPtcut != False:
        dfFlatEJ = dfFlatEJ[dfFlatEJ['jetPt'] > float(lJetPtcut)]

    # remove jets outside L1 acceptance
    dfFlatEJ = dfFlatEJ[np.abs(dfFlatEJ['jetEta']) < 5.191]

    # Apply cut for noisy towers: ieta=26 -> iem>=6, ieta=27 -> iem>=12, ieta=28 -> iem>=18
    dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 26) & (dfFlatET['iem'] < 6)].index, inplace = True)
    dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 27) & (dfFlatET['iem'] < 12)].index, inplace = True)
    dfFlatET.drop(dfFlatET[(np.abs(dfFlatET['ieta']) == 28) & (dfFlatET['iem'] < 18)].index, inplace = True)

    # Apply ECAL calibration
    ## 
    # TO BE DONE
    ##

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
    dfFlatEJ['dRsafe'] = deltarSelect(dfFlatEJ, dRcut)
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
        #print(dfFlatEJT.loc[1482])
        #exit()
        dfFlatEJT['iem'] = dfFlatEJT.apply(lambda row: round(row['iem'] * SFs[int( abs(row['ieta']) + 28*(row['iemBin']-1) ) -1]), axis=1)
        dfFlatEJT.set_index('uniqueIdx', inplace=True)

    print('starting padding') # DEBUG

    # do the padding of the dataframe to have 81 rows for each jet        
    paddedEJT = padDataFrame(dfFlatEJT)
    paddedEJT.drop_duplicates(['uniqueId', 'ieta', 'iphi'], keep='first', inplace=True)
    paddedEJT.set_index('uniqueId',inplace=True)

    # subtract iem/ihad to jetPt in oprder to get the correct training Pt to be be used for the NN
    if trainingPtVersion != False:
        group = paddedEJT.groupby('uniqueId')
        if trainingPtVersion=="ECAL": paddedEJT['trainingPt'] = group['jetPt'].mean() - group['hcalET'].sum()/2
        if trainingPtVersion=="HCAL": paddedEJT['trainingPt'] = group['jetPt'].mean() - group['iem'].sum()/2
    else:
        paddedEJT['trainingPt'] = paddedEJT['jetPt'].copy(deep=True)

    # keep only the jets that have a meaningful trainingPt to be used
    paddedEJT = paddedEJT[paddedEJT['trainingPt']>1]

    # append the DFs from the different files to one single big DF
    paddedEJT.reset_index(inplace=True)
    # shuffle the rows so that no order of the chunky donut gets learned
    paddedEJT = paddedEJT.sample(frac=1).copy(deep=True)

    dfTowers = paddedEJT[['uniqueId','ieta','iem','hcalET']].copy(deep=True)
    dfJets = paddedEJT[['uniqueId','jetPt','jetEta','jetPhi','trainingPt']].copy(deep=True)

    ## DEBUG
    # print(dfFlatEJT)
    # print(dfTowers)
    # print(len(dfTowers.event.unique()), 'events')
    # print(len(dfTowers.uniqueId.unique()), 'jets')
    # print(len(dfTowers), 'rows')
    print('storing')

    # save hdf5 files with dataframe formatted datasets
    storeT = pd.HDFStore(saveToDFs['towers']+'.hdf5', mode='w')
    storeT['towers'] = dfTowers
    storeT.close()

    storeJ = pd.HDFStore(saveToDFs['jets']+'.hdf5', mode='w')
    storeJ['jets'] = dfJets
    storeJ.close()

    # make the produced files accessible to the other people otherwise we cannot work together
    os.system('chmod 774 '+saveToDFs['towers']+'.hdf5')
    os.system('chmod 774 '+saveToDFs['jets']+'.hdf5')

    ## DEBUG
    print('starting one hot encoding')

    # define some variables on top
    dfTowers['ieta'] = abs(dfTowers['ieta'])
    dfTowers['iesum'] = dfTowers['iem'] + dfTowers['hcalET']
    dfE = dfTowers[['uniqueId', 'ieta', 'iem', 'hcalET', 'iesum']]

    # set the uniqueId indexing
    dfE.set_index('uniqueId',inplace=True)
    dfJets.drop_duplicates('uniqueId', keep='first', inplace=True)
    dfJets.set_index('uniqueId', inplace=True)

    # do the one hot encoding of ieta
    dfEOneHotEncoded = pd.get_dummies(dfE, columns=['ieta'])
    # pad the values of ieta that might be missing from the OHE
    for i in list(TowersEta.keys()):
        if 'ieta_'+str(i) not in dfEOneHotEncoded:
            dfEOneHotEncoded['ieta_'+str(i)] = 0

    ## DEBUG
    print('starting tensorisation')

    # convert to tensor for plotting
    # Y = np.array([dfJets.loc[i].values[0] for i in dfJets.index]).reshape(-1,1)
    # To keep both the information on jetPt and jetEta
    Y = np.array([dfJets.loc[i].values for i in dfJets.index])
    X = np.array([dfEOneHotEncoded.loc[i].to_numpy() for i in dfE.index.drop_duplicates(keep='first')])

    ## DEBUG
    # if len(X != 43): 
    #     print('Different lenght!')
    print('storing')

    # save .npz files with tensor formatted datasets
    np.savez_compressed(saveToTensors['towers']+'.npz', X)
    np.savez_compressed(saveToTensors['jets']+'.npz', Y)

    # make the produced files accessible to the other people otherwise we cannot work together
    os.system('chmod 774 '+saveToTensors['towers']+'.npz')
    os.system('chmod 774 '+saveToTensors['jets']+'.npz')

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
    parser.add_option("--trainPtVers", dest="trainPtVers", default=False)
    parser.add_option("--uJetPtCut",   dest="uJetPtCut",   default=False)
    parser.add_option("--lJetPtCut",   dest="lJetPtCut",   default=False)
    parser.add_option("--etacut",      dest="etacut",      default=False)
    parser.add_option("--ecalcut",     dest="ecalcut",     default=False)
    (options, args) = parser.parse_args()

    if (options.fin=='' or options.tag=='' or options.fout==''): print('** ERROR: wrong input options --> EXITING!!'); exit()

    # define the two paths where to read the hdf5 files
    readfrom = {
        'towers'  : options.fin+'/towers/towers'+options.tag,
        'jets'    : options.fin+'/jets/jets'+options.tag
    }

    # define the paths where to save the hdf5 files
    saveToDFs = {
        'towers'  : options.fout+'/dataframes/towers'+options.tag,
        'jets'    : options.fout+'/dataframes/jets'+options.tag
    }
    # define the two paths where to save the hdf5 files
    saveToTensors = {
        'towers'  : options.fout+'/tensors/towers'+options.tag,
        'jets'    : options.fout+'/tensors/jets'+options.tag
    }

    print(readfrom['towers']+'.hdf5')

    # read hdf5 files
    readT = pd.HDFStore(readfrom['towers']+'.hdf5', mode='r')
    dfET = readT['towers']
    readT.close()

    readJ = pd.HDFStore(readfrom['jets']+'.hdf5', mode='r')
    dfEJ = readJ['jets']
    readJ.close()

    mainReader(dfET, dfEJ, saveToDFs, saveToTensors, options.uJetPtCut, options.lJetPtCut, options.etacut, options.ecalcut, options.trainPtVers, options.calibrateECAL)
    print("DONE!")

