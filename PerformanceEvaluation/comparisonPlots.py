from array import array
import ROOT
import sys
import os

label = sys.argv[1]

detector = label.split("_")[0]
newTag   = label.split("_")[1]

os.system('mkdir -p PDFs/comparisons_'+label)
os.system('mkdir -p PNGs/comparisons_'+label)

#defining binning of histogram
if "HCAL_" in label: 
    ptBins  = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200, 500]
    etaBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.191]
if "ECAL_" in label:
    ptBins  = [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200]
    etaBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0]

# #############################
# ## RESOLUTIONS COMPARISONS ##

# file_unCalib  = ROOT.TFile("ROOTs/resolution_graphs_"+detector+"_uncalib.root", "r")
# file_oldCalib = ROOT.TFile("ROOTs/resolution_graphs_"+detector+"_oldCalib.root", "r")
# file_newCalib = ROOT.TFile("ROOTs/resolution_graphs_"+detector+"_"+newTag+".root", "r")

# #######
# # inclusive responses

# inclusive_resp_unCalib  = file_unCalib.Get("pt_response_ptInclusive")
# inclusive_resp_oldCalib = file_oldCalib.Get("pt_response_ptInclusive")
# inclusive_resp_newCalib = file_newCalib.Get("pt_response_ptInclusive")

# #define canvas for plotting
# canvas = ROOT.TCanvas("c","c",800,800)
# canvas.SetGrid(10,10);

# #use dummy histogram to define style
# inclusive_resp_unCalib.GetXaxis().SetTitle("E_{T}^{L1 jet} / p_{T}^{gen jet}")
# inclusive_resp_unCalib.SetTitle("")

# inclusive_resp_unCalib.GetXaxis().SetTitleOffset(1.3);
# inclusive_resp_unCalib.GetYaxis().SetTitle("a.u.");
# inclusive_resp_unCalib.GetYaxis().SetTitleOffset(1.3);
# inclusive_resp_unCalib.SetTitle("");
# inclusive_resp_unCalib.SetStats(0);

# inclusive_resp_unCalib.GetYaxis().SetRangeUser(0., 0.5 )
# inclusive_resp_unCalib.GetXaxis().SetRangeUser(0., 2. )

# inclusive_resp_oldCalib.SetLineWidth(2)
# inclusive_resp_oldCalib.SetMarkerStyle(8)
# inclusive_resp_oldCalib.SetMarkerColor(2)
# inclusive_resp_oldCalib.SetLineColor(2)

# inclusive_resp_newCalib.SetLineWidth(2)
# inclusive_resp_newCalib.SetMarkerStyle(8)
# inclusive_resp_newCalib.SetMarkerColor(3)
# inclusive_resp_newCalib.SetLineColor(3)

# inclusive_resp_unCalib.SetLineWidth(2)
# inclusive_resp_unCalib.SetMarkerStyle(8)
# inclusive_resp_unCalib.SetMarkerColor(1)
# inclusive_resp_unCalib.SetLineColor(1)

# inclusive_resp_unCalib.Draw("LPE")
# inclusive_resp_newCalib.Draw("LPE same")
# inclusive_resp_oldCalib.Draw("LPE same")

# legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
# legend.SetBorderSize(0)
# legend.AddEntry(inclusive_resp_unCalib,"Uncalibrated", "LPE")
# legend.AddEntry(inclusive_resp_oldCalib,"Old Calibration", "LPE")
# legend.AddEntry(inclusive_resp_newCalib,"New Calibration", "LPE")
# legend.Draw("same")

# tex = ROOT.TLatex()
# tex.SetTextSize(0.03);
# tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
# tex.Draw("same")

# tex2 = ROOT.TLatex();
# tex2.SetTextSize(0.035);
# tex2.SetTextAlign(31);
# tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
# tex2.Draw("same");

# canvas.SaveAs("PDFs/comparisons_"+label+"/response_inclusive_"+label+".pdf")
# canvas.SaveAs("PNGs/comparisons_"+label+"/response_inclusive_"+label+".png")

# del canvas, legend, tex2, tex

# #######
# # ptBins responses

# for i in range(len(ptBins)-1):
#     ptBins_resp_unCalib = file_unCalib.Get("pt_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]))
#     ptBins_resp_oldCalib = file_oldCalib.Get("pt_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]))
#     ptBins_resp_newCalib = file_newCalib.Get("pt_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]))

#     #define canvas for plotting
#     canvas = ROOT.TCanvas("c","c",800,800)
#     canvas.SetGrid(10,10);

#     #use dummy histogram to define style
#     ptBins_resp_unCalib.GetXaxis().SetTitle("E_{T}^{L1 jet} / p_{T}^{gen jet}")
#     ptBins_resp_unCalib.SetTitle("")

#     ptBins_resp_unCalib.GetXaxis().SetTitleOffset(1.3);
#     ptBins_resp_unCalib.GetYaxis().SetTitle("a.u.");
#     ptBins_resp_unCalib.GetYaxis().SetTitleOffset(1.3);
#     ptBins_resp_unCalib.SetTitle("");
#     ptBins_resp_unCalib.SetStats(0);

#     ptBins_resp_unCalib.GetYaxis().SetRangeUser(0., max(ptBins_resp_oldCalib.GetMaximum(),ptBins_resp_newCalib.GetMaximum())*1.3 )

#     ptBins_resp_oldCalib.SetLineWidth(2)
#     ptBins_resp_oldCalib.SetMarkerStyle(8)
#     ptBins_resp_oldCalib.SetMarkerColor(2)
#     ptBins_resp_oldCalib.SetLineColor(2)

#     ptBins_resp_newCalib.SetLineWidth(2)
#     ptBins_resp_newCalib.SetMarkerStyle(8)
#     ptBins_resp_newCalib.SetMarkerColor(3)
#     ptBins_resp_newCalib.SetLineColor(3)

#     ptBins_resp_unCalib.SetLineWidth(2)
#     ptBins_resp_unCalib.SetMarkerStyle(8)
#     ptBins_resp_unCalib.SetMarkerColor(1)
#     ptBins_resp_unCalib.SetLineColor(1)

#     ptBins_resp_unCalib.Draw("LPE")
#     ptBins_resp_newCalib.Draw("LPE same")
#     ptBins_resp_oldCalib.Draw("LPE same")

#     legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
#     legend.SetBorderSize(0)
#     legend.SetHeader(str(ptBins[i])+"<p_{T}^{gen jet}<"+str(ptBins[i+1]))
#     legend.AddEntry(ptBins_resp_unCalib,"Uncalibrated", "LPE")
#     legend.AddEntry(ptBins_resp_oldCalib,"Old Calibration", "LPE")
#     legend.AddEntry(ptBins_resp_newCalib,"New Calibration", "LPE")
#     legend.Draw("same")

#     tex = ROOT.TLatex()
#     tex.SetTextSize(0.03);
#     tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
#     tex.Draw("same")

#     tex2 = ROOT.TLatex();
#     tex2.SetTextSize(0.035);
#     tex2.SetTextAlign(31);
#     tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
#     tex2.Draw("same");

#     canvas.SaveAs("PDFs/comparisons_"+label+"/response_"+str(ptBins[i])+"pt"+str(ptBins[i+1])+"_"+label+".pdf")
#     canvas.SaveAs("PNGs/comparisons_"+label+"/response_"+str(ptBins[i])+"pt"+str(ptBins[i+1])+"_"+label+".png")

#     del canvas, legend, ptBins_resp_unCalib, ptBins_resp_oldCalib, ptBins_resp_newCalib, tex2, tex

# #######
# # etaBins responses

# for i in range(len(etaBins)-1):
#     etaBins_resp_unCalib = file_unCalib.Get("pt_resp_AbsEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]))
#     etaBins_resp_oldCalib = file_oldCalib.Get("pt_resp_AbsEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]))
#     etaBins_resp_newCalib = file_newCalib.Get("pt_resp_AbsEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]))

#     #define canvas for plotting
#     canvas = ROOT.TCanvas("c","c",800,800)
#     canvas.SetGrid(10,10);

#     #use dummy histogram to define style
#     etaBins_resp_unCalib.GetXaxis().SetTitle("E_{T}^{L1 jet} / p_{T}^{gen jet}")
#     etaBins_resp_unCalib.SetTitle("")

#     etaBins_resp_unCalib.GetXaxis().SetTitleOffset(1.3);
#     etaBins_resp_unCalib.GetYaxis().SetTitle("a.u.");
#     etaBins_resp_unCalib.GetYaxis().SetTitleOffset(1.3);
#     etaBins_resp_unCalib.SetTitle("");
#     etaBins_resp_unCalib.SetStats(0);

#     etaBins_resp_unCalib.GetYaxis().SetRangeUser(0., max(etaBins_resp_oldCalib.GetMaximum(),etaBins_resp_newCalib.GetMaximum())*1.3 )

#     etaBins_resp_oldCalib.SetLineWidth(2)
#     etaBins_resp_oldCalib.SetMarkerStyle(8)
#     etaBins_resp_oldCalib.SetMarkerColor(2)
#     etaBins_resp_oldCalib.SetLineColor(2)

#     etaBins_resp_newCalib.SetLineWidth(2)
#     etaBins_resp_newCalib.SetMarkerStyle(8)
#     etaBins_resp_newCalib.SetMarkerColor(3)
#     etaBins_resp_newCalib.SetLineColor(3)

#     etaBins_resp_unCalib.SetLineWidth(2)
#     etaBins_resp_unCalib.SetMarkerStyle(8)
#     etaBins_resp_unCalib.SetMarkerColor(1)
#     etaBins_resp_unCalib.SetLineColor(1)

#     etaBins_resp_unCalib.Draw("LPE")
#     etaBins_resp_newCalib.Draw("LPE same")
#     etaBins_resp_oldCalib.Draw("LPE same")

#     legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
#     legend.SetBorderSize(0)
#     legend.SetHeader(str(etaBins[i])+"<|#eta^{gen jet}|<"+str(etaBins[i+1]))
#     legend.AddEntry(etaBins_resp_unCalib,"Uncalibrated", "LPE")
#     legend.AddEntry(etaBins_resp_oldCalib,"Old Calibration", "LPE")
#     legend.AddEntry(etaBins_resp_newCalib,"New Calibration", "LPE")
#     legend.Draw("same")

#     tex = ROOT.TLatex()
#     tex.SetTextSize(0.03);
#     tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
#     tex.Draw("same")

#     tex2 = ROOT.TLatex();
#     tex2.SetTextSize(0.035);
#     tex2.SetTextAlign(31);
#     tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
#     tex2.Draw("same");

#     canvas.SaveAs("PDFs/comparisons_"+label+"/response_"+str(etaBins[i])+"eta"+str(etaBins[i+1])+"_"+label+".pdf")
#     canvas.SaveAs("PNGs/comparisons_"+label+"/response_"+str(etaBins[i])+"eta"+str(etaBins[i+1])+"_"+label+".png")

#     del canvas, legend, etaBins_resp_unCalib, etaBins_resp_oldCalib, etaBins_resp_newCalib, tex2, tex

# #######
# # ptBins resolution

# ptBins_resol_unCalib  = file_unCalib.Get("pt_resol_fctPt")
# ptBins_resol_oldCalib = file_oldCalib.Get("pt_resol_fctPt")
# ptBins_resol_newCalib = file_newCalib.Get("pt_resol_fctPt")

# #define canvas for plotting
# canvas = ROOT.TCanvas("c","c",800,800)
# canvas.SetGrid(10,10);

# #use dummy histogram to define style
# ptBins_resol_unCalib.GetXaxis().SetTitle("p_{T}^{gen jet} [GeV]")
# ptBins_resol_unCalib.SetTitle("")

# ptBins_resol_unCalib.GetXaxis().SetTitleOffset(1.3);
# ptBins_resol_unCalib.GetYaxis().SetTitle("E_{T}^{L1 jet} resolution");
# ptBins_resol_unCalib.GetYaxis().SetTitleOffset(1.3);
# ptBins_resol_unCalib.SetTitle("");
# ptBins_resol_unCalib.SetStats(0);

# ptBins_resol_unCalib.GetYaxis().SetRangeUser(0., max(ptBins_resol_oldCalib.GetMaximum(),ptBins_resol_newCalib.GetMaximum())*1.3 )

# ptBins_resol_oldCalib.SetLineWidth(2)
# ptBins_resol_oldCalib.SetMarkerStyle(8)
# ptBins_resol_oldCalib.SetMarkerColor(2)
# ptBins_resol_oldCalib.SetLineColor(2)

# ptBins_resol_newCalib.SetLineWidth(2)
# ptBins_resol_newCalib.SetMarkerStyle(8)
# ptBins_resol_newCalib.SetMarkerColor(3)
# ptBins_resol_newCalib.SetLineColor(3)

# ptBins_resol_unCalib.SetLineWidth(2)
# ptBins_resol_unCalib.SetMarkerStyle(8)
# ptBins_resol_unCalib.SetMarkerColor(1)
# ptBins_resol_unCalib.SetLineColor(1)

# ptBins_resol_unCalib.Draw("LPE")
# ptBins_resol_newCalib.Draw("LPE same")
# ptBins_resol_oldCalib.Draw("LPE same")

# legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
# legend.SetBorderSize(0)
# legend.AddEntry(ptBins_resol_unCalib,"Uncalibrated", "LPE")
# legend.AddEntry(ptBins_resol_oldCalib,"Old Calibration", "LPE")
# legend.AddEntry(ptBins_resol_newCalib,"New Calibration", "LPE")
# legend.Draw("same")

# tex = ROOT.TLatex()
# tex.SetTextSize(0.03);
# tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
# tex.Draw("same")

# tex2 = ROOT.TLatex();
# tex2.SetTextSize(0.035);
# tex2.SetTextAlign(31);
# tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
# tex2.Draw("same");

# canvas.SaveAs("PDFs/comparisons_"+label+"/resolution_ptBins_"+label+".pdf")
# canvas.SaveAs("PNGs/comparisons_"+label+"/resolution_ptBins_"+label+".png")

# del canvas, legend, tex2, tex

# #######
# # etaBins resolution

# etaBins_resol_unCalib  = file_unCalib.Get("pt_resol_fctEta")
# etaBins_resol_oldCalib = file_oldCalib.Get("pt_resol_fctEta")
# etaBins_resol_newCalib = file_newCalib.Get("pt_resol_fctEta")

# #define canvas for plotting
# canvas = ROOT.TCanvas("c","c",800,800)
# canvas.SetGrid(10,10);

# #use dummy histogram to define style
# etaBins_resol_unCalib.GetXaxis().SetTitle("#eta^{gen jet}")
# etaBins_resol_unCalib.SetTitle("")

# etaBins_resol_unCalib.GetXaxis().SetTitleOffset(1.3);
# etaBins_resol_unCalib.GetYaxis().SetTitle("E_{T}^{L1 jet} resolution");
# etaBins_resol_unCalib.GetYaxis().SetTitleOffset(1.3);
# etaBins_resol_unCalib.SetTitle("");
# etaBins_resol_unCalib.SetStats(0);

# if "ECAL_" in label: etaBins_resol_unCalib.GetYaxis().SetRangeUser(0., 1.)
# if "HCAL_" in label: etaBins_resol_unCalib.GetYaxis().SetRangeUser(0., 2.)

# etaBins_resol_oldCalib.SetLineWidth(2)
# etaBins_resol_oldCalib.SetMarkerStyle(8)
# etaBins_resol_oldCalib.SetMarkerColor(2)
# etaBins_resol_oldCalib.SetLineColor(2)

# etaBins_resol_newCalib.SetLineWidth(2)
# etaBins_resol_newCalib.SetMarkerStyle(8)
# etaBins_resol_newCalib.SetMarkerColor(3)
# etaBins_resol_newCalib.SetLineColor(3)

# etaBins_resol_unCalib.SetLineWidth(2)
# etaBins_resol_unCalib.SetMarkerStyle(8)
# etaBins_resol_unCalib.SetMarkerColor(1)
# etaBins_resol_unCalib.SetLineColor(1)

# etaBins_resol_unCalib.Draw("LPE")
# etaBins_resol_newCalib.Draw("LPE same")
# etaBins_resol_oldCalib.Draw("LPE same")

# b1 = ROOT.TBox(1.305,0.,1.479,2)
# b1.SetFillColor(16)
# b1.Draw("same")
# b2 = ROOT.TBox(-1.479,0.,-1.305,2)
# b2.SetFillColor(16)
# b2.Draw("same")
# b3 = ROOT.TBox(1.305,0.,1.479,2)
# b3.SetFillColor(1)
# b3.SetFillStyle(3004)
# b3.Draw("same")
# b4 = ROOT.TBox(-1.479,0.,-1.305,2)
# b4.SetFillColor(1)
# b4.SetFillStyle(3004)
# b4.Draw("same")

# legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
# legend.SetBorderSize(0)
# legend.AddEntry(etaBins_resol_unCalib,"Uncalibrated", "LPE")
# legend.AddEntry(etaBins_resol_oldCalib,"Old Calibration", "LPE")
# legend.AddEntry(etaBins_resol_newCalib,"New Calibration", "LPE")
# legend.Draw("same")

# tex = ROOT.TLatex()
# tex.SetTextSize(0.03);
# tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
# tex.Draw("same")

# tex2 = ROOT.TLatex();
# tex2.SetTextSize(0.035);
# tex2.SetTextAlign(31);
# tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
# tex2.Draw("same");

# canvas.SaveAs("PDFs/comparisons_"+label+"/resolution_etaBins_"+label+".pdf")
# canvas.SaveAs("PNGs/comparisons_"+label+"/resolution_etaBins_"+label+".png")

# del canvas, legend, tex2, tex


# #######
# # ptBins scale

# ptBins_scale_unCalib  = file_unCalib.Get("pt_scale_fctPt")
# ptBins_scale_oldCalib = file_oldCalib.Get("pt_scale_fctPt")
# ptBins_scale_newCalib = file_newCalib.Get("pt_scale_fctPt")

# #define canvas for plotting
# canvas = ROOT.TCanvas("c","c",800,800)
# canvas.SetGrid(10,10);

# #use dummy histogram to define style
# ptBins_scale_unCalib.GetXaxis().SetTitle("p_{T}^{gen jet} [GeV]")
# ptBins_scale_unCalib.SetTitle("")

# ptBins_scale_unCalib.GetXaxis().SetTitleOffset(1.3);
# ptBins_scale_unCalib.GetYaxis().SetTitle("E_{T}^{L1 jet} scale");
# ptBins_scale_unCalib.GetYaxis().SetTitleOffset(1.3);
# ptBins_scale_unCalib.SetTitle("");
# ptBins_scale_unCalib.SetStats(0);

# ptBins_scale_unCalib.GetYaxis().SetRangeUser(0., max(ptBins_scale_oldCalib.GetMaximum(),ptBins_scale_newCalib.GetMaximum())*1.3 )

# ptBins_scale_oldCalib.SetLineWidth(2)
# ptBins_scale_oldCalib.SetMarkerStyle(8)
# ptBins_scale_oldCalib.SetMarkerColor(2)
# ptBins_scale_oldCalib.SetLineColor(2)

# ptBins_scale_newCalib.SetLineWidth(2)
# ptBins_scale_newCalib.SetMarkerStyle(8)
# ptBins_scale_newCalib.SetMarkerColor(3)
# ptBins_scale_newCalib.SetLineColor(3)

# ptBins_scale_unCalib.SetLineWidth(2)
# ptBins_scale_unCalib.SetMarkerStyle(8)
# ptBins_scale_unCalib.SetMarkerColor(1)
# ptBins_scale_unCalib.SetLineColor(1)

# ptBins_scale_unCalib.Draw("LPE")
# ptBins_scale_newCalib.Draw("LPE same")
# ptBins_scale_oldCalib.Draw("LPE same")

# legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
# legend.SetBorderSize(0)
# legend.AddEntry(ptBins_scale_unCalib,"Uncalibrated", "LPE")
# legend.AddEntry(ptBins_scale_oldCalib,"Old Calibration", "LPE")
# legend.AddEntry(ptBins_scale_newCalib,"New Calibration", "LPE")
# legend.Draw("same")

# tex = ROOT.TLatex()
# tex.SetTextSize(0.03);
# tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
# tex.Draw("same")

# tex2 = ROOT.TLatex();
# tex2.SetTextSize(0.035);
# tex2.SetTextAlign(31);
# tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
# tex2.Draw("same");

# canvas.SaveAs("PDFs/comparisons_"+label+"/scale_ptBins_"+label+".pdf")
# canvas.SaveAs("PNGs/comparisons_"+label+"/scale_ptBins_"+label+".png")

# del canvas, legend, tex2, tex

# #######
# # etaBins scale

# etaBins_scale_unCalib  = file_unCalib.Get("pt_scale_fctEta")
# etaBins_scale_oldCalib = file_oldCalib.Get("pt_scale_fctEta")
# etaBins_scale_newCalib = file_newCalib.Get("pt_scale_fctEta")

# #define canvas for plotting
# canvas = ROOT.TCanvas("c","c",800,800)
# canvas.SetGrid(10,10);

# #use dummy histogram to define style
# etaBins_scale_unCalib.GetXaxis().SetTitle("#eta^{gen jet}")
# etaBins_scale_unCalib.SetTitle("")

# etaBins_scale_unCalib.GetXaxis().SetTitleOffset(1.3);
# etaBins_scale_unCalib.GetYaxis().SetTitle("E_{T}^{L1 jet} scale");
# etaBins_scale_unCalib.GetYaxis().SetTitleOffset(1.3);
# etaBins_scale_unCalib.SetTitle("");
# etaBins_scale_unCalib.SetStats(0);

# etaBins_scale_unCalib.GetYaxis().SetRangeUser(0., 2.)

# etaBins_scale_oldCalib.SetLineWidth(2)
# etaBins_scale_oldCalib.SetMarkerStyle(8)
# etaBins_scale_oldCalib.SetMarkerColor(2)
# etaBins_scale_oldCalib.SetLineColor(2)

# etaBins_scale_newCalib.SetLineWidth(2)
# etaBins_scale_newCalib.SetMarkerStyle(8)
# etaBins_scale_newCalib.SetMarkerColor(3)
# etaBins_scale_newCalib.SetLineColor(3)

# etaBins_scale_unCalib.SetLineWidth(2)
# etaBins_scale_unCalib.SetMarkerStyle(8)
# etaBins_scale_unCalib.SetMarkerColor(1)
# etaBins_scale_unCalib.SetLineColor(1)

# etaBins_scale_unCalib.Draw("LPE")
# etaBins_scale_newCalib.Draw("LPE same")
# etaBins_scale_oldCalib.Draw("LPE same")

# b1 = ROOT.TBox(1.305,0.,1.479,2)
# b1.SetFillColor(16)
# b1.Draw("same")
# b2 = ROOT.TBox(-1.479,0.,-1.305,2)
# b2.SetFillColor(16)
# b2.Draw("same")
# b3 = ROOT.TBox(1.305,0.,1.479,2)
# b3.SetFillColor(1)
# b3.SetFillStyle(3004)
# b3.Draw("same")
# b4 = ROOT.TBox(-1.479,0.,-1.305,2)
# b4.SetFillColor(1)
# b4.SetFillStyle(3004)
# b4.Draw("same")

# legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
# legend.SetBorderSize(0)
# legend.AddEntry(etaBins_scale_unCalib,"Uncalibrated", "LPE")
# legend.AddEntry(etaBins_scale_oldCalib,"Old Calibration", "LPE")
# legend.AddEntry(etaBins_scale_newCalib,"New Calibration", "LPE")
# legend.Draw("same")

# tex = ROOT.TLatex()
# tex.SetTextSize(0.03);
# tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
# tex.Draw("same")

# tex2 = ROOT.TLatex();
# tex2.SetTextSize(0.035);
# tex2.SetTextAlign(31);
# tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
# tex2.Draw("same");

# canvas.SaveAs("PDFs/comparisons_"+label+"/scale_etaBins_"+label+".pdf")
# canvas.SaveAs("PNGs/comparisons_"+label+"/scale_etaBins_"+label+".png")

# del canvas, legend, tex2, tex

# #######

# file_unCalib.Close() 
# file_oldCalib.Close() 
# file_newCalib.Close() 


#############################
## RATE COMPARISONS ##

file_unCalib  = ROOT.TFile("ROOTs/rate_graphs_"+detector+"_uncalib.root", "r")
file_oldCalib = ROOT.TFile("ROOTs/rate_graphs_"+detector+"_oldCalib.root", "r")
file_newCalib = ROOT.TFile("ROOTs/rate_graphs_"+detector+"_"+newTag+".root", "r")

if detector == "HCAL":
    #######
    # DoubleJet60 rates

    rateDi_unCalib  = file_unCalib.Get("rateDiProgression0")
    rateDi_oldCalib = file_oldCalib.Get("rateDiProgression0")
    rateDi_newCalib = file_newCalib.Get("rateDiProgression0")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);
    canvas.SetLogy()

    #use dummy histogram to define style
    rateDi_unCalib.GetXaxis().SetTitle("p_{T}^{L1 jet} [GeV]")
    rateDi_unCalib.SetTitle("")

    rateDi_unCalib.GetXaxis().SetTitleOffset(1.3);
    rateDi_unCalib.GetYaxis().SetTitle("Double-Obj Rate [kHz]");
    rateDi_unCalib.GetYaxis().SetTitleOffset(1.3);
    rateDi_unCalib.SetTitle("");
    rateDi_unCalib.SetStats(0);

    rateDi_unCalib.GetYaxis().SetRangeUser(0.1, 1e5)

    rateDi_oldCalib.SetLineWidth(2)
    rateDi_oldCalib.SetMarkerStyle(8)
    rateDi_oldCalib.SetMarkerColor(2)
    rateDi_oldCalib.SetLineColor(2)

    rateDi_newCalib.SetLineWidth(2)
    rateDi_newCalib.SetMarkerStyle(8)
    rateDi_newCalib.SetMarkerColor(3)
    rateDi_newCalib.SetLineColor(3)

    rateDi_unCalib.SetLineWidth(2)
    rateDi_unCalib.SetMarkerStyle(8)
    rateDi_unCalib.SetMarkerColor(1)
    rateDi_unCalib.SetLineColor(1)

    rateDi_unCalib.Draw("LPE")
    rateDi_newCalib.Draw("LPE same")
    rateDi_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(rateDi_unCalib,"Uncalibrated", "LPE")
    legend.AddEntry(rateDi_oldCalib,"Old Calibration", "LPE")
    legend.AddEntry(rateDi_newCalib,"New Calibration", "LPE")
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

    # calculate rates and thresholds
    unCalibAt60 = rateDi_unCalib.GetBinContent(61)
    oldCalibAt60 = rateDi_oldCalib.GetBinContent(61)
    newCalibAt60 = rateDi_newCalib.GetBinContent(61)
    for i in range(1,240):
        if rateDi_newCalib.GetBinContent(i) < oldCalibAt60:
            thrNewCalib_DoubleJet60 = rateDi_newCalib.GetBinLowEdge(i-1)
            break

    for i in range(1,240):
        if rateDi_unCalib.GetBinContent(i) < oldCalibAt60:
            thrUnCalib_DoubleJet60 = rateDi_unCalib.GetBinLowEdge(i-1)
            break

    texl1 = ROOT.TPaveText(0.42,0.52,0.89,0.72,"NDC")
    texl1.AddText("Uncalibrated:      DoubleJet60 rate = "+str(round(unCalibAt60,1))+" kHz")
    texl1.AddText("Old Calibration:  DoubleJet60 rate = "+str(round(oldCalibAt60,1))+" kHz")
    texl1.AddText("New Calibration: DoubleJet60 rate = "+str(round(newCalibAt60,1))+" kHz")
    texl1.AddText("")
    texl1.AddText("Uncalibrated:      fixed "+str(round(oldCalibAt60,1))+" kHz rate #rightarrow DoubleJet"+str(round(thrUnCalib_DoubleJet60)))
    texl1.AddText("New Calibration: fixed "+str(round(oldCalibAt60,1))+" kHz rate #rightarrow DoubleJet"+str(round(thrNewCalib_DoubleJet60)))
    texl1.SetTextSize(0.02)
    texl1.SetFillColor(0)
    texl1.SetBorderSize(0)
    texl1.SetTextAlign(11)
    texl1.Draw("same")

    canvas.SaveAs("PDFs/comparisons_"+label+"/rates_DoubleJet60.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/rates_DoubleJet60.png")

    del canvas, legend, tex2, tex, texl1

    #######
    # DoubleJet60er2p5 rates

    rateDi_unCalib  = file_unCalib.Get("rateDiProgression0er2p5")
    rateDi_oldCalib = file_oldCalib.Get("rateDiProgression0er2p5")
    rateDi_newCalib = file_newCalib.Get("rateDiProgression0er2p5")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);
    canvas.SetLogy()

    #use dummy histogram to define style
    rateDi_unCalib.GetXaxis().SetTitle("p_{T}^{L1 jet} [GeV]")
    rateDi_unCalib.SetTitle("")

    rateDi_unCalib.GetXaxis().SetTitleOffset(1.3);
    rateDi_unCalib.GetYaxis().SetTitle("Double-Obj Rate [kHz]");
    rateDi_unCalib.GetYaxis().SetTitleOffset(1.3);
    rateDi_unCalib.SetTitle("");
    rateDi_unCalib.SetStats(0);

    rateDi_unCalib.GetYaxis().SetRangeUser(0.1, 1e5)

    rateDi_oldCalib.SetLineWidth(2)
    rateDi_oldCalib.SetMarkerStyle(8)
    rateDi_oldCalib.SetMarkerColor(2)
    rateDi_oldCalib.SetLineColor(2)

    rateDi_newCalib.SetLineWidth(2)
    rateDi_newCalib.SetMarkerStyle(8)
    rateDi_newCalib.SetMarkerColor(3)
    rateDi_newCalib.SetLineColor(3)

    rateDi_unCalib.SetLineWidth(2)
    rateDi_unCalib.SetMarkerStyle(8)
    rateDi_unCalib.SetMarkerColor(1)
    rateDi_unCalib.SetLineColor(1)

    rateDi_unCalib.Draw("LPE")
    rateDi_newCalib.Draw("LPE same")
    rateDi_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(rateDi_unCalib,"Uncalibrated", "LPE")
    legend.AddEntry(rateDi_oldCalib,"Old Calibration", "LPE")
    legend.AddEntry(rateDi_newCalib,"New Calibration", "LPE")
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

    # calculate rates and thresholds
    unCalibAt60er2p5 = rateDi_unCalib.GetBinContent(61)
    oldCalibAt60er2p5 = rateDi_oldCalib.GetBinContent(61)
    newCalibAt60er2p5 = rateDi_newCalib.GetBinContent(61)
    for i in range(1,240):
        if rateDi_newCalib.GetBinContent(i) < oldCalibAt60er2p5:
            thrNewCalib_DoubleJet60er2p5 = rateDi_newCalib.GetBinLowEdge(i-1)
            break

    for i in range(1,240):
        if rateDi_unCalib.GetBinContent(i) < oldCalibAt60er2p5:
            thrUnCalib_DoubleJet60er2p5 = rateDi_unCalib.GetBinLowEdge(i-1)
            break

    texl1 = ROOT.TPaveText(0.42,0.52,0.89,0.72,"NDC")
    texl1.AddText("Uncalibrated:      DoubleJet60er2p5 rate = "+str(round(unCalibAt60er2p5,1))+" kHz")
    texl1.AddText("Old Calibration:  DoubleJet60er2p5 rate = "+str(round(oldCalibAt60er2p5,1))+" kHz")
    texl1.AddText("New Calibration: DoubleJet60er2p5 rate = "+str(round(newCalibAt60er2p5,1))+" kHz")
    texl1.AddText("")
    texl1.AddText("Uncalibrated:      fixed "+str(round(oldCalibAt60er2p5,1))+" kHz rate #rightarrow DoubleJet"+str(round(thrUnCalib_DoubleJet60er2p5))+"er2p5")
    texl1.AddText("New Calibration: fixed "+str(round(oldCalibAt60er2p5,1))+" kHz rate #rightarrow DoubleJet"+str(round(thrNewCalib_DoubleJet60er2p5))+"er2p5")
    texl1.SetTextSize(0.02)
    texl1.SetFillColor(0)
    texl1.SetBorderSize(0)
    texl1.SetTextAlign(11)
    texl1.Draw("same")

    canvas.SaveAs("PDFs/comparisons_"+label+"/rates_DoubleJet60er2p5.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/rates_DoubleJet60er2p5.png")

    del canvas, legend, tex2, tex, texl1

    #######
    # DoubleJet100 rates

    rateDi_unCalib  = file_unCalib.Get("rateDiProgression0")
    rateDi_oldCalib = file_oldCalib.Get("rateDiProgression0")
    rateDi_newCalib = file_newCalib.Get("rateDiProgression0")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);
    canvas.SetLogy()

    #use dummy histogram to define style
    rateDi_unCalib.GetXaxis().SetTitle("p_{T}^{L1 jet} [GeV]")
    rateDi_unCalib.SetTitle("")

    rateDi_unCalib.GetXaxis().SetTitleOffset(1.3);
    rateDi_unCalib.GetYaxis().SetTitle("Double-Obj Rate [kHz]");
    rateDi_unCalib.GetYaxis().SetTitleOffset(1.3);
    rateDi_unCalib.SetTitle("");
    rateDi_unCalib.SetStats(0);

    rateDi_unCalib.GetYaxis().SetRangeUser(0.1, 1e5)

    rateDi_oldCalib.SetLineWidth(2)
    rateDi_oldCalib.SetMarkerStyle(8)
    rateDi_oldCalib.SetMarkerColor(2)
    rateDi_oldCalib.SetLineColor(2)

    rateDi_newCalib.SetLineWidth(2)
    rateDi_newCalib.SetMarkerStyle(8)
    rateDi_newCalib.SetMarkerColor(3)
    rateDi_newCalib.SetLineColor(3)

    rateDi_unCalib.SetLineWidth(2)
    rateDi_unCalib.SetMarkerStyle(8)
    rateDi_unCalib.SetMarkerColor(1)
    rateDi_unCalib.SetLineColor(1)

    rateDi_unCalib.Draw("LPE")
    rateDi_newCalib.Draw("LPE same")
    rateDi_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(rateDi_unCalib,"Uncalibrated", "LPE")
    legend.AddEntry(rateDi_oldCalib,"Old Calibration", "LPE")
    legend.AddEntry(rateDi_newCalib,"New Calibration", "LPE")
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

    # calculate rates and thresholds
    unCalibAt100 = rateDi_unCalib.GetBinContent(101)
    oldCalibAt100 = rateDi_oldCalib.GetBinContent(101)
    newCalibAt100 = rateDi_newCalib.GetBinContent(101)
    for i in range(1,240):
        if rateDi_newCalib.GetBinContent(i) < oldCalibAt100:
            thrNewCalib_DoubleJet100 = rateDi_newCalib.GetBinLowEdge(i-1)
            break

    for i in range(1,240):
        if rateDi_unCalib.GetBinContent(i) < oldCalibAt100:
            thrUnCalib_DoubleJet100 = rateDi_unCalib.GetBinLowEdge(i-1)
            break

    texl1 = ROOT.TPaveText(0.42,0.52,0.89,0.72,"NDC")
    texl1.AddText("Uncalibrated:      DoubleJet100 rate = "+str(round(unCalibAt100,1))+" kHz")
    texl1.AddText("Old Calibration:  DoubleJet100 rate = "+str(round(oldCalibAt100,1))+" kHz")
    texl1.AddText("New Calibration: DoubleJet100 rate = "+str(round(newCalibAt100,1))+" kHz")
    texl1.AddText("")
    texl1.AddText("Uncalibrated:      fixed "+str(round(oldCalibAt100,1))+" kHz rate #rightarrow DoubleJet"+str(round(thrUnCalib_DoubleJet100)))
    texl1.AddText("New Calibration: fixed "+str(round(oldCalibAt100,1))+" kHz rate #rightarrow DoubleJet"+str(round(thrNewCalib_DoubleJet100)))
    texl1.SetTextSize(0.02)
    texl1.SetFillColor(0)
    texl1.SetBorderSize(0)
    texl1.SetTextAlign(11)
    texl1.Draw("same")

    canvas.SaveAs("PDFs/comparisons_"+label+"/rates_DoubleJet100.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/rates_DoubleJet100.png")

    del canvas, legend, tex2, tex, texl1


    #######
    # SingleJet60 rates

    rate_unCalib  = file_unCalib.Get("rateProgression0")
    rate_oldCalib = file_oldCalib.Get("rateProgression0")
    rate_newCalib = file_newCalib.Get("rateProgression0")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);
    canvas.SetLogy()

    #use dummy histogram to define style
    rate_unCalib.GetXaxis().SetTitle("p_{T}^{L1 jet} [GeV]")
    rate_unCalib.SetTitle("")

    rate_unCalib.GetXaxis().SetTitleOffset(1.3);
    rate_unCalib.GetYaxis().SetTitle("Single-Obj Rate [kHz]");
    rate_unCalib.GetYaxis().SetTitleOffset(1.3);
    rate_unCalib.SetTitle("");
    rate_unCalib.SetStats(0);

    rate_unCalib.GetYaxis().SetRangeUser(0.1, 1e5)

    rate_oldCalib.SetLineWidth(2)
    rate_oldCalib.SetMarkerStyle(8)
    rate_oldCalib.SetMarkerColor(2)
    rate_oldCalib.SetLineColor(2)

    rate_newCalib.SetLineWidth(2)
    rate_newCalib.SetMarkerStyle(8)
    rate_newCalib.SetMarkerColor(3)
    rate_newCalib.SetLineColor(3)

    rate_unCalib.SetLineWidth(2)
    rate_unCalib.SetMarkerStyle(8)
    rate_unCalib.SetMarkerColor(1)
    rate_unCalib.SetLineColor(1)

    rate_unCalib.Draw("LPE")
    rate_newCalib.Draw("LPE same")
    rate_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(rate_unCalib,"Uncalibrated", "LPE")
    legend.AddEntry(rate_oldCalib,"Old Calibration", "LPE")
    legend.AddEntry(rate_newCalib,"New Calibration", "LPE")
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

    # calculate rates and thresholds
    unCalibAt60 = rate_unCalib.GetBinContent(61)
    oldCalibAt60 = rate_oldCalib.GetBinContent(61)
    newCalibAt60 = rate_newCalib.GetBinContent(61)
    for i in range(1,240):
        if rate_newCalib.GetBinContent(i) < oldCalibAt60:
            thrNewCalib_SingleJet60 = rate_newCalib.GetBinLowEdge(i-1)
            break

    for i in range(1,240):
        if rate_unCalib.GetBinContent(i) < oldCalibAt60:
            thrUnCalib_SingleJet60 = rate_unCalib.GetBinLowEdge(i-1)
            break

    texl1 = ROOT.TPaveText(0.42,0.52,0.89,0.72,"NDC")
    texl1.AddText("Uncalibrated:      SingleJet60 rate = "+str(round(unCalibAt60,1))+" kHz")
    texl1.AddText("Old Calibration:  SingleJet60 rate = "+str(round(oldCalibAt60,1))+" kHz")
    texl1.AddText("New Calibration: SingleJet60 rate = "+str(round(newCalibAt60,1))+" kHz")
    texl1.AddText("")
    texl1.AddText("Uncalibrated:      fixed "+str(round(oldCalibAt60,1))+" kHz rate #rightarrow SingleJet"+str(int(round(thrUnCalib_SingleJet60))))
    texl1.AddText("New Calibration: fixed "+str(round(oldCalibAt60,1))+" kHz rate #rightarrow SingleJet"+str(int(round(thrNewCalib_SingleJet60))))
    texl1.SetTextSize(0.02)
    texl1.SetFillColor(0)
    texl1.SetBorderSize(0)
    texl1.SetTextAlign(11)
    texl1.Draw("same")

    canvas.SaveAs("PDFs/comparisons_"+label+"/rates_SingleJet60.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/rates_SingleJet60.png")

    del canvas, legend, tex2, tex, texl1

if detector == "ECAL":
    #######
    # SingleEG32er2p5 rates

    rate_unCalib  = file_unCalib.Get("rateProgression0er2p5")
    rate_oldCalib = file_oldCalib.Get("rateProgression0er2p5")
    rate_newCalib = file_newCalib.Get("rateProgression0er2p5")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);
    canvas.SetLogy()

    #use dummy histogram to define style
    rate_unCalib.GetXaxis().SetTitle("p_{T}^{L1 jet} [GeV]")
    rate_unCalib.SetTitle("")

    rate_unCalib.GetXaxis().SetTitleOffset(1.3);
    rate_unCalib.GetYaxis().SetTitle("Single-Obj Rate [kHz]");
    rate_unCalib.GetYaxis().SetTitleOffset(1.3);
    rate_unCalib.SetTitle("");
    rate_unCalib.SetStats(0);

    rate_unCalib.GetXaxis().SetRangeUser(0., 80.)
    rate_unCalib.GetYaxis().SetRangeUser(0.1, 1e5)

    rate_oldCalib.SetLineWidth(2)
    rate_oldCalib.SetMarkerStyle(8)
    rate_oldCalib.SetMarkerColor(2)
    rate_oldCalib.SetLineColor(2)

    rate_newCalib.SetLineWidth(2)
    rate_newCalib.SetMarkerStyle(8)
    rate_newCalib.SetMarkerColor(3)
    rate_newCalib.SetLineColor(3)

    rate_unCalib.SetLineWidth(2)
    rate_unCalib.SetMarkerStyle(8)
    rate_unCalib.SetMarkerColor(1)
    rate_unCalib.SetLineColor(1)

    rate_unCalib.Draw("LPE")
    rate_newCalib.Draw("LPE same")
    rate_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(rate_unCalib,"Uncalibrated", "LPE")
    legend.AddEntry(rate_oldCalib,"Old Calibration", "LPE")
    legend.AddEntry(rate_newCalib,"New Calibration", "LPE")
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

    # calculate rates and thresholds
    unCalibAt32 = rate_unCalib.GetBinContent(33)
    oldCalibAt32 = rate_oldCalib.GetBinContent(33)
    newCalibAt32 = rate_newCalib.GetBinContent(33)
    for i in range(1,240):
        if rate_newCalib.GetBinContent(i) < oldCalibAt32:
            thrNewCalib_SingleEG32er2p5 = rate_newCalib.GetBinLowEdge(i-1)
            break

    for i in range(1,240):
        if rate_unCalib.GetBinContent(i) < oldCalibAt32:
            thrUnCalib_SingleEG32er2p5 = rate_unCalib.GetBinLowEdge(i-1)
            break

    texl1 = ROOT.TPaveText(0.42,0.52,0.89,0.72,"NDC")
    texl1.AddText("Uncalibrated:      SingleEG32er2p5 rate = "+str(round(unCalibAt32,1))+" kHz")
    texl1.AddText("Old Calibration:  SingleEG32er2p5 rate = "+str(round(oldCalibAt32,1))+" kHz")
    texl1.AddText("New Calibration: SingleEG32er2p5 rate = "+str(round(newCalibAt32,1))+" kHz")
    texl1.AddText("")
    texl1.AddText("Uncalibrated:      fixed "+str(round(oldCalibAt32,1))+" kHz rate #rightarrow SingleEG"+str(int(round(thrUnCalib_SingleEG32er2p5)))+"er2p5")
    texl1.AddText("New Calibration: fixed "+str(round(oldCalibAt32,1))+" kHz rate #rightarrow SingleEG"+str(int(round(thrNewCalib_SingleEG32er2p5)))+"er2p5")
    texl1.SetTextSize(0.02)
    texl1.SetFillColor(0)
    texl1.SetBorderSize(0)
    texl1.SetTextAlign(11)
    texl1.Draw("same")

    canvas.SaveAs("PDFs/comparisons_"+label+"/rates_SingleEG32er2p5.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/rates_SingleEG32er2p5.png")

    del canvas, legend, tex2, tex, texl1

file_unCalib.Close()
file_oldCalib.Close()
file_newCalib.Close()


#############################
## TURNON COMPARISONS ##

file_unCalib  = ROOT.TFile("ROOTs/efficiency_graphs_"+detector+"_uncalib.root", "r")
file_oldCalib = ROOT.TFile("ROOTs/efficiency_graphs_"+detector+"_oldCalib.root", "r")
file_newCalib = ROOT.TFile("ROOTs/efficiency_graphs_"+detector+"_"+newTag+".root", "r")

if detector == 'HCAL':
    #######
    # DoubleJet60 turnons

    turnon_unCalib  = file_unCalib.Get("divide_passing"+str(int(round(thrUnCalib_DoubleJet60)))+"_by_total")
    turnon_oldCalib = file_oldCalib.Get("divide_passing"+str(int(round(60)))+"_by_total")
    turnon_newCalib = file_newCalib.Get("divide_passing"+str(int(round(thrNewCalib_DoubleJet60)))+"_by_total")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);

    #use dummy histogram to define style
    turnon_unCalib.GetXaxis().SetTitle("p_{T}^{gen jet} [GeV]")
    turnon_unCalib.SetTitle("")

    turnon_unCalib.GetXaxis().SetTitleOffset(1.3);
    turnon_unCalib.GetYaxis().SetTitle("Efficiency");
    turnon_unCalib.GetYaxis().SetTitleOffset(1.3);
    turnon_unCalib.SetTitle("");

    turnon_unCalib.GetXaxis().SetRangeUser(0.,250.);
    turnon_unCalib.GetYaxis().SetRangeUser(0.,1.3);

    turnon_oldCalib.SetMarkerStyle(8)
    turnon_oldCalib.SetMarkerColor(2)
    turnon_oldCalib.SetLineColor(2)

    turnon_newCalib.SetMarkerStyle(8)
    turnon_newCalib.SetMarkerColor(3)
    turnon_newCalib.SetLineColor(3)

    turnon_unCalib.SetMarkerStyle(8)
    turnon_unCalib.SetMarkerColor(1)
    turnon_unCalib.SetLineColor(1)

    turnon_unCalib.Draw()
    turnon_newCalib.Draw("LPE same")
    turnon_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(turnon_unCalib,"Uncalibrated: p_{T}^{L1 jet}>"+str(int(round(thrUnCalib_DoubleJet60)))+" GeV", "LPE")
    legend.AddEntry(turnon_oldCalib,"Old Calibration: p_{T}^{L1 jet}>"+str(int(round(60)))+" GeV", "LPE")
    legend.AddEntry(turnon_newCalib,"New Calibration: p_{T}^{L1 jet}>"+str(int(round(thrNewCalib_DoubleJet60)))+" GeV", "LPE")
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

    canvas.SaveAs("PDFs/comparisons_"+label+"/turnons_DoubleJet60.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/turnons_DoubleJet60.png")

    del canvas, legend, tex2, tex

    #######
    # DoubleJet60er2p5 turnons

    turnon_unCalib  = file_unCalib.Get("divide_passing"+str(int(round(thrUnCalib_DoubleJet60er2p5)))+"_by_total")
    turnon_oldCalib = file_oldCalib.Get("divide_passing"+str(int(round(60)))+"_by_total")
    turnon_newCalib = file_newCalib.Get("divide_passing"+str(int(round(thrNewCalib_DoubleJet60er2p5)))+"_by_total")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);

    #use dummy histogram to define style
    turnon_unCalib.GetXaxis().SetTitle("p_{T}^{gen jet} [GeV]")
    turnon_unCalib.SetTitle("")

    turnon_unCalib.GetXaxis().SetTitleOffset(1.3);
    turnon_unCalib.GetYaxis().SetTitle("Efficiency");
    turnon_unCalib.GetYaxis().SetTitleOffset(1.3);
    turnon_unCalib.SetTitle("");

    turnon_unCalib.GetXaxis().SetRangeUser(0.,250.);
    turnon_unCalib.GetYaxis().SetRangeUser(0.,1.3);

    turnon_oldCalib.SetMarkerStyle(8)
    turnon_oldCalib.SetMarkerColor(2)
    turnon_oldCalib.SetLineColor(2)

    turnon_newCalib.SetMarkerStyle(8)
    turnon_newCalib.SetMarkerColor(3)
    turnon_newCalib.SetLineColor(3)

    turnon_unCalib.SetMarkerStyle(8)
    turnon_unCalib.SetMarkerColor(1)
    turnon_unCalib.SetLineColor(1)

    turnon_unCalib.Draw()
    turnon_newCalib.Draw("LPE same")
    turnon_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(turnon_unCalib,"Uncalibrated: p_{T}^{L1 jet}>"+str(int(round(thrUnCalib_DoubleJet60er2p5)))+" GeV", "LPE")
    legend.AddEntry(turnon_oldCalib,"Old Calibration: p_{T}^{L1 jet}>"+str(int(round(60)))+" GeV", "LPE")
    legend.AddEntry(turnon_newCalib,"New Calibration: p_{T}^{L1 jet}>"+str(int(round(thrNewCalib_DoubleJet60er2p5)))+" GeV", "LPE")
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

    canvas.SaveAs("PDFs/comparisons_"+label+"/turnons_DoubleJet60er2p5.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/turnons_DoubleJet60er2p5.png")

    del canvas, legend, tex2, tex

    #######
    # DoubleJet100 turnons

    turnon_unCalib  = file_unCalib.Get("divide_passing"+str(int(round(thrUnCalib_DoubleJet100)))+"_by_total")
    turnon_oldCalib = file_oldCalib.Get("divide_passing"+str(int(round(100)))+"_by_total")
    turnon_newCalib = file_newCalib.Get("divide_passing"+str(int(round(thrNewCalib_DoubleJet100)))+"_by_total")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);

    #use dummy histogram to define style
    turnon_unCalib.GetXaxis().SetTitle("p_{T}^{gen jet} [GeV]")
    turnon_unCalib.SetTitle("")

    turnon_unCalib.GetXaxis().SetTitleOffset(1.3);
    turnon_unCalib.GetYaxis().SetTitle("Efficiency");
    turnon_unCalib.GetYaxis().SetTitleOffset(1.3);
    turnon_unCalib.SetTitle("");

    turnon_unCalib.GetXaxis().SetRangeUser(0.,250.);
    turnon_unCalib.GetYaxis().SetRangeUser(0.,1.3);

    turnon_oldCalib.SetMarkerStyle(8)
    turnon_oldCalib.SetMarkerColor(2)
    turnon_oldCalib.SetLineColor(2)

    turnon_newCalib.SetMarkerStyle(8)
    turnon_newCalib.SetMarkerColor(3)
    turnon_newCalib.SetLineColor(3)

    turnon_unCalib.SetMarkerStyle(8)
    turnon_unCalib.SetMarkerColor(1)
    turnon_unCalib.SetLineColor(1)

    turnon_unCalib.Draw()
    turnon_newCalib.Draw("LPE same")
    turnon_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(turnon_unCalib,"Uncalibrated: p_{T}^{L1 jet}>"+str(int(round(thrUnCalib_DoubleJet100)))+" GeV", "LPE")
    legend.AddEntry(turnon_oldCalib,"Old Calibration: p_{T}^{L1 jet}>"+str(int(round(100)))+" GeV", "LPE")
    legend.AddEntry(turnon_newCalib,"New Calibration: p_{T}^{L1 jet}>"+str(int(round(thrNewCalib_DoubleJet100)))+" GeV", "LPE")
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

    canvas.SaveAs("PDFs/comparisons_"+label+"/turnons_DoubleJet100.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/turnons_DoubleJet100.png")

    del canvas, legend, tex2, tex

if detector == "ECAL":
    #######
    # SingleEG32er2p5 turnons

    turnon_unCalib  = file_unCalib.Get("divide_passing"+str(int(round(thrUnCalib_SingleEG32er2p5)))+"_by_total")
    turnon_oldCalib = file_oldCalib.Get("divide_passing"+str(int(round(32)))+"_by_total")
    turnon_newCalib = file_newCalib.Get("divide_passing"+str(int(round(thrNewCalib_SingleEG32er2p5)))+"_by_total")

    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);

    #use dummy histogram to define style
    turnon_unCalib.GetXaxis().SetTitle("p_{T}^{gen jet} [GeV]")
    turnon_unCalib.SetTitle("")

    turnon_unCalib.GetXaxis().SetTitleOffset(1.3);
    turnon_unCalib.GetYaxis().SetTitle("Efficiency");
    turnon_unCalib.GetYaxis().SetTitleOffset(1.3);
    turnon_unCalib.SetTitle("");

    turnon_unCalib.GetXaxis().SetRangeUser(0.,250.);
    turnon_unCalib.GetYaxis().SetRangeUser(0.,1.3);

    turnon_oldCalib.SetMarkerStyle(8)
    turnon_oldCalib.SetMarkerColor(2)
    turnon_oldCalib.SetLineColor(2)

    turnon_newCalib.SetMarkerStyle(8)
    turnon_newCalib.SetMarkerColor(3)
    turnon_newCalib.SetLineColor(3)

    turnon_unCalib.SetMarkerStyle(8)
    turnon_unCalib.SetMarkerColor(1)
    turnon_unCalib.SetLineColor(1)

    turnon_unCalib.Draw()
    turnon_newCalib.Draw("LPE same")
    turnon_oldCalib.Draw("LPE same")

    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(turnon_unCalib,"Uncalibrated: p_{T}^{L1 jet}>"+str(int(round(thrUnCalib_SingleEG32er2p5)))+" GeV", "LPE")
    legend.AddEntry(turnon_oldCalib,"Old Calibration: p_{T}^{L1 jet}>"+str(int(round(32)))+" GeV", "LPE")
    legend.AddEntry(turnon_newCalib,"New Calibration: p_{T}^{L1 jet}>"+str(int(round(thrNewCalib_SingleEG32er2p5)))+" GeV", "LPE")
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

    canvas.SaveAs("PDFs/comparisons_"+label+"/turnons_SingleEG32er2p5.pdf")
    canvas.SaveAs("PNGs/comparisons_"+label+"/turnons_SingleEG32er2p5.png")

    del canvas, legend, tex2, tex

file_unCalib.Close()
file_oldCalib.Close()
file_newCalib.Close()
































