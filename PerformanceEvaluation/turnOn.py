from array import array
import numpy as np
import pickle
import ROOT
ROOT.gROOT.SetBatch(True)
import sys
import os
from tqdm import tqdm
import warnings
warnings.simplefilter(action='ignore')

import matplotlib.pyplot as plt
import matplotlib
import mplhep
plt.style.use(mplhep.style.CMS)

def save_obj(obj,dest):
    with open(dest,'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

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

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--indir",     dest="indir",    default=None)
parser.add_option("--tag",       dest="tag",      default='')
parser.add_option("--outdir",    dest="outdir",   default=None)
parser.add_option("--label",     dest="label",    default=None)
parser.add_option("--nEvts",     dest="nEvts",    type=int, default=-1)
parser.add_option("--target",    dest="target",   default=None)
parser.add_option("--reco",      dest="reco",     action='store_true', default=False)
parser.add_option("--gen",       dest="gen",      action='store_true', default=False)
parser.add_option("--unpacked",  dest="unpacked", action='store_true', default=False)
parser.add_option("--raw",       dest="raw",      action='store_true', default=False)
parser.add_option("--jetPtcut",  dest="jetPtcut", type=float, default=None)
parser.add_option("--LooseEle",  dest="LooseEle", action='store_true', default=False)
parser.add_option("--PuppiJet",  dest="PuppiJet", action='store_true', default=False)
parser.add_option("--er",        dest="er",       default='2.5') #eta restriction
(options, args) = parser.parse_args()

cmap = matplotlib.colormaps.get_cmap('Set1')

# get/create folders
indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/"+options.indir
outdir = "/data_CMS/cms/motta/CaloL1calibraton/"+options.outdir
label = options.label
os.system('mkdir -p '+outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs')
os.system('mkdir -p '+outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs')
os.system('mkdir -p '+outdir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs')

# define input trees
if options.reco:
    if options.target == 'jet': targetTree = ROOT.TChain("l1JetRecoTree/JetRecoTree")
    if options.target == 'ele': targetTree = ROOT.TChain("l1ElectronRecoTree/ElectronRecoTree")
    if options.target == 'met': targetTree = ROOT.TChain("l1JetRecoTree/JetRecoTree")

if options.gen:
    targetTree = ROOT.TChain("l1GeneratorTree/L1GenTree")

if options.unpacked: level1Tree = ROOT.TChain("l1UpgradeTree/L1UpgradeTree")
else:                level1Tree = ROOT.TChain("l1UpgradeEmuTree/L1UpgradeTree")

# read input files
targetTree.Add(indir+"/Ntuple*.root")
level1Tree.Add(indir+"/Ntuple*.root")

nEntries = targetTree.GetEntries()
print("got",nEntries,"entries")

# run on entries specified by usuer, or only on entries available if that is exceeded
nevents = options.nEvts
if (nevents > nEntries) or (nevents==-1): nevents = nEntries
print("will process",nevents,"events...")

#defining binning of histogram
bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 100, 120, 150, 180, 250]

#list the ET thresholds to be tested
thresholds = np.linspace(8,150,143).tolist()
thresholds2plot = [10, 20, 35, 50, 100, 150]

# total histogram (denominator)
total = ROOT.TH1F("total","total",len(bins)-1, array('f',bins))
total_Er2p5 = ROOT.TH1F("total_Er2p5","total_Er2p5",len(bins)-1, array('f',bins))
if options.er:
    er_label = options.er.replace(".", "p")
    total_Er0p0 = ROOT.TH1F("total_Er{}".format(er_label),"total_Er{}".format(er_label),len(bins)-1, array('f',bins))

# passing histograms (numerators)
passing = []
for threshold in thresholds:
    passing.append(ROOT.TH1F("passing_"+str(int(threshold)),"passing_"+str(int(threshold)),len(bins)-1, array('f',bins)))
passing_Er2p5 = []
for threshold in thresholds:
    passing_Er2p5.append(ROOT.TH1F("passing_Er2p5_"+str(int(threshold)),"passing_Er2p5_"+str(int(threshold)),len(bins)-1, array('f',bins)))
if options.er:
    passing_Er0p0 = []
    for threshold in thresholds:
        passing_Er0p0.append(ROOT.TH1F("passing_Er"+er_label+"_"+str(int(threshold)),"passing_Er"+er_label+"_"+str(int(threshold)),len(bins)-1, array('f',bins)))

print("looping on events")
for i in tqdm(range(0, nevents)):
    # if i%1000==0: print(i)
    #getting entries
    entry2 = level1Tree.GetEntry(i)
    entry3 = targetTree.GetEntry(i)

    # skip corrupted entries
    if not entry2 or not entry3: continue

    if options.target == 'met':

        # targetObj = targetTree.Sums.met
        targetObj = targetTree.Sums.pfMetNoMu

        iSUM = -1 
        for i, typ in enumerate(level1Tree.L1Upgrade.sumType):
            if typ == 2:
                iSUM = i
                break
        if iSUM < 0: continue
        level1Obj = level1Tree.L1Upgrade.sumEt[iSUM]

        # apply selection on reco jets
        foundJet = False
        for ijet in range(0, targetTree.Jet.nJets):
            if targetTree.Jet.etCorr[ijet] > 30 and abs(targetTree.Jet.eta[ijet])<5.:
                foundJet = True
                break
        if not foundJet: continue

        total.Fill(targetObj)

        #fill numerator histograms for every thresholds
        for i, thr in enumerate(thresholds): 
            if level1Obj>float(thr): passing[i].Fill(targetObj)

        # in the case of MET just move to the next event
        continue

    L1_nObjs = 0
    if options.target == 'jet':
        L1_nObjs = level1Tree.L1Upgrade.nJets
        if options.PuppiJet:
            target_nObjs = targetTree.Jet.puppi_nJets
        else:
            target_nObjs = targetTree.Jet.nJets
    if options.target == 'ele':
        L1_nObjs = level1Tree.L1Upgrade.nEGs
        target_nObjs = targetTree.Electron.nElectrons
    
    #loop on generator jets
    for iTargetObj in range(0,target_nObjs):

        if options.target == 'jet':
            targetObj = ROOT.TLorentzVector()
            if options.PuppiJet:
                targetObj.SetPtEtaPhiM(targetTree.Jet.puppi_etCorr[iTargetObj], targetTree.Jet.puppi_eta[iTargetObj], targetTree.Jet.puppi_phi[iTargetObj], 0)
            else:
                targetObj.SetPtEtaPhiM(targetTree.Jet.etCorr[iTargetObj], targetTree.Jet.eta[iTargetObj], targetTree.Jet.phi[iTargetObj], 0)

        if options.target == 'ele':
            targetObj = ROOT.TLorentzVector()
            targetObj.SetPtEtaPhiM(targetTree.Electron.et[iTargetObj], targetTree.Electron.eta[iTargetObj], targetTree.Electron.phi[iTargetObj], 0)

        # skip jets that cannot be reconstructed by L1 (limit is 5.191)
        if targetObj.Eta()>5.0: continue
        
        # skip egs that cannot be reconstructed by L1 (limit is 3.0)
        # if options.target == 'ele' and targetObj.Eta()>3.0: continue
        #reject very soft jets, usually poorly defined
        # if options.target == 'jet' and targetObj.Pt()<30.: continue
        
        ################# APPLY CUTS #################
        if options.jetPtcut: 
            if targetObj.Pt() < float(options.jetPtcut): continue
        if options.target == 'ele' and options.LooseEle:
            if targetTree.Electron.isLooseElectron[iTargetObj] == 0: continue
        #############################################

        total.Fill(targetObj.Pt())

        # loop on L1 jets to find match
        matched = False
        highestL1Pt = -99.
        myGood_iL1Obj = 0
        myGoodLevel1Obj = ROOT.TLorentzVector()
        for iL1Obj in range(0, L1_nObjs):
            level1Obj = ROOT.TLorentzVector()
            if options.target == 'jet': 
                if options.raw:
                    # new method of plotting results by just looking at the raw output from the Layer-1
                    level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.jetRawEt[iL1Obj]/2, level1Tree.L1Upgrade.jetEta[iL1Obj], level1Tree.L1Upgrade.jetPhi[iL1Obj], 0)
                else:
                    level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.jetEt[iL1Obj], level1Tree.L1Upgrade.jetEta[iL1Obj], level1Tree.L1Upgrade.jetPhi[iL1Obj], 0)
            if options.target == 'ele': 
                if options.raw:
                    # new method of plotting results by just looking at the raw output from the Layer-1
                    level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.egRawEt[iL1Obj]/2, level1Tree.L1Upgrade.egEta[iL1Obj], level1Tree.L1Upgrade.egPhi[iL1Obj], 0)
                else:
                    level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.egEt[iL1Obj], level1Tree.L1Upgrade.egEta[iL1Obj], level1Tree.L1Upgrade.egPhi[iL1Obj], 0)

            #check matching
            if targetObj.DeltaR(level1Obj)<0.5:
                matched = True
                #keep only L1 match with highest pT
                if level1Obj.Pt() > highestL1Pt:
                    myGoodLevel1Obj = level1Obj
                    myGood_iL1Obj = iL1Obj
                    highestL1Pt = level1Obj.Pt()

        if matched:
            #fill numerator histograms for every thresholds
            for i, thr in enumerate(thresholds): 
                if matched and highestL1Pt > float(thr): passing[i].Fill(targetObj.Pt())
        
        if targetObj.Eta()<2.5:

            total_Er2p5.Fill(targetObj.Pt())
            # loop on L1 jets to find match
            matched = False
            highestL1Pt = -99.
            myGood_iL1Obj = 0
            myGoodLevel1Obj = ROOT.TLorentzVector()
            for iL1Obj in range(0, L1_nObjs):
                level1Obj = ROOT.TLorentzVector()
                if options.target == 'jet': 
                    if options.raw:
                        # new method of plotting results by just looking at the raw output from the Layer-1
                        level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.jetRawEt[iL1Obj]/2, level1Tree.L1Upgrade.jetEta[iL1Obj], level1Tree.L1Upgrade.jetPhi[iL1Obj], 0)
                    else:
                        level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.jetEt[iL1Obj], level1Tree.L1Upgrade.jetEta[iL1Obj], level1Tree.L1Upgrade.jetPhi[iL1Obj], 0)
                if options.target == 'ele': 
                    if options.raw:
                        # new method of plotting results by just looking at the raw output from the Layer-1
                        level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.egRawEt[iL1Obj]/2, level1Tree.L1Upgrade.egEta[iL1Obj], level1Tree.L1Upgrade.egPhi[iL1Obj], 0)
                    else:
                        level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.egEt[iL1Obj], level1Tree.L1Upgrade.egEta[iL1Obj], level1Tree.L1Upgrade.egPhi[iL1Obj], 0)

                #check matching
                if targetObj.DeltaR(level1Obj)<0.5:
                    matched = True
                    #keep only L1 match with highest pT
                    if level1Obj.Pt() > highestL1Pt:
                        myGoodLevel1Obj = level1Obj
                        myGood_iL1Obj = iL1Obj
                        highestL1Pt = level1Obj.Pt()

            if matched:
                #fill numerator histograms for every thresholds
                for i, thr in enumerate(thresholds): 
                    if matched and highestL1Pt > float(thr): passing_Er2p5[i].Fill(targetObj.Pt())

        if options.er:

            if targetObj.Eta()<float(options.er):

                total_Er0p0.Fill(targetObj.Pt())
                # loop on L1 jets to find match
                matched = False
                highestL1Pt = -99.
                myGood_iL1Obj = 0
                myGoodLevel1Obj = ROOT.TLorentzVector()
                for iL1Obj in range(0, L1_nObjs):
                    level1Obj = ROOT.TLorentzVector()
                    if options.target == 'jet': 
                        if options.raw:
                            # new method of plotting results by just looking at the raw output from the Layer-1
                            level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.jetRawEt[iL1Obj]/2, level1Tree.L1Upgrade.jetEta[iL1Obj], level1Tree.L1Upgrade.jetPhi[iL1Obj], 0)
                        else:
                            level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.jetEt[iL1Obj], level1Tree.L1Upgrade.jetEta[iL1Obj], level1Tree.L1Upgrade.jetPhi[iL1Obj], 0)
                    if options.target == 'ele': 
                        if options.raw:
                            # new method of plotting results by just looking at the raw output from the Layer-1
                            level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.egRawEt[iL1Obj]/2, level1Tree.L1Upgrade.egEta[iL1Obj], level1Tree.L1Upgrade.egPhi[iL1Obj], 0)
                        else:
                            level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.egEt[iL1Obj], level1Tree.L1Upgrade.egEta[iL1Obj], level1Tree.L1Upgrade.egPhi[iL1Obj], 0)

                    #check matching
                    if targetObj.DeltaR(level1Obj)<0.5:
                        matched = True
                        #keep only L1 match with highest pT
                        if level1Obj.Pt() > highestL1Pt:
                            myGoodLevel1Obj = level1Obj
                            myGood_iL1Obj = iL1Obj
                            highestL1Pt = level1Obj.Pt()

                if matched:
                    #fill numerator histograms for every thresholds
                    for i, thr in enumerate(thresholds): 
                        if matched and highestL1Pt > float(thr): passing_Er0p0[i].Fill(targetObj.Pt())

#define TGraphAsymmErrors for efficiency turn-ons
turnons = []

#defining binning of offline translation
offline_pts = []
for i in range(len(bins)-1):
    offline_pts.append((bins[i+1]+bins[i])/2)
mapping_dict = {'threshold':[], 'pt95eff':[], 'pt90eff':[], 'pt50eff':[]}

for i, thr in enumerate(thresholds):
    turnons.append(ROOT.TGraphAsymmErrors(passing[i], total, "cp"))

    turnonY = []
    shift = 0
    for ibin in range(0,len(offline_pts)):
        if turnons[i].GetPointX(ibin-shift) == offline_pts[ibin]:
            turnonY.append(turnons[i].GetPointY(ibin-shift))
        else:
            turnonY.append(0.0)
            shift += 1

    if len(turnonY) < len(offline_pts):
        for i in range(len(offline_pts)-len(turnonY)):
            turnonY.append(1.0)

    mapping_dict['pt95eff'].append(np.interp(0.95, turnonY, offline_pts)) #,right=-99,left=-98)
    mapping_dict['pt90eff'].append(np.interp(0.90, turnonY, offline_pts)) #,right=-99,left=-98)
    mapping_dict['pt50eff'].append(np.interp(0.50, turnonY, offline_pts)) #,right=-99,left=-98)

save_obj(mapping_dict, outdir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/online2offline_mapping_'+label+'.pkl')

turnons_Er2p5 = []

mapping_dict_Er2p5 = {'threshold':[], 'pt95eff':[], 'pt90eff':[], 'pt50eff':[]}
for i, thr in enumerate(thresholds):
    turnons_Er2p5.append(ROOT.TGraphAsymmErrors(passing_Er2p5[i], total_Er2p5, "cp"))

    turnonY_Er2p5 = []
    shift = 0
    for ibin in range(0,len(offline_pts)):
        if turnons_Er2p5[i].GetPointX(ibin-shift) == offline_pts[ibin]:
            turnonY_Er2p5.append(turnons_Er2p5[i].GetPointY(ibin-shift))
        else:
            turnonY_Er2p5.append(0.0)
            shift += 1

    if len(turnonY_Er2p5) < len(offline_pts):
        for i in range(len(offline_pts)-len(turnonY_Er2p5)):
            turnonY_Er2p5.append(1.0)

    mapping_dict_Er2p5['pt95eff'].append(np.interp(0.95, turnonY_Er2p5, offline_pts)) #,right=-99,left=-98)
    mapping_dict_Er2p5['pt90eff'].append(np.interp(0.90, turnonY_Er2p5, offline_pts)) #,right=-99,left=-98)
    mapping_dict_Er2p5['pt50eff'].append(np.interp(0.50, turnonY_Er2p5, offline_pts)) #,right=-99,left=-98)

save_obj(mapping_dict, outdir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/online2offline_mapping_Er2p5'+label+'.pkl')

if options.er:
        
    turnons_Er0p0 = []

    mapping_dict_Er0p0 = {'threshold':[], 'pt95eff':[], 'pt90eff':[], 'pt50eff':[]}
    for i, thr in enumerate(thresholds):
        turnons_Er0p0.append(ROOT.TGraphAsymmErrors(passing_Er0p0[i], total_Er0p0, "cp"))

        turnonY_Er0p0 = []
        shift = 0
        for ibin in range(0,len(offline_pts)):
            if turnons_Er0p0[i].GetPointX(ibin-shift) == offline_pts[ibin]:
                turnonY_Er0p0.append(turnons_Er0p0[i].GetPointY(ibin-shift))
            else:
                turnonY_Er0p0.append(0.0)
                shift += 1

        if len(turnonY_Er0p0) < len(offline_pts):
            for i in range(len(offline_pts)-len(turnonY_Er0p0)):
                turnonY_Er0p0.append(1.0)

        mapping_dict_Er0p0['pt95eff'].append(np.interp(0.95, turnonY_Er0p0, offline_pts)) #,right=-99,left=-98)
        mapping_dict_Er0p0['pt90eff'].append(np.interp(0.90, turnonY_Er0p0, offline_pts)) #,right=-99,left=-98)
        mapping_dict_Er0p0['pt50eff'].append(np.interp(0.50, turnonY_Er0p0, offline_pts)) #,right=-99,left=-98)

    save_obj(mapping_dict, outdir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/online2offline_mapping_Er'+er_label+label+'.pkl')

# Plot O2O

fig, ax = plt.subplots(figsize=(10,10))
plt.plot(thresholds, mapping_dict['pt95eff'], label='@ 95% efficiency', linewidth=2, color='blue')
plt.plot(thresholds, mapping_dict['pt90eff'], label='@ 90% efficiency', linewidth=2, color='red')
plt.plot(thresholds, mapping_dict['pt50eff'], label='@ 50% efficiency', linewidth=2, color='green')
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
leg = plt.legend(loc = 'lower right', fontsize=20)
leg._legend_box.align = "left"
plt.xlabel('L1 Threshold [GeV]')
plt.ylabel('Offline threshold [GeV]')
plt.xlim(20, 100)
plt.ylim(20, 120)
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.grid()
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/online2offline_mapping_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/online2offline_mapping_'+label+'_'+options.target+'.png')
plt.close()

fig, ax = plt.subplots(figsize=(10,10))
plt.plot(thresholds, mapping_dict_Er2p5['pt95eff'], label='@ 95% efficiency', linewidth=2, color='blue')
plt.plot(thresholds, mapping_dict_Er2p5['pt90eff'], label='@ 90% efficiency', linewidth=2, color='red')
plt.plot(thresholds, mapping_dict_Er2p5['pt50eff'], label='@ 50% efficiency', linewidth=2, color='green')
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
leg = plt.legend(loc = 'lower right', fontsize=20)
leg._legend_box.align = "left"
plt.xlabel('L1 Threshold [GeV]')
plt.ylabel('Offline threshold [GeV]')
plt.xlim(20, 100)
plt.ylim(20, 120)
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.grid()
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/online2offline_mapping_Er2p5'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/online2offline_mapping_Er2p5'+label+'_'+options.target+'.png')
plt.close()

if options.er:
    fig, ax = plt.subplots(figsize=(10,10))
    plt.plot(thresholds, mapping_dict_Er0p0['pt95eff'], label='@ 95% efficiency', linewidth=2, color='blue')
    plt.plot(thresholds, mapping_dict_Er0p0['pt90eff'], label='@ 90% efficiency', linewidth=2, color='red')
    plt.plot(thresholds, mapping_dict_Er0p0['pt50eff'], label='@ 50% efficiency', linewidth=2, color='green')
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc = 'lower right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel('L1 Threshold [GeV]')
    plt.ylabel('Offline threshold [GeV]')
    plt.xlim(20, 100)
    plt.ylim(20, 120)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/online2offline_mapping_Er'+er_label+label+'_'+options.target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/online2offline_mapping_Er'+er_label+label+'_'+options.target+'.png')
    plt.close()

# Plot Turn ons

if options.reco:
    if options.target == 'jet': x_label = '$E_{T}^{jet, offline}$ [GeV]'
    if options.target == 'ele': x_label = '$E_{T}^{e, offline}$ [GeV]'
    if options.target == 'met': x_label = '$MET_{\mu corrected}^{offline}$ [GeV]'
if options.gen:
    x_label = '$E_{T}^{jet, gen}$ [GeV]'

# cmap = matplotlib.cm.get_cmap('tab20c')
fig, ax = plt.subplots(figsize=(10,10))
for i, thr in enumerate(thresholds2plot):
    X = [] ; Y = [] ; Y_low = [] ; Y_high = []
    turnon = turnons[thresholds.index(thr)]
    for ibin in range(0,turnon.GetN()):
        X.append(turnon.GetPointX(ibin))
        Y.append(turnon.GetPointY(ibin))
        Y_low.append(turnon.GetErrorYlow(ibin))
        Y_high.append(turnon.GetErrorYhigh(ibin))
    ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label="$p_{T}^{L1} > $"+str(thr)+" GeV", lw=2, marker='o', color=cmap(i))
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
leg = plt.legend(loc = 'lower right', fontsize=20)
leg._legend_box.align = "left"
plt.xlabel(x_label)
plt.ylabel('Efficiency')
plt.xlim(0, 220)
plt.ylim(0, 1.05)
plt.grid()
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/turnOns_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/turnOns_'+label+'_'+options.target+'.png')
plt.close()

fig, ax = plt.subplots(figsize=(10,10))
for i, thr in enumerate(thresholds2plot):
    X = [] ; Y = [] ; Y_low = [] ; Y_high = []
    turnon = turnons_Er2p5[thresholds.index(thr)]
    for ibin in range(0,turnon.GetN()):
        X.append(turnon.GetPointX(ibin))
        Y.append(turnon.GetPointY(ibin))
        Y_low.append(turnon.GetErrorYlow(ibin))
        Y_high.append(turnon.GetErrorYhigh(ibin))
    ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label="$p_{T}^{L1} > $"+str(thr)+" GeV", lw=2, marker='o', color=cmap(i))
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
leg = plt.legend(loc = 'lower right', fontsize=20)
leg._legend_box.align = "left"
plt.xlabel(x_label)
plt.ylabel('Efficiency')
plt.xlim(0, 220)
plt.ylim(0, 1.05)
plt.grid()
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/turnOns_Er2p5_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/turnOns_Er2p5_'+label+'_'+options.target+'.png')
plt.close()

if options.er:
    fig, ax = plt.subplots(figsize=(10,10))
    for i, thr in enumerate(thresholds2plot):
        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnons_Er0p0[thresholds.index(thr)]
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label="$p_{T}^{L1} > $"+str(thr)+" GeV", lw=2, marker='o', color=cmap(i))
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc = 'lower right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Efficiency')
    plt.xlim(0, 220)
    plt.ylim(0, 1.05)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/turnOns_Er'+er_label+'_'+label+'_'+options.target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/turnOns_Er'+er_label+'_'+label+'_'+options.target+'.png')
    plt.close()

print("saving histograms and efficiencies in root file for later plotting if desired")
fileout = ROOT.TFile(outdir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/efficiency_graphs_'+label+'_'+options.target+'.root','RECREATE')
total.Write()
total_Er2p5.Write()
if options.er:
    total_Er0p0.Write()
for i, thr in enumerate(thresholds): 
    passing[i].Write()
    turnons[i].Write()
    passing_Er2p5[i].Write()
    turnons_Er2p5[i].Write()
    if options.er:
        passing_Er0p0[i].Write()
        turnons_Er0p0[i].Write()       

fileout.Close()
