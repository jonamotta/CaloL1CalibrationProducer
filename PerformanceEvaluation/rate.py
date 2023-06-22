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

def load_obj(source):
    with open(source,'rb') as f:
        return pickle.load(f)

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
parser.add_option("--unpacked",  dest="unpacked", action='store_true', default=False)
parser.add_option("--offline",   dest="offline",  action='store_true', default=False)
parser.add_option("--er",        dest="er",       default='2.5') #eta restriction
parser.add_option("--raw",       dest="raw",      action='store_true', default=False)
(options, args) = parser.parse_args()

# get/create folders
indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/"+options.indir
outdir = "/data_CMS/cms/motta/CaloL1calibraton/"+options.outdir
label = options.label
os.system('mkdir -p '+outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs')
os.system('mkdir -p '+outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs')
os.system('mkdir -p '+outdir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs')

# define input trees
if options.unpacked: level1Tree = ROOT.TChain("l1UpgradeTree/L1UpgradeTree")
else:                level1Tree = ROOT.TChain("l1UpgradeEmuTree/L1UpgradeTree")

# read input files
level1Tree.Add(indir+"/Ntuple*.root")
nEntries = level1Tree.GetEntries()
print(nEntries, "entries")

#run on entries specified by usuer, or only on entries available if that is exceeded
nevents = options.nEvts
if (nevents > nEntries) or (nevents==-1): nevents = nEntries
print("will process",nevents,"events...")

denominator = 0.
nb = 2544.
scale = 0.001*(nb*11245.6)

ptProgression0 = ROOT.TH1F("ptProgression0","ptProgression0",240,0.,240.)
ptDiProgression0 = ROOT.TH2F("ptDiProgression0","ptDiProgression0",240,0.,240.,240,0.,240.)
rateProgression0 = ROOT.TH1F("rateProgression0","rateProgression0",240,0.,240.)
rateDiProgression0 = ROOT.TH1F("rateDiProgression0","rateDiProgression0",240,0.,240.)
ptProgression0er2p5 = ROOT.TH1F("ptProgression0er2p5","ptProgression0er2p5",240,0.,240.)
ptDiProgression0er2p5 = ROOT.TH2F("ptDiProgression0er2p5","ptDiProgression0er2p5",240,0.,240.,240,0.,240.)
rateProgression0er2p5 = ROOT.TH1F("rateProgression0er2p5","rateProgression0er2p5",240,0.,240.)
rateDiProgression0er2p5 = ROOT.TH1F("rateDiProgression0er2p5","rateProgression0er2p5",240,0.,240.)
if options.er:
    er_label = options.er.replace(".", "p")
    ptProgression0er0p0 = ROOT.TH1F("ptProgression0er{}".format(er_label),"ptProgression0er{}".format(er_label),240,0.,240.)
    ptDiProgression0er0p0 = ROOT.TH2F("ptDiProgression0er{}".format(er_label),"ptDiProgression0er{}".format(er_label),240,0.,240.,240,0.,240.)
    rateProgression0er0p0 = ROOT.TH1F("rateProgression0er{}".format(er_label),"rateProgression0er{}".format(er_label),240,0.,240.)
    rateDiProgression0er0p0 = ROOT.TH1F("rateDiProgression0er{}".format(er_label),"rateProgression0er{}".format(er_label),240,0.,240.)

thresholds = [0, 20, 35, 50, 100, 150]
offline = options.offline
if offline:
    mapping_dict = load_obj(outdir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/online2offline_mapping_'+label+'.pkl')
    online_thresholds = np.linspace(20,150,131).tolist()

print("looping on events")
for i in tqdm(range(0, nevents)):
    # if i%1000==0: print(i)
    #getting entries
    entry = level1Tree.GetEntry(i)
    
    # skip corrupted entries
    if not entry: continue

    denominator += 1.

    filledProgression0  = False
    filledProgression0er2p5  = False
    if options.er: filledProgression0er0p0  = False

    IndexJetsProgression0 = array('f',[-1,-1])
    ptJetsProgression0 = array('f',[-99.,-99.])

    IndexJetsProgression0er2p5 = array('f',[-1,-1])
    ptJetsProgression0er2p5 = array('f',[-99.,-99.])

    if options.er: IndexJetsProgression0er0p0 = array('f',[-1,-1])
    if options.er: ptJetsProgression0er0p0 = array('f',[-99.,-99.])

    L1_nObjs = 0
    if options.target == 'jet':
        L1_nObjs = level1Tree.L1Upgrade.nJets
    if options.target == 'ele':
        L1_nObjs = level1Tree.L1Upgrade.nEGs

    #loop on L1 jets to find match
    for iL1Obj in range(0, L1_nObjs):

        if options.target == 'jet' and level1Tree.L1Upgrade.jetBx[iL1Obj] != 0: continue
        if options.target == 'ele' and level1Tree.L1Upgrade.egBx[iL1Obj] != 0: continue

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
        
        # single
        if filledProgression0==False:
            if offline: ptProgression0.Fill(np.interp(level1Obj.Pt(), online_thresholds, mapping_dict[offline]))
            else:       ptProgression0.Fill(level1Obj.Pt())
            filledProgression0 = True

        # di
        if level1Obj.Pt()>=ptJetsProgression0[0]:
            IndexJetsProgression0[1]=IndexJetsProgression0[0]
            ptJetsProgression0[1]=ptJetsProgression0[0]
            IndexJetsProgression0[0]=iL1Obj
            ptJetsProgression0[0]=level1Obj.Pt()
        elif level1Obj.Pt()>=ptJetsProgression0[1]:
            IndexJetsProgression0[1]=iL1Obj
            ptJetsProgression0[1]=level1Obj.Pt()                

        if abs(level1Obj.Eta())<2.5:

            # single
            if filledProgression0er2p5==False:
                if offline: ptProgression0er2p5.Fill(np.interp(level1Obj.Pt(), online_thresholds, mapping_dict[offline]))
                else:       ptProgression0er2p5.Fill(level1Obj.Pt())
                filledProgression0er2p5 = True

            # di
            if level1Obj.Pt()>=ptJetsProgression0er2p5[0]:
                IndexJetsProgression0er2p5[1]=IndexJetsProgression0er2p5[0]
                ptJetsProgression0er2p5[1]=ptJetsProgression0er2p5[0]
                IndexJetsProgression0er2p5[0]=iL1Obj
                ptJetsProgression0er2p5[0]=level1Obj.Pt()
            elif level1Obj.Pt()>=ptJetsProgression0er2p5[1]:
                IndexJetsProgression0er2p5[1]=iL1Obj
                ptJetsProgression0er2p5[1]=level1Obj.Pt()

        if options.er:
            if abs(level1Obj.Eta())<float(options.er):
                # single
                if filledProgression0er0p0==False:
                    if offline: ptProgression0er0p0.Fill(np.interp(level1Obj.Pt(), online_thresholds, mapping_dict[offline]))
                    else:       ptProgression0er0p0.Fill(level1Obj.Pt())
                    filledProgression0er0p0 = True

                # di
                if level1Obj.Pt()>=ptJetsProgression0er0p0[0]:
                    IndexJetsProgression0er0p0[1]=IndexJetsProgression0er0p0[0]
                    ptJetsProgression0er0p0[1]=ptJetsProgression0er0p0[0]
                    IndexJetsProgression0er0p0[0]=iL1Obj
                    ptJetsProgression0er0p0[0]=level1Obj.Pt()
                elif level1Obj.Pt()>=ptJetsProgression0er0p0[1]:
                    IndexJetsProgression0er0p0[1]=iL1Obj
                    ptJetsProgression0er0p0[1]=level1Obj.Pt()

    if IndexJetsProgression0[0]>=0 and IndexJetsProgression0[1]>=0:
        if offline: ptDiProgression0.Fill(np.interp(ptJetsProgression0[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression0[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression0.Fill(ptJetsProgression0[0],ptJetsProgression0[1])
    
    if IndexJetsProgression0er2p5[0]>=0 and IndexJetsProgression0er2p5[1]>=0:
        if offline: ptDiProgression0er2p5.Fill(np.interp(ptJetsProgression0er2p5[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression0er2p5[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression0er2p5.Fill(ptJetsProgression0er2p5[0],ptJetsProgression0er2p5[1])

    if options.er:
        if IndexJetsProgression0er0p0[0]>=0 and IndexJetsProgression0er0p0[1]>=0:
            if offline: ptDiProgression0er0p0.Fill(np.interp(ptJetsProgression0er0p0[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression0er0p0[1], online_thresholds, mapping_dict[offline]))
            else:       ptDiProgression0er0p0.Fill(ptJetsProgression0er0p0[0],ptJetsProgression0er0p0[1])

for i in range(0,241):
    rateProgression0.SetBinContent(i+1,ptProgression0.Integral(i+1,241)/denominator*scale)
    rateDiProgression0.SetBinContent(i+1,ptDiProgression0.Integral(i+1,241,i+1,241)/denominator*scale)
    rateProgression0er2p5.SetBinContent(i+1,ptProgression0er2p5.Integral(i+1,241)/denominator*scale)
    rateDiProgression0er2p5.SetBinContent(i+1,ptDiProgression0er2p5.Integral(i+1,241,i+1,241)/denominator*scale)
    if options.er:
        rateProgression0er0p0.SetBinContent(i+1,ptProgression0er0p0.Integral(i+1,241)/denominator*scale)
        rateDiProgression0er0p0.SetBinContent(i+1,ptDiProgression0er0p0.Integral(i+1,241,i+1,241)/denominator*scale)


cmap = matplotlib.cm.get_cmap('Set1')

if options.target == 'jet':
    label_singleObj = r'Single-jet'
    label_doubleObj = r'Double-jet'
    x_label = r'$E_{T}^{jet, L1}$'
if options.target == 'ele':
    label_singleObj = r'Single-$e/\gamma$'
    label_doubleObj = r'Double-$e/\gamma$'
    x_label = r'$E_{T}^{e/\gamma, L1}$'

fig, ax = plt.subplots(figsize=(10,10))

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = rateProgression0
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=label_singleObj, lw=2, marker='o', color=cmap(0))

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = rateDiProgression0
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=label_doubleObj, lw=2, marker='o', color=cmap(1))

for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
leg = plt.legend(loc = 'upper right', fontsize=20)
leg._legend_box.align = "left"
plt.xlabel(x_label)
plt.ylabel('Rate [kHz]')
plt.xlim(0, 120)
plt.ylim(0.1, 1E5)
# plt.xscale('symlog')
plt.yscale('log')
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.grid()
mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/rate_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/rate_'+label+'_'+options.target+'.png')
plt.close()


if options.target == 'jet':
    label_singleObj = r'Single-jet $|\eta|<2.5$'
    label_doubleObj = r'Double-jet $|\eta|<2.5$'
    x_label = r'$E_{T}^{jet, L1}$'
if options.target == 'ele':
    label_singleObj = r'Single-$e/\gamma$ $|\eta|<2.5$'
    label_doubleObj = r'Double-$e/\gamma$ $|\eta|<2.5$'
    x_label = r'$E_{T}^{e/\gamma, L1}$'

fig, ax = plt.subplots(figsize=(10,10))

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = rateProgression0er2p5
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=label_singleObj, lw=2, marker='o', color=cmap(0))

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = rateDiProgression0er2p5
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=label_doubleObj, lw=2, marker='o', color=cmap(1))

for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
leg = plt.legend(loc = 'upper right', fontsize=20)
leg._legend_box.align = "left"
plt.xlabel(x_label)
plt.ylabel('Rate [kHz]')
plt.xlim(0, 120)
# plt.xscale('symlog')
plt.ylim(0.1, 1E5)
plt.yscale('log')
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.grid()
mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/rateEr2p5_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/rateEr2p5_'+label+'_'+options.target+'.png')
plt.close()



if options.er:
    if options.target == 'jet':
        label_singleObj = r'Single-jet $|\eta|<{}$'.format(options.er)
        label_doubleObj = r'Double-jet $|\eta|<{}$'.format(options.er)
        x_label = r'$E_{T}^{jet, L1}$'
    if options.target == 'ele':
        label_singleObj = r'Single-$e/\gamma$ $|\eta|<{}$'.format(options.er)
        label_doubleObj = r'Double-$e/\gamma$ $|\eta|<{}$'.format(options.er)
        x_label = r'$E_{T}^{e/\gamma, L1}$'

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateProgression0er0p0
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=label_singleObj, lw=2, marker='o', color=cmap(0))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateDiProgression0er0p0
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=label_doubleObj, lw=2, marker='o', color=cmap(1))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc = 'upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Rate [kHz]')
    plt.xlim(0, 120)
    # plt.xscale('symlog')
    plt.ylim(0.1, 1E5)
    plt.yscale('log')
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/rateEr'+er_label+'_'+label+'_'+options.target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/rateEr'+er_label+'_'+label+'_'+options.target+'.png')
    plt.close()

####################

print("saving histograms and efficiencies in root file for later plotting if desired")
fileout = ROOT.TFile(outdir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/rate_graphs_'+label+'_'+options.target+'.root','RECREATE')
ptProgression0.Write()
ptDiProgression0.Write()
rateProgression0.Write()
rateDiProgression0.Write()
ptProgression0er2p5.Write()
ptDiProgression0er2p5.Write()
rateProgression0er2p5.Write()
rateDiProgression0er2p5.Write()
if options.er:
    ptProgression0er0p0.Write()
    ptDiProgression0er0p0.Write()
    rateProgression0er0p0.Write()
    rateDiProgression0er0p0.Write()
fileout.Close()






