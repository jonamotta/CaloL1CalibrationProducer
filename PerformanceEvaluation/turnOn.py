from array import array
import numpy as np
import ROOT
import sys
import os

#print('cmd entry:', sys.argv)

#reading input parameters
directory = sys.argv[1]
nevents = int(sys.argv[2])
label = sys.argv[3]

os.system('mkdir -p PDFs/'+label)
os.system('mkdir -p ROOTs/')

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
bins = [0, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 100, 120, 150, 180, 250]

#list the ET thresholds to be tested
thresholds = np.linspace(20,100,81).tolist()
thresholds.append(120)
thresholds.append(150)

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
    entry3 = genTree.GetEntry(i)

    L1_nJets = emuTree.L1Upgrade.nJets
    Gen_nJets = genTree.Generator.nJet

    #loop on generator jets
    for igenJet in range(0,Gen_nJets):

        Gen_jet = ROOT.TLorentzVector()
        Gen_jet.SetPtEtaPhiM(genTree.Generator.jetPt[igenJet], genTree.Generator.jetEta[igenJet], genTree.Generator.jetPhi[igenJet], 0)

        #reject very soft jets, usually poorly defined
        if ("HCAL" in label) and Gen_jet.Pt()<15.: continue

        total.Fill(Gen_jet.Pt())
        pt.Fill(Gen_jet.Pt())

        matched = False
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
        for i,ele in enumerate(thresholds): 
            if matched and highestL1Pt>float(ele): passing[i].Fill(Gen_jet.Pt())

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

empty.Draw()
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

canvas.SaveAs("PDFs/"+label+"/turnOn_"+label+".pdf")
#canvas.SaveAs("turnOn_"+label+".root")

print("saving histograms and efficiencies in root file for later plotting if desired")
fileout = ROOT.TFile("ROOTs/efficiency_graphs_"+label+".root","RECREATE")
total.Write()
pt.Write()
for i,ele in enumerate(thresholds): 
    passing[i].Write()
    turnons[i].Write()

fileout.Close()
