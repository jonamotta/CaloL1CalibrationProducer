from array import array
import uproot3
import sys
import os
import pandas as pd
import numpy as np
from itertools import chain
import ROOT
import math
from tqdm import tqdm

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import matplotlib
import mplhep
plt.style.use(mplhep.style.CMS)

def chunker(seq, size):
    for pos in range(0, len(seq), size):
        yield seq.iloc[pos:pos + size] 

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

def GetECALSFs (file_ECAl):

    SFs = []
    f_ECAL = open(file_ECAl)
    f_ECAL_lines = f_ECAL.readlines()
    for i, line in enumerate(f_ECAL_lines):
        if '#' in line: continue
        sf_line_ECAL = line.split(',\n')[0]
        sf_vec_ECAL = [float(j) for j in sf_line_ECAL.split(',')]
        SFs = SFs + sf_vec_ECAL
    print('First line:', SFs[:28])
    return SFs

def GetHCALSFs (file_HCAL, file_HF):

    SFs = []
    f_HCAL = open(file_HCAL)
    f_HF = open(file_HF)
    f_HCAL_lines = f_HCAL.readlines()
    f_HF_lines = f_HF.readlines()
    for i, line in enumerate(f_HCAL_lines):
        if '#' in line: continue
        sf_line_HCAL = line.split(',\n')[0]
        sf_vec_HCAL = [float(j) for j in sf_line_HCAL.split(',')]
        sf_line_HF = f_HF_lines[i].split(',\n')[0]
        sf_vec_HF = [float(j) for j in sf_line_HF.split(',')]
        SFs = SFs + sf_vec_HCAL + sf_vec_HF
    print('First line:', SFs[:40])
    return SFs

newHCALEnergyBins = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 256]

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

'''
python3 PrintNtuples.py --v HCAL \
--unc Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples/ \
--old Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json/GoodNtuples/ \
--new Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json/GoodNtuples/

python3 PrintNtuples.py --v HCAL \
--unc JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples \
--old JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json/GoodNtuples \
--new JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json/GoodNtuples
'''

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--indir",       dest="indir",                            default="/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/")
parser.add_option("--v",           dest="v",                                default='HCAL')
parser.add_option("--unc",         dest="uncalib_dir",                      default="Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples/")
parser.add_option("--old",         dest="oldcalib_dir",                     default="Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json/GoodNtuples/")
parser.add_option("--new",         dest="newcalib_dir",                     default="Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json/GoodNtuples/")
parser.add_option("--ptcut",       dest="ptcut",                            default=True)
parser.add_option("--etacut",      dest="etacut",                           default=True)
parser.add_option("--HoTotcut",    dest="HoTotcut",                         default=None)
(options, args) = parser.parse_args()

version = options.v

printout = False
indir = options.indir
uncalib_dir  = indir+options.uncalib_dir
oldcalib_dir = indir+options.oldcalib_dir
newcalib_dir = indir+options.newcalib_dir

if "Muon" in options.uncalib_dir:
    ntuple =  "Ntuple_0"
    sample = "Muon"
else:
    ntuple =  "Ntuple_112"
    sample = "JetMET"

keyEvents = "l1EventTree/L1EventTree"
branchesEvents = ["Event/event"]

keyTowers = "l1CaloTowerEmuTree/L1CaloTowerTree"
branchesTowers = ["L1CaloTower/ieta", "L1CaloTower/iphi", "L1CaloTower/iem", "L1CaloTower/ihad", "L1CaloTower/iet"]

if version == 'ECAL':
    keyTarget = "l1ElectronRecoTree/ElectronRecoTree"
    branchesTarget = ["Electron/eta", "Electron/phi", "Electron/etCorr"]
if version == 'HCAL':
    keyTarget = "l1JetRecoTree/JetRecoTree"
    branchesTarget = ["Jet/eta", "Jet/phi", "Jet/etCorr"]

if version == 'ECAL':
    keyLevel1 = "l1UpgradeEmuTree/L1UpgradeTree"
    branchesLevel1 = ["L1Upgrade/egEta", "L1Upgrade/egPhi", "L1Upgrade/egIEta", "L1Upgrade/egIPhi", "L1Upgrade/egEt", "L1Upgrade/egRawEt"]
if version == 'HCAL':
    keyLevel1 = "l1UpgradeEmuTree/L1UpgradeTree"
    branchesLevel1 = ["L1Upgrade/jetEta", "L1Upgrade/jetPhi", "L1Upgrade/jetIEta", "L1Upgrade/jetIPhi", "L1Upgrade/jetEt", "L1Upgrade/jetRawEt"]

if version == 'ECAL':
    Eta = b'egEta'; Phi = b'egPhi'; IEta = b'egIEta'; IPhi = b'egIPhi'; Et = b'egEt'; RawEt = b'egRawEt'
if version == 'HCAL':
    Eta = b'jetEta'; Phi = b'jetPhi'; IEta = b'jetIEta'; IPhi = b'jetIPhi'; Et = b'jetEt'; RawEt = b'jetRawEt'

# Uncalibrated
print('\n ### Reading Uncalib: '+uncalib_dir+"/"+ntuple+".root")
InFile = uproot3.open(uncalib_dir+"/"+ntuple+".root")

eventsTree = InFile[keyEvents]
towersTree = InFile[keyTowers]
targetTree = InFile[keyTarget]
level1Tree = InFile[keyLevel1]
del InFile

arrEvents = eventsTree.arrays(branchesEvents)
arrTowers = towersTree.arrays(branchesTowers)
arrTarget = targetTree.arrays(branchesTarget)
arrLevel1 = level1Tree.arrays(branchesLevel1)
del eventsTree, towersTree, targetTree, level1Tree

dfE = pd.DataFrame(arrEvents)
dfT = pd.DataFrame(arrTowers)
dfJ = pd.DataFrame(arrTarget)
dfL = pd.DataFrame(arrLevel1)
del arrEvents, arrTowers, arrTarget, arrLevel1

uncalib_dfET = pd.concat([dfE, dfT], axis=1)
uncalib_dfEJ = pd.concat([dfE, dfJ], axis=1)
uncalib_dfEL = pd.concat([dfE, dfL], axis=1)
uncalib_dfET = uncalib_dfET.dropna(axis=0)
uncalib_dfEJ = uncalib_dfEJ.dropna(axis=0)
uncalib_dfEL = uncalib_dfEL.dropna(axis=0)
n_events = len(dfE[b'event'].unique())
print(' ### Nevents =', n_events)
del dfE, dfT, dfJ, dfL

# Old Calibration
print('\n ### Reading OldCalib: '+oldcalib_dir+"/"+ntuple+".root")
InFile = uproot3.open(oldcalib_dir+"/"+ntuple+".root")

eventsTree = InFile[keyEvents]
towersTree = InFile[keyTowers]
targetTree = InFile[keyTarget]
level1Tree = InFile[keyLevel1]
del InFile

arrEvents = eventsTree.arrays(branchesEvents)
arrTowers = towersTree.arrays(branchesTowers)
arrTarget = targetTree.arrays(branchesTarget)
arrLevel1 = level1Tree.arrays(branchesLevel1)
del eventsTree, towersTree, targetTree, level1Tree

dfE = pd.DataFrame(arrEvents)
dfT = pd.DataFrame(arrTowers)
dfJ = pd.DataFrame(arrTarget)
dfL = pd.DataFrame(arrLevel1)
del arrEvents, arrTowers, arrTarget, arrLevel1

oldcalib_dfET = pd.concat([dfE, dfT], axis=1)
oldcalib_dfEJ = pd.concat([dfE, dfJ], axis=1)
oldcalib_dfEL = pd.concat([dfE, dfL], axis=1)
oldcalib_dfET = oldcalib_dfET.dropna(axis=0)
oldcalib_dfEJ = oldcalib_dfEJ.dropna(axis=0)
oldcalib_dfEL = oldcalib_dfEL.dropna(axis=0)
n_events = len(dfE[b'event'].unique())
print(' ### Nevents =', n_events)
del dfE, dfT, dfJ, dfL

# New Calibration
print('\n ### Reading NewCalib: '+newcalib_dir+"/"+ntuple+".root")
InFile = uproot3.open(newcalib_dir+"/"+ntuple+".root")

eventsTree = InFile[keyEvents]
towersTree = InFile[keyTowers]
targetTree = InFile[keyTarget]
level1Tree = InFile[keyLevel1]
del InFile

arrEvents = eventsTree.arrays(branchesEvents)
arrTowers = towersTree.arrays(branchesTowers)
arrTarget = targetTree.arrays(branchesTarget)
arrLevel1 = level1Tree.arrays(branchesLevel1)
del eventsTree, towersTree, targetTree, level1Tree

dfE = pd.DataFrame(arrEvents)
dfT = pd.DataFrame(arrTowers)
dfJ = pd.DataFrame(arrTarget)
dfL = pd.DataFrame(arrLevel1)
del arrEvents, arrTowers, arrTarget, arrLevel1

newcalib_dfET = pd.concat([dfE, dfT], axis=1)
newcalib_dfEJ = pd.concat([dfE, dfJ], axis=1)
newcalib_dfEL = pd.concat([dfE, dfL], axis=1)
newcalib_dfET = newcalib_dfET.dropna(axis=0)
newcalib_dfEJ = newcalib_dfEJ.dropna(axis=0)
newcalib_dfEL = newcalib_dfEL.dropna(axis=0)
n_events = len(dfE[b'event'].unique())
print(' ### Nevents =', n_events)
del dfE, dfT, dfJ, dfL

u_resp = []
o_resp = []
n_resp = []

u_error = 0
o_error = 0
n_error = 0

file_HCAL = '/data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV42/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv'
file_HF = '/data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV42/HCALtrainingDataReco/data_A/ScaleFactors_HF_energystep2iEt.csv'
file_ECAL = '/data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33/ECALtrainingDataReco_normalOrder/data/ScaleFactors_ECAL_energystep2iEt_BadRounding.csv'

NewHCALenergy_bins = np.array(newHCALEnergyBins)*2 # to convert to iEt and shift to center of bin
NewECALenergy_bins = np.array(newHCALEnergyBins)*2 # to convert to iEt and shift to center of bin
NewHCALSFs = GetHCALSFs(file_HCAL, file_HF)
NewECALSFs = GetECALSFs(file_ECAL)


chunk_size = 100
i = 0
for u_ET, u_EJ, u_EL, o_ET, o_EJ, o_EL, n_ET, n_EJ, n_EL in zip(chunker(uncalib_dfET, chunk_size),chunker(uncalib_dfEJ, chunk_size), chunker(uncalib_dfEL, chunk_size), chunker(oldcalib_dfET, chunk_size),chunker(oldcalib_dfEJ, chunk_size), chunker(oldcalib_dfEL, chunk_size), chunker(newcalib_dfET, chunk_size), chunker(newcalib_dfEJ, chunk_size), chunker(newcalib_dfEL, chunk_size)):

    u_dfFlatET = pd.DataFrame({
        'event': np.repeat(u_ET[b'event'].values, u_ET[b'ieta'].str.len()), # event IDs are copied to keep proper track of what is what
        'ieta': list(chain.from_iterable(u_ET[b'ieta'])),
        'iphi': list(chain.from_iterable(u_ET[b'iphi'])),
        'iem' : list(chain.from_iterable(u_ET[b'iem'])),
        'ihad': list(chain.from_iterable(u_ET[b'ihad'])),
        'iet' : list(chain.from_iterable(u_ET[b'iet']))
        })
    o_dfFlatET = pd.DataFrame({
        'event': np.repeat(o_ET[b'event'].values, o_ET[b'ieta'].str.len()), # event IDs are copied to keep proper track of what is what
        'ieta': list(chain.from_iterable(o_ET[b'ieta'])),
        'iphi': list(chain.from_iterable(o_ET[b'iphi'])),
        'iem' : list(chain.from_iterable(o_ET[b'iem'])),
        'ihad': list(chain.from_iterable(o_ET[b'ihad'])),
        'iet' : list(chain.from_iterable(o_ET[b'iet']))
        })
    n_dfFlatET = pd.DataFrame({
        'event': np.repeat(o_ET[b'event'].values, n_ET[b'ieta'].str.len()), # event IDs are copied to keep proper track of what is what
        'ieta': list(chain.from_iterable(n_ET[b'ieta'])),
        'iphi': list(chain.from_iterable(n_ET[b'iphi'])),
        'iem' : list(chain.from_iterable(n_ET[b'iem'])),
        'ihad': list(chain.from_iterable(n_ET[b'ihad'])),
        'iet' : list(chain.from_iterable(n_ET[b'iet']))
        })

    u_dfFlatEJ = pd.DataFrame({
        'event': np.repeat(u_EJ[b'event'].values, u_EJ[b'eta'].str.len()), # event IDs are copied to keep proper track of what is what
        'jetEta': list(chain.from_iterable(u_EJ[b'eta'])),
        'jetPhi': list(chain.from_iterable(u_EJ[b'phi'])),
        'jetPt' : list(chain.from_iterable(u_EJ[b'etCorr']))
        })
    o_dfFlatEJ = pd.DataFrame({
        'event': np.repeat(o_EJ[b'event'].values, o_EJ[b'eta'].str.len()), # event IDs are copied to keep proper track of what is what
        'jetEta': list(chain.from_iterable(o_EJ[b'eta'])),
        'jetPhi': list(chain.from_iterable(o_EJ[b'phi'])),
        'jetPt' : list(chain.from_iterable(o_EJ[b'etCorr']))
        })
    n_dfFlatEJ = pd.DataFrame({
        'event': np.repeat(n_EJ[b'event'].values, n_EJ[b'eta'].str.len()), # event IDs are copied to keep proper track of what is what
        'jetEta': list(chain.from_iterable(n_EJ[b'eta'])),
        'jetPhi': list(chain.from_iterable(n_EJ[b'phi'])),
        'jetPt' : list(chain.from_iterable(n_EJ[b'etCorr']))
        })

    u_dfFlatEL = pd.DataFrame({
        'event': np.repeat(u_EL[b'event'].values, u_EL[Eta].str.len()), # event IDs are copied to keep proper track of what is what
        'jetEta': list(chain.from_iterable(u_EL[Eta])),
        'jetPhi': list(chain.from_iterable(u_EL[Phi])),
        'jetIEta': list(chain.from_iterable(u_EL[IEta])),
        'jetIPhi': list(chain.from_iterable(u_EL[IPhi])),
        'jetEt' : list(chain.from_iterable(u_EL[Et])),
        'jetRawEt' : list(chain.from_iterable(u_EL[RawEt]))
        })
    o_dfFlatEL = pd.DataFrame({
        'event': np.repeat(o_EL[b'event'].values, o_EL[Eta].str.len()), # event IDs are copied to keep proper track of what is what
        'jetEta': list(chain.from_iterable(o_EL[Eta])),
        'jetPhi': list(chain.from_iterable(o_EL[Phi])),
        'jetIEta': list(chain.from_iterable(o_EL[IEta])),
        'jetIPhi': list(chain.from_iterable(o_EL[IPhi])),
        'jetEt' : list(chain.from_iterable(o_EL[Et])),
        'jetRawEt' : list(chain.from_iterable(o_EL[RawEt]))
        })
    n_dfFlatEL = pd.DataFrame({
        'event': np.repeat(n_EL[b'event'].values, n_EL[Eta].str.len()), # event IDs are copied to keep proper track of what is what
        'jetEta': list(chain.from_iterable(n_EL[Eta])),
        'jetPhi': list(chain.from_iterable(n_EL[Phi])),
        'jetIEta': list(chain.from_iterable(n_EL[IEta])),
        'jetIPhi': list(chain.from_iterable(n_EL[IPhi])),
        'jetEt' : list(chain.from_iterable(n_EL[Et])),
        'jetRawEt' : list(chain.from_iterable(n_EL[RawEt]))
        })

    if options.ptcut:
        u_dfFlatEJ = u_dfFlatEJ[u_dfFlatEJ['jetPt'] > 30]
    if options.etacut:
        u_dfFlatEJ = u_dfFlatEJ[(u_dfFlatEJ['jetEta'] < 1.305) & (u_dfFlatEJ['jetEta'] > -1.305)]

    # for idx in tqdm(u_dfFlatEJ.index):
    for n,idx in enumerate(u_dfFlatEJ.index):
    
        i_event = u_dfFlatEJ[u_dfFlatEJ.index == idx].event.values[0]
        print(i, i_event)

        matched = False
        highestL1Pt = -99
        good_jdx = 0
        good_IEta = 0
        good_IPhi = 0

        targetObj = ROOT.TLorentzVector()
        targetObj.SetPtEtaPhiM(u_dfFlatEJ[u_dfFlatEJ.index == idx].jetPt, u_dfFlatEJ[u_dfFlatEJ.index == idx].jetEta, u_dfFlatEJ[u_dfFlatEJ.index == idx].jetPhi, 0)

        u_dfFlatEL_ev = u_dfFlatEL[u_dfFlatEL['event'] == i_event]
        for jdx in u_dfFlatEL_ev.index:
            level1Obj = ROOT.TLorentzVector()
            level1Obj.SetPtEtaPhiM(u_dfFlatEL_ev[u_dfFlatEL_ev.index == jdx].jetRawEt, u_dfFlatEL_ev[u_dfFlatEL_ev.index == jdx].jetEta, u_dfFlatEL_ev[u_dfFlatEL_ev.index == jdx].jetPhi, 0)
            
            if targetObj.DeltaR(level1Obj) < 0.5:
                matched = True
                #keep only L1 match with highest pT
                # if level1Obj.Pt() > highestL1Pt:
                highestL1Pt = level1Obj.Pt()
                good_jdx = jdx
                good_IEta = u_dfFlatEL_ev[u_dfFlatEL_ev.index == jdx].jetIEta.values[0]
                good_IPhi = u_dfFlatEL_ev[u_dfFlatEL_ev.index == jdx].jetIPhi.values[0]
                break

        if matched == True:

            # print(good_IEta, good_IPhi)
            max_IEta = NextEtaTower(NextEtaTower(NextEtaTower(NextEtaTower(good_IEta))))
            min_IEta = PrevEtaTower(PrevEtaTower(PrevEtaTower(PrevEtaTower(good_IEta))))
            max_IPhi = NextPhiTower(NextPhiTower(NextPhiTower(NextPhiTower(good_IPhi))))
            min_IPhi = PrevPhiTower(PrevPhiTower(PrevPhiTower(PrevPhiTower(good_IPhi))))
            
            u_dfFlatET_ev = u_dfFlatET[u_dfFlatET['event'] == i_event]
            if min_IPhi <= max_IPhi:
                u_CD = u_dfFlatET_ev[(u_dfFlatET_ev['ieta'] <= max_IEta) & (u_dfFlatET_ev['ieta'] >= min_IEta) & (u_dfFlatET_ev['iphi'] <= max_IPhi) & (u_dfFlatET_ev['iphi'] >= min_IPhi)]
            else:
                u_CD = u_dfFlatET_ev[(u_dfFlatET_ev['ieta'] <= max_IEta) & (u_dfFlatET_ev['ieta'] >= min_IEta) & ((u_dfFlatET_ev['iphi'] >= min_IPhi) | (u_dfFlatET_ev['iphi'] <= max_IPhi))]
            if options.HoTotcut:
                if float(u_CD.ihad.sum()/(u_CD.iem.sum() + u_CD.ihad.sum())) < float(options.HoTotcut): continue
            u_resp.append(u_CD.iet.sum()/targetObj.Pt()/2)
            # print(u_CD)

            o_dfFlatET_ev = o_dfFlatET[o_dfFlatET['event'] == i_event]
            if min_IPhi <= max_IPhi:
                o_CD = o_dfFlatET_ev[(o_dfFlatET_ev['ieta'] <= max_IEta) & (o_dfFlatET_ev['ieta'] >= min_IEta) & (o_dfFlatET_ev['iphi'] <= max_IPhi) & (o_dfFlatET_ev['iphi'] >= min_IPhi)]
            else:
                o_CD = o_dfFlatET_ev[(o_dfFlatET_ev['ieta'] <= max_IEta) & (o_dfFlatET_ev['ieta'] >= min_IEta) & ((o_dfFlatET_ev['iphi'] >= min_IPhi) | (o_dfFlatET_ev['iphi'] <= max_IPhi))]
            o_resp.append(o_CD.iet.sum()/targetObj.Pt()/2)
            # print(o_CD)

            n_dfFlatET_ev = n_dfFlatET[n_dfFlatET['event'] == i_event]
            if min_IPhi <= max_IPhi:
                n_CD = n_dfFlatET_ev[(n_dfFlatET_ev['ieta'] <= max_IEta) & (n_dfFlatET_ev['ieta'] >= min_IEta) & (n_dfFlatET_ev['iphi'] <= max_IPhi) & (n_dfFlatET_ev['iphi'] >= min_IPhi)]
            else:
                n_CD = n_dfFlatET_ev[(n_dfFlatET_ev['ieta'] <= max_IEta) & (n_dfFlatET_ev['ieta'] >= min_IEta) & ((n_dfFlatET_ev['iphi'] >= min_IPhi) | (n_dfFlatET_ev['iphi'] <= max_IPhi))]
            n_resp.append(n_CD.iet.sum()/targetObj.Pt()/2)
            # print(n_CD)

            i = i + 1

            if True:
                u_iet_sum = 0
                o_iet_sum = 0
                n_iet_sum = 0
                for i_tt in u_CD.index:
                    TT = u_CD[u_CD.index == i_tt]
                    ieta = TT.ieta.values[0]
                    iphi = TT.iphi.values[0]
                    u_iem = TT.iem.values[0]
                    u_ihad = TT.ihad.values[0]

                    u_iet_sum += u_iem + u_ihad

                    if printout:
                        print('\n ### ieta='+str(ieta)+' iphi='+str(iphi))
                        print(' ### UNCALIB  iem='+str(u_iem)+' ihad='+str(u_ihad))

                    o_TT = o_CD[(o_CD.ieta == ieta) & (o_CD.iphi == iphi)]
                    o_iem = o_TT.iem.values[0]
                    o_ihad = o_TT.ihad.values[0]
                    o_iet_sum += o_iem + o_ihad
                    if printout:
                        print(' ### OLDCALIB iem='+str(o_iem)+' ihad='+str(o_ihad))

                    n_TT = n_CD[(n_CD.ieta == ieta) & (n_CD.iphi == iphi)]
                    if len(n_TT) > 0:
                        n_iem = n_TT.iem.values[0]
                        n_ihad = n_TT.ihad.values[0]
                        if printout:
                            print(' ### NEWCALIB iem='+str(n_iem)+' ihad='+str(n_ihad))
                    else:
                        n_iem = 0
                        n_ihad = 0
                        if printout:
                            print(' ### NEWCALIB iem=0 ihad=0')
                    n_iet_sum += n_iem + n_ihad
                    # get predicted ihad
                    HCALsf = NewHCALSFs[int( abs(ieta) + 40*(np.digitize(u_ihad, NewHCALenergy_bins)-1) ) -1]
                    predicted_ihad = math.floor(u_ihad * HCALsf)
                    # get predicted iem
                    ECALsf = NewECALSFs[int( abs(ieta) + 28*(np.digitize(u_iem, NewECALenergy_bins)-1) ) -1]
                    predicted_iem = math.floor(u_iem * ECALsf)
                    if printout:
                        print(' ### REFCALIB iem='+str(predicted_iem)+' ihad='+str(predicted_ihad))
                        print(' ### ECAL SF = '+str(ECALsf) + ' HCAL SF = '+str(HCALsf) )
                    
                    # if (predicted_ihad != n_ihad) or (predicted_iem != n_iem):
                    #     if not ((n_ihad == 255) or (n_iem == 255)): 
                    #         print('ERROR')
                    #         breakpoint()
                    
                # compare iet_sum to L1 object pt
                u_dfFlatEL_ev = u_dfFlatEL[u_dfFlatEL['event'] == i_event]
                u_RawEt = u_dfFlatEL_ev[(u_dfFlatEL_ev['jetIEta'] == good_IEta) & (u_dfFlatEL_ev['jetIPhi'] == good_IPhi)].jetRawEt.values
                if len(u_RawEt) > 0: u_RawEt = u_RawEt[0]
                else: u_RawEt = 0
                if u_RawEt != u_iet_sum:
                    print(' ### ERROR: UNCALIB Raw Et = '+str(u_RawEt)+' UNCALIB CD sum = '+str(u_iet_sum))
                    u_error += 1
                o_dfFlatEL_ev = o_dfFlatEL[o_dfFlatEL['event'] == i_event]
                o_RawEt = o_dfFlatEL_ev[(o_dfFlatEL_ev['jetIEta'] == good_IEta) & (o_dfFlatEL_ev['jetIPhi'] == good_IPhi)].jetRawEt.values
                if len(o_RawEt) > 0: o_RawEt = o_RawEt[0]
                else: o_RawEt = 0
                if o_RawEt != o_iet_sum:
                    print(' ### ERROR: OLDCALIB Raw Et = '+str(o_RawEt)+' OLDCALIB CD sum = '+str(o_iet_sum))
                    o_error += 1
                n_dfFlatEL_ev = n_dfFlatEL[n_dfFlatEL['event'] == i_event]
                n_RawEt = n_dfFlatEL_ev[(n_dfFlatEL_ev['jetIEta'] == good_IEta) & (n_dfFlatEL_ev['jetIPhi'] == good_IPhi)].jetRawEt.values
                if len(n_RawEt) > 0: n_RawEt = n_RawEt[0]
                else: n_RawEt = 0
                if n_RawEt != n_iet_sum:
                    print(' ### ERROR: NEWCALIB Raw Et = '+str(n_RawEt)+' NEWCALIB CD sum = '+str(n_iet_sum))
                    n_error += 1
                
                if i_event in [529249441, 528256637, 529105997, 528808856, 529328946, 528758355, 528408185, 528250548, 529007734]:
                    print("Found event")
                    breakpoint()
                    
                # if (u_RawEt != u_iet_sum) or (o_RawEt != o_iet_sum) or (n_RawEt != n_iet_sum):
                #     if i in [72, 153, 154, 170, 175, 176, 250, 276, 352]:
                #         continue
                #     else:
                #         print(good_IEta, good_IPhi)
                #         breakpoint()

                # 72, 175, 250: new Calib changes central tower
                # 153, 352: old Calib changes central tower
                # 154, 276: new Calib of ECAL underestimates from 8 to 7 and the jet disappears (but it was fully EM)
                # 170: 510 become 511 so 1 Et difference for all when saturating signals
                # 176: not clear

    if i > 1500:
        break

print(u_error, o_error, n_error)

c_uncalib = 'black'
c_oldcalib = 'red'
c_newcalib = 'green'

leg_uncalib = 'No calib'
leg_oldcalib = 'Old calib'
leg_newcalib = 'New calib'

bins_res = np.linspace(0,3,50)

odir = './'
u_resp = np.array(u_resp); o_resp = np.array(o_resp); n_resp = np.array(n_resp)
plt.figure(figsize=(10,10))
text_1 = leg_uncalib+r': $\mu={:.3f}, res={:.3f}$'.format(u_resp.mean(), u_resp.std()/u_resp.mean())
plt.hist(u_resp, bins=bins_res, label=text_1, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
text_2 = leg_oldcalib+r': $\mu={:.3f}, res={:.3f}$'.format(o_resp.mean(), o_resp.std()/o_resp.mean())
plt.hist(o_resp, bins=bins_res, label=text_2, histtype='step', density=True, stacked=True, linewidth=2, color=c_oldcalib)
text_3 = leg_newcalib+r': $\mu={:.3f}, res={:.3f}$'.format(n_resp.mean(), n_resp.std()/n_resp.mean())
plt.hist(n_resp, bins=bins_res, label=text_3, histtype='step', density=True, stacked=True, linewidth=2, color=c_newcalib)
plt.xlabel('Response')
plt.ylabel('a.u.')
plt.grid(linestyle='dotted')
plt.legend(fontsize=15, loc='upper left')
mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
# plt.title('Jets Resolution {}'.format(v_sample))
savefile = odir + '/Res_{}_{}'.format(version, sample)
if options.ptcut:
    savefile = savefile + "_pt30"
if options.etacut:
    savefile = savefile + "_eta1p305"
if options.HoTotcut:
    savefile = savefile + "_HoTot" + options.HoTotcut
savefile = savefile + ".png"
plt.savefig(savefile)
print(savefile)
plt.close()

    # dfFlatEL = dfFlatEL[(dfFlatEL['jetEta'] < 1.5) & (dfFlatEL['jetEta'] > -1.5)]

    # dfFlatET = dfFlatET[(dfFlatET['ieta'] < 20) & (dfFlatET['ieta'] > -20)]

    # dfFlatET.set_index('event', inplace=True)
    # dfFlatEJ.set_index('event', inplace=True)
    # dfFlatEL.set_index('event', inplace=True)

    # print(dfFlatEJ[dfFlatEJ.index == 11389468])
    # print(dfFlatET[dfFlatET.index == 11389468])
    # print(dfFlatEL[dfFlatEL.index == 11389468])
