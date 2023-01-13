from array import array
import numpy as np
import ROOT
import sys
import os
import pandas as pd

ROOT.gROOT.SetBatch(True)

def findXPoint (xa, xb, ya, yb, yc):
    s = pd.Series([xa, np.nan, xb], index=[ya, yc, yb])
    s1 = s.interpolate(method='index')
    xc = s1[s1.index==yc].values[0]
    return xc

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
# for each L1 pt from 0 to 300 we build a turn on and we extract the offline pt giving a 95% efficiency

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

Nbins_L1 = 290
Min_L1 = 10.
Max_L1 = 300.

Nbins_TurnOn = 600
Min_TurnOn = 0.
Max_TurnOn = 600.

# L1_cuts = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
L1_cuts = np.linspace(Min_L1,Max_L1,Nbins_L1+1)

Offline_cuts_95, Offline_cuts_90, Offline_cuts_50, Rates = array('d'), array('d'), array('d'), array('d')

Numerators = []
Denominator = ROOT.TH1F("Denominator","Denominator",Nbins_TurnOn,Min_TurnOn,Max_TurnOn)
for L1_cut in L1_cuts:
    name = "Numerator_{}".format(int(L1_cut))
    Numerators.append(ROOT.TH1F(name,name,Nbins_TurnOn,Min_TurnOn,Max_TurnOn))

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

empty = ROOT.TH1F("empty","empty",Nbins_TurnOn,Min_TurnOn,Max_TurnOn)
empty1 = ROOT.TH1F("empty1","empty1",Nbins_TurnOn,Min_TurnOn,Max_TurnOn)

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
    empty.GetXaxis().SetRangeUser(Min_L1,Max_L1)
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
    empty1.GetXaxis().SetRangeUser(Min_L1,Max_L1)
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
    x_previous, y_previous = [0,0]

    for x,y in zip(x_points, y_points):
        if (found == False) and (y > th) and (x > L1_cut): # [FIXME] L1_cut condition should be removed after changing the range
            x_interpolation = findXPoint(x_previous, x, y_previous, y, th)
            print(x_interpolation)
            Offline_cuts_95.append(x_interpolation)
            found = True
        x_previous = x
        y_previous = y

    if found == False:
        Offline_cuts_95.append(-1)

    th = 0.9
    found = False
    x_points = list(TurnOn_Jet.GetX())
    y_points = list(TurnOn_Jet.GetY())
    # print(len(x_points), len(y_points))
    x_previous, y_previous = [0,0]

    for x,y in zip(x_points, y_points):
        if (found == False) and (y > th):
            x_interpolation = findXPoint(x_previous, x, y_previous, y, th)
            print(x_interpolation)
            Offline_cuts_90.append(x_interpolation)
            found = True
        x_previous = x
        y_previous = y

    if found == False:
        Offline_cuts_90.append(-1)

    th = 0.5
    found = False
    x_points = list(TurnOn_Jet.GetX())
    y_points = list(TurnOn_Jet.GetY())
    # print(len(x_points), len(y_points))
    x_previous, y_previous = [0,0]

    for x,y in zip(x_points, y_points):
        if (found == False) and (y > th):
            x_interpolation = findXPoint(x_previous, x, y_previous, y, th)
            print(x_interpolation)
            Offline_cuts_50.append(x_interpolation)
            found = True
        x_previous = x
        y_previous = y

    if found == False:
        Offline_cuts_50.append(-1)

fileout.Close()

# print(L1_cuts)
# print(Offline_cuts_95)


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

ptProgression = ROOT.TH1F("ptProgression","ptProgression",Nbins_L1,Min_L1,Max_L1)

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
    fin_bin = Nbins_L1
    # print(L1_cut, ptProgression.GetBinLowEdge(in_bin))
    # print(ptProgression.Integral(in_bin, fin_bin))
    Rates.append(ptProgression.Integral(in_bin, fin_bin))

print("\L1_cuts:\n",L1_cuts)
print("\nOffline_cuts_95:\n",Offline_cuts_95)
print("\nRates\n",Rates)

#Rates for 95% efficiency

RatesVSOffline_95 = ROOT.TGraphErrors(len(Offline_cuts_95), Offline_cuts_95, Rates)
RatesVSOnline = ROOT.TGraphErrors(len(L1_cuts), L1_cuts, Rates)

canvas3 = ROOT.TCanvas("c_3","c_3",800,800)
canvas3.SetGrid(10,10)
canvas3.SetLogy()
RatesVSOffline_95.SetTitle("")
RatesVSOffline_95.GetXaxis().SetTitle("p_{T}^{Offline}(jet)")
RatesVSOffline_95.GetYaxis().SetTitle("Rates [kHz]")
RatesVSOffline_95.GetYaxis().SetRangeUser(0.1,1.3*max(Rates))
RatesVSOffline_95.GetXaxis().SetRangeUser(Min_L1,Max_L1)
RatesVSOffline_95.SetLineWidth(2)
RatesVSOffline_95.SetMarkerColor(1)
RatesVSOffline_95.SetMarkerStyle(8)
RatesVSOffline_95.SetLineColor(1)
RatesVSOffline_95.Draw()

Tex31 = ROOT.TLatex()
Tex31.SetTextSize(0.03)
Tex31.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
Tex31.Draw("same")

Tex32 = ROOT.TLatex()
Tex32.SetTextSize(0.035)
Tex32.SetTextAlign(31)
Tex32.DrawLatexNDC(0.90,0.91,"(14 TeV)")
Tex32.Draw("same")

canvas3.SaveAs(Rates_folder_png+"/RatesVSOffline_95.png")
canvas3.SaveAs(Rates_folder_pdf+"/RatesVSOffline_95.pdf")

#Rates for 90% efficiency

RatesVSOffline_90 = ROOT.TGraphErrors(len(Offline_cuts_90), Offline_cuts_90, Rates)
RatesVSOnline = ROOT.TGraphErrors(len(L1_cuts), L1_cuts, Rates)

canvas4 = ROOT.TCanvas("c_4","c_4",800,800)
canvas4.SetGrid(10,10)
canvas4.SetLogy()
RatesVSOffline_90.SetTitle("")
RatesVSOffline_90.GetXaxis().SetTitle("p_{T}^{Offline}(jet)")
RatesVSOffline_90.GetYaxis().SetTitle("Rates [kHz]")
RatesVSOffline_90.GetYaxis().SetRangeUser(0.1,1.3*max(Rates))
RatesVSOffline_90.GetXaxis().SetRangeUser(Min_L1,Max_L1)
RatesVSOffline_90.SetLineWidth(2)
RatesVSOffline_90.SetMarkerColor(1)
RatesVSOffline_90.SetMarkerStyle(8)
RatesVSOffline_90.SetLineColor(1)
RatesVSOffline_90.Draw()

Tex41 = ROOT.TLatex()
Tex41.SetTextSize(0.03)
Tex41.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
Tex41.Draw("same")

Tex42 = ROOT.TLatex()
Tex42.SetTextSize(0.035)
Tex42.SetTextAlign(31)
Tex42.DrawLatexNDC(0.90,0.91,"(14 TeV)")
Tex42.Draw("same")

canvas4.SaveAs(Rates_folder_png+"/RatesVSOffline_90.png")
canvas4.SaveAs(Rates_folder_pdf+"/RatesVSOffline_90.pdf")

#Rates for 90% efficiency

RatesVSOffline_50 = ROOT.TGraphErrors(len(Offline_cuts_50), Offline_cuts_50, Rates)
RatesVSOnline = ROOT.TGraphErrors(len(L1_cuts), L1_cuts, Rates)

canvas5 = ROOT.TCanvas("c_5","c_5",800,800)
canvas5.SetGrid(10,10)
canvas5.SetLogy()
RatesVSOffline_50.SetTitle("")
RatesVSOffline_50.GetXaxis().SetTitle("p_{T}^{Offline}(jet)")
RatesVSOffline_50.GetYaxis().SetTitle("Rates [kHz]")
RatesVSOffline_50.GetYaxis().SetRangeUser(0.1,1.3*max(Rates))
RatesVSOffline_50.GetXaxis().SetRangeUser(Min_L1,Max_L1)
RatesVSOffline_50.SetLineWidth(2)
RatesVSOffline_50.SetMarkerColor(1)
RatesVSOffline_50.SetMarkerStyle(8)
RatesVSOffline_50.SetLineColor(1)
RatesVSOffline_50.Draw()

Tex51 = ROOT.TLatex()
Tex51.SetTextSize(0.03)
Tex51.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
Tex51.Draw("same")

Tex52 = ROOT.TLatex()
Tex52.SetTextSize(0.035)
Tex52.SetTextAlign(31)
Tex52.DrawLatexNDC(0.90,0.91,"(14 TeV)")
Tex52.Draw("same")

canvas5.SaveAs(Rates_folder_png+"/RatesVSOffline_50.png")
canvas5.SaveAs(Rates_folder_pdf+"/RatesVSOffline_50.pdf")

#saving root graphs
fileout = ROOT.TFile(ROOTs_folder + "/Rate_"+label+".root","RECREATE")
fileout.WriteObject(RatesVSOffline_95, "RatesVSOffline_95")
fileout.WriteObject(RatesVSOffline_90, "RatesVSOffline_90")
fileout.WriteObject(RatesVSOffline_50, "RatesVSOffline_50")
fileout.WriteObject(RatesVSOnline, "RatesVSOnline")
fileout.Close()
