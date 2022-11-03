from array import array
import ROOT
import sys
import os

#print('cmd entry:', sys.argv)

#reading input parameters
directory = sys.argv[1]
nevents = int(sys.argv[2])
label = sys.argv[3]
outdir = sys.argv[4]

os.system('mkdir -p '+outdir+'/PDFs/'+label)
os.system('mkdir -p '+outdir+'/PNGs/'+label)
os.system('mkdir -p '+outdir+'/ROOTs/')

print("defining input trees")
eventTree = ROOT.TChain("l1EventTree/L1EventTree")
genTree = ROOT.TChain("l1GeneratorTree/L1GenTree")
emuTree = ROOT.TChain("l1UpgradeEmuTree/L1UpgradeTree")

print("reading input files")
eventTree.Add(directory + "/Ntuple*.root")
genTree.Add(directory + "/Ntuple*.root")
emuTree.Add(directory + "/Ntuple*.root")

print("getting entries")
nEntries = eventTree.GetEntries()

#run on entries specified by usuer, or only on entries available if that is exceeded
if (nevents > nEntries) or (nevents==-1): nevents = nEntries
print("will process",nevents,"events...")

denominator = 0.
nb = 2544.
scale = 0.001*(nb*11245.6)

etaBinsAsTT = array("d", [0., 0.087, 0.174, 0.261, 0.348, 0.435, 0.522, 0.609, 0.696, 0.783, 0.870, 0.957, 1.044, 1.131, 1.218, 1.305, 1.392, 1.479, 1.566, 1.653, 1.740, 1.830, 1.930, 2.043, 2.172, 2.322, 2.5, 2.650, 3., 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889, 5.191])

#dummy histogram for plotting
empty = ROOT.TH1F("empty","empty",240,0.,240.)
empty1 = ROOT.TH1F("empty1","empty1",len(etaBinsAsTT)-1,etaBinsAsTT)

ptProgression = ROOT.TH1F("ptProgression","ptProgression",240,0.,240.)
ptDiProgression = ROOT.TH2F("ptDiProgression","ptDiProgression",240,0.,240.,240,0.,240.)
etaProgression = ROOT.TH1F("etaProgression","eatProgression",len(etaBinsAsTT)-1,etaBinsAsTT)
etaDiProgression = ROOT.TH2F("etaDiProgression","eatDiProgression",len(etaBinsAsTT)-1,etaBinsAsTT,len(etaBinsAsTT)-1,etaBinsAsTT)
ratePtProgression = ROOT.TH1F("ratePtProgression","ratePtProgression",240,0.,240.)
ratePtDiProgression = ROOT.TH1F("ratePtDiProgression","ratePtDiProgression",240,0.,240.)
rateEtaProgression = ROOT.TH1F("rateEtaProgression","rateEtaProgression",len(etaBinsAsTT)-1,etaBinsAsTT)
rateEtaDiProgression = ROOT.TH1F("rateEtaDiProgression","rateEtaDiProgression",len(etaBinsAsTT)-1,etaBinsAsTT)
ptVsEtaProgression = ROOT.TH2F("ptVsEtaProgression","ptVsEtaProgression",240,0.,240.,len(etaBinsAsTT)-1,etaBinsAsTT)
ratePtVsEtaProgression = ROOT.TH2F("ratePtVsEtaProgression","ratePtVsEtaProgression",240,0.,240.,len(etaBinsAsTT)-1,etaBinsAsTT)

ptProgressionEr = ROOT.TH1F("ptProgressionEr","ptProgressionEr",240,0.,240.)
ptDiProgressionEr = ROOT.TH2F("ptDiProgressionEr","ptDiProgressionEr",240,0.,240.,240,0.,240.)
etaProgressionEr = ROOT.TH1F("etaProgressionEr","eatProgressionEr",len(etaBinsAsTT)-1,etaBinsAsTT)
etaDiProgressionEr = ROOT.TH2F("etaDiProgressionEr","eatDiProgressionEr",len(etaBinsAsTT)-1,etaBinsAsTT,len(etaBinsAsTT)-1,etaBinsAsTT)
ratePtProgressionEr = ROOT.TH1F("ratePtProgressionEr","ratePtProgressionEr",240,0.,240.)
ratePtDiProgressionEr = ROOT.TH1F("ratePtDiProgressionEr","ratePtDiProgressionEr",240,0.,240.)
rateEtaProgressionEr = ROOT.TH1F("rateEtaProgressionEr","rateEtaProgressionEr",len(etaBinsAsTT)-1,etaBinsAsTT)
rateEtaDiProgressionEr = ROOT.TH1F("rateEtaDiProgressionEr","rateEtaDiProgressionEr",len(etaBinsAsTT)-1,etaBinsAsTT)
ptVsEtaProgressionEr = ROOT.TH2F("ptVsEtaProgressionEr","ptVsEtaProgressionEr",240,0.,240.,len(etaBinsAsTT)-1,etaBinsAsTT)
ratePtVsEtaProgressionEr = ROOT.TH2F("ratePtVsEtaProgressionEr","ratePtVsEtaProgressionEr",240,0.,240.,len(etaBinsAsTT)-1,etaBinsAsTT)

etaPlotLim = 5.191
if "ECAL_" in label: etaPlotLim = 3.

etaRestictedLim = 1.479

print("looping on events")
for i in range(0, nevents):
    if i%1000==0: print(i)
    #getting entries
    entry = eventTree.GetEntry(i)
    entry2 = emuTree.GetEntry(i)
    entry3 = genTree.GetEntry(i)

    # restrict to nominal lumiPOG 47 PU +-5
    # (this distribution will be very unrealistic!! Need to "gaussianize it")
    #if eventTree.Event.nPV_True < 42 or eventTree.Event.nPV_True > 52: continue

    denominator += 1.

    filledProgression  = False
    filledProgressionEr  = False

    IndexOBJsProgression = array('f',[-1,-1])
    ptOBJsProgression = array('f',[-99.,-99.])
    etaOBJsProgression = array('f',[-99.,-99.])

    IndexOBJsProgressionEr = array('f',[-1,-1])
    ptOBJsProgressionEr = array('f',[-99.,-99.])
    etaOBJsProgressionEr = array('f',[-99.,-99.])

    L1_nOBJs = 0
    if "HCAL_" in label: L1_nOBJs = emuTree.L1Upgrade.nJets
    if "ECAL_" in label: L1_nOBJs = emuTree.L1Upgrade.nEGs

    #loop on L1 jets to find match
    for iOBJ in range(0, L1_nOBJs):

        L1_obj = ROOT.TLorentzVector()    
        if "HCAL_" in label: L1_obj.SetPtEtaPhiM(emuTree.L1Upgrade.jetEt[iOBJ], emuTree.L1Upgrade.jetEta[iOBJ], emuTree.L1Upgrade.jetPhi[iOBJ], 0)
        if "ECAL_" in label: L1_obj.SetPtEtaPhiM(emuTree.L1Upgrade.egEt[iOBJ], emuTree.L1Upgrade.egEta[iOBJ], emuTree.L1Upgrade.egPhi[iOBJ], 0)

        # single
        if filledProgression==False:
            ptProgression.Fill(L1_obj.Pt())
            etaProgression.Fill(abs(L1_obj.Eta()))
            ptVsEtaProgression.Fill(L1_obj.Pt(),abs(L1_obj.Eta()))
            filledProgression = True

        # di
        if L1_obj.Pt()>=ptOBJsProgression[0]:
            IndexOBJsProgression[1]=IndexOBJsProgression[0]
            ptOBJsProgression[1]=ptOBJsProgression[0]
            etaOBJsProgression[1]=etaOBJsProgression[0]
            IndexOBJsProgression[0]=iOBJ
            ptOBJsProgression[0]=L1_obj.Pt()
            etaOBJsProgression[0]=abs(L1_obj.Eta())
        elif L1_obj.Pt()>=ptOBJsProgression[1]:
            IndexOBJsProgression[1]=iOBJ
            ptOBJsProgression[1]=L1_obj.Pt()
            etaOBJsProgression[1]=abs(L1_obj.Eta())

        if abs(L1_obj.Eta()) >= etaRestictedLim: continue

        # single
        if filledProgressionEr==False:
            ptProgressionEr.Fill(L1_obj.Pt())
            etaProgressionEr.Fill(abs(L1_obj.Eta()))
            ptVsEtaProgressionEr.Fill(L1_obj.Pt(),abs(L1_obj.Eta()))
            filledProgressionEr = True

        # di
        if L1_obj.Pt()>=ptOBJsProgressionEr[0]:
            IndexOBJsProgressionEr[1]=IndexOBJsProgressionEr[0]
            ptOBJsProgressionEr[1]=ptOBJsProgressionEr[0]
            etaOBJsProgressionEr[1]=etaOBJsProgressionEr[0]
            IndexOBJsProgressionEr[0]=iOBJ
            ptOBJsProgressionEr[0]=L1_obj.Pt()
            etaOBJsProgressionEr[0]=abs(L1_obj.Eta())
        elif L1_obj.Pt()>=ptOBJsProgressionEr[1]:
            IndexOBJsProgressionEr[1]=iOBJ
            ptOBJsProgressionEr[1]=L1_obj.Pt()
            etaOBJsProgressionEr[1]=abs(L1_obj.Eta())
        
    if IndexOBJsProgression[0]>=0 and IndexOBJsProgression[1]>=0:
        ptDiProgression.Fill(ptOBJsProgression[0],ptOBJsProgression[1])
        etaDiProgression.Fill(etaOBJsProgression[0],etaOBJsProgression[1])

    if IndexOBJsProgressionEr[0]>=0 and IndexOBJsProgressionEr[1]>=0:
        ptDiProgressionEr.Fill(ptOBJsProgressionEr[0],ptOBJsProgressionEr[1])
        etaDiProgressionEr.Fill(etaOBJsProgressionEr[0],etaOBJsProgressionEr[1])
    


for i in range(0,241):
    ratePtProgression.SetBinContent(i+1,ptProgression.Integral(i+1,241)/denominator*scale);
    ratePtDiProgression.SetBinContent(i+1,ptDiProgression.Integral(i+1,241,i+1,241)/denominator*scale);

for i in range(0,len(etaBinsAsTT)):
    rateEtaProgression.SetBinContent(i+1,etaProgression.GetBinContent(i+1)/denominator*scale);
    rateEtaDiProgression.SetBinContent(i+1,etaDiProgression.GetBinContent(i+1,i+1)/denominator*scale);
    
for i in range(0,241):
    for j in range(0,len(etaBinsAsTT)):
        ratePtVsEtaProgression.SetBinContent(i+1,j+1,ptVsEtaProgression.Integral(i+1,241,j+1,j+1)/denominator*scale)

for i in range(0,241):
    ratePtProgressionEr.SetBinContent(i+1,ptProgressionEr.Integral(i+1,241)/denominator*scale);
    ratePtDiProgressionEr.SetBinContent(i+1,ptDiProgressionEr.Integral(i+1,241,i+1,241)/denominator*scale);

for i in range(0,len(etaBinsAsTT)):
    rateEtaProgressionEr.SetBinContent(i+1,etaProgressionEr.GetBinContent(i+1)/denominator*scale);
    rateEtaDiProgressionEr.SetBinContent(i+1,etaDiProgressionEr.GetBinContent(i+1,i+1)/denominator*scale);
    
for i in range(0,241):
    for j in range(0,len(etaBinsAsTT)):
        ratePtVsEtaProgressionEr.SetBinContent(i+1,j+1,ptVsEtaProgressionEr.Integral(i+1,241,j+1,j+1)/denominator*scale)


####################

ROOT.gStyle.SetOptStat(000000)

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
empty.SetTitle("")
empty.GetXaxis().SetRangeUser(0.,240.);
empty.GetYaxis().SetRangeUser(0.1,1e5);
empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("Rate [kHz]");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);
empty.Draw()

ratePtProgression.SetLineWidth(2)
ratePtProgression.SetMarkerColor(1)
ratePtProgression.SetLineColor(1)
ratePtProgression.Draw("same")

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(ratePtProgression,"Single-Obj rate","LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPt_SingleObj_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPt_SingleObj_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("#eta^{L1}")
empty1.SetTitle("")
empty1.GetXaxis().SetRangeUser(0.,etaPlotLim);
empty1.GetYaxis().SetRangeUser(0.1,1e5);
empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

rateEtaProgression.SetLineWidth(2)
rateEtaProgression.SetMarkerColor(1)
rateEtaProgression.SetLineColor(1)
rateEtaProgression.Draw("same")

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaProgression,"Single-Obj rate","LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsEta_SingleObj_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsEta_SingleObj_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c1","c1",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
empty.SetTitle("")
empty.GetXaxis().SetRangeUser(0.,240.);
empty.GetYaxis().SetRangeUser(0.1,1e5);
empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("Rate [kHz]");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);
empty.Draw()

ratePtDiProgression.SetLineWidth(2)
ratePtDiProgression.SetMarkerColor(1)
ratePtDiProgression.SetLineColor(1)
ratePtDiProgression.Draw("same")

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(ratePtDiProgression,"Di-Obj rate","LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPt_DiObj_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPt_DiObj_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c1","c1",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("#eta^{L1}")
empty1.SetTitle("")
empty1.GetXaxis().SetRangeUser(0.,etaPlotLim);
empty1.GetYaxis().SetRangeUser(0.1,1e5);
empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

rateEtaDiProgression.SetLineWidth(2)
rateEtaDiProgression.SetMarkerColor(1)
rateEtaDiProgression.SetLineColor(1)
rateEtaDiProgression.Draw("same")

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaDiProgression,"Di-Obj rate","LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPt_DiObj_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPt_DiObj_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c2","c2",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
empty.SetTitle("")
empty.GetXaxis().SetRangeUser(0.,240.);
empty.GetYaxis().SetRangeUser(0.1,1e5);
empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("Rate [kHz]");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);
empty.Draw()

ratePtProgression.SetLineWidth(2)
ratePtProgression.SetMarkerColor(1)
ratePtProgression.SetLineColor(1)
ratePtProgression.Draw("same")

ratePtDiProgression.SetLineWidth(2)
ratePtDiProgression.SetMarkerColor(2)
ratePtDiProgression.SetLineColor(2)
ratePtDiProgression.Draw("same")

legend = ROOT.TLegend(0.60,0.81,0.88,0.89)
legend.SetBorderSize(0)
legend.AddEntry(ratePtProgression,"Single-Obj rate","LPE")
legend.AddEntry(ratePtDiProgression,"Di-Obj rate","LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPt_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPt_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c2","c2",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("#eta^{L1}")
empty1.SetTitle("")
empty1.GetXaxis().SetRangeUser(0.,etaPlotLim);
empty1.GetYaxis().SetRangeUser(0.1,1e5);
empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

rateEtaProgression.SetLineWidth(2)
rateEtaProgression.SetMarkerColor(1)
rateEtaProgression.SetLineColor(1)
rateEtaProgression.Draw("same")

rateEtaDiProgression.SetLineWidth(2)
rateEtaDiProgression.SetMarkerColor(2)
rateEtaDiProgression.SetLineColor(2)
rateEtaDiProgression.Draw("same")

legend = ROOT.TLegend(0.60,0.81,0.88,0.89)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaProgression,"Single-Obj rate","LPE")
legend.AddEntry(rateEtaDiProgression,"Di-Obj rate","LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsEta_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsEta_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c2","c2",900,800)
canvas.SetRightMargin(0.175);
canvas.SetLeftMargin(0.1);
canvas.SetGrid(10,10);
canvas.SetLogz()

#use dummy histogram to define style
ratePtVsEtaProgression.SetTitle("")
ratePtVsEtaProgression.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
ratePtVsEtaProgression.GetYaxis().SetTitle("#eta^{L1}")
ratePtVsEtaProgression.GetZaxis().SetTitle("Rate [kHz]");
ratePtVsEtaProgression.GetXaxis().SetRangeUser(0.,240.);
ratePtVsEtaProgression.GetYaxis().SetRangeUser(0.,etaPlotLim);
ratePtVsEtaProgression.GetXaxis().SetTitleOffset(1.3);
ratePtVsEtaProgression.GetZaxis().SetTitleOffset(1.7);
ratePtVsEtaProgression.SetContour(256)
ratePtVsEtaProgression.Draw("colz same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.1,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.82,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPtVsEta_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPtVsEta_"+label+".png")

del canvas, tex, tex2

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
empty.SetTitle("")
empty.GetXaxis().SetRangeUser(0.,240.);
empty.GetYaxis().SetRangeUser(0.1,1e5);
empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("Rate [kHz]");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);
empty.Draw()

ratePtProgressionEr.SetLineWidth(2)
ratePtProgressionEr.SetMarkerColor(1)
ratePtProgressionEr.SetLineColor(1)
ratePtProgressionEr.Draw("same")

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(ratePtProgressionEr,"Single-Obj rate |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPt_SingleObjEr_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPt_SingleObj_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("#eta^{L1}")
empty1.SetTitle("")
empty1.GetXaxis().SetRangeUser(0.,etaRestictedLim);
empty1.GetYaxis().SetRangeUser(0.1,1e5);
empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

rateEtaProgressionEr.SetLineWidth(2)
rateEtaProgressionEr.SetMarkerColor(1)
rateEtaProgressionEr.SetLineColor(1)
rateEtaProgressionEr.Draw("same")

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaProgressionEr,"Single-Obj rate |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsEta_SingleObjEr_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsEta_SingleObj_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c1","c1",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
empty.SetTitle("")
empty.GetXaxis().SetRangeUser(0.,240.);
empty.GetYaxis().SetRangeUser(0.1,1e5);
empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("Rate [kHz]");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);
empty.Draw()

ratePtDiProgressionEr.SetLineWidth(2)
ratePtDiProgressionEr.SetMarkerColor(1)
ratePtDiProgressionEr.SetLineColor(1)
ratePtDiProgressionEr.Draw("same")

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(ratePtDiProgressionEr,"Di-Obj rate |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPt_DiObjEr_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPt_DiObj_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c1","c1",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("#eta^{L1}")
empty1.SetTitle("")
empty1.GetXaxis().SetRangeUser(0.,etaRestictedLim);
empty1.GetYaxis().SetRangeUser(0.1,1e5);
empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

rateEtaDiProgressionEr.SetLineWidth(2)
rateEtaDiProgressionEr.SetMarkerColor(1)
rateEtaDiProgressionEr.SetLineColor(1)
rateEtaDiProgressionEr.Draw("same")

legend = ROOT.TLegend(0.60,0.84,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaDiProgressionEr,"Di-Obj rate |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPt_DiObjEr_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPt_DiObj_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c2","c2",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
empty.SetTitle("")
empty.GetXaxis().SetRangeUser(0.,240.);
empty.GetYaxis().SetRangeUser(0.1,1e5);
empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("Rate [kHz]");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);
empty.Draw()

ratePtProgressionEr.SetLineWidth(2)
ratePtProgressionEr.SetMarkerColor(1)
ratePtProgressionEr.SetLineColor(1)
ratePtProgressionEr.Draw("same")

ratePtDiProgressionEr.SetLineWidth(2)
ratePtDiProgressionEr.SetMarkerColor(2)
ratePtDiProgressionEr.SetLineColor(2)
ratePtDiProgressionEr.Draw("same")

legend = ROOT.TLegend(0.60,0.81,0.88,0.89)
legend.SetBorderSize(0)
legend.AddEntry(ratePtProgressionEr,"Single-Obj rate |#eta|<"+str(etaRestictedLim),"LPE")
legend.AddEntry(ratePtDiProgressionEr,"Di-Obj rate |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPt_Er_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPt_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c2","c2",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("#eta^{L1}")
empty1.SetTitle("")
empty1.GetXaxis().SetRangeUser(0.,etaRestictedLim);
empty1.GetYaxis().SetRangeUser(0.1,1e5);
empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

rateEtaProgressionEr.SetLineWidth(2)
rateEtaProgressionEr.SetMarkerColor(1)
rateEtaProgressionEr.SetLineColor(1)
rateEtaProgressionEr.Draw("same")

rateEtaDiProgressionEr.SetLineWidth(2)
rateEtaDiProgressionEr.SetMarkerColor(2)
rateEtaDiProgressionEr.SetLineColor(2)
rateEtaDiProgressionEr.Draw("same")

legend = ROOT.TLegend(0.60,0.81,0.88,0.89)
legend.SetBorderSize(0)
legend.AddEntry(rateEtaProgressionEr,"Single-Obj rate |#eta|<"+str(etaRestictedLim),"LPE")
legend.AddEntry(rateEtaDiProgressionEr,"Di-Obj rate |#eta|<"+str(etaRestictedLim),"LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsEta_Er_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsEta_"+label+".png")

del canvas, tex, tex2, legend

####################

#define canvas for plotting
canvas = ROOT.TCanvas("c2","c2",900,800)
canvas.SetRightMargin(0.175);
canvas.SetLeftMargin(0.1);
canvas.SetGrid(10,10);
canvas.SetLogz()

#use dummy histogram to define style
ratePtVsEtaProgressionEr.SetTitle("")
ratePtVsEtaProgressionEr.GetXaxis().SetTitle("p_{T}^{L1} [GeV]")
ratePtVsEtaProgressionEr.GetYaxis().SetTitle("#eta^{L1}")
ratePtVsEtaProgressionEr.GetZaxis().SetTitle("Rate [kHz]");
ratePtVsEtaProgressionEr.GetXaxis().SetRangeUser(0.,240.);
ratePtVsEtaProgressionEr.GetYaxis().SetRangeUser(0.,etaRestictedLim);
ratePtVsEtaProgressionEr.GetXaxis().SetTitleOffset(1.3);
ratePtVsEtaProgressionEr.GetZaxis().SetTitleOffset(1.7);
ratePtVsEtaProgressionEr.SetContour(256)
ratePtVsEtaProgressionEr.Draw("colz same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.1,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.82,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+"/PDFs/"+label+"/rateVsPtVsEta_Er_"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/rateVsPtVsEta_"+label+".png")

del canvas, tex, tex2

####################

print("saving histograms and efficiencies in root file for later plotting if desired")
fileout = ROOT.TFile(outdir+"/ROOTs/rate_graphs_"+label+".root","RECREATE")

ptProgression.Write()
ptDiProgression.Write()
etaProgression.Write()
etaDiProgression.Write()
ratePtProgression.Write()
ratePtDiProgression.Write()
rateEtaProgression.Write()
rateEtaDiProgression.Write()
ptVsEtaProgression.Write()
ratePtVsEtaProgression.Write()

ptProgressionEr.Write()
ptDiProgressionEr.Write()
etaProgressionEr.Write()
etaDiProgressionEr.Write()
ratePtProgressionEr.Write()
ratePtDiProgressionEr.Write()
rateEtaProgressionEr.Write()
rateEtaDiProgressionEr.Write()
ptVsEtaProgressionEr.Write()
ratePtVsEtaProgressionEr.Write()

fileout.Close()






