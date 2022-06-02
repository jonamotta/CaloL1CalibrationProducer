from itertools import chain
from xml.dom.expatbuilder import parseString
import pandas as pd
import numpy as np
import argparse
import glob
import sys
import csv
import os
import ROOT
from array import array

#print('cmd entry:', sys.argv)

#reading input parameters
directory = sys.argv[1]
nevents = int(sys.argv[2])
label = sys.argv[3]

#defining input trees
eventTree = ROOT.TChain("l1EventTree/L1EventTree")
genTree = ROOT.TChain("l1GeneratorTree/L1GenTree")
emuTree = ROOT.TChain("l1UpgradeEmuTree/L1UpgradeTree")

#reading input files
eventTree.Add(directory + "/Ntuple*.root")
genTree.Add(directory + "/Ntuple*.root")
emuTree.Add(directory + "/Ntuple*.root")

#getting entries
nEntries = eventTree.GetEntries()

#run on entries specified by usuer, or only on entries available if that is exceeded
if nevents > nEntries: nevents = nEntries
print("will process",nevents,"events...")

#defining binning of histogram
bins = [0, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 100, 120, 150, 180, 250]

#list the ET thresholds to be tested
thresholds = [20, 35, 50, 100, 150]

#passing histograms (numerators)
passing = []
for threshold in thresholds:
        passing.append(ROOT.TH1F("passing"+str(threshold),"passing"+str(threshold),len(bins)-1, array('f',bins)))

#dummy histogram for plotting of turn-ons and resolutions_in_eta_bins
empty = ROOT.TH1F("empty","empty",len(bins)-1, array('f',bins))
empty_res = ROOT.TH1F("empty_res","empty_res",20,0.,2.)

#resolution in bins of eta histograms
resolution_inclusive = ROOT.TH1F("resolution_inclusive","resolution_inclusive",40,0.,2.)

eta_bins = [0, 0.8, 1.5, 3., 5.]
resolutions_in_eta_bins  = []

pt_bins = [15, 30, 40, 50, 70., 100., 150., 250., 500.]
resolutions_in_pt_bins  = []

for i,eta_bin in enumerate(eta_bins):
    if i<len(eta_bins)-1: resolutions_in_eta_bins.append(ROOT.TH1F("resolution_"+str(eta_bins[i])+"_"+str(eta_bins[i+1]),"resolution_"+str(eta_bins[i])+"_"+str(eta_bins[i+1]),40, 0., 2.))

for i,pt_bin in enumerate(pt_bins):
    if i<len(pt_bins)-1: resolutions_in_pt_bins.append(ROOT.TH1F("resolution_"+str(pt_bins[i])+"_"+str(pt_bins[i+1]),"resolution_"+str(pt_bins[i])+"_"+str(pt_bins[i+1]),40, 0., 2.))


#pt spectrum
pt = ROOT.TH1F("pt","pt",len(bins)-1, array('f',bins))

#denominator
total = ROOT.TH1F("total","total",len(bins)-1, array('f',bins))

#loop on events
for i in range(0, nevents):
    if i%100==0: print(i)
    #getting entries
    entry = eventTree.GetEntry(i)
    entry2 = emuTree.GetEntry(i)
    entry3 = genTree.GetEntry(i)

    L1_nJets = emuTree.L1Upgrade.nJets
    Gen_nJets = genTree.Generator.nJet

    #loop on generator jets
    for igenJet in range(0,Gen_nJets):

        Gen_jet = ROOT.TLorentzVector()
        Gen_jet.SetPtEtaPhiM(genTree.Generator.jetPt[igenJet], genTree.Generator.jetEta[igenJet], genTree.Generator.jetPhi[igenJet], 0)

        #reject very soft jets, usually poorly defined
        if Gen_jet.Pt()<15.: continue

        total.Fill(Gen_jet.Pt())
        pt.Fill(Gen_jet.Pt())

        matched = False
        FilledTurnOn = False
        FilledReso = False
        highestL1Pt = -99.

        #loop on L1 jets to find match
        for ijet in range(0, L1_nJets):
            L1_jet = ROOT.TLorentzVector()
            L1_jet.SetPtEtaPhiM(emuTree.L1Upgrade.jetEt[ijet], emuTree.L1Upgrade.jetEta[ijet], emuTree.L1Upgrade.jetPhi[ijet], 0)

            #check matching
            if Gen_jet.DeltaR(L1_jet)<0.5:
                matched = True
                #keep only L1 match with highest pT
                if L1_jet.Pt()>highestL1Pt:
                    highestL1Pt = L1_jet.Pt()

        #fill numerator histograms for every thresholds
        if not FilledTurnOn:
            FilledTurOn = True
            for i,ele in enumerate(thresholds): 
                if matched and highestL1Pt>float(ele): passing[i].Fill(Gen_jet.Pt())

        if matched:
            #if highestL1Pt<10.: continue
            if not FilledReso:
                FilledReso = True
                resolution_inclusive.Fill(highestL1Pt/Gen_jet.Pt())
                for ieta,eta_bin in enumerate(eta_bins):
                    if ieta<len(eta_bins)-1:
                        if abs(Gen_jet.Eta())<eta_bins[ieta+1] and abs(Gen_jet.Eta())>=eta_bins[ieta]:
                            resolutions_in_eta_bins[ieta].Fill(highestL1Pt/Gen_jet.Pt())
                            #print("Gen pT = ",Gen_jet.Pt(),", L1 pT = ",highestL1Pt)
                for ipt,pt_bin in enumerate(pt_bins):
                    if ipt<len(pt_bins)-1:
                        if Gen_jet.Pt()<pt_bins[ipt+1] and Gen_jet.Pt()>=pt_bins[ipt]: resolutions_in_pt_bins[ipt].Fill(highestL1Pt/Gen_jet.Pt())
        else:
            if not FilledReso:
                FilledReso = True    
                resolution_inclusive.Fill(0.)
                for ieta,eta_bin in enumerate(eta_bins):
                    if ieta<len(eta_bins)-1:
                        if abs(Gen_jet.Eta())<eta_bins[ieta+1] and abs(Gen_jet.Eta())>=eta_bins[ieta]:
                            resolutions_in_eta_bins[ieta].Fill(0.)
                for ipt,pt_bin in enumerate(pt_bins):
                    if ipt<len(pt_bins)-1:
                        if Gen_jet.Pt()<pt_bins[ipt+1] and Gen_jet.Pt()>=pt_bins[ipt]: resolutions_in_pt_bins[ipt].Fill(0.)                            
                
#define TGraphAsymmErrors for efficiency turn-ons
turnons = []

for i,ele in enumerate(thresholds):
        turnons.append(ROOT.TGraphAsymmErrors(passing[i], total, "cp"))

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

for i,ele in enumerate(thresholds):
    mg.Add(turnons[i],"PE")
    turnons[i].SetMarkerColor(i+1)
    turnons[i].SetLineColor(i+1)

empty.Draw();
mg.Draw()

legend = ROOT.TLegend(0.15,0.75,0.48,0.88)
legend.SetBorderSize(0)
for i,ele in enumerate(thresholds):
    legend.AddEntry(turnons[i],"p_{T}^{L1} > "+str(thresholds[i])+" GeV","LPE")

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

canvas.SaveAs("turnOn_"+label+".pdf")
canvas.SaveAs("turnOn_"+label+".root")


#define canvas for plotting resolutions_in_eta_bins / inclusive
canvas_res = ROOT.TCanvas("c_res","c_res",800,800)
canvas_res.SetGrid(10,10);

#use dummy histogram to define style
empty_res.GetXaxis().SetTitle("E_{T}^{L1 jet} / p_{T}^{Gen jet}")
empty_res.SetTitle("")

empty_res.GetXaxis().SetRangeUser(0.,2.);
maximum_eta = -1.
for res_plot in resolutions_in_eta_bins:
    if res_plot.Integral()<0.0001: continue
    if res_plot.GetMaximum()/res_plot.Integral()>maximum_eta: maximum_eta = res_plot.GetMaximum()/res_plot.Integral()
empty_res.GetYaxis().SetRangeUser(0.,maximum_eta*1.3);

empty_res.GetXaxis().SetTitleOffset(1.3);
empty_res.GetYaxis().SetTitle("Integral normalized to unity");
empty_res.GetYaxis().SetTitleOffset(1.45);
empty_res.SetTitle("");
empty_res.SetStats(0);

#empty_res.SetMarkerStyle(2)
empty_res.Draw("E");

for i,ele in enumerate(resolutions_in_eta_bins):
    #resolutions_in_eta_bins[i].SetMarkerStyle(2)
    resolutions_in_eta_bins[i].SetMarkerColor(i+2)
    resolutions_in_eta_bins[i].SetLineColor(i+2)
    #resolutions_in_eta_bins[i].SetLineWidth(0)
    resolutions_in_eta_bins[i].DrawNormalized("Esame")

#resolution_inclusive.SetMarkerStyle(2)
resolution_inclusive.SetMarkerColor(1)
resolution_inclusive.SetLineColor(1)
#resolution_inclusive.SetLineWidth(0)
resolution_inclusive.DrawNormalized("Esame")

legend_res = ROOT.TLegend(0.15,0.75,0.48,0.88)
legend_res.SetBorderSize(0)
legend_res.AddEntry(resolution_inclusive,"Inclusive","EL")

for i,ele in enumerate(eta_bins):
    if i<len(eta_bins)-1: legend_res.AddEntry(resolutions_in_eta_bins[i],str(eta_bins[i])+" < |#eta| < "+str(eta_bins[i+1]),"EL")

legend_res.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

canvas_res.SaveAs("resolution_in_eta_bins_"+label+".pdf")
canvas_res.SaveAs("resolution_in_eta_bins_"+label+".root")

print("--")

#define canvas for plotting resolutions_in_pt_bins / inclusive
canvas_res_pt = ROOT.TCanvas("c_res_pt","c_res_pt",800,800)
canvas_res_pt.SetGrid(10,10);

#use dummy histogram to define style
maximum_pt = -1.
for res_plot in resolutions_in_pt_bins:
    if res_plot.Integral()<0.0001: continue
    if res_plot.GetMaximum()/res_plot.Integral()>maximum_pt: maximum_pt = res_plot.GetMaximum()/res_plot.Integral()
empty_res.GetYaxis().SetRangeUser(0.,maximum_pt*1.3);
empty_res.Draw("E");

for i,ele in enumerate(resolutions_in_pt_bins):
    #resolutions_in_eta_bins[i].SetMarkerStyle(2)
    resolutions_in_pt_bins[i].SetMarkerColor(i+2)
    resolutions_in_pt_bins[i].SetLineColor(i+2)
    #resolutions_in_pt_bins[i].SetLineWidth(0)
    resolutions_in_pt_bins[i].DrawNormalized("Esame")

#resolution_inclusive.SetMarkerStyle(2)
resolution_inclusive.SetMarkerColor(1)
resolution_inclusive.SetLineColor(1)
#resolution_inclusive.SetLineWidth(0)
resolution_inclusive.DrawNormalized("ELsame")

legend_res_pt = ROOT.TLegend(0.62782,0.452196,0.860902,0.883721)
legend_res_pt.SetBorderSize(0)
legend_res_pt.AddEntry(resolution_inclusive,"Inclusive","EL")

for i,ele in enumerate(pt_bins):
    if i<len(pt_bins)-1: legend_res_pt.AddEntry(resolutions_in_pt_bins[i],str(int(pt_bins[i]+0.1))+" < p_{T}^{Gen jet} < "+str(int(pt_bins[i+1]+0.1))+" GeV","EL")

legend_res_pt.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

canvas_res_pt.SaveAs("resolution_in_pt_bins_"+label+".pdf")
canvas_res_pt.SaveAs("resolution_in_pt_bins_"+label+".root")

print("--")

#saving histograms and efficiencies in root file for later plotting if desired
fileout = ROOT.TFile("efficiency_graphs_"+label+".root","RECREATE")
for i,ele in enumerate(thresholds): 
    passing[i].Write()
    turnons[i].Write()

total.Write()
pt.Write()

fileout.Close()
