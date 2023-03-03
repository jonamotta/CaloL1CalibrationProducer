from array import array
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(000000)
import sys
import os

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import matplotlib
import mplhep
plt.style.use(mplhep.style.CMS)

def save_obj(obj,dest):
    with open(dest,'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--indir",     dest="indir",    default=None)
parser.add_option("--outdir",    dest="outdir",   default=None)
parser.add_option("--label",     dest="label",    default=None)
parser.add_option("--nEvts",     dest="nEvts",    type=int, default=-1)
parser.add_option("--target",    dest="target",   default=None)
parser.add_option("--reco",      dest="reco",     action='store_true', default=False)
parser.add_option("--gen",       dest="gen",      action='store_true', default=False)
parser.add_option("--unpacked",  dest="unpacked", action='store_true', default=False)
(options, args) = parser.parse_args()

# get/create folders
indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/"+options.indir
outdir = "/data_CMS/cms/motta/CaloL1calibraton/"+options.outdir
label = options.label
os.system('mkdir -p '+outdir+'/PerformancePlots/'+label+'/PDFs')
os.system('mkdir -p '+outdir+'/PerformancePlots/'+label+'/PNGs')
os.system('mkdir -p '+outdir+'/PerformancePlots/'+label+'/ROOTs')

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
if options.target == 'jet':
    ptBins  = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200, 500]
    etaBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.191]
    signedEtaBins = [-5.191, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.479, -1.305, -1.0, -0.5, 0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.191]
if options.target == 'ele':
    ptBins  = [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200]
    etaBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0]
    signedEtaBins = [-3.0, -2.5, -2.0, -1.479, -1.305, -1.0, -0.5, 0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0]

# PT RESPONSE - INCLUSIVE HISTOGRAMS
pt_response_ptInclusive = ROOT.TH1F("pt_response_ptInclusive","pt_response_ptInclusive",60,0,3)
pt_barrel_resp_ptInclusive = ROOT.TH1F("pt_barrel_resp_ptInclusive","pt_barrel_resp_ptInclusive",60,0,3)
pt_endcap_resp_ptInclusive = ROOT.TH1F("pt_endcap_resp_ptInclusive","pt_endcap_resp_ptInclusive",60,0,3)

# PT RESPONSE - PT BINS HISTOGRAMS
response_ptBins = []
barrel_response_ptBins = []
endcap_response_ptBins = []
for i in range(len(ptBins)-1):
    response_ptBins.append(ROOT.TH1F("pt_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]),"pt_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]),60,0,3))
    barrel_response_ptBins.append(ROOT.TH1F("pt_barrel_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]),"pt_barrel_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]),60,0,3))
    endcap_response_ptBins.append(ROOT.TH1F("pt_endcap_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]),"pt_endcap_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]),60,0,3))

# PT RESPONSE -  ETA BINS HISTIGRAMS
absEta_response_ptBins = []
minusEta_response_ptBins = []
plusEta_response_ptBins = []
for i in range(len(etaBins)-1):
    absEta_response_ptBins.append(ROOT.TH1F("pt_resp_AbsEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]),"pt_resp_AbsEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]),60,0,3))
    minusEta_response_ptBins.append(ROOT.TH1F("pt_resp_MinusEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]),"pt_resp_MinusEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]),60,0,3))
    plusEta_response_ptBins.append(ROOT.TH1F("pt_resp_PlusEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]),"pt_resp_PlusEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]),60,0,3))

pt_resp_PtEtaBin = []
for i in range(len(ptBins)-1):
    for j in range(len(etaBins)-1):
        lowP  = str(ptBins[i])
        lowE  = str(etaBins[j])
        highP = str(ptBins[i+1])
        highE = str(etaBins[j+1])
        pt_resp_PtEtaBin.append(ROOT.TH1F("pt_resp_PtBin"+lowP+"to"+highP+"_EtaBin"+lowE+"to"+highE,"pt_resp_PtBin"+lowP+"to"+highP+"_EtaBin"+lowE+"to"+highE,60,0,3))

print("looping on events")
for i in range(0, nevents):
    if i%1000==0: print(i)
    #getting entries
    entry2 = level1Tree.GetEntry(i)
    entry3 = targetTree.GetEntry(i)

    L1_nObjs = 0
    if options.target == 'jet':
        L1_nObjs = level1Tree.L1Upgrade.nJets
        target_nObjs = targetTree.Jet.nJets
    if options.target == 'ele':
        L1_nObjs = level1Tree.L1Upgrade.nEGs
        target_nObjs = targetTree.Electron.nElectrons

    #loop on generator jets
    for igenJet in range(0,target_nObjs):

        if options.target == 'jet':
            targetObj = ROOT.TLorentzVector()
            targetObj.SetPtEtaPhiM(targetTree.Jet.etCorr[igenJet], targetTree.Jet.eta[igenJet], targetTree.Jet.phi[igenJet], 0)

        if options.target == 'ele':
            targetObj = ROOT.TLorentzVector()
            targetObj.SetPtEtaPhiM(targetTree.Electron.et[igenJet], targetTree.Electron.eta[igenJet], targetTree.Electron.phi[igenJet], 0)

        # skip jets that cannot be reconstructed by L1 (limit is 5.191)
        if targetObj.Eta()>5.0: continue
        
        # skip egs that cannot be reconstructed by L1 (limit is 3.0)
        if options.target == 'ele' and targetObj.Eta()>3.0: continue

        #reject very soft jets, usually poorly defined
        if options.target == 'jet' and targetObj.Pt()<15.: continue

        matched = False
        highestL1Pt = -99.

        #loop on L1 jets to find match
        for iL1Obj in range(0, L1_nObjs):
            level1Obj = ROOT.TLorentzVector()
            if options.target == 'jet': level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.jetEt[iL1Obj], level1Tree.L1Upgrade.jetEta[iL1Obj], level1Tree.L1Upgrade.jetPhi[iL1Obj], 0)
            if options.target == 'ele': level1Obj.SetPtEtaPhiM(level1Tree.L1Upgrade.egEt[iL1Obj], level1Tree.L1Upgrade.egEta[iL1Obj], level1Tree.L1Upgrade.egPhi[iL1Obj], 0)

            #check matching
            if targetObj.DeltaR(level1Obj)<0.5:
                matched = True
                #keep only L1 match with highest pT
                if level1Obj.Pt()>highestL1Pt:
                    highestL1Pt = level1Obj.Pt()

        if matched:
            pt_response_ptInclusive.Fill(highestL1Pt/targetObj.Pt())

            if abs(targetObj.Eta()) < 1.305:
                pt_barrel_resp_ptInclusive.Fill(highestL1Pt/targetObj.Pt())
            elif abs(targetObj.Eta()) < 5.191 and abs(targetObj.Eta()) > 1.479:
                pt_endcap_resp_ptInclusive.Fill(highestL1Pt/targetObj.Pt())

            for i in range(len(ptBins)-1):
                if targetObj.Pt() > ptBins[i] and targetObj.Pt() <= ptBins[i+1]:
                    response_ptBins[i].Fill(highestL1Pt/targetObj.Pt())
                    
                    if abs(targetObj.Eta()) < 1.305:
                        barrel_response_ptBins[i].Fill(highestL1Pt/targetObj.Pt())
                    elif abs(targetObj.Eta()) < 5.191 and abs(targetObj.Eta()) > 1.479:
                        endcap_response_ptBins[i].Fill(highestL1Pt/targetObj.Pt())

            for i in range(len(etaBins)-1):
                if abs(targetObj.Eta()) > etaBins[i] and abs(targetObj.Eta()) < etaBins[i+1]:
                    absEta_response_ptBins[i].Fill(highestL1Pt/targetObj.Pt())

                if targetObj.Eta() > etaBins[i] and targetObj.Eta() < etaBins[i+1]:
                    plusEta_response_ptBins[i].Fill(highestL1Pt/targetObj.Pt())

                elif targetObj.Eta() < -etaBins[i] and targetObj.Eta() > -etaBins[i+1]:
                    minusEta_response_ptBins[i].Fill(highestL1Pt/targetObj.Pt())

            k = 0
            for i in range(len(ptBins)-1):
                for j in range(len(etaBins)-1):
                    if abs(targetObj.Eta()) > etaBins[j] and abs(targetObj.Eta()) < etaBins[j+1] and targetObj.Pt() > ptBins[i] and targetObj.Pt() < ptBins[i+1]:
                        pt_resp_PtEtaBin[k].Fill(highestL1Pt/targetObj.Pt());

                    k += 1

        # else:
        #     pt_response_ptInclusive.Fill(0.)

        #     if abs(targetObj.Eta()) < 1.305:
        #         pt_barrel_resp_ptInclusive.Fill(0.)
        #     elif abs(targetObj.Eta()) < 5.191 and abs(targetObj.Eta()) > 1.479:
        #         pt_endcap_resp_ptInclusive.Fill(0.)

        #     for i in range(len(ptBins)-1):
        #         if targetObj.Pt() > ptBins[i] and targetObj.Pt() <= ptBins[i+1]:
        #             response_ptBins[i].Fill(0)
                    
        #             if abs(targetObj.Eta()) < 1.305:
        #                 barrel_response_ptBins[i].Fill(0.)
        #             elif abs(targetObj.Eta()) < 5.191 and abs(targetObj.Eta()) > 1.479:
        #                 endcap_response_ptBins[i].Fill(0.)

        #     for i in range(len(etaBins)-1):
        #         if abs(targetObj.Eta()) > etaBins[i] and abs(targetObj.Eta()) < etaBins[i+1]:
        #             absEta_response_ptBins[i].Fill(0.)

        #         if targetObj.Eta() > etaBins[i] and targetObj.Eta() < etaBins[i+1]:
        #             plusEta_response_ptBins[i].Fill(0.)

        #         elif targetObj.Eta() < -etaBins[i] and targetObj.Eta() > -etaBins[i+1]:
        #             minusEta_response_ptBins[i].Fill(0.)


# scale everything to unity
pt_response_ptInclusive.Scale(1.0/pt_response_ptInclusive.Integral())
pt_barrel_resp_ptInclusive.Scale(1.0/pt_barrel_resp_ptInclusive.Integral())
pt_endcap_resp_ptInclusive.Scale(1.0/pt_endcap_resp_ptInclusive.Integral())

for i in range(len(response_ptBins)):
    response_ptBins[i].Scale(1.0/response_ptBins[i].Integral())
    barrel_response_ptBins[i].Scale(1.0/barrel_response_ptBins[i].Integral())
    endcap_response_ptBins[i].Scale(1.0/endcap_response_ptBins[i].Integral())

for i in range(len(minusEta_response_ptBins)):
    minusEta_response_ptBins[i].Scale(1.0/minusEta_response_ptBins[i].Integral())
    plusEta_response_ptBins[i].Scale(1.0/plusEta_response_ptBins[i].Integral())
    absEta_response_ptBins[i].Scale(1.0/absEta_response_ptBins[i].Integral())

# make resolution plots
pt_resol_fctPt = ROOT.TH1F("pt_resol_fctPt","pt_resol_fctPt",len(ptBins)-1, array('f',ptBins))
pt_resol_barrel_fctPt = ROOT.TH1F("pt_resol_barrel_fctPt","pt_resol_barrel_fctPt",len(ptBins)-1, array('f',ptBins))
pt_resol_endcap_fctPt = ROOT.TH1F("pt_resol_endcap_fctPt","pt_resol_endcap_fctPt",len(ptBins)-1, array('f',ptBins))
pt_resol_fctAbsEta = ROOT.TH1F("pt_resol_fctAbsEta","pt_resol_fctAbsEta",len(etaBins)-1, array('f',etaBins))
pt_resol_fctEta = ROOT.TH1F("pt_resol_fctEta","pt_resol_fctEta",len(signedEtaBins)-1, array('f',signedEtaBins))

pt_scale_fctPt = ROOT.TH1F("pt_scale_fctPt","pt_scale_fctPt",len(ptBins)-1, array('f',ptBins))
pt_scale_fctEta = ROOT.TH1F("pt_scale_fctEta","pt_scale_fctEta",len(signedEtaBins)-1, array('f',signedEtaBins))

PTvsETA_resolution = ROOT.TH2F("PTvsETA_resolution","PTvsETA_resolution",len(ptBins)-1, array('f',ptBins),len(etaBins)-1, array('f',etaBins));
PTvsETA_scale = ROOT.TH2F("PTvsETA_events","PTvsETA_events",len(ptBins)-1, array('f',ptBins),len(etaBins)-1, array('f',etaBins));

for i in range(len(barrel_response_ptBins)):
    pt_scale_fctPt.SetBinContent(i+1, response_ptBins[i].GetMean())
    pt_scale_fctPt.SetBinError(i+1, response_ptBins[i].GetMeanError())

    pt_resol_fctPt.SetBinContent(i+1, response_ptBins[i].GetRMS()/response_ptBins[i].GetMean())
    pt_resol_fctPt.SetBinError(i+1, response_ptBins[i].GetRMSError()/response_ptBins[i].GetMean())

    pt_resol_barrel_fctPt.SetBinContent(i+1, barrel_response_ptBins[i].GetRMS()/barrel_response_ptBins[i].GetMean())
    pt_resol_endcap_fctPt.SetBinError(i+1, barrel_response_ptBins[i].GetRMSError()/barrel_response_ptBins[i].GetMean())

    pt_resol_endcap_fctPt.SetBinContent(i+1, endcap_response_ptBins[i].GetRMS()/endcap_response_ptBins[i].GetMean())
    pt_resol_endcap_fctPt.SetBinError(i+1, endcap_response_ptBins[i].GetRMSError()/endcap_response_ptBins[i].GetMean())

for i in range(len(minusEta_response_ptBins)):
    pt_scale_fctEta.SetBinContent(len(etaBins)-1-i, minusEta_response_ptBins[i].GetMean())
    pt_scale_fctEta.SetBinError(len(etaBins)-1-i, minusEta_response_ptBins[i].GetMeanError())
    pt_scale_fctEta.SetBinContent(i+len(etaBins), plusEta_response_ptBins[i].GetMean())
    pt_scale_fctEta.SetBinError(i+len(etaBins), plusEta_response_ptBins[i].GetMeanError())

    pt_resol_fctEta.SetBinContent(len(etaBins)-1-i, minusEta_response_ptBins[i].GetRMS()/minusEta_response_ptBins[i].GetMean())
    pt_resol_fctEta.SetBinError(len(etaBins)-1-i, minusEta_response_ptBins[i].GetRMSError()/minusEta_response_ptBins[i].GetMean())
    pt_resol_fctEta.SetBinContent(i+len(etaBins), plusEta_response_ptBins[i].GetRMS()/plusEta_response_ptBins[i].GetMean())
    pt_resol_fctEta.SetBinError(i+len(etaBins), plusEta_response_ptBins[i].GetRMSError()/plusEta_response_ptBins[i].GetMean())


k = 0;
for i in range(len(ptBins)-1):
    for j in range(len(etaBins)-1):
        if pt_resp_PtEtaBin[k].GetMean() != 0.:
            PTvsETA_resolution.SetBinContent(i,j,pt_resp_PtEtaBin[k].GetRMS()/pt_resp_PtEtaBin[k].GetMean());
            PTvsETA_resolution.SetBinError(i,j,pt_resp_PtEtaBin[k].GetRMSError()/pt_resp_PtEtaBin[k].GetMean());
            
            PTvsETA_scale.SetBinContent(i,j,pt_resp_PtEtaBin[k].GetMean());
            PTvsETA_scale.SetBinError(i,j,pt_resp_PtEtaBin[k].GetMeanError());

        k += 1


cmap = matplotlib.cm.get_cmap('Set1')

############################################################################################
## response in pt bins

if options.reco:
    if options.target == 'jet':
        x_lim = (0.,3.)
        barrel_label = r'Barrel $|\eta^{jet, offline}|<1.305$'
        endcap_label = r'Endcap $1.479<|\eta^{jet, offline}|<5.191$'
        inclusive_label = r'Inclusive $|\eta^{jet, offline}|<5.191$'
        legend_label = r'$<|p_{T}^{jet, offline}|<$'
        x_label = r'$p_{T}^{jet, offline}$'
    if options.target == 'ele':
        x_lim = (0.,3.)
        barrel_label = r'Barrel $|\eta^{e, offline}|<1.305$'
        endcap_label = r'Endcap $1.479<|\eta^{e, offline}|<3.0$'
        inclusive_label = r'Inclusive $|\eta^{e, offline}|<3.0$'
        legend_label = r'$<|p_{T}^{e, offline}|<$'
        x_label = r'$p_{T}^{e, offline}$'
if options.gen:
    if options.target == 'jet':
        x_lim = (0.,3.)
        barrel_label = r'Barrel $|\eta^{jet, gen}|<1.305$'
        endcap_label = r'Endcap $1.479<|\eta^{jet, gen}|<5.191$'
        inclusive_label = r'Inclusive $|\eta^{jet, gen}|<5.191$'
        legend_label = r'$<|p_{T}^{jet, gen}|<$'
        x_label = r'$p_{T}^{jet, gen}$'
    if options.target == 'ele':
        x_lim = (0.,3.)
        barrel_label = r'Barrel $|\eta^{e, gen}|<1.305$'
        endcap_label = r'Endcap $1.479<|\eta^{e, gen}|<3.0$'
        inclusive_label = r'Inclusive $|\eta^{e, gen}|<3.0$'
        legend_label = r'$<|p_{T}^{e, gen}|<$'
        x_label = r'$p_{T}^{e, gen}$'

for i in range(len(barrel_response_ptBins)):
    fig, ax = plt.subplots(figsize=(10,10))
    
    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = barrel_response_ptBins[i]
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=barrel_label, lw=2, marker='o', color=cmap(0))
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = endcap_response_ptBins[i]
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=endcap_label, lw=2, marker='o', color=cmap(1))
    Ymax = max(Ymax, max(Y))
    
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc = 'upper right', fontsize=20, title=str(ptBins[i])+legend_label+str(ptBins[i+1]), title_fontsize=18)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('a.u.')
    plt.xlim(x_lim)
    plt.ylim(0., Ymax*1.3)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots/'+label+'/PDFs/response_'+str(ptBins[i])+"pt"+str(ptBins[i+1])+'_'+label+'_'+options.target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots/'+label+'/PNGs/response_'+str(ptBins[i])+"pt"+str(ptBins[i+1])+'_'+label+'_'+options.target+'.png')
    plt.close()

############################################################################################
## response inclusive 

fig, ax = plt.subplots(figsize=(10,10))

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = pt_barrel_resp_ptInclusive
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=barrel_label, lw=2, marker='o', color=cmap(0))
Ymax = max(Y)

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = pt_endcap_resp_ptInclusive
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=endcap_label, lw=2, marker='o', color=cmap(1))
Ymax = max(Ymax, max(Y))

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = pt_response_ptInclusive
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=barrel_label, lw=2, marker='o', color=cmap(2))
Ymax = max(Ymax, max(Y))

for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
leg = plt.legend(loc = 'upper right', fontsize=20)
leg._legend_box.align = "left"
plt.xlabel(x_label)
plt.ylabel('a.u.')
plt.xlim(x_lim)
plt.ylim(0., Ymax*1.3)
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.grid()
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots/'+label+'/PDFs/response_ptInclusive_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots/'+label+'/PNGs/response_ptInclusive_'+label+'_'+options.target+'.png')
plt.close()

############################################################################################
## resolution in pt bins

fig, ax = plt.subplots(figsize=(10,10))
    
X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = pt_resol_barrel_fctPt
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=barrel_label, lw=2, marker='o', color=cmap(0))
Ymax = max(Y)

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = pt_resol_endcap_fctPt
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=endcap_label, lw=2, marker='o', color=cmap(1))
Ymax = max(Ymax, max(Y))

for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
leg = plt.legend(loc = 'upper right', fontsize=20)
leg._legend_box.align = "left"
plt.xlabel(x_label)
plt.ylabel('Energy resolution')
plt.xlim(0,150)
plt.ylim(0., Ymax*1.3)
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.grid()
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots/'+label+'/PDFs/resolution_ptBins_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots/'+label+'/PNGs/resolution_ptBins_'+label+'_'+options.target+'.png')
plt.close()

############################################################################################
## scale in pt bins

fig, ax = plt.subplots(figsize=(10,10))
    
X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = pt_scale_fctPt
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, lw=2, marker='o', color=cmap(0))

for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.xlabel(x_label)
plt.ylabel('Energy scale')
plt.xlim()
plt.ylim(0.5, 1.5)
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.grid()
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots/'+label+'/PDFs/scale_ptBins_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots/'+label+'/PNGs/scale_ptBins_'+label+'_'+options.target+'.png')
plt.close()

############################################################################################
## resolution in eta bins

if options.reco:
    if options.target == 'jet':
        x_lim = (-5.2,5.2)
    if options.target == 'ele':
        x_lim = (-3.01,3.01)

fig, ax = plt.subplots(figsize=(10,10))
plt.grid(zorder=0)

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = pt_resol_fctEta
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, ls='None', lw=2, marker='o', color=cmap(0), zorder=1)
Ymax = max(Y)

rect1 = patches.Rectangle((-1.479, 0), 0.174, Ymax*1.3, linewidth=1, edgecolor='gray', facecolor='gray', zorder=2)
rect2 = patches.Rectangle((1.305, 0), 0.174, Ymax*1.3, linewidth=1, edgecolor='gray', facecolor='gray', zorder=2)
ax.add_patch(rect1)
ax.add_patch(rect2)

for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.xlabel(x_label)
plt.ylabel('Energy resolution')
plt.xlim()
plt.ylim(0., Ymax*1.3)
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots/'+label+'/PDFs/resolution_etaBins_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots/'+label+'/PNGs/resolution_etaBins_'+label+'_'+options.target+'.png')
plt.close()

############################################################################################
## scale in eta bins

if options.reco:
    if options.target == 'jet':
        x_lim = (-5.2,5.2)
    if options.target == 'ele':
        x_lim = (-3.01,3.01)

fig, ax = plt.subplots(figsize=(10,10))
plt.grid(zorder=0)

X = [] ; Y = [] ; X_err = [] ; Y_err = []
histo = pt_scale_fctEta
for ibin in range(0,histo.GetNbinsX()):
    X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
    Y.append(histo.GetBinContent(ibin+1))
    X_err.append(histo.GetBinWidth(ibin+1)/2.)
    Y_err.append(histo.GetBinError(ibin+1))
ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, lw=2, marker='o', color=cmap(0), zorder=1)
Ymax = max(Y)

rect1 = patches.Rectangle((-1.479, 0.5), 0.174, 1.5, linewidth=1, edgecolor='gray', facecolor='gray', zorder=2)
rect2 = patches.Rectangle((1.305, 0.5), 0.174, 1.5, linewidth=1, edgecolor='gray', facecolor='gray', zorder=2)
ax.add_patch(rect1)
ax.add_patch(rect2)

for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
plt.xlabel(x_label)
plt.ylabel('Energy scale')
plt.xlim()
plt.ylim(0.5, 1.5)
for xtick in ax.xaxis.get_major_ticks():
    xtick.set_pad(10)
if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
plt.savefig(outdir+'/PerformancePlots/'+label+'/PDFs/scale_etaBins_'+label+'_'+options.target+'.pdf')
plt.savefig(outdir+'/PerformancePlots/'+label+'/PNGs/scale_etaBins_'+label+'_'+options.target+'.png')
plt.close()

############################################################################################
## response in eta bins

if options.reco:
    if options.target == 'jet':
        x_lim = (0.,3.)
        legend_label = r'$<|\eta^{jet, offline}|<$'
        x_label = r'$E_{T}^{jet, L1} / p_{T}^{jet, offline}$'
    if options.target == 'ele':
        x_lim = (0.,3.)
        legend_label = r'$<|\eta^{ele, offline}|<$'
        x_label = r'$E_{T}^{e/\gamma, L1} / p_{T}^{e, offline}$'
if options.gen:
    if options.target == 'jet':
        x_lim = (0.,3.)
        legend_label = r'$<|\eta^{jet, gen}|<$'
        x_label = r'$E_{T}^{jet, L1} / p_{T}^{jet, gen}$'
    if options.target == 'ele':
        x_lim = (0.,3.)
        legend_label = r'$<|\eta^{ele, gen}|<$'
        x_label = r'$E_{T}^{e/\gamma, L1} / p_{T}^{e, gen}$'

for i in range(len(absEta_response_ptBins)):
    fig, ax = plt.subplots(figsize=(10,10))
    
    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = absEta_response_ptBins[i]
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label=str(etaBins[i])+legend_label+str(etaBins[i+1]), lw=2, marker='o', color=cmap(0))
    Ymax = max(Y)
    
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc = 'upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('a.u.')
    plt.xlim(x_lim)
    plt.ylim(0., Ymax*1.3)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots/'+label+'/PDFs/response_'+str(etaBins[i])+"eta"+str(etaBins[i+1])+'_'+label+'_'+options.target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots/'+label+'/PNGs/response_'+str(etaBins[i])+"eta"+str(etaBins[i+1])+'_'+label+'_'+options.target+'.png')
    plt.close()


############################################################################################
## 2D resolution

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetRightMargin(0.15)
canvas.SetGrid(10,10);

#use dummy histogram to define style
PTvsETA_resolution.SetTitle("");
PTvsETA_resolution.GetXaxis().SetRangeUser(15.,200.);
PTvsETA_resolution.GetXaxis().SetTitle("p_{T}^{Gen jet} [GeV]");
PTvsETA_resolution.GetYaxis().SetTitle("#eta^{Gen jet} [GeV]");
PTvsETA_resolution.GetZaxis().SetTitle("Resolution");
PTvsETA_resolution.Draw("colz");

b1 = ROOT.TBox(15., 1.305,200.,1.479)
b1.SetFillColor(16)
b1.Draw("same")
b3 = ROOT.TBox(15., 1.305,200.,1.479)
b3.SetFillColor(1)
b3.SetFillStyle(3004)
b3.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+'/PerformancePlots/'+label+'/PDFs/resolution_ptVSeta_'+label+'_'+options.target+'.pdf')
canvas.SaveAs(outdir+'/PerformancePlots/'+label+'/PDFs/resolution_ptVSeta_'+label+'_'+options.target+'.png')

del canvas

############################################################################################
## 2D scale

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetRightMargin(0.15)
canvas.SetGrid(10,10);

#use dummy histogram to define style
PTvsETA_scale.SetTitle("");
PTvsETA_scale.GetXaxis().SetRangeUser(15.,200.);
PTvsETA_scale.GetXaxis().SetTitle("p_{T}^{Gen jet} [GeV]");
PTvsETA_scale.GetYaxis().SetTitle("#eta^{Gen jet} [GeV]");
PTvsETA_scale.GetZaxis().SetTitle("Scale");
PTvsETA_scale.Draw("colz");


b1 = ROOT.TBox(15., 1.305,200.,1.479)
b1.SetFillColor(16)
b1.Draw("same")
b3 = ROOT.TBox(15., 1.305,200.,1.479)
b3.SetFillColor(1)
b3.SetFillStyle(3004)
b3.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+'/PerformancePlots/'+label+'/PDFs/scale_ptVSeta_'+label+'_'+options.target+'.pdf')
canvas.SaveAs(outdir+'/PerformancePlots/'+label+'/PDFs/scale_ptVSeta_'+label+'_'+options.target+'.png')

del canvas

##############

#saving histograms and efficiencies in root file for later plotting if desired
fileout = ROOT.TFile(outdir+'/PerformancePlots/'+label+'/ROOTs/resolution_graphs_'+label+'_'+options.target+'.root','RECREATE')
pt_scale_fctPt.Write()
pt_scale_fctEta.Write()
pt_resol_fctPt.Write()
pt_resol_barrel_fctPt.Write()
pt_resol_endcap_fctPt.Write()
pt_resol_fctAbsEta.Write()
pt_resol_fctEta.Write()
pt_response_ptInclusive.Write()
pt_barrel_resp_ptInclusive.Write()
pt_endcap_resp_ptInclusive.Write()
PTvsETA_resolution.Write()
PTvsETA_scale.Write()
for i in range(len(response_ptBins)):
    response_ptBins[i].Write()
    barrel_response_ptBins[i].Write()
    endcap_response_ptBins[i].Write()
for i in range(len(minusEta_response_ptBins)):
    absEta_response_ptBins[i].Write()
    minusEta_response_ptBins[i].Write()
    plusEta_response_ptBins[i].Write()
