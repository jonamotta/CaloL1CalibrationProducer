from array import array
import ROOT
import sys
import os
import numpy as np

ROOT.gStyle.SetOptStat(000000)
ROOT.gROOT.SetBatch(True)

# python3 comparison_JB.py Plots_JB HCAL_uncalib HCAL_oldcalib HCAL_newCalibManualSaturation_2

outdir = sys.argv[1]
label_uncalib = sys.argv[2]
label_oldcalib = sys.argv[3]
label_newcalib = sys.argv[4]

os.system('mkdir -p '+outdir+'/Comparison/')
os.system('mkdir -p '+outdir+'/Comparison/PNGs')
os.system('mkdir -p '+outdir+'/Comparison/PDFs')

# detector = label.split("_")[0]
# newTag   = label.split("_")[1]
# outdir   = sys.argv[2]

# os.system('mkdir -p '+outdir+'/PDFs/comparisons_'+label)
# os.system('mkdir -p '+outdir+'/PNGs/comparisons_'+label)

##################################################################
######################## COMPARE TURN ONS ########################
##################################################################

Nbins = 241
Min = 0 
Max = 241
L1_cuts = np.linspace(Min,Max,Nbins+1)

print("Import ROOT files: \n")
print(outdir+"/ROOTs/TurnOn_"+label_uncalib+".root")
print(outdir+"/ROOTs/TurnOn_"+label_oldcalib+".root")
print(outdir+"/ROOTs/TurnOn_"+label_newcalib+".root")

file_unCalib  = ROOT.TFile(outdir+"/ROOTs/TurnOn_"+label_uncalib+".root", "r")
file_oldCalib = ROOT.TFile(outdir+"/ROOTs/TurnOn_"+label_oldcalib+".root", "r")
file_newCalib = ROOT.TFile(outdir+"/ROOTs/TurnOn_"+label_newcalib+".root", "r")

empty = ROOT.TH1F("empty","empty",Nbins,Min,Max)

for L1_cut in L1_cuts:

    if L1_cut % 20 == 0:

        TurnOn_unCalib  = file_unCalib.Get("divide_Numerator_{}_by_Denominator".format(int(L1_cut)))
        TurnOn_oldCalib = file_oldCalib.Get("divide_Numerator_{}_by_Denominator".format(int(L1_cut)))
        TurnOn_newCalib = file_newCalib.Get("divide_Numerator_{}_by_Denominator".format(int(L1_cut)))

        canvas = ROOT.TCanvas("c","c",800,800)
        canvas.SetGrid(10,10)

        #use dummy histogram to define style
        empty.SetTitle("")
        empty.GetXaxis().SetTitle("p_{T}^{Offline} (jet) [GeV]")
        empty.GetXaxis().SetRangeUser(0., 240.)
        empty.GetXaxis().SetTitleOffset(1.3)
        empty.GetYaxis().SetTitle("L1 Efficiency")
        empty.GetYaxis().SetRangeUser(0., 1.05)
        empty.GetYaxis().SetTitleOffset(1.3)
        empty.SetStats(0)
        empty.Draw()

        TurnOn_unCalib.SetLineWidth(2)
        TurnOn_unCalib.SetMarkerStyle(8)
        TurnOn_unCalib.SetMarkerColor(2)
        TurnOn_unCalib.SetLineColor(2)

        TurnOn_oldCalib.SetLineWidth(2)
        TurnOn_oldCalib.SetMarkerStyle(8)
        TurnOn_oldCalib.SetMarkerColor(3)
        TurnOn_oldCalib.SetLineColor(3)

        TurnOn_newCalib.SetLineWidth(2)
        TurnOn_newCalib.SetMarkerStyle(8)
        TurnOn_newCalib.SetMarkerColor(1)
        TurnOn_newCalib.SetLineColor(1)

        TurnOn_unCalib.Draw("LPE")
        TurnOn_oldCalib.Draw("LPE same")
        TurnOn_newCalib.Draw("LPE same")

        legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
        legend.SetBorderSize(0)
        legend.AddEntry(TurnOn_unCalib,"Uncalibrated", "LPE")
        legend.AddEntry(TurnOn_oldCalib,"Old Calibration", "LPE")
        legend.AddEntry(TurnOn_newCalib,"New Calibration", "LPE")
        legend.Draw("same")

        tex = ROOT.TLatex()
        tex.SetTextSize(0.03)
        tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
        tex.Draw("same")

        tex2 = ROOT.TLatex()
        tex2.SetTextSize(0.035)
        tex2.SetTextAlign(31)
        tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)")
        tex2.Draw("same")

        canvas.SaveAs(outdir+"/Comparison/PNGs/TurnOn_"+str(int(L1_cut))+"_"+label_newcalib+".png")
        canvas.SaveAs(outdir+"/Comparison/PDFs/TurnOn_"+str(int(L1_cut))+"_"+label_newcalib+".pdf")

        del canvas
        del TurnOn_unCalib
        del TurnOn_oldCalib
        del TurnOn_newCalib

##################################################################
######################## COMPARE RATES ###########################
##################################################################

file_unCalib  = ROOT.TFile(outdir+"/ROOTs/Rate_"+label_uncalib+".root", "r")
file_oldCalib = ROOT.TFile(outdir+"/ROOTs/Rate_"+label_oldcalib+".root", "r")
file_newCalib = ROOT.TFile(outdir+"/ROOTs/Rate_"+label_newcalib+".root", "r")

# remove -1 points from plotting
Rate_unCalib_all = file_unCalib.Get("RatesVSOffline")
Offline_cuts, Rates = array('d'), array('d')
for x,y in zip(Rate_unCalib_all.GetX(), Rate_unCalib_all.GetY()):
    if x >= 0:
        Offline_cuts.append(x)
        Rates.append(y)
Rate_unCalib = ROOT.TGraphErrors(len(Offline_cuts), Offline_cuts, Rates)

Rate_oldCalib_all = file_oldCalib.Get("RatesVSOffline")
Offline_cuts, Rates = array('d'), array('d')
for x,y in zip(Rate_oldCalib_all.GetX(), Rate_oldCalib_all.GetY()):
    if x >= 0:
        Offline_cuts.append(x)
        Rates.append(y)
Rate_oldCalib = ROOT.TGraphErrors(len(Offline_cuts), Offline_cuts, Rates)

Rate_newCalib_all = file_newCalib.Get("RatesVSOffline")
Offline_cuts, Rates = array('d'), array('d')
for x,y in zip(Rate_newCalib_all.GetX(), Rate_newCalib_all.GetY()):
    if x >= 0:
        Offline_cuts.append(x)
        Rates.append(y)
Rate_newCalib = ROOT.TGraphErrors(len(Offline_cuts), Offline_cuts, Rates)

y_uncalib_max = max(Rate_unCalib.GetY())
y_oldcalib_max = max(Rate_oldCalib.GetY())
y_newcalib_max = max(Rate_newCalib.GetY())

canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10)
canvas.SetLogy()

empty = ROOT.TH1F("empty","empty",Nbins,Min,Max)

#use dummy histogram to define style
empty.SetTitle("")
empty.GetXaxis().SetTitle("p_{T}^{Offline} (jet) [GeV]")
empty.GetXaxis().SetRangeUser(0., 240.)
empty.GetXaxis().SetTitleOffset(1.3)
empty.GetYaxis().SetTitle("Single-Object Rate [KHz]")
empty.GetYaxis().SetRangeUser(0.1, max(y_uncalib_max,y_oldcalib_max,y_newcalib_max)*1.3)
empty.GetYaxis().SetTitleOffset(1.3)
# Rate_unCalib.SetStats(0)
empty.Draw()

Rate_unCalib.SetLineWidth(2)
Rate_unCalib.SetMarkerStyle(8)
Rate_unCalib.SetMarkerColor(2)
Rate_unCalib.SetLineColor(2)

Rate_oldCalib.SetLineWidth(2)
Rate_oldCalib.SetMarkerStyle(8)
Rate_oldCalib.SetMarkerColor(3)
Rate_oldCalib.SetLineColor(3)

Rate_newCalib.SetLineWidth(2)
Rate_newCalib.SetMarkerStyle(8)
Rate_newCalib.SetMarkerColor(1)
Rate_newCalib.SetLineColor(1)

Rate_unCalib.Draw("LPE same")
Rate_oldCalib.Draw("LPE same")
Rate_newCalib.Draw("LPE same")

legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(Rate_unCalib,"Uncalibrated", "LPE")
legend.AddEntry(Rate_oldCalib,"Old Calibration", "LPE")
legend.AddEntry(Rate_newCalib,"New Calibration", "LPE")
legend.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03)
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex()
tex2.SetTextSize(0.035)
tex2.SetTextAlign(31)
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)")
tex2.Draw("same")

canvas.SaveAs(outdir+"/Comparison/PNGs/Rate_"+label_newcalib+".png")
canvas.SaveAs(outdir+"/Comparison/PDFs/Rate_"+label_newcalib+".pdf")

del canvas

##################################################################
######################## COMPARE RATES ###########################
##################################################################

file_unCalib  = ROOT.TFile(outdir+"/ROOTs/Rate_"+label_uncalib+".root", "r")
file_oldCalib = ROOT.TFile(outdir+"/ROOTs/Rate_"+label_oldcalib+".root", "r")
file_newCalib = ROOT.TFile(outdir+"/ROOTs/Rate_"+label_newcalib+".root", "r")

Rate_unCalib  = file_unCalib.Get("RatesVSOnline")
Rate_oldCalib = file_oldCalib.Get("RatesVSOnline")
Rate_newCalib = file_newCalib.Get("RatesVSOnline")

y_uncalib_max = max(Rate_unCalib.GetY())
y_oldcalib_max = max(Rate_oldCalib.GetY())
y_newcalib_max = max(Rate_newCalib.GetY())

canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10)
canvas.SetLogy()

empty = ROOT.TH1F("empty","empty",Nbins,Min,Max)

#use dummy histogram to define style
empty.SetTitle("")
empty.GetXaxis().SetTitle("p_{T}^{L1} (jet) [GeV]")
empty.GetXaxis().SetRangeUser(0., 240.)
empty.GetXaxis().SetTitleOffset(1.3)
empty.GetYaxis().SetTitle("Single-Object Rate [KHz]")
empty.GetYaxis().SetRangeUser(0.1, max(y_uncalib_max,y_oldcalib_max,y_newcalib_max)*1.3)
empty.GetYaxis().SetTitleOffset(1.3)
empty.SetStats(0)
empty.Draw()

Rate_unCalib.SetLineWidth(2)
Rate_unCalib.SetMarkerStyle(8)
Rate_unCalib.SetMarkerColor(2)
Rate_unCalib.SetLineColor(2)

Rate_oldCalib.SetLineWidth(2)
Rate_oldCalib.SetMarkerStyle(8)
Rate_oldCalib.SetMarkerColor(3)
Rate_oldCalib.SetLineColor(3)

Rate_newCalib.SetLineWidth(2)
Rate_newCalib.SetMarkerStyle(8)
Rate_newCalib.SetMarkerColor(1)
Rate_newCalib.SetLineColor(1)

Rate_unCalib.Draw("LPE same")
Rate_oldCalib.Draw("LPE same")
Rate_newCalib.Draw("LPE same")

legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(Rate_unCalib,"Uncalibrated", "LPE")
legend.AddEntry(Rate_oldCalib,"Old Calibration", "LPE")
legend.AddEntry(Rate_newCalib,"New Calibration", "LPE")
legend.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03)
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex()
tex2.SetTextSize(0.035)
tex2.SetTextAlign(31)
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)")
tex2.Draw("same")

canvas.SaveAs(outdir+"/Comparison/PNGs/Rate_L1_"+label_newcalib+".png")
canvas.SaveAs(outdir+"/Comparison/PDFs/Rate_L1_"+label_newcalib+".pdf")