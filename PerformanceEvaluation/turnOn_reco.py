from array import array
import numpy as np
import pickle
import ROOT
ROOT.gROOT.SetBatch(True)
import sys
import os

import matplotlib.pyplot as plt
import matplotlib
import mplhep
plt.style.use(mplhep.style.CMS)

def save_obj(obj,dest):
    with open(dest,'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

#print('cmd entry:', sys.argv)

#reading input parameters
directory = sys.argv[1]
nevents = int(sys.argv[2])
label = sys.argv[3]
outdir = sys.argv[4]
if len(sys.argv)>=6: unpacked = sys.argv[5]
else:                unpacked = False

os.system('mkdir -p '+outdir+'/PDFs/'+label)
os.system('mkdir -p '+outdir+'/PNGs/'+label)
os.system('mkdir -p '+outdir+'/ROOTs/')

print("defining input trees")
eventTree = ROOT.TChain("l1EventTree/L1EventTree")
if "HCAL_" in label: recoTree = ROOT.TChain("l1JetRecoTree/JetRecoTree")
if "ECAL_" in label: recoTree = ROOT.TChain("l1ElectronRecoTree/ElectronRecoTree")
if unpacked: emuTree = ROOT.TChain("l1UpgradeTree/L1UpgradeTree")
else:        emuTree = ROOT.TChain("l1UpgradeEmuTree/L1UpgradeTree")

print("reading input files")
eventTree.Add(directory + "/Ntuple*.root")
recoTree.Add(directory + "/Ntuple*.root")
emuTree.Add(directory + "/Ntuple*.root")

nEntries = eventTree.GetEntries()
print("getting "+str(nEntries)+" entries")

#run on entries specified by usuer, or only on entries available if that is exceeded
if (nevents > nEntries) or (nevents==-1): nevents = nEntries
print("will process",nevents,"events...")

#defining binning of histogram
bins =      [0,    5,  10,   15,   20,   25,   30,   35,   40,   45,   50, 60, 70, 80, 100, 120, 150, 180, 250]

#defining binning of offline translation
offline_pts = [2.5, 7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5, 55.0, 65.0, 75.0, 90.0, 110.0,  135.0, 165.0, 215.0]
mapping_dict = {'threshold':[], 'pt95eff':[], 'pt90eff':[], 'pt50eff':[]}

#list the ET thresholds to be tested
thresholds = np.linspace(20,150,131).tolist()

thresholds2plot = [20, 35, 50, 100, 150]

#passing histograms (numerators)
passing = []
for threshold in thresholds:
        passing.append(ROOT.TH1F("passing"+str(int(threshold)),"passing"+str(int(threshold)),len(bins)-1, array('f',bins)))

#dummy histogram for plotting
empty = ROOT.TH1F("empty","empty",len(bins)-1, array('f',bins))

#pt spectrum
pt = ROOT.TH1F("pt","pt",len(bins)-1, array('f',bins))

#denominator
total = ROOT.TH1F("total","total",len(bins)-1, array('f',bins))

print("looping on events")
for i in range(0, nevents):
    if i%1000==0: print(i)
    #getting entries
    entry = eventTree.GetEntry(i)
    entry2 = emuTree.GetEntry(i)
    entry3 = recoTree.GetEntry(i)

    L1_nJets = 0
    if "HCAL_" in label:
        L1_nJets = emuTree.L1Upgrade.nJets
        reco_nJets = recoTree.Jet.nJets
    if "ECAL_" in label:
        L1_nJets = emuTree.L1Upgrade.nEGs
        reco_nJets = recoTree.Electron.nElectrons
    
    #loop on generator jets
    for igenJet in range(0,reco_nJets):

        if "HCAL_" in label:
            reco_jet = ROOT.TLorentzVector()
            reco_jet.SetPtEtaPhiM(recoTree.Jet.et[igenJet], recoTree.Jet.eta[igenJet], recoTree.Jet.phi[igenJet], 0)

        if "ECAL_" in label:
            reco_jet = ROOT.TLorentzVector()
            reco_jet.SetPtEtaPhiM(recoTree.Electron.et[igenJet], recoTree.Electron.eta[igenJet], recoTree.Electron.phi[igenJet], 0)

        # skip jets that cannot be reconstructed by L1 (limit is 5.191)
        if reco_jet.Eta()>5.0: continue
        # skip egs that cannot be reconstructed by L1 (limit is 3.0)
        if "ECAL_" in label and reco_jet.Eta()>3.0: continue

        #reject very soft jets, usually poorly defined
        if "HCAL_" in label and reco_jet.Pt()<15.: continue

        total.Fill(reco_jet.Pt())
        pt.Fill(reco_jet.Pt())

        matched = False
        highestL1Pt = -99.

        #loop on L1 jets to find match
        for ijet in range(0, L1_nJets):
            L1_jet = ROOT.TLorentzVector()
            if "HCAL_" in label: L1_jet.SetPtEtaPhiM(emuTree.L1Upgrade.jetEt[ijet], emuTree.L1Upgrade.jetEta[ijet], emuTree.L1Upgrade.jetPhi[ijet], 0)
            if "ECAL_" in label: L1_jet.SetPtEtaPhiM(emuTree.L1Upgrade.egEt[ijet], emuTree.L1Upgrade.egEta[ijet], emuTree.L1Upgrade.egPhi[ijet], 0)

            #check matching
            if reco_jet.DeltaR(L1_jet)<0.5:
                matched = True
                #keep only L1 match with highest pT
                if L1_jet.Pt()>highestL1Pt:
                    highestL1Pt = L1_jet.Pt()

        #fill numerator histograms for every thresholds
        for i,ele in enumerate(thresholds): 
            if matched and highestL1Pt>float(ele): passing[i].Fill(reco_jet.Pt())

#define TGraphAsymmErrors for efficiency turn-ons
turnons = []

for i,ele in enumerate(thresholds):
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

save_obj(mapping_dict, 'ROOTs/online2offline_mapping_'+label+'.pkl')

plt.figure(figsize=(10,10))
plt.plot(thresholds, mapping_dict['pt95eff'], label='@ 95% efficiency', linewidth=2, color='blue')
plt.plot(thresholds, mapping_dict['pt90eff'], label='@ 90% efficiency', linewidth=2, color='red')
plt.plot(thresholds, mapping_dict['pt50eff'], label='@ 50% efficiency', linewidth=2, color='green')
plt.legend(loc = 'lower right', fontsize=14)
plt.xlabel('L1 Threshold [GeV]')
plt.ylabel('Offline threshold [GeV]')
plt.xlim(20, 100)
plt.ylim(20, 120)
plt.grid()
mplhep.cms.label(data=False, rlabel='13.6 TeV')
plt.savefig(outdir+"/PDFs/"+label+"/online2offline_mapping_"+label+".pdf")
plt.close()

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);

#use dummy histogram to define style
empty.GetXaxis().SetTitle("Gen jet p_{T} [GeV]")
empty.SetTitle("")

empty.GetXaxis().SetRangeUser(0.,250.);
empty.GetYaxis().SetRangeUser(0.,1.3);

empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("L1 Efficiency");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);

#use multigraph for plotting all turn-ons on the same canvas
mg = ROOT.TMultiGraph("mg","")

for i,ele in enumerate(thresholds2plot):
    mg.Add(turnons[thresholds.index(ele)],"PE")
    turnons[thresholds.index(ele)].SetMarkerColor(i+1)
    turnons[thresholds.index(ele)].SetLineColor(i+1)

empty.Draw()
mg.Draw()

legend = ROOT.TLegend(0.15,0.75,0.48,0.88)
legend.SetBorderSize(0)
for i,ele in enumerate(thresholds2plot):
    legend.AddEntry(turnons[thresholds.index(ele)],"p_{T}^{L1} > "+str(thresholds[thresholds.index(ele)])+" GeV","LPE")

legend.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+"/PDFs/"+label+"/turnOn_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/turnOn_"+label+".png")

print("saving histograms and efficiencies in root file for later plotting if desired")
fileout = ROOT.TFile(outdir+"/ROOTs/efficiency_graphs_"+label+".root","RECREATE")
total.Write()
pt.Write()
for i,ele in enumerate(thresholds): 
    passing[i].Write()
    turnons[i].Write()

fileout.Close()
