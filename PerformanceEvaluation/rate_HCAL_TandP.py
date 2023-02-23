from array import array
import numpy as np
import pickle
import ROOT
ROOT.gROOT.SetBatch(True)
import sys
import os

def load_obj(source):
    with open(source,'rb') as f:
        return pickle.load(f)

#print('cmd entry:', sys.argv)

#reading input parameters
inName = sys.argv[1]
nevents = int(sys.argv[2])
label = sys.argv[3]
emu = int(sys.argv[4])
if len(sys.argv)>=6:
    offline = sys.argv[5]
else:
    offline = False

os.system('mkdir -p PDFs/'+label)
os.system('mkdir -p PNGs/'+label)
os.system('mkdir -p ROOTs/')

# inName = "/data_CMS/cms/davignon/Layer1SFsNtuples/Rate/Run362616_newLayer1SFs/Tot_Ntuple_Rate_Run362616_newL1SFs.root" # --> emulated is "new SFs"
# inName = "/data_CMS/cms/davignon/Layer1SFsNtuples/Rate/Run362616_noCalib/Tot_Ntuple_Rate_Run362616_noCalib.root" # --> unpacked is old
                                                                                                                   # --> emulated is no calib

inFile = ROOT.TFile(inName, "READ")
inTree = inFile.Get("ZeroBias/ZeroBias");
# inTree.SetBranchAddress("l1tPtJet",     PtJet);
# inTree.SetBranchAddress("l1tEtaJet",    EtaJet);
# inTree.SetBranchAddress("l1tEmuPtJet",  EmuPtJet);
# inTree.SetBranchAddress("l1tEmuEtaJet", EmuEtaJet);
# inTree.SetBranchAddress("l1tEGPt",      EGPt);
# inTree.SetBranchAddress("l1tEGEta",     EGEta);
# inTree.SetBranchAddress("l1tEmuEGPt",   EmuEGPt);
# inTree.SetBranchAddress("l1tEmuEGEta",  EmuEGEta);

nEntries = inTree.GetEntries()
print(nEntries, "entries")

#run on entries specified by usuer, or only on entries available if that is exceeded
if (nevents > nEntries) or (nevents==-1): nevents = nEntries
print("will process",nevents,"events...")

thresholds = [0, 20, 35, 50, 100, 150]

denominator = 0.
nb = 2544.
scale = 0.001*(nb*11245.6)

#dummy histogram for plotting
empty = ROOT.TH1F("empty","empty",240,0.,240.)
empty1 = ROOT.TH1F("empty1","empty1",240,0.,240.)

ptProgression0 = ROOT.TH1F("ptProgression0","ptProgression0",240,0.,240.)
ptProgression20 = ROOT.TH1F("ptProgression20","ptProgression20",240,0.,240.)
ptProgression35 = ROOT.TH1F("ptProgression35","ptProgression35",240,0.,240.)
ptProgression50 = ROOT.TH1F("ptProgression50","ptProgression50",240,0.,240.)
ptProgression100 = ROOT.TH1F("ptProgression100","ptProgression100",240,0.,240.)
ptProgression150 = ROOT.TH1F("ptProgression150","ptProgression150",240,0.,240.)

ptDiProgression0 = ROOT.TH2F("ptDiProgression0","ptDiProgression0",240,0.,240.,240,0.,240.)
ptDiProgression20 = ROOT.TH2F("ptDiProgression20","ptDiProgression20",240,0.,240.,240,0.,240.)
ptDiProgression35 = ROOT.TH2F("ptDiProgression35","ptDiProgression35",240,0.,240.,240,0.,240.)
ptDiProgression50 = ROOT.TH2F("ptDiProgression50","ptDiProgression50",240,0.,240.,240,0.,240.)
ptDiProgression100 = ROOT.TH2F("ptDiProgression100","ptDiProgression100",240,0.,240.,240,0.,240.)
ptDiProgression150 = ROOT.TH2F("ptDiProgression150","ptDiProgression150",240,0.,240.,240,0.,240.)

rateProgression0 = ROOT.TH1F("rateProgression0","rateProgression0",240,0.,240.)
rateProgression20 = ROOT.TH1F("rateProgression20","rateProgression20",240,0.,240.)
rateProgression35 = ROOT.TH1F("rateProgression35","rateProgression35",240,0.,240.)
rateProgression50 = ROOT.TH1F("rateProgression50","rateProgression50",240,0.,240.)
rateProgression100 = ROOT.TH1F("rateProgression100","rateProgression100",240,0.,240.)
rateProgression150 = ROOT.TH1F("rateProgression150","rateProgression150",240,0.,240.)

rateDiProgression0 = ROOT.TH1F("rateDiProgression0","rateDiProgression0",240,0.,240.)
rateDiProgression20 = ROOT.TH1F("rateDiProgression20","rateDiProgression20",240,0.,240.)
rateDiProgression35 = ROOT.TH1F("rateDiProgression35","rateDiProgression35",240,0.,240.)
rateDiProgression50 = ROOT.TH1F("rateDiProgression50","rateDiProgression50",240,0.,240.)
rateDiProgression100 = ROOT.TH1F("rateDiProgression100","rateDiProgression100",240,0.,240.)
rateDiProgression150 = ROOT.TH1F("rateDiProgression150","rateDiProgression150",240,0.,240.)

ptProgression0er2p5 = ROOT.TH1F("ptProgression0er2p5","ptProgression0er2p5",240,0.,240.)
ptProgression20er2p5 = ROOT.TH1F("ptProgression20er2p5","ptProgression20er2p5",240,0.,240.)
ptProgression35er2p5 = ROOT.TH1F("ptProgression35er2p5","ptProgression35er2p5",240,0.,240.)
ptProgression50er2p5 = ROOT.TH1F("ptProgression50er2p5","ptProgression50er2p5",240,0.,240.)
ptProgression100er2p5 = ROOT.TH1F("ptProgression100er2p5","ptProgression100er2p5",240,0.,240.)
ptProgression150er2p5 = ROOT.TH1F("ptProgression150er2p5","ptProgression150er2p5",240,0.,240.)

ptDiProgression0er2p5 = ROOT.TH2F("ptDiProgression0er2p5","ptDiProgression0er2p5",240,0.,240.,240,0.,240.)
ptDiProgression20er2p5 = ROOT.TH2F("ptDiProgression20er2p5","ptDiProgression20er2p5",240,0.,240.,240,0.,240.)
ptDiProgression35er2p5 = ROOT.TH2F("ptDiProgression35er2p5","ptDiProgression35er2p5",240,0.,240.,240,0.,240.)
ptDiProgression50er2p5 = ROOT.TH2F("ptDiProgression50er2p5","ptDiProgression50er2p5",240,0.,240.,240,0.,240.)
ptDiProgression100er2p5 = ROOT.TH2F("ptDiProgression100er2p5","ptDiProgression100er2p5",240,0.,240.,240,0.,240.)
ptDiProgression150er2p5 = ROOT.TH2F("ptDiProgression150er2p5","ptDiProgression150er2p5",240,0.,240.,240,0.,240.)

rateProgression0er2p5 = ROOT.TH1F("rateProgression0er2p5","rateProgression0er2p5",240,0.,240.)
rateProgression20er2p5 = ROOT.TH1F("rateProgression20er2p5","rateProgression20er2p5",240,0.,240.)
rateProgression35er2p5 = ROOT.TH1F("rateProgression35er2p5","rateProgression35er2p5",240,0.,240.)
rateProgression50er2p5 = ROOT.TH1F("rateProgression50er2p5","rateProgression50er2p5",240,0.,240.)
rateProgression100er2p5 = ROOT.TH1F("rateProgression100er2p5","rateProgression100er2p5",240,0.,240.)
rateProgression150er2p5 = ROOT.TH1F("rateProgression150er2p5","rateProgression150er2p5",240,0.,240.)

rateDiProgression0er2p5 = ROOT.TH1F("rateDiProgression0er2p5","rateDiProgression0er2p5",240,0.,240.)
rateDiProgression20er2p5 = ROOT.TH1F("rateDiProgression20er2p5","rateDiProgression20er2p5",240,0.,240.)
rateDiProgression35er2p5 = ROOT.TH1F("rateDiProgression35er2p5","rateDiProgression35er2p5",240,0.,240.)
rateDiProgression50er2p5 = ROOT.TH1F("rateDiProgression50er2p5","rateDiProgression50er2p5",240,0.,240.)
rateDiProgression100er2p5 = ROOT.TH1F("rateDiProgression100er2p5","rateDiProgression100er2p5",240,0.,240.)
rateDiProgression150er2p5 = ROOT.TH1F("rateDiProgression150er2p5","rateDiProgression150er2p5",240,0.,240.)

mapping_dict = load_obj('ROOTs/online2offline_mapping_'+label+'.pkl')
online_thresholds = np.linspace(20,150,131).tolist()

print("looping on events")
for i in range(0, nevents):
    if i%1000==0: print(i)
    #getting entries
    entry = inTree.GetEntry(i)

    # restrict to nominal lumiPOG 47 PU +-5
    # (this distribution will be very unrealistic!! Need to "gaussianize it")
    #if eventTree.Event.nPV_True < 42 or eventTree.Event.nPV_True > 52: continue

    denominator += 1.

    filledProgression0  = False
    filledProgression20  = False
    filledProgression35  = False
    filledProgression50  = False
    filledProgression100 = False
    filledProgression150 = False

    IndexJetsProgression0 = array('f',[-1,-1])
    ptJetsProgression0 = array('f',[-99.,-99.])

    IndexJetsProgression20 = array('f',[-1,-1])
    ptJetsProgression20 = array('f',[-99.,-99.])

    IndexJetsProgression35 = array('f',[-1,-1])
    ptJetsProgression35 = array('f',[-99.,-99.])

    IndexJetsProgression50 = array('f',[-1,-1])
    ptJetsProgression50 = array('f',[-99.,-99.])

    IndexJetsProgression100 = array('f',[-1,-1])
    ptJetsProgression100 = array('f',[-99.,-99.])

    IndexJetsProgression150 = array('f',[-1,-1])
    ptJetsProgression150 = array('f',[-99.,-99.])


    filledProgression0er2p5  = False
    filledProgression20er2p5  = False
    filledProgression35er2p5  = False
    filledProgression50er2p5  = False
    filledProgression100er2p5 = False
    filledProgression150er2p5 = False

    IndexJetsProgression0er2p5 = array('f',[-1,-1])
    ptJetsProgression0er2p5 = array('f',[-99.,-99.])

    IndexJetsProgression20er2p5 = array('f',[-1,-1])
    ptJetsProgression20er2p5 = array('f',[-99.,-99.])

    IndexJetsProgression35er2p5 = array('f',[-1,-1])
    ptJetsProgression35er2p5 = array('f',[-99.,-99.])

    IndexJetsProgression50er2p5 = array('f',[-1,-1])
    ptJetsProgression50er2p5 = array('f',[-99.,-99.])

    IndexJetsProgression100er2p5 = array('f',[-1,-1])
    ptJetsProgression100er2p5 = array('f',[-99.,-99.])

    IndexJetsProgression150er2p5 = array('f',[-1,-1])
    ptJetsProgression150er2p5 = array('f',[-99.,-99.])

    if emu: L1_nJets = len(inTree.l1tEmuEtaJet)
    else:   L1_nJets = len(inTree.l1tEtaJet)

    #loop on L1 jets to find match
    for ijet in range(0, L1_nJets):
        
        if emu:
            JetPt = inTree.l1tEmuPtJet[ijet]
            JetEta = inTree.l1tEmuEtaJet[ijet]
        else:
            JetPt = inTree.l1tPtJet[ijet]
            JetEta = inTree.l1tEtaJet[ijet]

        # single
        if filledProgression0==False:
            if offline: ptProgression0.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
            else:       ptProgression0.Fill(JetPt)
            filledProgression0 = True

        # di
        if JetPt>=ptJetsProgression0[0]:
            IndexJetsProgression0[1]=IndexJetsProgression0[0]
            ptJetsProgression0[1]=ptJetsProgression0[0]
            IndexJetsProgression0[0]=ijet
            ptJetsProgression0[0]=JetPt
        elif JetPt>=ptJetsProgression0[1]:
            IndexJetsProgression0[1]=ijet
            ptJetsProgression0[1]=JetPt

        if JetPt>20:
            # single
            if filledProgression20==False:
                if offline: ptProgression20.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression20.Fill(JetPt)
                filledProgression20 = True

            # di
            if JetPt>=ptJetsProgression20[0]:
                IndexJetsProgression20[1]=IndexJetsProgression20[0]
                ptJetsProgression20[1]=ptJetsProgression20[0]
                IndexJetsProgression20[0]=ijet
                ptJetsProgression20[0]=JetPt
            elif JetPt>=ptJetsProgression20[1]:
                IndexJetsProgression20[1]=ijet
                ptJetsProgression20[1]=JetPt


        if JetPt>35:
            # single
            if filledProgression35==False:
                if offline: ptProgression35.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression35.Fill(JetPt)
                filledProgression35 = True

            # di
            if JetPt>=ptJetsProgression35[0]:
                IndexJetsProgression35[1]=IndexJetsProgression35[0]
                ptJetsProgression35[1]=ptJetsProgression35[0]
                IndexJetsProgression35[0]=ijet
                ptJetsProgression35[0]=JetPt
            elif JetPt>=ptJetsProgression35[1]:
                IndexJetsProgression35[1]=ijet
                ptJetsProgression35[1]=JetPt

        if JetPt>50:
            # single
            if filledProgression50==False:
                if offline: ptProgression50.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression50.Fill(JetPt)
                filledProgression50 = True

            # di
            if JetPt>=ptJetsProgression50[0]:
                IndexJetsProgression50[1]=IndexJetsProgression50[0]
                ptJetsProgression50[1]=ptJetsProgression50[0]
                IndexJetsProgression50[0]=ijet
                ptJetsProgression50[0]=JetPt
            elif JetPt>=ptJetsProgression50[1]:
                IndexJetsProgression50[1]=ijet
                ptJetsProgression50[1]=JetPt

        if JetPt>100:
            # single
            if filledProgression100==False:
                if offline: ptProgression100.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression100.Fill(JetPt)
                filledProgression100 = True

            # di
            if JetPt>=ptJetsProgression100[0]:
                IndexJetsProgression100[1]=IndexJetsProgression100[0]
                ptJetsProgression100[1]=ptJetsProgression100[0]
                IndexJetsProgression100[0]=ijet
                ptJetsProgression100[0]=JetPt
            elif JetPt>=ptJetsProgression100[1]:
                IndexJetsProgression100[1]=ijet
                ptJetsProgression100[1]=JetPt

        if JetPt>150:
            # single
            if filledProgression150==False:
                if offline: ptProgression150.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression150.Fill(JetPt)
                filledProgression150 = True

            # di
            if JetPt>=ptJetsProgression150[0]:
                IndexJetsProgression150[1]=IndexJetsProgression150[0]
                ptJetsProgression150[1]=ptJetsProgression150[0]
                IndexJetsProgression150[0]=ijet
                ptJetsProgression150[0]=JetPt
            elif JetPt>=ptJetsProgression150[1]:
                IndexJetsProgression150[1]=ijet
                ptJetsProgression150[1]=JetPt

        # if abs(JetEta)>2.1315: continue;
        if abs(JetEta)>2.5000: continue

        # single
        if filledProgression0er2p5==False:
            if offline: ptProgression0er2p5.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
            else:       ptProgression0er2p5.Fill(JetPt)
            filledProgression0er2p5 = True

        # di
        if JetPt>=ptJetsProgression0er2p5[0]:
            IndexJetsProgression0er2p5[1]=IndexJetsProgression0er2p5[0]
            ptJetsProgression0er2p5[1]=ptJetsProgression0er2p5[0]
            IndexJetsProgression0er2p5[0]=ijet
            ptJetsProgression0er2p5[0]=JetPt
        elif JetPt>=ptJetsProgression0er2p5[1]:
            IndexJetsProgression0er2p5[1]=ijet
            ptJetsProgression0er2p5[1]=JetPt

        if JetPt>20:
            # single
            if filledProgression20er2p5==False:
                if offline: ptProgression20er2p5.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression20er2p5.Fill(JetPt)
                filledProgression20er2p5 = True

            # di
            if JetPt>=ptJetsProgression20er2p5[0]:
                IndexJetsProgression20er2p5[1]=IndexJetsProgression20er2p5[0]
                ptJetsProgression20er2p5[1]=ptJetsProgression20er2p5[0]
                IndexJetsProgression20er2p5[0]=ijet
                ptJetsProgression20er2p5[0]=JetPt
            elif JetPt>=ptJetsProgression20er2p5[1]:
                IndexJetsProgression20er2p5[1]=ijet
                ptJetsProgression20er2p5[1]=JetPt


        if JetPt>35:
            # single
            if filledProgression35er2p5==False:
                if offline: ptProgression35er2p5.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression35er2p5.Fill(JetPt)
                filledProgression35er2p5 = True

            # di
            if JetPt>=ptJetsProgression35er2p5[0]:
                IndexJetsProgression35er2p5[1]=IndexJetsProgression35er2p5[0]
                ptJetsProgression35er2p5[1]=ptJetsProgression35er2p5[0]
                IndexJetsProgression35er2p5[0]=ijet
                ptJetsProgression35er2p5[0]=JetPt
            elif JetPt>=ptJetsProgression35er2p5[1]:
                IndexJetsProgression35er2p5[1]=ijet
                ptJetsProgression35er2p5[1]=JetPt

        if JetPt>50:
            # single
            if filledProgression50er2p5==False:
                if offline: ptProgression50er2p5.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression50er2p5.Fill(JetPt)
                filledProgression50er2p5 = True

            # di
            if JetPt>=ptJetsProgression50er2p5[0]:
                IndexJetsProgression50er2p5[1]=IndexJetsProgression50er2p5[0]
                ptJetsProgression50er2p5[1]=ptJetsProgression50er2p5[0]
                IndexJetsProgression50er2p5[0]=ijet
                ptJetsProgression50er2p5[0]=JetPt
            elif JetPt>=ptJetsProgression50er2p5[1]:
                IndexJetsProgression50er2p5[1]=ijet
                ptJetsProgression50er2p5[1]=JetPt

        if JetPt>100:
            # single
            if filledProgression100er2p5==False:
                if offline: ptProgression100er2p5.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression100er2p5.Fill(JetPt)
                filledProgression100er2p5 = True

            # di
            if JetPt>=ptJetsProgression100er2p5[0]:
                IndexJetsProgression100er2p5[1]=IndexJetsProgression100er2p5[0]
                ptJetsProgression100er2p5[1]=ptJetsProgression100er2p5[0]
                IndexJetsProgression100er2p5[0]=ijet
                ptJetsProgression100er2p5[0]=JetPt
            elif JetPt>=ptJetsProgression100er2p5[1]:
                IndexJetsProgression100er2p5[1]=ijet
                ptJetsProgression100er2p5[1]=JetPt

        if JetPt>150:
            # single
            if filledProgression150er2p5==False:
                if offline: ptProgression150er2p5.Fill(np.interp(JetPt, online_thresholds, mapping_dict[offline]))
                else:       ptProgression150er2p5.Fill(JetPt)
                filledProgression150er2p5 = True

            # di
            if JetPt>=ptJetsProgression150er2p5[0]:
                IndexJetsProgression150er2p5[1]=IndexJetsProgression150er2p5[0]
                ptJetsProgression150er2p5[1]=ptJetsProgression150er2p5[0]
                IndexJetsProgression150er2p5[0]=ijet
                ptJetsProgression150er2p5[0]=JetPt
            elif JetPt>=ptJetsProgression150er2p5[1]:
                IndexJetsProgression150er2p5[1]=ijet
                ptJetsProgression150er2p5[1]=JetPt


        
    if IndexJetsProgression0[0]>=0 and IndexJetsProgression0[1]>=0:
        if offline: ptDiProgression0.Fill(np.interp(ptJetsProgression0[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression0[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression0.Fill(ptJetsProgression0[0],ptJetsProgression0[1])
    
    if IndexJetsProgression20[0]>=0 and IndexJetsProgression20[1]>=0:
        if offline: ptDiProgression20.Fill(np.interp(ptJetsProgression20[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression20[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression20.Fill(ptJetsProgression20[0],ptJetsProgression20[1])

    if IndexJetsProgression35[0]>=0 and IndexJetsProgression35[1]>=0:
        if offline: ptDiProgression35.Fill(np.interp(ptJetsProgression35[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression35[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression35.Fill(ptJetsProgression35[0],ptJetsProgression35[1])

    if IndexJetsProgression50[0]>=0 and IndexJetsProgression50[1]>=0:
        if offline: ptDiProgression50.Fill(np.interp(ptJetsProgression50[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression50[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression50.Fill(ptJetsProgression50[0],ptJetsProgression50[1])

    if IndexJetsProgression100[0]>=0 and IndexJetsProgression100[1]>=0:
        if offline: ptDiProgression100.Fill(np.interp(ptJetsProgression100[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression100[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression100.Fill(ptJetsProgression100[0],ptJetsProgression100[1])

    if IndexJetsProgression150[0]>=0 and IndexJetsProgression150[1]>=0:
        if offline: ptDiProgression150.Fill(np.interp(ptJetsProgression150[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression150[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression150.Fill(ptJetsProgression150[0],ptJetsProgression150[1])

    if IndexJetsProgression0er2p5[0]>=0 and IndexJetsProgression0er2p5[1]>=0:
        if offline: ptDiProgression0er2p5.Fill(np.interp(ptJetsProgression0er2p5[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression0er2p5[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression0er2p5.Fill(ptJetsProgression0er2p5[0],ptJetsProgression0er2p5[1])
    
    if IndexJetsProgression20er2p5[0]>=0 and IndexJetsProgression20er2p5[1]>=0:
        if offline: ptDiProgression20er2p5.Fill(np.interp(ptJetsProgression20er2p5[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression20er2p5[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression20er2p5.Fill(ptJetsProgression20er2p5[0],ptJetsProgression20er2p5[1])

    if IndexJetsProgression35er2p5[0]>=0 and IndexJetsProgression35er2p5[1]>=0:
        if offline: ptDiProgression35er2p5.Fill(np.interp(ptJetsProgression35er2p5[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression35er2p5[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression35er2p5.Fill(ptJetsProgression35er2p5[0],ptJetsProgression35er2p5[1])

    if IndexJetsProgression50er2p5[0]>=0 and IndexJetsProgression50er2p5[1]>=0:
        if offline: ptDiProgression50er2p5.Fill(np.interp(ptJetsProgression50er2p5[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression50er2p5[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression50er2p5.Fill(ptJetsProgression50er2p5[0],ptJetsProgression50er2p5[1])

    if IndexJetsProgression100er2p5[0]>=0 and IndexJetsProgression100er2p5[1]>=0:
        if offline: ptDiProgression100er2p5.Fill(np.interp(ptJetsProgression100er2p5[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression100er2p5[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression100er2p5.Fill(ptJetsProgression100er2p5[0],ptJetsProgression100er2p5[1])

    if IndexJetsProgression150er2p5[0]>=0 and IndexJetsProgression150er2p5[1]>=0:
        if offline: ptDiProgression150er2p5.Fill(np.interp(ptJetsProgression150er2p5[0], online_thresholds, mapping_dict[offline]), np.interp(ptJetsProgression150er2p5[1], online_thresholds, mapping_dict[offline]))
        else:       ptDiProgression150er2p5.Fill(ptJetsProgression150er2p5[0],ptJetsProgression150er2p5[1])


for i in range(0,241):
    rateProgression0.SetBinContent(i+1,ptProgression0.Integral(i+1,241)/denominator*scale);
    rateProgression20.SetBinContent(i+1,ptProgression20.Integral(i+1,241)/denominator*scale);
    rateProgression35.SetBinContent(i+1,ptProgression35.Integral(i+1,241)/denominator*scale);
    rateProgression50.SetBinContent(i+1,ptProgression50.Integral(i+1,241)/denominator*scale);
    rateProgression100.SetBinContent(i+1,ptProgression100.Integral(i+1,241)/denominator*scale);
    rateProgression150.SetBinContent(i+1,ptProgression150.Integral(i+1,241)/denominator*scale);

    rateDiProgression0.SetBinContent(i+1,ptDiProgression0.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression20.SetBinContent(i+1,ptDiProgression20.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression35.SetBinContent(i+1,ptDiProgression35.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression50.SetBinContent(i+1,ptDiProgression50.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression100.SetBinContent(i+1,ptDiProgression100.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression150.SetBinContent(i+1,ptDiProgression150.Integral(i+1,241,i+1,241)/denominator*scale);

    rateProgression0er2p5.SetBinContent(i+1,ptProgression0er2p5.Integral(i+1,241)/denominator*scale);
    rateProgression20er2p5.SetBinContent(i+1,ptProgression20er2p5.Integral(i+1,241)/denominator*scale);
    rateProgression35er2p5.SetBinContent(i+1,ptProgression35er2p5.Integral(i+1,241)/denominator*scale);
    rateProgression50er2p5.SetBinContent(i+1,ptProgression50er2p5.Integral(i+1,241)/denominator*scale);
    rateProgression100er2p5.SetBinContent(i+1,ptProgression100er2p5.Integral(i+1,241)/denominator*scale);
    rateProgression150er2p5.SetBinContent(i+1,ptProgression150er2p5.Integral(i+1,241)/denominator*scale);

    rateDiProgression0er2p5.SetBinContent(i+1,ptDiProgression0er2p5.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression20er2p5.SetBinContent(i+1,ptDiProgression20er2p5.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression35er2p5.SetBinContent(i+1,ptDiProgression35er2p5.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression50er2p5.SetBinContent(i+1,ptDiProgression50er2p5.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression100er2p5.SetBinContent(i+1,ptDiProgression100er2p5.Integral(i+1,241,i+1,241)/denominator*scale);
    rateDiProgression150er2p5.SetBinContent(i+1,ptDiProgression150er2p5.Integral(i+1,241,i+1,241)/denominator*scale);

ptProgressions = []
ptProgressions.append(ptProgression0)
ptProgressions.append(ptProgression20)
ptProgressions.append(ptProgression35)
ptProgressions.append(ptProgression50)
ptProgressions.append(ptProgression100)
ptProgressions.append(ptProgression150)
ptDiProgressions = []
ptDiProgressions.append(ptDiProgression0)
ptDiProgressions.append(ptDiProgression20)
ptDiProgressions.append(ptDiProgression35)
ptDiProgressions.append(ptDiProgression50)
ptDiProgressions.append(ptDiProgression100)
ptDiProgressions.append(ptDiProgression150)

ptProgressionsEr2p5 = []
ptProgressionsEr2p5.append(ptProgression0er2p5)
ptProgressionsEr2p5.append(ptProgression20er2p5)
ptProgressionsEr2p5.append(ptProgression35er2p5)
ptProgressionsEr2p5.append(ptProgression50er2p5)
ptProgressionsEr2p5.append(ptProgression100er2p5)
ptProgressionsEr2p5.append(ptProgression150er2p5)
ptDiProgressionsEr2p5 = []
ptDiProgressionsEr2p5.append(ptDiProgression0er2p5)
ptDiProgressionsEr2p5.append(ptDiProgression20er2p5)
ptDiProgressionsEr2p5.append(ptDiProgression35er2p5)
ptDiProgressionsEr2p5.append(ptDiProgression50er2p5)
ptDiProgressionsEr2p5.append(ptDiProgression100er2p5)
ptDiProgressionsEr2p5.append(ptDiProgression150er2p5)

rateCurves = []
rateCurves.append(rateProgression0)
rateCurves.append(rateProgression20)
rateCurves.append(rateProgression35)
rateCurves.append(rateProgression50)
rateCurves.append(rateProgression100)
rateCurves.append(rateProgression150)
rateDiCurves = []
rateDiCurves.append(rateDiProgression0)
rateDiCurves.append(rateDiProgression20)
rateDiCurves.append(rateDiProgression35)
rateDiCurves.append(rateDiProgression50)
rateDiCurves.append(rateDiProgression100)
rateDiCurves.append(rateDiProgression150)

rateCurvesEr2p5 = []
rateCurvesEr2p5.append(rateProgression0er2p5)
rateCurvesEr2p5.append(rateProgression20er2p5)
rateCurvesEr2p5.append(rateProgression35er2p5)
rateCurvesEr2p5.append(rateProgression50er2p5)
rateCurvesEr2p5.append(rateProgression100er2p5)
rateCurvesEr2p5.append(rateProgression150er2p5)
rateDiCurvesEr2p5 = []
rateDiCurvesEr2p5.append(rateDiProgression0er2p5)
rateDiCurvesEr2p5.append(rateDiProgression20er2p5)
rateDiCurvesEr2p5.append(rateDiProgression35er2p5)
rateDiCurvesEr2p5.append(rateDiProgression50er2p5)
rateDiCurvesEr2p5.append(rateDiProgression100er2p5)
rateDiCurvesEr2p5.append(rateDiProgression150er2p5)

print("SingleObj60 rate = ", rateProgression0.GetBinContent(61))
print("DoubleObj60 rate = ", rateDiProgression0.GetBinContent(61))

print("SingleObj60er2p5 rate = ", rateProgression0er2p5.GetBinContent(61))
print("DoubleObj60er2p5 rate = ", rateDiProgression0er2p5.GetBinContent(61))

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty.GetXaxis().SetTitle("p_{T}^{L1}(jet) [GeV]")
empty.SetTitle("")

empty.GetXaxis().SetRangeUser(0.,240.);
empty.GetYaxis().SetRangeUser(0.1,1e5);

empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("Rate [kHz]");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);

empty.Draw()

for i,ele in enumerate(thresholds):
    rateCurves[i].SetLineWidth(2)
    rateCurves[i].SetMarkerColor(i+1)
    rateCurves[i].SetLineColor(i+1)
    rateCurves[i].Draw("same")

legend = ROOT.TLegend(0.55,0.65,0.88,0.88)
legend.SetBorderSize(0)
for i,ele in enumerate(thresholds):
    legend.AddEntry(rateCurves[i],"Single-Obj rate @ p_{T}^{L1} > "+str(thresholds[i])+" GeV","LPE")
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

if offline:
    canvas.SaveAs("PDFs/"+label+"/rateSingleObj_"+label+"_"+offline+".pdf")
    canvas.SaveAs("PNGs/"+label+"/rateSingleObj_"+label+"_"+offline+".png")
else:
    canvas.SaveAs("PDFs/"+label+"/rateSingleObj_"+label+".pdf")
    canvas.SaveAs("PNGs/"+label+"/rateSingleObj_"+label+".png")

####################

#define canvas for plotting
canvas1 = ROOT.TCanvas("c1","c1",800,800)
canvas1.SetGrid(10,10);
canvas1.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("p_{T}^{L1}(jet) [GeV]")
empty1.SetTitle("")

empty1.GetXaxis().SetRangeUser(0.,240.);
empty1.GetYaxis().SetRangeUser(0.1,1e5);

empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

for i,ele in enumerate(thresholds):
    rateDiCurves[i].SetLineWidth(2)
    rateDiCurves[i].SetMarkerColor(i+1)
    rateDiCurves[i].SetLineColor(i+1)
    rateDiCurves[i].Draw("same")

legend1 = ROOT.TLegend(0.55,0.65,0.88,0.88)
legend1.SetBorderSize(0)
for i,ele in enumerate(thresholds):
    legend1.AddEntry(rateDiCurves[i],"Di-Obj rate @ p_{T}^{L1} > "+str(thresholds[i])+" GeV (both jets)","LPE")
legend1.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

if offline:
    canvas1.SaveAs("PDFs/"+label+"/rateDiObj_"+label+"_"+offline+".pdf")
    canvas1.SaveAs("PNGs/"+label+"/rateDiObj_"+label+"_"+offline+".png")
else:
    canvas1.SaveAs("PDFs/"+label+"/rateDiObj_"+label+".pdf")
    canvas1.SaveAs("PNGs/"+label+"/rateDiObj_"+label+".png")

####################

#define canvas for plotting
canvas2 = ROOT.TCanvas("c2","c2",800,800)
canvas2.SetGrid(10,10);
canvas2.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("p_{T}^{L1}(jet) [GeV]")
empty1.SetTitle("")

empty1.GetXaxis().SetRangeUser(0.,240.);
empty1.GetYaxis().SetRangeUser(0.1,1e5);

empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

# for i,ele in enumerate(thresholds):
#     rateCurves[i].SetLineWidth(2)
#     rateCurves[i].SetLineColor(1)
#     rateCurves[i].Draw("same")

# for i,ele in enumerate(thresholds):
#     rateDiCurves[i].SetLineWidth(2)
#     rateDiCurves[i].SetLineColor(2)
#     rateDiCurves[i].Draw("same")

rateCurves[0].SetLineWidth(2)
rateCurves[0].SetMarkerColor(1)
rateCurves[0].SetLineColor(1)
rateCurves[0].Draw("same")

rateDiCurves[0].SetLineWidth(2)
rateDiCurves[0].SetMarkerColor(2)
rateDiCurves[0].SetLineColor(2)
rateDiCurves[0].Draw("same")

legend2 = ROOT.TLegend(0.55,0.80,0.88,0.88)
legend2.SetBorderSize(0)
legend2.AddEntry(rateCurves[0],"Single-Obj rate","LPE")
legend2.AddEntry(rateDiCurves[0],"Di-Obj rate","LPE")
legend2.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

if offline:
    canvas2.SaveAs("PDFs/"+label+"/rate_"+label+"_"+offline+".pdf")
    canvas2.SaveAs("PNGs/"+label+"/rate_"+label+"_"+offline+".png")
else:
    canvas2.SaveAs("PDFs/"+label+"/rate_"+label+".pdf")
    canvas2.SaveAs("PNGs/"+label+"/rate_"+label+".png")

####################

del canvas, canvas1, canvas2

#define canvas for plotting
canvas = ROOT.TCanvas("c","c",800,800)
canvas.SetGrid(10,10);
canvas.SetLogy()

#use dummy histogram to define style
empty.GetXaxis().SetTitle("p_{T}^{L1}(jet) [GeV]")
empty.SetTitle("")

empty.GetXaxis().SetRangeUser(0.,240.);
empty.GetYaxis().SetRangeUser(0.1,1e5);

empty.GetXaxis().SetTitleOffset(1.3);
empty.GetYaxis().SetTitle("Rate [kHz]");
empty.GetYaxis().SetTitleOffset(1.3);
empty.SetTitle("");
empty.SetStats(0);

empty.Draw()

for i,ele in enumerate(thresholds):
    rateCurvesEr2p5[i].SetLineWidth(2)
    rateCurvesEr2p5[i].SetMarkerColor(i+1)
    rateCurvesEr2p5[i].SetLineColor(i+1)
    rateCurvesEr2p5[i].Draw("same")

legend = ROOT.TLegend(0.55,0.65,0.88,0.88)
legend.SetBorderSize(0)
legend.SetHeader("|#eta|<2.5")
for i,ele in enumerate(thresholds):
    legend.AddEntry(rateCurvesEr2p5[i],"Single-Obj rate @ p_{T}^{L1} > "+str(thresholds[i])+" GeV","LPE")
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

if offline:
    canvas.SaveAs("PDFs/"+label+"/rateSingleObjEr2p5_"+label+"_"+offline+".pdf")
    canvas.SaveAs("PNGs/"+label+"/rateSingleObjEr2p5_"+label+"_"+offline+".png")
else:
    canvas.SaveAs("PDFs/"+label+"/rateSingleObjEr2p5_"+label+".pdf")
    canvas.SaveAs("PNGs/"+label+"/rateSingleObjEr2p5_"+label+".png")

####################

#define canvas for plotting
canvas1 = ROOT.TCanvas("c1","c1",800,800)
canvas1.SetGrid(10,10);
canvas1.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("p_{T}^{L1}(jet) [GeV]")
empty1.SetTitle("")

empty1.GetXaxis().SetRangeUser(0.,240.);
empty1.GetYaxis().SetRangeUser(0.1,1e5);

empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

for i,ele in enumerate(thresholds):
    rateDiCurvesEr2p5[i].SetLineWidth(2)
    rateDiCurvesEr2p5[i].SetMarkerColor(i+1)
    rateDiCurvesEr2p5[i].SetLineColor(i+1)
    rateDiCurvesEr2p5[i].Draw("same")

legend1 = ROOT.TLegend(0.55,0.65,0.88,0.88)
legend1.SetBorderSize(0)
legend.SetHeader("|#eta|<2.5")
for i,ele in enumerate(thresholds):
    legend1.AddEntry(rateDiCurvesEr2p5[i],"Di-Obj rate @ p_{T}^{L1} > "+str(thresholds[i])+" GeV (both jets)","LPE")
legend1.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

if offline:
    canvas1.SaveAs("PDFs/"+label+"/rateDiObjEr2p5_"+label+"_"+offline+".pdf")
    canvas1.SaveAs("PNGs/"+label+"/rateDiObjEr2p5_"+label+"_"+offline+".png")
else:
    canvas1.SaveAs("PDFs/"+label+"/rateDiObjEr2p5_"+label+".pdf")
    canvas1.SaveAs("PNGs/"+label+"/rateDiObjEr2p5_"+label+".png")

####################

#define canvas for plotting
canvas2 = ROOT.TCanvas("c2","c2",800,800)
canvas2.SetGrid(10,10);
canvas2.SetLogy()

#use dummy histogram to define style
empty1.GetXaxis().SetTitle("p_{T}^{L1}(jet) [GeV]")
empty1.SetTitle("")

empty1.GetXaxis().SetRangeUser(0.,240.);
empty1.GetYaxis().SetRangeUser(0.1,1e5);

empty1.GetXaxis().SetTitleOffset(1.3);
empty1.GetYaxis().SetTitle("Rate [kHz]");
empty1.GetYaxis().SetTitleOffset(1.3);
empty1.SetTitle("");
empty1.SetStats(0);
empty1.Draw()

# for i,ele in enumerate(thresholds):
#     rateCurves[i].SetLineWidth(2)
#     rateCurves[i].SetLineColor(1)
#     rateCurves[i].Draw("same")

# for i,ele in enumerate(thresholds):
#     rateDiCurves[i].SetLineWidth(2)
#     rateDiCurves[i].SetLineColor(2)
#     rateDiCurves[i].Draw("same")

rateCurvesEr2p5[0].SetLineWidth(2)
rateCurvesEr2p5[0].SetMarkerColor(1)
rateCurvesEr2p5[0].SetLineColor(1)
rateCurvesEr2p5[0].Draw("same")

rateDiCurvesEr2p5[0].SetLineWidth(2)
rateDiCurvesEr2p5[0].SetMarkerColor(2)
rateDiCurvesEr2p5[0].SetLineColor(2)
rateDiCurvesEr2p5[0].Draw("same")

legend2 = ROOT.TLegend(0.55,0.80,0.88,0.88)
legend2.SetBorderSize(0)
legend.SetHeader("|#eta|<2.5")
legend2.AddEntry(rateCurvesEr2p5[0],"Single-Obj rate","LPE")
legend2.AddEntry(rateDiCurvesEr2p5[0],"Di-Obj rate","LPE")
legend2.Draw("same")

tex = ROOT.TLatex()
tex.SetTextSize(0.03);
tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
tex.Draw("same")

tex2 = ROOT.TLatex();
tex2.SetTextSize(0.035);
tex2.SetTextAlign(31);
tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
tex2.Draw("same");

if offline:
    canvas2.SaveAs("PDFs/"+label+"/rateEr2p5_"+label+"_"+offline+".pdf")
    canvas2.SaveAs("PNGs/"+label+"/rateEr2p5_"+label+"_"+offline+".png")
else:
    canvas2.SaveAs("PDFs/"+label+"/rateEr2p5_"+label+".pdf")
    canvas2.SaveAs("PNGs/"+label+"/rateEr2p5_"+label+".png")

####################

print("saving histograms and efficiencies in root file for later plotting if desired")
if offline: fileout = ROOT.TFile("ROOTs/rate_graphs_"+label+".root","RECREATE")
else:       fileout = ROOT.TFile("ROOTs/rate_graphs_"+label+"_"+offline+".root","RECREATE")
for i,ele in enumerate(thresholds): 
    rateCurves[i].Write()
    rateDiCurves[i].Write()
    ptProgressions[i].Write()
    ptDiProgressions[i].Write()
    rateCurvesEr2p5[i].Write()
    rateDiCurvesEr2p5[i].Write()
    ptProgressionsEr2p5[i].Write()
    ptDiProgressionsEr2p5[i].Write()

fileout.Close()






