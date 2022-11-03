from array import array
import ROOT
import sys
import os

L1CalibTag1 = sys.argv[1]
L1CalibTag2 = sys.argv[2]
outdir = sys.argv[3]

os.system('mkdir -p '+outdir+'/PDFs/comparisons_'+L1CalibTag2)
os.system('mkdir -p '+outdir+'/PNGs/comparisons_'+L1CalibTag2)

etaPlotLim = 5.191
if "ECAL_" in L1CalibTag1: etaPlotLim = 3.

etaRestictedLim = 1.479

etaBinsAsTT = array("d", [0., 0.087, 0.174, 0.261, 0.348, 0.435, 0.522, 0.609, 0.696, 0.783, 0.870, 0.957, 1.044, 1.131, 1.218, 1.305, 1.392, 1.479, 1.566, 1.653, 1.740, 1.830, 1.930, 2.043, 2.172, 2.322, 2.5, 2.650, 3., 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889, 5.191])

InFileName1 = outdir+"/ROOTs/rate_graphs_"+L1CalibTag1+".root"
InFileName2 = outdir+"/ROOTs/rate_graphs_"+L1CalibTag2+".root"
fIn1 = ROOT.TFile(InFileName1,"READ");
fIn2 = ROOT.TFile(InFileName2,"READ");

ratePtProgression1 = fIn1.Get("ratePtProgression")
ratePtDiProgression1 = fIn1.Get("ratePtDiProgression")
rateEtaProgression1 = fIn1.Get("rateEtaProgression")
rateEtaDiProgression1 = fIn1.Get("rateEtaDiProgression")
ratePtVsEtaProgression1 = fIn1.Get("ratePtVsEtaProgression")

ratePtProgression2 = fIn2.Get("ratePtProgression")
ratePtDiProgression2 = fIn2.Get("ratePtDiProgression")
rateEtaProgression2 = fIn2.Get("rateEtaProgression")
rateEtaDiProgression2 = fIn2.Get("rateEtaDiProgression")
ratePtVsEtaProgression2 = fIn2.Get("ratePtVsEtaProgression")

relative_ratePtProgression = ROOT.TH1F("relative_ratePtProgression", "relative_ratePtProgression", 240,0.,240.)
relative_ratePtDiProgression = ROOT.TH1F("relative_ratePtDiProgression", "relative_ratePtDiProgression", 240,0.,240.)
relative_rateEtaProgression = ROOT.TH1F("relative_rateEtaProgression", "relative_rateEtaProgression", len(etaBinsAsTT)-1,etaBinsAsTT)
relative_rateEtaDiProgression = ROOT.TH1F("relative_rateEtaDiProgression", "relative_rateEtaDiProgression", len(etaBinsAsTT)-1,etaBinsAsTT)
relative_ratePtVsEtaProgression = ROOT.TH2F("relative_ratePtVsEtaProgression", "relative_ratePtVsEtaProgression", 240,0.,240.,len(etaBinsAsTT)-1,etaBinsAsTT)

ratePtProgression1Er = fIn1.Get("ratePtProgressionEr")
ratePtDiProgression1Er = fIn1.Get("ratePtDiProgressionEr")
rateEtaProgression1Er = fIn1.Get("rateEtaProgressionEr")
rateEtaDiProgression1Er = fIn1.Get("rateEtaDiProgressionEr")
ratePtVsEtaProgression1Er = fIn1.Get("ratePtVsEtaProgressionEr")

ratePtProgression2Er = fIn2.Get("ratePtProgressionEr")
ratePtDiProgression2Er = fIn2.Get("ratePtDiProgressionEr")
rateEtaProgression2Er = fIn2.Get("rateEtaProgressionEr")
rateEtaDiProgression2Er = fIn2.Get("rateEtaDiProgressionEr")
ratePtVsEtaProgression2Er = fIn2.Get("ratePtVsEtaProgressionEr")

relative_ratePtProgressionEr = ROOT.TH1F("relative_ratePtProgressionEr", "relative_ratePtProgressionEr", 240,0.,240.)
relative_ratePtDiProgressionEr = ROOT.TH1F("relative_ratePtDiProgressionEr", "relative_ratePtDiProgressionEr", 240,0.,240.)
relative_rateEtaProgressionEr = ROOT.TH1F("relative_rateEtaProgressionEr", "relative_rateEtaProgressionEr", len(etaBinsAsTT)-1,etaBinsAsTT)
relative_rateEtaDiProgressionEr = ROOT.TH1F("relative_rateEtaDiProgressionEr", "relative_rateEtaDiProgressionEr", len(etaBinsAsTT)-1,etaBinsAsTT)
relative_ratePtVsEtaProgressionEr = ROOT.TH2F("relative_ratePtVsEtaProgressionEr", "relative_ratePtVsEtaProgressionEr", 240,0.,240.,len(etaBinsAsTT)-1,etaBinsAsTT)



for i in range(1,ratePtVsEtaProgression1.GetNbinsX()+1):
    for j in range(1,ratePtVsEtaProgression1.GetNbinsY()+1):
        rate1 = ratePtVsEtaProgression1.GetBinContent(i,j);
        rate2 = ratePtVsEtaProgression2.GetBinContent(i,j);

        if rate1 == 0.0: continue

        rel_rate = (rate2 - rate1)/rate1 * 100
        relative_ratePtVsEtaProgression.SetBinContent(i,j,rel_rate);

for i in range(1,ratePtProgression1.GetNbinsX()+1):
    # single
    rate1 = ratePtProgression1.GetBinContent(i);
    rate2 = ratePtProgression2.GetBinContent(i);

    if rate1 == 0.0: continue

    rel_rate = (rate2 - rate1)/rate1 * 100
    relative_ratePtProgression.SetBinContent(i,rel_rate);

for i in range(1,ratePtProgression1.GetNbinsX()+1):
    # di
    rate1 = ratePtDiProgression1.GetBinContent(i);
    rate2 = ratePtDiProgression2.GetBinContent(i);

    if rate1 == 0.0: continue

    rel_rate = (rate2 - rate1)/rate1 * 100
    relative_ratePtDiProgression.SetBinContent(i,rel_rate);

for i in range(1,rateEtaProgression1.GetNbinsX()+1):
    # single
    rate1 = rateEtaProgression1.GetBinContent(i);
    rate2 = rateEtaProgression2.GetBinContent(i);

    if rate1 == 0.0: continue

    rel_rate = (rate2 - rate1)/rate1 * 100
    relative_rateEtaProgression.SetBinContent(i,rel_rate);

for i in range(1,rateEtaProgression1.GetNbinsX()+1):
    # di
    rate1 = rateEtaDiProgression1.GetBinContent(i);
    rate2 = rateEtaDiProgression2.GetBinContent(i);

    if rate1 == 0.0: continue

    rel_rate = (rate2 - rate1)/rate1 * 100
    relative_rateEtaDiProgression.SetBinContent(i,rel_rate);





for i in range(1,ratePtVsEtaProgression1Er.GetNbinsX()+1):
    for j in range(1,ratePtVsEtaProgression1Er.GetNbinsY()+1):
        rate1 = ratePtVsEtaProgression1Er.GetBinContent(i,j);
        rate2 = ratePtVsEtaProgression2Er.GetBinContent(i,j);

        if rate1 == 0.0: continue

        rel_rate = (rate2 - rate1)/rate1 * 100
        relative_ratePtVsEtaProgressionEr.SetBinContent(i,j,rel_rate);

for i in range(1,ratePtProgression1Er.GetNbinsX()+1):
    # single
    rate1 = ratePtProgression1Er.GetBinContent(i);
    rate2 = ratePtProgression2Er.GetBinContent(i);

    if rate1 == 0.0: continue

    rel_rate = (rate2 - rate1)/rate1 * 100
    relative_ratePtProgressionEr.SetBinContent(i,rel_rate);

for i in range(1,ratePtProgression1Er.GetNbinsX()+1):
    # di
    rate1 = ratePtDiProgression1Er.GetBinContent(i);
    rate2 = ratePtDiProgression2Er.GetBinContent(i);

    if rate1 == 0.0: continue

    rel_rate = (rate2 - rate1)/rate1 * 100
    relative_ratePtDiProgressionEr.SetBinContent(i,rel_rate);

for i in range(1,rateEtaProgression1Er.GetNbinsX()+1):
    # single
    rate1 = rateEtaProgression1Er.GetBinContent(i);
    rate2 = rateEtaProgression2Er.GetBinContent(i);

    if rate1 == 0.0: continue

    rel_rate = (rate2 - rate1)/rate1 * 100
    relative_rateEtaProgressionEr.SetBinContent(i,rel_rate);

for i in range(1,rateEtaProgression1Er.GetNbinsX()+1):
    # di
    rate1 = rateEtaDiProgression1Er.GetBinContent(i);
    rate2 = rateEtaDiProgression2Er.GetBinContent(i);

    if rate1 == 0.0: continue

    rel_rate = (rate2 - rate1)/rate1 * 100
    relative_rateEtaDiProgressionEr.SetBinContent(i,rel_rate);






####################

ROOT.gStyle.SetOptStat(000000)

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
# canvas.SetLogy()

#use dummy histogram to define style
relative_ratePtProgression.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
relative_ratePtProgression.SetTitle("")
relative_ratePtProgression.GetXaxis().SetRangeUser(0.,240.);
relative_ratePtProgression.GetYaxis().SetRangeUser(1,max(relative_ratePtProgression.GetMaximum(),relative_ratePtDiProgression.GetMaximum())*1.3);
relative_ratePtProgression.GetXaxis().SetTitleOffset(1.3);
relative_ratePtProgression.GetYaxis().SetTitle("Relative rate difference [%]");
relative_ratePtProgression.GetYaxis().SetTitleOffset(1.3);
relative_ratePtProgression.SetTitle("");
relative_ratePtProgression.SetLineWidth(2)
relative_ratePtProgression.SetMarkerColor(1)
relative_ratePtProgression.SetLineColor(1)
relative_ratePtProgression.Draw()

relative_ratePtDiProgression.SetLineWidth(2)
relative_ratePtDiProgression.SetMarkerColor(2)
relative_ratePtDiProgression.SetLineColor(2)
relative_ratePtDiProgression.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(relative_ratePtProgression,"Single-Obj","LPE")
legend.AddEntry(relative_ratePtDiProgression,"Double-Obj","LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsPt_relative_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
# canvas.SetLogy()

#use dummy histogram to define style
relative_rateEtaProgression.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
relative_rateEtaProgression.SetTitle("")
relative_rateEtaProgression.GetXaxis().SetRangeUser(0.,etaPlotLim);
relative_rateEtaProgression.GetYaxis().SetRangeUser(1,max(relative_rateEtaProgression.GetMaximum(),relative_rateEtaDiProgression.GetMaximum())*1.3);
relative_rateEtaProgression.GetXaxis().SetTitleOffset(1.3);
relative_rateEtaProgression.GetYaxis().SetTitle("Relative rate difference [%]");
relative_rateEtaProgression.GetYaxis().SetTitleOffset(1.3);
relative_rateEtaProgression.SetTitle("");
relative_rateEtaProgression.SetLineWidth(2)
relative_rateEtaProgression.SetMarkerColor(1)
relative_rateEtaProgression.SetLineColor(1)
relative_rateEtaProgression.Draw()

relative_rateEtaDiProgression.SetLineWidth(2)
relative_rateEtaDiProgression.SetMarkerColor(2)
relative_rateEtaDiProgression.SetLineColor(2)
relative_rateEtaDiProgression.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(relative_rateEtaProgression,"Single-Obj","LPE")
legend.AddEntry(relative_rateEtaDiProgression,"Double-Obj","LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsEta_relative_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

###################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
ratePtProgression1.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
ratePtProgression1.SetTitle("")
ratePtProgression1.GetXaxis().SetRangeUser(0.,240.);
ratePtProgression1.GetYaxis().SetRangeUser(1,1e5);
ratePtProgression1.GetXaxis().SetTitleOffset(1.3);
ratePtProgression1.GetYaxis().SetTitle("Rate [kHz]");
ratePtProgression1.GetYaxis().SetTitleOffset(1.3);
ratePtProgression1.SetTitle("");
ratePtProgression1.SetLineWidth(2)
ratePtProgression1.SetMarkerColor(1)
ratePtProgression1.SetLineColor(1)
ratePtProgression1.Draw()

ratePtProgression2.SetLineWidth(2)
ratePtProgression2.SetMarkerColor(2)
ratePtProgression2.SetLineColor(2)
ratePtProgression2.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(ratePtProgression1,"Old calibration","LPE")
legend.AddEntry(ratePtProgression2,"New calibration","LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsPt_superimposed_SingleObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
rateEtaProgression1.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
rateEtaProgression1.SetTitle("")
rateEtaProgression1.GetXaxis().SetRangeUser(0.,etaPlotLim);
rateEtaProgression1.GetYaxis().SetRangeUser(1,1e5);
rateEtaProgression1.GetXaxis().SetTitleOffset(1.3);
rateEtaProgression1.GetYaxis().SetTitle("Rate [kHz]");
rateEtaProgression1.GetYaxis().SetTitleOffset(1.3);
rateEtaProgression1.SetTitle("");
rateEtaProgression1.SetLineWidth(2)
rateEtaProgression1.SetMarkerColor(1)
rateEtaProgression1.SetLineColor(1)
rateEtaProgression1.Draw()

rateEtaProgression2.SetLineWidth(2)
rateEtaProgression2.SetMarkerColor(2)
rateEtaProgression2.SetLineColor(2)
rateEtaProgression2.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaProgression1,"Old calibration","LPE")
legend.AddEntry(rateEtaProgression2,"New calibration","LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsEta_superimposed_SingleObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

###################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
ratePtDiProgression1.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
ratePtDiProgression1.SetTitle("")
ratePtDiProgression1.GetXaxis().SetRangeUser(0.,240.);
ratePtDiProgression1.GetYaxis().SetRangeUser(1,1e5);
ratePtDiProgression1.GetXaxis().SetTitleOffset(1.3);
ratePtDiProgression1.GetYaxis().SetTitle("Rate [kHz]");
ratePtDiProgression1.GetYaxis().SetTitleOffset(1.3);
ratePtDiProgression1.SetTitle("");
ratePtDiProgression1.SetLineWidth(2)
ratePtDiProgression1.SetMarkerColor(1)
ratePtDiProgression1.SetLineColor(1)
ratePtDiProgression1.Draw()

ratePtDiProgression2.SetLineWidth(2)
ratePtDiProgression2.SetMarkerColor(2)
ratePtDiProgression2.SetLineColor(2)
ratePtDiProgression2.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(ratePtDiProgression1,"Old calibration","LPE")
legend.AddEntry(ratePtDiProgression2,"New calibration","LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsPt_superimposed_DiObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
rateEtaDiProgression1.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
rateEtaDiProgression1.SetTitle("")
rateEtaDiProgression1.GetXaxis().SetRangeUser(0.,etaPlotLim);
rateEtaDiProgression1.GetYaxis().SetRangeUser(1,1e5);
rateEtaDiProgression1.GetXaxis().SetTitleOffset(1.3);
rateEtaDiProgression1.GetYaxis().SetTitle("Rate [kHz]");
rateEtaDiProgression1.GetYaxis().SetTitleOffset(1.3);
rateEtaDiProgression1.SetTitle("");
rateEtaDiProgression1.SetLineWidth(2)
rateEtaDiProgression1.SetMarkerColor(1)
rateEtaDiProgression1.SetLineColor(1)
rateEtaDiProgression1.Draw()

rateEtaDiProgression2.SetLineWidth(2)
rateEtaDiProgression2.SetMarkerColor(2)
rateEtaDiProgression2.SetLineColor(2)
rateEtaDiProgression2.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaDiProgression1,"Old calibration","LPE")
legend.AddEntry(rateEtaDiProgression2,"New calibration","LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsEta_superimposed_DiObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

###################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
ratePtProgression1Er.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
ratePtProgression1Er.SetTitle("")
ratePtProgression1Er.GetXaxis().SetRangeUser(0.,240.);
ratePtProgression1Er.GetYaxis().SetRangeUser(1,1e5);
ratePtProgression1Er.GetXaxis().SetTitleOffset(1.3);
ratePtProgression1Er.GetYaxis().SetTitle("Rate [kHz]");
ratePtProgression1Er.GetYaxis().SetTitleOffset(1.3);
ratePtProgression1Er.SetTitle("");
ratePtProgression1Er.SetLineWidth(2)
ratePtProgression1Er.SetMarkerColor(1)
ratePtProgression1Er.SetLineColor(1)
ratePtProgression1Er.Draw()

ratePtProgression2Er.SetLineWidth(2)
ratePtProgression2Er.SetMarkerColor(2)
ratePtProgression2Er.SetLineColor(2)
ratePtProgression2Er.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(ratePtProgression1Er,"Old calibration |#eta|<"+str(etaRestictedLim),"LPE")
legend.AddEntry(ratePtProgression2Er,"New calibration |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsPt_Er_superimposed_SingleObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
rateEtaProgression1Er.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
rateEtaProgression1Er.SetTitle("")
rateEtaProgression1Er.GetXaxis().SetRangeUser(0.,etaRestictedLim);
rateEtaProgression1Er.GetYaxis().SetRangeUser(1,1e5);
rateEtaProgression1Er.GetXaxis().SetTitleOffset(1.3);
rateEtaProgression1Er.GetYaxis().SetTitle("Relative rate difference [%]");
rateEtaProgression1Er.GetYaxis().SetTitleOffset(1.3);
rateEtaProgression1Er.SetTitle("");
rateEtaProgression1Er.SetLineWidth(2)
rateEtaProgression1Er.SetMarkerColor(1)
rateEtaProgression1Er.SetLineColor(1)
rateEtaProgression1Er.Draw()

rateEtaProgression2Er.SetLineWidth(2)
rateEtaProgression2Er.SetMarkerColor(2)
rateEtaProgression2Er.SetLineColor(2)
rateEtaProgression2Er.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaProgression1Er,"Old calibration |#eta|<"+str(etaRestictedLim),"LPE")
legend.AddEntry(rateEtaProgression2Er,"New calibration |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsEta_Er_superimposed_SingleObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

###################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
ratePtDiProgression1Er.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
ratePtDiProgression1Er.SetTitle("")
ratePtDiProgression1Er.GetXaxis().SetRangeUser(0.,240.);
ratePtDiProgression1Er.GetYaxis().SetRangeUser(1,1e5);
ratePtDiProgression1Er.GetXaxis().SetTitleOffset(1.3);
ratePtDiProgression1Er.GetYaxis().SetTitle("Rate [kHz]");
ratePtDiProgression1Er.GetYaxis().SetTitleOffset(1.3);
ratePtDiProgression1Er.SetTitle("");
ratePtDiProgression1Er.SetLineWidth(2)
ratePtDiProgression1Er.SetMarkerColor(1)
ratePtDiProgression1Er.SetLineColor(1)
ratePtDiProgression1Er.Draw()

ratePtDiProgression2Er.SetLineWidth(2)
ratePtDiProgression2Er.SetMarkerColor(2)
ratePtDiProgression2Er.SetLineColor(2)
ratePtDiProgression2Er.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(ratePtDiProgression1Er,"Old calibration |#eta|<"+str(etaRestictedLim),"LPE")
legend.AddEntry(ratePtDiProgression2Er,"New calibration |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsPt_Er_superimposed_DiObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
rateEtaDiProgression1Er.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
rateEtaDiProgression1Er.SetTitle("")
rateEtaDiProgression1Er.GetXaxis().SetRangeUser(0.,etaRestictedLim);
rateEtaDiProgression1Er.GetYaxis().SetRangeUser(1,1e5);
rateEtaDiProgression1Er.GetXaxis().SetTitleOffset(1.3);
rateEtaDiProgression1Er.GetYaxis().SetTitle("Relative rate difference [%]");
rateEtaDiProgression1Er.GetYaxis().SetTitleOffset(1.3);
rateEtaDiProgression1Er.SetTitle("");
rateEtaDiProgression1Er.SetLineWidth(2)
rateEtaDiProgression1Er.SetMarkerColor(1)
rateEtaDiProgression1Er.SetLineColor(1)
rateEtaDiProgression1Er.Draw()

rateEtaDiProgression2Er.SetLineWidth(2)
rateEtaDiProgression2Er.SetMarkerColor(2)
rateEtaDiProgression2Er.SetLineColor(2)
rateEtaDiProgression2Er.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaDiProgression1Er,"Old calibration |#eta|<"+str(etaRestictedLim),"LPE")
legend.AddEntry(rateEtaDiProgression2Er,"New calibration |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsEta_Er_superimposed_DiObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

maxi = 0.;
mini = 0.;
val_white = 0.;
per_white = 0.;
Number = 3;
Red   = array("d", [0., 1., 1.])
Green = array("d", [0., 1., 0.])
Blue  = array("d", [1., 1., 0.])
nb= 256;

canvas = ROOT.TCanvas("c","c",900,800);
canvas.SetRightMargin(0.175);
canvas.SetLeftMargin(0.1);
canvas.SetGrid(10,10);
# canvas.SetLogz()

maxi = relative_ratePtVsEtaProgression.GetMaximum();
mini = min(relative_ratePtVsEtaProgression.GetMinimum(), 0.0);
per_white = (val_white-mini)/(maxi-mini);
Stops1 = array("d", [0., per_white, 1.])
relative_ratePtVsEtaProgression.SetContour(nb);
ROOT.TColor.CreateGradientColorTable(Number,Stops1,Red,Green,Blue,nb);

relative_ratePtVsEtaProgression.SetTitle("");
relative_ratePtVsEtaProgression.GetXaxis().SetTitle("p_{T}^{L1} [GeV]");
relative_ratePtVsEtaProgression.GetYaxis().SetTitle("#eta^{L1}");
relative_ratePtVsEtaProgression.GetZaxis().SetTitle("Relative rate difference [%]");
relative_ratePtVsEtaProgression.GetZaxis().SetTitleOffset(1.7);
relative_ratePtVsEtaProgression.GetXaxis().SetRangeUser(0.,240.);
relative_ratePtVsEtaProgression.GetYaxis().SetRangeUser(0.,etaPlotLim);
relative_ratePtVsEtaProgression.Draw("colz");

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(relative_ratePtVsEtaProgression,"Single-Obj", "LPE")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.1,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.82,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/PtVsEta_relative_rate_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
# canvas.SetLogy()

#use dummy histogram to define style
relative_ratePtProgressionEr.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
relative_ratePtProgressionEr.SetTitle("")
relative_ratePtProgressionEr.GetXaxis().SetRangeUser(0.,240.);
relative_ratePtProgressionEr.GetYaxis().SetRangeUser(1,max(relative_ratePtProgressionEr.GetMaximum(),relative_ratePtDiProgressionEr.GetMaximum())*1.3);
relative_ratePtProgressionEr.GetXaxis().SetTitleOffset(1.3);
relative_ratePtProgressionEr.GetYaxis().SetTitle("Relative rate difference [%]");
relative_ratePtProgressionEr.GetYaxis().SetTitleOffset(1.3);
relative_ratePtProgressionEr.SetTitle("");
relative_ratePtProgressionEr.SetLineWidth(2)
relative_ratePtProgressionEr.SetMarkerColor(1)
relative_ratePtProgressionEr.SetLineColor(1)
relative_ratePtProgressionEr.Draw()

relative_ratePtDiProgressionEr.SetLineWidth(2)
relative_ratePtDiProgressionEr.SetMarkerColor(2)
relative_ratePtDiProgressionEr.SetLineColor(2)
relative_ratePtDiProgressionEr.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(relative_ratePtProgressionEr,"Single-Obj","LPE")
legend.AddEntry(relative_ratePtDiProgressionEr,"Double-Obj","LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsPt_Er_relative_SingleObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
# canvas.SetLogy()

#use dummy histogram to define style
relative_rateEtaProgressionEr.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
relative_rateEtaProgressionEr.SetTitle("")
relative_rateEtaProgressionEr.GetXaxis().SetRangeUser(0.,etaRestictedLim);
relative_rateEtaProgressionEr.GetYaxis().SetRangeUser(1,max(relative_rateEtaProgressionEr.GetMaximum(),relative_rateEtaDiProgressionEr.GetMaximum())*1.3);
relative_rateEtaProgressionEr.GetXaxis().SetTitleOffset(1.3);
relative_rateEtaProgressionEr.GetYaxis().SetTitle("Relative rate difference [%]");
relative_rateEtaProgressionEr.GetYaxis().SetTitleOffset(1.3);
relative_rateEtaProgressionEr.SetTitle("");
relative_rateEtaProgressionEr.SetLineWidth(2)
relative_rateEtaProgressionEr.SetMarkerColor(1)
relative_rateEtaProgressionEr.SetLineColor(1)
relative_rateEtaProgressionEr.Draw()

relative_rateEtaDiProgressionEr.SetLineWidth(2)
relative_rateEtaDiProgressionEr.SetMarkerColor(2)
relative_rateEtaDiProgressionEr.SetLineColor(2)
relative_rateEtaDiProgressionEr.Draw("same")

legend = ROOT.TLegend(0.60,0.80,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(relative_rateEtaProgressionEr,"Single-Obj","LPE")
legend.AddEntry(relative_rateEtaDiProgressionEr,"Double-Obj","LPE")
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

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/rateVsEta_Er_relative_SingleObj_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")

del canvas, tex, tex2, legend

####################

maxi = 0.;
mini = 0.;
val_white = 0.;
per_white = 0.;
Number = 3;
Red   = array("d", [0., 1., 1.])
Green = array("d", [0., 1., 0.])
Blue  = array("d", [1., 1., 0.])
nb= 256;

canvas = ROOT.TCanvas("c","c",900,800);
canvas.SetRightMargin(0.175);
canvas.SetLeftMargin(0.1);
canvas.SetGrid(10,10);
# canvas.SetLogz()

maxi = relative_ratePtVsEtaProgressionEr.GetMaximum();
mini = min(relative_ratePtVsEtaProgressionEr.GetMinimum(), 0.0);
per_white = (val_white-mini)/(maxi-mini);
Stops1 = array("d", [0., per_white, 1.])
relative_ratePtVsEtaProgressionEr.SetContour(nb);
ROOT.TColor.CreateGradientColorTable(Number,Stops1,Red,Green,Blue,nb);

relative_ratePtVsEtaProgressionEr.SetTitle("");
relative_ratePtVsEtaProgressionEr.GetXaxis().SetTitle("p_{T}^{L1} [GeV]");
relative_ratePtVsEtaProgressionEr.GetYaxis().SetTitle("#eta^{L1}");
relative_ratePtVsEtaProgressionEr.GetZaxis().SetTitle("Relative rate difference [%]");
relative_ratePtVsEtaProgressionEr.GetZaxis().SetTitleOffset(1.7);
relative_ratePtVsEtaProgressionEr.GetXaxis().SetRangeUser(0.,240.);
relative_ratePtVsEtaProgressionEr.GetYaxis().SetRangeUser(0.,etaRestictedLim);
relative_ratePtVsEtaProgressionEr.Draw("colz");

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(relative_ratePtVsEtaProgressionEr,"Single-Obj", "LPE")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.1,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.82,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+"/PDFs/comparisons_"+L1CalibTag2+"/PtVsEta_Er_relative_rate_"+L1CalibTag1+"_vs_"+L1CalibTag2+".pdf")
