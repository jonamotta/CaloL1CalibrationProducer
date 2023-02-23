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

#defining binning of histogram
if "HCAL_" in label: 
    ptBins  = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200, 500]
    etaBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.191]
    signedEtaBins = [-5.191, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.479, -1.305, -1.0, -0.5, 0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.191]
if "ECAL_" in label:
    ptBins  = [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200]
    etaBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0]
    signedEtaBins = [-3.0, -2.5, -2.0, -1.479, -1.305, -1.0, -0.5, 0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0]


empty = ROOT.TH1F("empty","empty",60,0.,3.)

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
    entry = eventTree.GetEntry(i)
    entry2 = emuTree.GetEntry(i)
    entry3 = genTree.GetEntry(i)

    L1_nJets = 0
    if "HCAL_" in label: L1_nJets = emuTree.L1Upgrade.nJets
    if "ECAL_" in label: L1_nJets = emuTree.L1Upgrade.nEGs
    Gen_nJets = genTree.Generator.nJet

    #loop on generator jets
    for igenJet in range(0,Gen_nJets):

        Gen_jet = ROOT.TLorentzVector()
        Gen_jet.SetPtEtaPhiM(genTree.Generator.jetPt[igenJet], genTree.Generator.jetEta[igenJet], genTree.Generator.jetPhi[igenJet], 0)

        #reject very soft jets, usually poorly defined
        if "HCAL_" in label and Gen_jet.Pt()<15.: continue

        matched = False
        highestL1Pt = -99.

        #loop on L1 jets to find match
        for ijet in range(0, L1_nJets):
            L1_jet = ROOT.TLorentzVector()
            if "HCAL_" in label: L1_jet.SetPtEtaPhiM(emuTree.L1Upgrade.jetEt[ijet], emuTree.L1Upgrade.jetEta[ijet], emuTree.L1Upgrade.jetPhi[ijet], 0)
            if "ECAL_" in label: L1_jet.SetPtEtaPhiM(emuTree.L1Upgrade.egEt[ijet], emuTree.L1Upgrade.egEta[ijet], emuTree.L1Upgrade.egPhi[ijet], 0)

            #check matching
            if Gen_jet.DeltaR(L1_jet)<0.5:
                matched = True
                #keep only L1 match with highest pT
                if L1_jet.Pt()>highestL1Pt:
                    highestL1Pt = L1_jet.Pt()

        if matched:
            pt_response_ptInclusive.Fill(highestL1Pt/Gen_jet.Pt())

            if abs(Gen_jet.Eta()) < 1.305:
                pt_barrel_resp_ptInclusive.Fill(highestL1Pt/Gen_jet.Pt())
            elif abs(Gen_jet.Eta()) < 5.191 and abs(Gen_jet.Eta()) > 1.479:
                pt_endcap_resp_ptInclusive.Fill(highestL1Pt/Gen_jet.Pt())

            for i in range(len(ptBins)-1):
                if Gen_jet.Pt() > ptBins[i] and Gen_jet.Pt() <= ptBins[i+1]:
                    response_ptBins[i].Fill(highestL1Pt/Gen_jet.Pt())
                    
                    if abs(Gen_jet.Eta()) < 1.305:
                        barrel_response_ptBins[i].Fill(highestL1Pt/Gen_jet.Pt())
                    elif abs(Gen_jet.Eta()) < 5.191 and abs(Gen_jet.Eta()) > 1.479:
                        endcap_response_ptBins[i].Fill(highestL1Pt/Gen_jet.Pt())

            for i in range(len(etaBins)-1):
                if abs(Gen_jet.Eta()) > etaBins[i] and abs(Gen_jet.Eta()) < etaBins[i+1]:
                    absEta_response_ptBins[i].Fill(highestL1Pt/Gen_jet.Pt())

                if Gen_jet.Eta() > etaBins[i] and Gen_jet.Eta() < etaBins[i+1]:
                    plusEta_response_ptBins[i].Fill(highestL1Pt/Gen_jet.Pt())

                elif Gen_jet.Eta() < -etaBins[i] and Gen_jet.Eta() > -etaBins[i+1]:
                    minusEta_response_ptBins[i].Fill(highestL1Pt/Gen_jet.Pt())

            k = 0
            for i in range(len(ptBins)-1):
                for j in range(len(etaBins)-1):
                    if abs(Gen_jet.Eta()) > etaBins[j] and abs(Gen_jet.Eta()) < etaBins[j+1] and Gen_jet.Pt() > ptBins[i] and Gen_jet.Pt() < ptBins[i+1]:
                        pt_resp_PtEtaBin[k].Fill(highestL1Pt/Gen_jet.Pt());

                    k += 1

        # else:
        #     pt_response_ptInclusive.Fill(0.)

        #     if abs(Gen_jet.Eta()) < 1.305:
        #         pt_barrel_resp_ptInclusive.Fill(0.)
        #     elif abs(Gen_jet.Eta()) < 5.191 and abs(Gen_jet.Eta()) > 1.479:
        #         pt_endcap_resp_ptInclusive.Fill(0.)

        #     for i in range(len(ptBins)-1):
        #         if Gen_jet.Pt() > ptBins[i] and Gen_jet.Pt() <= ptBins[i+1]:
        #             response_ptBins[i].Fill(0)
                    
        #             if abs(Gen_jet.Eta()) < 1.305:
        #                 barrel_response_ptBins[i].Fill(0.)
        #             elif abs(Gen_jet.Eta()) < 5.191 and abs(Gen_jet.Eta()) > 1.479:
        #                 endcap_response_ptBins[i].Fill(0.)

        #     for i in range(len(etaBins)-1):
        #         if abs(Gen_jet.Eta()) > etaBins[i] and abs(Gen_jet.Eta()) < etaBins[i+1]:
        #             absEta_response_ptBins[i].Fill(0.)

        #         if Gen_jet.Eta() > etaBins[i] and Gen_jet.Eta() < etaBins[i+1]:
        #             plusEta_response_ptBins[i].Fill(0.)

        #         elif Gen_jet.Eta() < -etaBins[i] and Gen_jet.Eta() > -etaBins[i+1]:
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


ROOT.gStyle.SetOptStat(000000)

for i in range(len(barrel_response_ptBins)):
    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);

    #use dummy histogram to define style
    empty.GetXaxis().SetTitle("E_{T}^{L1 jet} / p_{T}^{gen jet}")
    empty.SetTitle("")

    #empty.GetXaxis().SetRangeUser(0.,250.);
    empty.GetYaxis().SetRangeUser(0., max(barrel_response_ptBins[i].GetMaximum(),endcap_response_ptBins[i].GetMaximum())*1.3 )

    empty.GetXaxis().SetTitleOffset(1.3);
    empty.GetYaxis().SetTitle("a.u.");
    empty.GetYaxis().SetTitleOffset(1.3);
    empty.SetTitle("");
    empty.SetStats(0);

    empty.Draw()

    barrel_response_ptBins[i].SetLineWidth(2)
    barrel_response_ptBins[i].SetMarkerColor(1)
    barrel_response_ptBins[i].SetLineColor(1)

    endcap_response_ptBins[i].SetLineWidth(2)
    endcap_response_ptBins[i].SetMarkerColor(2)
    endcap_response_ptBins[i].SetLineColor(2)

    barrel_response_ptBins[i].Draw("same")
    endcap_response_ptBins[i].Draw("same")


    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.SetHeader(str(ptBins[i])+"p_{T}^{gen jet}"+str(ptBins[i+1]))
    legend.AddEntry(barrel_response_ptBins[i],"Barrel |#eta^{gen jet}|<1.305","LPE")
    legend.AddEntry(endcap_response_ptBins[i],"Endcap 1.479<|#eta^{gen jet}|<5.191","LPE")

    legend.Draw("same")

    canvas.SaveAs(outdir+"/PDFs/"+label+"/response_"+str(ptBins[i])+"pt"+str(ptBins[i+1])+"_"+label+".pdf")
    canvas.SaveAs(outdir+"/PNGs/"+label+"/response_"+str(ptBins[i])+"pt"+str(ptBins[i+1])+"_"+label+".png")

    del canvas, legend

for i in range(len(absEta_response_ptBins)):
    #define canvas for plotting
    canvas = ROOT.TCanvas("c","c",800,800)
    canvas.SetGrid(10,10);

    #use dummy histogram to define style
    empty.GetXaxis().SetTitle("E_{T}^{L1 jet} / p_{T}^{gen jet}")
    empty.SetTitle("")

    #empty.GetXaxis().SetRangeUser(0.,250.);
    empty.GetYaxis().SetRangeUser(0., absEta_response_ptBins[i].GetMaximum()*1.3 )

    empty.GetXaxis().SetTitleOffset(1.3);
    empty.GetYaxis().SetTitle("a.u.");
    empty.GetYaxis().SetTitleOffset(1.3);
    empty.SetTitle("");
    empty.SetStats(0);

    empty.Draw()

    absEta_response_ptBins[i].SetLineWidth(2)
    absEta_response_ptBins[i].SetMarkerColor(1)
    absEta_response_ptBins[i].SetLineColor(1)

    barrel_response_ptBins[i].Draw("same")


    legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.AddEntry(absEta_response_ptBins[i],str(etaBins[i])+"<|#eta^{gen jet}|<"+str(etaBins[i+1]),"LPE")
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

    canvas.SaveAs(outdir+"/PDFs/"+label+"/response_"+str(etaBins[i])+"eta"+str(etaBins[i+1])+"_"+label+".pdf")
    canvas.SaveAs(outdir+"/PNGs/"+label+"/response_"+str(etaBins[i])+"eta"+str(etaBins[i+1])+"_"+label+".png")

    del canvas, legend

##############

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);

#use dummy histogram to define style
pt_resol_barrel_fctPt.GetXaxis().SetTitle("p^{gen jet}_{T} [GeV]")
pt_resol_barrel_fctPt.SetTitle("")

pt_resol_barrel_fctPt.GetXaxis().SetTitleOffset(1.3);
pt_resol_barrel_fctPt.GetYaxis().SetTitle("E^{L1 jet}_{T} resolution");
pt_resol_barrel_fctPt.GetYaxis().SetTitleOffset(1.3);
pt_resol_barrel_fctPt.SetTitle("");
pt_resol_barrel_fctPt.SetStats(0);

pt_resol_barrel_fctPt.GetXaxis().SetRangeUser(15.,200.);

pt_resol_barrel_fctPt.SetLineWidth(2)
pt_resol_barrel_fctPt.SetMarkerColor(1)
pt_resol_barrel_fctPt.SetLineColor(1)

pt_resol_endcap_fctPt.SetLineWidth(2)
pt_resol_endcap_fctPt.SetMarkerColor(2)
pt_resol_endcap_fctPt.SetLineColor(2)

pt_resol_barrel_fctPt.Draw("LPE")
pt_resol_endcap_fctPt.Draw("same LPE")

legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(pt_resol_barrel_fctPt,"Barrel |#eta^{gen jet}|<1.305","LPE")
legend.AddEntry(pt_resol_endcap_fctPt,"Endcap 1.479<|#eta^{gen jet}|<5.191","LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/resolution_ptBins"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/resolution_ptBins"+label+".png")

del canvas, legend

##############

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);

#use dummy histogram to define style
pt_resol_fctEta.GetXaxis().SetTitle("#eta^{gen jet}")
pt_resol_fctEta.SetTitle("")

pt_resol_fctEta.GetYaxis().SetRangeUser(0., 2.)

pt_resol_fctEta.GetXaxis().SetTitleOffset(1.3);
pt_resol_fctEta.GetYaxis().SetTitle("E^{L1 jet}_{T} resolution");
pt_resol_fctEta.GetYaxis().SetTitleOffset(1.3);
pt_resol_fctEta.SetTitle("");
pt_resol_fctEta.SetStats(0);

pt_resol_fctEta.SetLineWidth(2)
pt_resol_fctEta.SetMarkerColor(1)
pt_resol_fctEta.SetLineColor(1)

pt_resol_fctEta.Draw("LPE")

b1 = ROOT.TBox(1.305,0.,1.479,2)
b1.SetFillColor(16)
b1.Draw("same")
b2 = ROOT.TBox(-1.479,0.,-1.305,2)
b2.SetFillColor(16)
b2.Draw("same")
b3 = ROOT.TBox(1.305,0.,1.479,2)
b3.SetFillColor(1)
b3.SetFillStyle(3004)
b3.Draw("same")
b4 = ROOT.TBox(-1.479,0.,-1.305,2)
b4.SetFillColor(1)
b4.SetFillStyle(3004)
b4.Draw("same")

# legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
# legend.SetBorderSize(0)
# legend.AddEntry(pt_resol_fctEta,"Barrel |#eta^{gen jet}|<1.305","LPE")
# legend.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+"/PDFs/"+label+"/resolution_etaBins"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/resolution_etaBins"+label+".png")

del canvas

##############

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);

#use dummy histogram to define style
pt_scale_fctEta.GetXaxis().SetTitle("#eta^{gen jet}")
pt_scale_fctEta.SetTitle("")

pt_scale_fctEta.GetYaxis().SetRangeUser(0., 2.)

pt_scale_fctEta.GetXaxis().SetTitleOffset(1.3);
pt_scale_fctEta.GetYaxis().SetTitle("E^{L1 jet}_{T} scale");
pt_scale_fctEta.GetYaxis().SetTitleOffset(1.3);
pt_scale_fctEta.SetTitle("");
pt_scale_fctEta.SetStats(0);

pt_scale_fctEta.SetLineWidth(2)
pt_scale_fctEta.SetMarkerColor(1)
pt_scale_fctEta.SetLineColor(1)

pt_scale_fctEta.Draw("LPE")

b1 = ROOT.TBox(1.305,0.,1.479,2)
b1.SetFillColor(16)
b1.Draw("same")
b2 = ROOT.TBox(-1.479,0.,-1.305,2)
b2.SetFillColor(16)
b2.Draw("same")
b3 = ROOT.TBox(1.305,0.,1.479,2)
b3.SetFillColor(1)
b3.SetFillStyle(3004)
b3.Draw("same")
b4 = ROOT.TBox(-1.479,0.,-1.305,2)
b4.SetFillColor(1)
b4.SetFillStyle(3004)
b4.Draw("same")

# legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
# legend.SetBorderSize(0)
# legend.AddEntry(pt_scale_fctEta,"Barrel |#eta^{gen jet}|<1.305","LPE")
# legend.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+"/PDFs/"+label+"/scale_etaBins"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/scale_etaBins"+label+".png")

del canvas

##############

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);

#use dummy histogram to define style
pt_scale_fctPt.GetXaxis().SetTitle("p^{gen jet}_{T} [GeV]")
pt_scale_fctPt.SetTitle("")

pt_scale_fctPt.GetYaxis().SetRangeUser(0., 2.)

pt_scale_fctPt.GetXaxis().SetTitleOffset(1.3);
pt_scale_fctPt.GetYaxis().SetTitle("E^{L1 jet}_{T} scale");
pt_scale_fctPt.GetYaxis().SetTitleOffset(1.3);
pt_scale_fctPt.SetTitle("");
pt_scale_fctPt.SetStats(0);

pt_scale_fctPt.SetLineWidth(2)
pt_scale_fctPt.SetMarkerColor(1)
pt_scale_fctPt.SetLineColor(1)

pt_scale_fctPt.Draw("LPE")

# legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
# legend.SetBorderSize(0)
# legend.AddEntry(pt_scale_fctPt,"Barrel |#eta^{gen jet}|<1.305","LPE")
# legend.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

canvas.SaveAs(outdir+"/PDFs/"+label+"/scale_ptBins"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/scale_ptBins"+label+".png")

del canvas

##############

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);

#use dummy histogram to define style
pt_response_ptInclusive.GetXaxis().SetTitle("E^{L1 jet}_{T} / p^{gen jet}_{T}")
pt_response_ptInclusive.SetTitle("")

pt_response_ptInclusive.GetXaxis().SetTitleOffset(1.3);
pt_response_ptInclusive.GetYaxis().SetTitle("a.u.");
pt_response_ptInclusive.GetYaxis().SetTitleOffset(1.3);
pt_response_ptInclusive.SetTitle("");
pt_response_ptInclusive.SetStats(0);

pt_response_ptInclusive.GetYaxis().SetRangeUser(0., max(pt_barrel_resp_ptInclusive.GetMaximum(),pt_endcap_resp_ptInclusive.GetMaximum())*1.3 )

pt_barrel_resp_ptInclusive.SetLineWidth(2)
pt_barrel_resp_ptInclusive.SetMarkerColor(1)
pt_barrel_resp_ptInclusive.SetLineColor(1)

pt_endcap_resp_ptInclusive.SetLineWidth(2)
pt_endcap_resp_ptInclusive.SetMarkerColor(2)
pt_endcap_resp_ptInclusive.SetLineColor(2)

pt_response_ptInclusive.SetLineWidth(2)
pt_response_ptInclusive.SetMarkerColor(4)
pt_response_ptInclusive.SetLineColor(4)

pt_response_ptInclusive.Draw()
pt_endcap_resp_ptInclusive.Draw("same")
pt_barrel_resp_ptInclusive.Draw("same")

legend = ROOT.TLegend(0.55,0.75,0.88,0.88)
legend.SetBorderSize(0)
legend.AddEntry(pt_response_ptInclusive,"Inclusive |#eta^{gen jet}|<5.191","LPE")
legend.AddEntry(pt_barrel_resp_ptInclusive,"Barrel |#eta^{gen jet}|<1.305","LPE")
legend.AddEntry(pt_endcap_resp_ptInclusive,"Endcap 1.479<|#eta^{gen jet}|<5.191","LPE")
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

canvas.SaveAs(outdir+"/PDFs/"+label+"/response_inclusive"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/response_inclusive"+label+".png")

del canvas

##############

#define canvas for plotting response_ptBins / inclusive
canvas_res_pt = ROOT.TCanvas("c_res_pt","c_res_pt",800,800)
canvas_res_pt.SetGrid(10,10);

#use dummy histogram to define style
maximum_pt = -1.
for res_plot in response_ptBins:
    if res_plot.Integral()<0.0001: continue
    if res_plot.GetMaximum()/res_plot.Integral()>maximum_pt: maximum_pt = res_plot.GetMaximum()/res_plot.Integral()
empty.GetYaxis().SetRangeUser(0.,maximum_pt*1.3);
empty.Draw("E");

for i,ele in enumerate(response_ptBins):
    response_ptBins[i].SetMarkerColor(i+2)
    response_ptBins[i].SetLineColor(i+2)
    response_ptBins[i].SetLineWidth(2)
    response_ptBins[i].Draw("LEPsame")

pt_response_ptInclusive.SetMarkerColor(1)
pt_response_ptInclusive.SetLineColor(1)
pt_response_ptInclusive.SetLineWidth(2)
pt_response_ptInclusive.Draw("LEPsame")

legend_res_pt = ROOT.TLegend(0.62782,0.452196,0.860902,0.883721)
legend_res_pt.SetBorderSize(0)
legend_res_pt.AddEntry(pt_response_ptInclusive,"Inclusive","LEP")

for i,ele in enumerate(ptBins):
    if i<len(ptBins)-1: legend_res_pt.AddEntry(response_ptBins[i],str(int(ptBins[i]+0.1))+" < p_{T}^{Gen jet} < "+str(int(ptBins[i+1]+0.1))+" GeV","EL")

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

canvas_res_pt.SaveAs(outdir+"/PDFs/"+label+"/response_in_ptBins_"+label+".pdf")
canvas_res_pt.SaveAs(outdir+"/PNGs/"+label+"/response_in_ptBins_"+label+".png")

##############

#define canvas for plotting absEta_response_ptBins / inclusive
canvas_res = ROOT.TCanvas("c_res","c_res",800,800)
canvas_res.SetGrid(10,10);

#use dummy histogram to define style
empty.GetXaxis().SetTitle("E_{T}^{L1 jet} / p_{T}^{Gen jet}")
empty.SetTitle("")

empty.GetXaxis().SetRangeUser(0.,2.);
maximum_eta = -1.
for res_plot in absEta_response_ptBins:
    if res_plot.Integral()<0.0001: continue
    if res_plot.GetMaximum()/res_plot.Integral()>maximum_eta: maximum_eta = res_plot.GetMaximum()/res_plot.Integral()
empty.GetYaxis().SetRangeUser(0.,maximum_eta*1.3);

empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("a.u.");
empty.GetYaxis().SetTitleOffset(1.45);
empty.SetTitle("");
empty.SetStats(0);

#empty.SetMarkerStyle(2)
empty.Draw("E");

for i,ele in enumerate(absEta_response_ptBins):
    if ele==1.479: continue
    #absEta_response_ptBins[i].SetMarkerStyle(2)
    absEta_response_ptBins[i].SetMarkerColor(i+2)
    absEta_response_ptBins[i].SetLineColor(i+2)
    #absEta_response_ptBins[i].SetLineWidth(0)
    absEta_response_ptBins[i].DrawNormalized("Esame")

#pt_response_ptInclusive.SetMarkerStyle(2)
pt_response_ptInclusive.SetMarkerColor(1)
pt_response_ptInclusive.SetLineColor(1)
#pt_response_ptInclusive.SetLineWidth(0)
pt_response_ptInclusive.DrawNormalized("Esame")

legend_res = ROOT.TLegend(0.15,0.75,0.48,0.88)
legend_res.SetBorderSize(0)
legend_res.AddEntry(pt_response_ptInclusive,"Inclusive","EL")

for i,ele in enumerate(etaBins):
    if i<len(etaBins)-1: legend_res.AddEntry(absEta_response_ptBins[i],str(etaBins[i])+" < |#eta^{gen jet}| < "+str(etaBins[i+1]),"EL")

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

canvas_res.SaveAs(outdir+"/PDFs/"+label+"/response_in_eta_bins_"+label+".pdf")
canvas_res.SaveAs(outdir+"/PNGs/"+label+"/response_in_eta_bins_"+label+".png")

##############

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

canvas.SaveAs(outdir+"/PDFs/"+label+"/resolution_ptVSeta"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/resolution_ptVSeta"+label+".png")

del canvas

##############

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

canvas.SaveAs(outdir+"/PDFs/"+label+"/scale_ptVSeta"+label+".pdf")
canvas.SaveAs(outdir+"/PNGs/"+label+"/scale_ptVSeta"+label+".png")

del canvas

##############

#saving histograms and efficiencies in root file for later plotting if desired
fileout = ROOT.TFile(outdir+"/ROOTs/resolution_graphs_"+label+".root","RECREATE")
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
