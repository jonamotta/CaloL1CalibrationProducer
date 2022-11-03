from array import array
import numpy as np
import ROOT
import sys
import os

ROOT.gROOT.SetBatch(True)

# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW_newCalibManualSaturation_2_applyHCALpfa1p/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_newCalibManualSaturation_2_applyHCALpfa1p/ HCAL_newCalibManualSaturation_2 Plots_JB 10000000

# reading input parameters
if len(sys.argv) > 2 :
    directory_TurnOns = sys.argv[1]
    directory_Rates = sys.argv[2]
else:
    directory = '/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/'
    directory_TurnOns = directory + 'QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW_newCalibManualSaturation_2_applyHCALpfa1p/'
    directory_Rates = directory + 'SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_newCalibManualSaturation_2_applyHCALpfa1p/'

if len(sys.argv) > 3 :
    label = sys.argv[3]
else:
    label = 'HCAL_newCalibManualSaturation_2'

if len(sys.argv) > 4 :
    outdir = sys.argv[4]
else:
    outdir = 'Plots_JB'

if len(sys.argv) > 5 :
    nevents = int(sys.argv[5])
else:
    nevents = 10000

##########################################################################################
######################################## TURN ONS ########################################
##########################################################################################

# I have to convert the x axis from L1 pt threshold to offline pt threshold
# for each L1 pt from 0 to 241 we build a turn on and we extract the offline pt giving a 95% efficiency

TurnOn_folder_png = outdir+'/TurnOns/PNGs/'+label
TurnOn_folder_pdf = outdir+'/TurnOns/PDFs/'+label

Rates_folder_png = outdir+'/Rates/PNGs/'+label
Rates_folder_pdf = outdir+'/Rates/PDFs/'+label

ROOTs_folder = outdir+'/ROOTs'

os.system('mkdir -p '+outdir)
os.system('mkdir -p '+outdir+'/ROOTs')
os.system('mkdir -p '+outdir+'/TurnOns/')
os.system('mkdir -p '+outdir+'/TurnOns/PNGs')
os.system('mkdir -p '+outdir+'/TurnOns/PNGs/'+label)
os.system('mkdir -p '+outdir+'/TurnOns/PDFs')
os.system('mkdir -p '+outdir+'/TurnOns/PDFs/'+label)
os.system('mkdir -p '+outdir+'/Rates/')
os.system('mkdir -p '+outdir+'/Rates/PNGs/'+label)
os.system('mkdir -p '+outdir+'/Rates/PNGs')
os.system('mkdir -p '+outdir+'/Rates/PDFs/'+label)

print("\n\nCREATE TURN ONS\n\n")

print("defining input trees")
eventTree = ROOT.TChain("l1EventTree/L1EventTree")
genTree = ROOT.TChain("l1GeneratorTree/L1GenTree")
emuTree = ROOT.TChain("l1UpgradeEmuTree/L1UpgradeTree")

print("reading input files")
eventTree.Add(directory_TurnOns + "/Ntuple*.root")
genTree.Add(directory_TurnOns + "/Ntuple*.root")
emuTree.Add(directory_TurnOns + "/Ntuple*.root")

print("getting entries")
nEntries = eventTree.GetEntries()

#run on entries specified by usuer, or only on entries available if that is exceeded
if (nevents > nEntries) or (nevents==-1): nevents = nEntries
print("will process",nevents,"events...")

#defining binning of histogram
#we wnat to have the same binning for the turnons (Offline JetPt) and for the rate:
#L1 and Offline JetPt bins have to correspond

Nbins = 300
Min = 0 
Max = 300

# L1_cuts = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
L1_cuts = np.linspace(Min,Max,Nbins+1)

Offline_cuts, Rates = array('d'), array('d')

Numerators = []
Denominator = ROOT.TH1F("Denominator","Denominator",Nbins,Min,Max)
for L1_cut in L1_cuts:
    name = "Numerator_{}".format(int(L1_cut))
    Numerators.append(ROOT.TH1F(name,name,Nbins,Min,Max))

# loop over all events
for i in range(0, nevents):

    # print('\nEvent', i)
    if i%10000==0: print(i)

    entry1 = eventTree.GetEntry(i)
    entry2 = emuTree.GetEntry(i)
    entry3 = genTree.GetEntry(i)

    L1_nJets = emuTree.L1Upgrade.nJets
    Gen_nJets = genTree.Generator.nJet

    matched = False
    myGoodGenPt = -99.
    myGoodL1Pt = -99.

    for igenJet in range(0,Gen_nJets):

        # print('JetPt', genTree.Generator.jetPt[igenJet])
        if not matched:
            Gen_jet = ROOT.TLorentzVector()
            Gen_jet.SetPtEtaPhiM(genTree.Generator.jetPt[igenJet], genTree.Generator.jetEta[igenJet], genTree.Generator.jetPhi[igenJet], 0)

            for iL1jet in range(0,L1_nJets):

                if not matched:
                    # for HCAL (Pt in Et)
                    L1_jet = ROOT.TLorentzVector()
                    L1_jet.SetPtEtaPhiM(emuTree.L1Upgrade.jetEt[iL1jet], emuTree.L1Upgrade.jetEta[iL1jet], emuTree.L1Upgrade.jetPhi[iL1jet], 0)
                    # for ECAL (Pt in Et)
                    # L1_jet.SetPtEtaPhiM(emuTree.L1Upgrade.egEt[ijet], emuTree.L1Upgrade.egEta[ijet], emuTree.L1Upgrade.egPhi[ijet], 0)

                    if Gen_jet.DeltaR(L1_jet)<0.5:
                        matched = True
                        myGoodGenPt = Gen_jet.Pt()
                        myGoodL1Pt = L1_jet.Pt()
                        break

    Denominator.Fill(myGoodGenPt)
    for i, L1_cut in enumerate(L1_cuts):
        if myGoodL1Pt > L1_cut:
            Numerators[i].Fill(myGoodGenPt)

empty = ROOT.TH1F("empty","empty",Nbins,Min,Max)
empty1 = ROOT.TH1F("empty1","empty1",Nbins,Min,Max)

#saving root histograms
fileout = ROOT.TFile(ROOTs_folder + "/TurnOn_"+label+".root","RECREATE")
Denominator.Write()

for i, L1_cut in enumerate(L1_cuts):

    c1_name = "c1_{}".format(i)
    #define canvas for plotting
    canvas1 = ROOT.TCanvas(c1_name,c1_name,800,800)
    canvas1.SetGrid(10,10)
    canvas1.SetLogy()

    #use dummy histogram to define style
    empty.GetXaxis().SetTitle("p_{T}^{Offline}(jet) [GeV]")
    empty.SetTitle("")
    empty.GetXaxis().SetRangeUser(Min,Max)
    empty.GetYaxis().SetRangeUser(0.01,1.2*max(Numerators[i].GetMaximum(),Denominator.GetMaximum()))
    empty.GetXaxis().SetTitleOffset(1.3)
    empty.GetYaxis().SetTitle("#Entries")
    empty.GetYaxis().SetTitleOffset(1.3)
    empty.SetTitle("")
    empty.SetStats(0)
    empty.Draw()

    Numerators[i].Draw("same")
    Numerators[i].SetLineWidth(2)
    Numerators[i].SetLineColor(3)
    Denominator.Draw("same")
    Denominator.SetLineWidth(2)
    Denominator.SetLineColor(6)

    Legend = ROOT.TLegend(0.65,0.15,0.88,0.23)
    Legend.SetBorderSize(0)
    Legend.AddEntry(Numerators[i], "L1 Trigger: p_{T}^{L1}(jet) > "+str(L1_cut)+" GeV", "LPE")
    Legend.AddEntry(Denominator, "Inclusive", "LPE")
    Legend.Draw()

    Tex1 = ROOT.TLatex()
    Tex1.SetTextSize(0.03)
    Tex1.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
    Tex1.Draw("same")

    Tex2 = ROOT.TLatex()
    Tex2.SetTextSize(0.035)
    Tex2.SetTextAlign(31)
    Tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)")
    Tex2.Draw("same")

    if int(L1_cut) % 20 == 0:
        canvas1.SaveAs(TurnOn_folder_png+"/JetPassing_{}.png".format(int(L1_cut)))
        canvas1.SaveAs(TurnOn_folder_pdf+"/JetPassing_{}.pdf".format(int(L1_cut)))

    # -----------------------------------------------------------

    #define canvas for plotting
    c_name = "c_{}".format(i)
    canvas = ROOT.TCanvas(c_name,c_name,800,800)
    canvas.SetGrid(10,10)
    # canvas.SetLogy()

    # #use dummy histogram to define style
    empty1.GetXaxis().SetTitle("p_{T}^{Offline}(jet) [GeV]")
    empty1.SetTitle("")
    empty1.GetXaxis().SetRangeUser(Min,Max)
    empty1.GetYaxis().SetRangeUser(0.,1.)
    empty1.GetXaxis().SetTitleOffset(1.3)
    empty1.GetYaxis().SetTitle("Efficiency")
    empty1.GetYaxis().SetTitleOffset(1.3)
    empty1.SetTitle("")
    empty1.SetStats(0)
    empty1.Draw()

    TurnOn_Jet = ROOT.TGraphAsymmErrors("TurnOn_Jet","TurnOn_Jet")
    TurnOn_Jet = ROOT.TGraphAsymmErrors(Numerators[i], Denominator, "cp")

    TurnOn_Jet.SetTitle("")
    TurnOn_Jet.Draw("same ALP")
    TurnOn_Jet.SetMarkerStyle(21)
    TurnOn_Jet.SetMarkerColor(4)
    TurnOn_Jet.SetLineColor(4)

    Legend = ROOT.TLegend(0.65,0.15,0.88,0.23)
    Legend.SetBorderSize(0)
    Legend.AddEntry(TurnOn_Jet, "L1 Trigger: p_{T}^{L1}(jet) > "+str(L1_cut)+" GeV", "LPE")
    Legend.Draw()

    Tex11 = ROOT.TLatex()
    Tex11.SetTextSize(0.03)
    Tex11.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
    Tex11.Draw("same")

    Tex22 = ROOT.TLatex()
    Tex22.SetTextSize(0.035)
    Tex22.SetTextAlign(31)
    Tex22.DrawLatexNDC(0.90,0.91,"(14 TeV)")
    Tex22.Draw("same")

    if int(L1_cut) % 20 == 0:
        canvas.SaveAs(TurnOn_folder_png+"/TurnOn_{}.png".format(int(L1_cut)))
        canvas.SaveAs(TurnOn_folder_pdf+"/TurnOn_{}.pdf".format(int(L1_cut)))

    Numerators[i].Write()
    TurnOn_Jet.Write()

    # -----------------------------------------------------------

    # extract the Offline pt giving 95% efficiency

    th = 0.95
    found = False
    x_points = list(TurnOn_Jet.GetX())
    y_points = list(TurnOn_Jet.GetY())
    # print(len(x_points), len(y_points))

    for x,y in zip(x_points, y_points):
        if (found == False) and (y > th) and (x > L1_cut):
            Offline_cuts.append(x)
            found = True

    if found == False:
        Offline_cuts.append(-1)

fileout.Close()

# print(L1_cuts)
# print(Offline_cuts)


##########################################################################################
########################################## RATES #########################################
##########################################################################################

print("\n\nCOMPUTE RATES\n\n")

print("defining input trees")
eventTree = ROOT.TChain("l1EventTree/L1EventTree")
genTree = ROOT.TChain("l1GeneratorTree/L1GenTree")
emuTree = ROOT.TChain("l1UpgradeEmuTree/L1UpgradeTree")

print("reading input files")
eventTree.Add(directory_Rates + "/Ntuple*.root")
genTree.Add(directory_Rates + "/Ntuple*.root")
emuTree.Add(directory_Rates + "/Ntuple*.root")

print("getting entries")
nEntries = eventTree.GetEntries()

#run on entries specified by usuer, or only on entries available if that is exceeded
if (nevents > nEntries) or (nevents==-1): nevents = nEntries
print("will process",nevents,"events...")

thresholds = [0]
threshold = 0

denominator = 0.
nb = 2544.
scale = 0.001*(nb*11245.6)

ptProgression = ROOT.TH1F("ptProgression","ptProgression",Nbins,Min,Max)

print("looping on events")
for i in range(0, nevents):
    if i%1000==0: print(i)
    #getting entries
    entry1 = eventTree.GetEntry(i)
    entry2 = emuTree.GetEntry(i)
    entry3 = genTree.GetEntry(i)

    denominator += 1.

    # I'm just filling a histogram with the most energetic L1 jet
    # Then I will do the integral

    L1_nJets = emuTree.L1Upgrade.nJets
    if L1_nJets > 0:
        ptProgression.Fill(emuTree.L1Upgrade.jetEt[0])

# plot the distribution of the leading jet L1 pt
canvas2 = ROOT.TCanvas("c_2","c_2",800,800)
canvas2.SetGrid(10,10)
ptProgression.SetTitle("")
ptProgression.GetXaxis().SetTitle("p_{T}^{L1}(leading jet)")
ptProgression.GetYaxis().SetTitle("#Entries")
ptProgression.SetStats(0)
ptProgression.SetLineWidth(2)
ptProgression.SetMarkerColor(4)
ptProgression.SetLineColor(4)
ptProgression.Draw()

Tex21 = ROOT.TLatex()
Tex21.SetTextSize(0.03)
Tex21.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
Tex21.Draw("same")

Tex22 = ROOT.TLatex()
Tex22.SetTextSize(0.035)
Tex22.SetTextAlign(31)
Tex22.DrawLatexNDC(0.90,0.91,"(14 TeV)")
Tex22.Draw("same")

canvas2.SaveAs(Rates_folder_png+"/L1JetPtDistribution.png")
canvas2.SaveAs(Rates_folder_pdf+"/L1JetPtDistribution.pdf")

for i, L1_cut in enumerate(L1_cuts[:-1]):
    in_bin = i+1 # [FIXME] conversion between binning of turn on and L1 pt binning
    fin_bin = Nbins
    # print(L1_cut, ptProgression.GetBinLowEdge(in_bin))
    # print(ptProgression.Integral(in_bin, fin_bin))
    Rates.append(ptProgression.Integral(in_bin, fin_bin))

print("\L1_cuts:\n",L1_cuts)
print("\nOffline_cuts:\n",Offline_cuts)
print("\nRates\n",Rates)

RatesVSOffline = ROOT.TGraphErrors(len(Offline_cuts), Offline_cuts, Rates)
RatesVSOnline = ROOT.TGraphErrors(len(L1_cuts), L1_cuts, Rates)

canvas3 = ROOT.TCanvas("c_3","c_3",800,800)
canvas3.SetGrid(10,10)
canvas3.SetLogy()
RatesVSOffline.SetTitle("")
RatesVSOffline.GetXaxis().SetTitle("p_{T}^{Offline}(jet)")
RatesVSOffline.GetYaxis().SetTitle("Rates [kHz]")
RatesVSOffline.GetYaxis().SetRangeUser(0.1,1e5)
RatesVSOffline.GetXaxis().SetRangeUser(0.,240.)
RatesVSOffline.SetLineWidth(2)
RatesVSOffline.SetMarkerColor(1)
RatesVSOffline.SetLineColor(1)
RatesVSOffline.Draw()

Tex31 = ROOT.TLatex()
Tex31.SetTextSize(0.03)
Tex31.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
Tex31.Draw("same")

Tex32 = ROOT.TLatex()
Tex32.SetTextSize(0.035)
Tex32.SetTextAlign(31)
Tex32.DrawLatexNDC(0.90,0.91,"(14 TeV)")
Tex32.Draw("same")

canvas3.SaveAs(Rates_folder_png+"/RatesVSOffline.png")
canvas3.SaveAs(Rates_folder_pdf+"/RatesVSOffline.pdf")

#saving root graphs
fileout = ROOT.TFile(ROOTs_folder + "/Rate_"+label+".root","RECREATE")
fileout.WriteObject(RatesVSOffline, "RatesVSOffline")
fileout.WriteObject(RatesVSOnline, "RatesVSOnline")
fileout.Close()