from itertools import chain
from TowerGeometry import *
import pandas as pd
import numpy as np
import argparse
import glob
import sys
import csv
import os
import ROOT
from array import array

print('cmd entry:', sys.argv)

directory = sys.argv[1]
nevents = int(sys.argv[2])
label = sys.argv[3]

#f = ROOT.TFile("/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt-15to7000_TuneCP5_Flat_13p6TeV-pythia8__Run3Winter22DR-PUForTRK_DIGI_122X_mcRun3_2021_realistic_v9-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p/Ntuple_200.root")

#directory = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt-15to7000_TuneCP5_Flat_13p6TeV-pythia8__Run3Winter22DR-PUForTRK_DIGI_122X_mcRun3_2021_realistic_v9-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p/"
#nevents = 10000

eventTree = ROOT.TChain("l1EventTree/L1EventTree")
genTree = ROOT.TChain("l1GeneratorTree/L1GenTree")
emuTree = ROOT.TChain("l1UpgradeEmuTree/L1UpgradeTree")

eventTree.Add(directory + "/Ntuple*.root")
genTree.Add(directory + "/Ntuple*.root")
emuTree.Add(directory + "/Ntuple*.root")

nEntries = eventTree.GetEntries()
if nevents > nEntries: nevents = nEntries
print("will process",nevents,"events...")

bins = [0, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 100, 120, 150, 180, 250]

empty = ROOT.TH1F("empty","empty",len(bins)-1, array('f',bins))
pt = ROOT.TH1F("pt","pt",len(bins)-1, array('f',bins))
passing20 = ROOT.TH1F("passing20","passing20",len(bins)-1, array('f',bins))
passing35 = ROOT.TH1F("passing35","passing35",len(bins)-1, array('f',bins))
passing50 = ROOT.TH1F("passing50","passing50",len(bins)-1, array('f',bins))
passing100 = ROOT.TH1F("passing100","passing100",len(bins)-1, array('f',bins))
passing150 = ROOT.TH1F("passing150","passing150",len(bins)-1, array('f',bins))

total = ROOT.TH1F("total","total",len(bins)-1, array('f',bins))


for i in range(0, nevents):
    if i%100==0: print(i)
    entry = eventTree.GetEntry(i)
    entry2 = emuTree.GetEntry(i)
    entry3 = genTree.GetEntry(i)

    L1_nJets = emuTree.L1Upgrade.nJets
    #if L1_nJets > 0: print(emuTree.L1Upgrade.jetEt[0])

    Gen_nJets = genTree.Generator.nJet

    for igenJet in range(0,Gen_nJets):

        Gen_jet = ROOT.TLorentzVector()
        Gen_jet.SetPtEtaPhiM(genTree.Generator.jetPt[igenJet], genTree.Generator.jetEta[igenJet], genTree.Generator.jetPhi[igenJet], 0)

        if Gen_jet.Pt()<15.: continue
        #if Gen_jet.Pt()<87. or Gen_jet.Pt()>88.: continue
        #print(Gen_jet.Pt())

        total.Fill(Gen_jet.Pt())
        pt.Fill(Gen_jet.Pt())

        matched = False
        highestL1Pt = -99.

        for ijet in range(0, L1_nJets):
            L1_jet = ROOT.TLorentzVector()
            L1_jet.SetPtEtaPhiM(emuTree.L1Upgrade.jetEt[ijet], emuTree.L1Upgrade.jetEta[ijet], emuTree.L1Upgrade.jetPhi[ijet], 0)

            if Gen_jet.DeltaR(L1_jet)<0.5:
                matched = True
                if L1_jet.Pt()>highestL1Pt:
                    highestL1Pt = L1_jet.Pt()
                
        if matched and highestL1Pt>20.: passing20.Fill(Gen_jet.Pt())
        if matched and highestL1Pt>35.: passing35.Fill(Gen_jet.Pt())
        if matched and highestL1Pt>50.: passing50.Fill(Gen_jet.Pt())
        if matched and highestL1Pt>100.: passing100.Fill(Gen_jet.Pt())
        if matched and highestL1Pt>150.: passing150.Fill(Gen_jet.Pt())


        #print("after match: ",Gen_jet.Pt())

#print(passing20.Integral())
#print(total.Integral())

fileout = ROOT.TFile("efficiency_graphs_"+label+".root","RECREATE")
passing20.Write()
passing35.Write()
passing50.Write()
passing100.Write()
passing150.Write()

total.Write()
pt.Write()

turnon20 = ROOT.TGraphAsymmErrors(passing20,total,"cp")
turnon35 = ROOT.TGraphAsymmErrors(passing35,total,"cp")
turnon50 = ROOT.TGraphAsymmErrors(passing50,total,"cp")
turnon100 = ROOT.TGraphAsymmErrors(passing100,total,"cp")
turnon150 = ROOT.TGraphAsymmErrors(passing150,total,"cp")

canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);

empty.GetXaxis().SetTitle("Gen jet p_{T} [GeV]")
#empty.GetYaxis().SetTitle("Efficiency")
empty.SetTitle("")
#empty.SetMaximum(1.4)

empty.GetXaxis().SetRangeUser(0.,250.);
empty.GetYaxis().SetRangeUser(0.,1.3);

#empty.GetXaxis().SetTitle("p_{T}^{offl.} [GeV]");
empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("L1 Efficiency");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);

mg = ROOT.TMultiGraph("mg","")

mg.Add(turnon20,"PE")
mg.Add(turnon35,"PE")
mg.Add(turnon50,"PE")
mg.Add(turnon100,"PE")
mg.Add(turnon150,"PE")

turnon20.SetMarkerColor(ROOT.kBlack)
turnon35.SetMarkerColor(ROOT.kRed)
turnon50.SetMarkerColor(ROOT.kBlue)
turnon100.SetMarkerColor(ROOT.kGreen)
turnon150.SetMarkerColor(ROOT.kMagenta)

turnon20.SetLineColor(ROOT.kBlack)
turnon35.SetLineColor(ROOT.kRed)
turnon50.SetLineColor(ROOT.kBlue)
turnon100.SetLineColor(ROOT.kGreen)
turnon150.SetLineColor(ROOT.kMagenta)

empty.Draw();
mg.Draw()
#mg.GetXaxis().SetTitle("Gen jet p_{T} [GeV]")
#mg.GetYaxis().SetTitle("Efficiency")
#mg.SetTitle("")
#turnon20.Draw("APE")

legend = ROOT.TLegend(0.15,0.75,0.48,0.88)
legend.SetBorderSize(0)
legend.AddEntry(turnon20,"p_{T}^{L1} > 20 GeV","LPE")
legend.AddEntry(turnon35,"p_{T}^{L1} > 35 GeV","LPE")
legend.AddEntry(turnon50,"p_{T}^{L1} > 50 GeV","LPE")
legend.AddEntry(turnon100,"p_{T}^{L1} > 100 GeV","LPE")
legend.AddEntry(turnon150,"p_{T}^{L1} > 150 GeV","LPE")
legend.Draw("same")

canvas.SaveAs("turnOn_"+label+".pdf")
canvas.SaveAs("turnOn_"+label+".root")

turnon20.Write()
print("--")


    
