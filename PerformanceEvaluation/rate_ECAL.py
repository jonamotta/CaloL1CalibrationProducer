from array import array
import ROOT
import sys
import os

#print('cmd entry:', sys.argv)

#reading input parameters
directory = sys.argv[1]
nevents = int(sys.argv[2])
label = sys.argv[3]

os.system('mkdir -p PDFs/'+label)
os.system('mkdir -p PNGs/'+label)
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

    filledProgression0  = False
    filledProgression20  = False
    filledProgression35  = False
    filledProgression50  = False
    filledProgression100 = False
    filledProgression150 = False

    IndexEGsProgression0 = array('f',[-1,-1])
    ptEGsProgression0 = array('f',[-99.,-99.])

    IndexEGsProgression20 = array('f',[-1,-1])
    ptEGsProgression20 = array('f',[-99.,-99.])

    IndexEGsProgression35 = array('f',[-1,-1])
    ptEGsProgression35 = array('f',[-99.,-99.])

    IndexEGsProgression50 = array('f',[-1,-1])
    ptEGsProgression50 = array('f',[-99.,-99.])

    IndexEGsProgression100 = array('f',[-1,-1])
    ptEGsProgression100 = array('f',[-99.,-99.])

    IndexEGsProgression150 = array('f',[-1,-1])
    ptEGsProgression150 = array('f',[-99.,-99.])


    filledProgression0er2p5  = False
    filledProgression20er2p5  = False
    filledProgression35er2p5  = False
    filledProgression50er2p5  = False
    filledProgression100er2p5 = False
    filledProgression150er2p5 = False

    IndexEGsProgression0er2p5 = array('f',[-1,-1])
    ptEGsProgression0er2p5 = array('f',[-99.,-99.])

    IndexEGsProgression20er2p5 = array('f',[-1,-1])
    ptEGsProgression20er2p5 = array('f',[-99.,-99.])

    IndexEGsProgression35er2p5 = array('f',[-1,-1])
    ptEGsProgression35er2p5 = array('f',[-99.,-99.])

    IndexEGsProgression50er2p5 = array('f',[-1,-1])
    ptEGsProgression50er2p5 = array('f',[-99.,-99.])

    IndexEGsProgression100er2p5 = array('f',[-1,-1])
    ptEGsProgression100er2p5 = array('f',[-99.,-99.])

    IndexEGsProgression150er2p5 = array('f',[-1,-1])
    ptEGsProgression150er2p5 = array('f',[-99.,-99.])

    L1_nEGs = emuTree.L1Upgrade.nEGs

    #loop on L1 jets to find match
    for iEG in range(0, L1_nEGs):
        
        # single
        if filledProgression0==False:
            ptProgression0.Fill(emuTree.L1Upgrade.egEt[iEG])
            filledProgression0 = True

        # di
        if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression0[0]:
            IndexEGsProgression0[1]=IndexEGsProgression0[0]
            ptEGsProgression0[1]=ptEGsProgression0[0]
            IndexEGsProgression0[0]=iEG
            ptEGsProgression0[0]=emuTree.L1Upgrade.egEt[iEG]
        elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression0[1]:
            IndexEGsProgression0[1]=iEG
            ptEGsProgression0[1]=emuTree.L1Upgrade.egEt[iEG]

        if emuTree.L1Upgrade.egEt[iEG]>20:
            # single
            if filledProgression20==False:
                ptProgression20.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression20 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression20[0]:
                IndexEGsProgression20[1]=IndexEGsProgression20[0]
                ptEGsProgression20[1]=ptEGsProgression20[0]
                IndexEGsProgression20[0]=iEG
                ptEGsProgression20[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression20[1]:
                IndexEGsProgression20[1]=iEG
                ptEGsProgression20[1]=emuTree.L1Upgrade.egEt[iEG]


        if emuTree.L1Upgrade.egEt[iEG]>35:
            # single
            if filledProgression35==False:
                ptProgression35.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression35 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression35[0]:
                IndexEGsProgression35[1]=IndexEGsProgression35[0]
                ptEGsProgression35[1]=ptEGsProgression35[0]
                IndexEGsProgression35[0]=iEG
                ptEGsProgression35[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression35[1]:
                IndexEGsProgression35[1]=iEG
                ptEGsProgression35[1]=emuTree.L1Upgrade.egEt[iEG]

        if emuTree.L1Upgrade.egEt[iEG]>50:
            # single
            if filledProgression50==False:
                ptProgression50.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression50 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression50[0]:
                IndexEGsProgression50[1]=IndexEGsProgression50[0]
                ptEGsProgression50[1]=ptEGsProgression50[0]
                IndexEGsProgression50[0]=iEG
                ptEGsProgression50[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression50[1]:
                IndexEGsProgression50[1]=iEG
                ptEGsProgression50[1]=emuTree.L1Upgrade.egEt[iEG]

        if emuTree.L1Upgrade.egEt[iEG]>100:
            # single
            if filledProgression100==False:
                ptProgression100.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression100 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression100[0]:
                IndexEGsProgression100[1]=IndexEGsProgression100[0]
                ptEGsProgression100[1]=ptEGsProgression100[0]
                IndexEGsProgression100[0]=iEG
                ptEGsProgression100[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression100[1]:
                IndexEGsProgression100[1]=iEG
                ptEGsProgression100[1]=emuTree.L1Upgrade.egEt[iEG]

        if emuTree.L1Upgrade.egEt[iEG]>150:
            # single
            if filledProgression150==False:
                ptProgression150.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression150 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression150[0]:
                IndexEGsProgression150[1]=IndexEGsProgression150[0]
                ptEGsProgression150[1]=ptEGsProgression150[0]
                IndexEGsProgression150[0]=iEG
                ptEGsProgression150[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression150[1]:
                IndexEGsProgression150[1]=iEG
                ptEGsProgression150[1]=emuTree.L1Upgrade.egEt[iEG]

        # if abs(emuTree.L1Upgrade.egEta[iEG])>2.1315: continue;
        if abs(emuTree.L1Upgrade.egEta[iEG])>2.5000: continue

        # single
        if filledProgression0er2p5==False:
            ptProgression0er2p5.Fill(emuTree.L1Upgrade.egEt[iEG])
            filledProgression0er2p5 = True

        # di
        if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression0er2p5[0]:
            IndexEGsProgression0er2p5[1]=IndexEGsProgression0er2p5[0]
            ptEGsProgression0er2p5[1]=ptEGsProgression0er2p5[0]
            IndexEGsProgression0er2p5[0]=iEG
            ptEGsProgression0er2p5[0]=emuTree.L1Upgrade.egEt[iEG]
        elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression0er2p5[1]:
            IndexEGsProgression0er2p5[1]=iEG
            ptEGsProgression0er2p5[1]=emuTree.L1Upgrade.egEt[iEG]

        if emuTree.L1Upgrade.egEt[iEG]>20:
            # single
            if filledProgression20er2p5==False:
                ptProgression20er2p5.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression20er2p5 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression20er2p5[0]:
                IndexEGsProgression20er2p5[1]=IndexEGsProgression20er2p5[0]
                ptEGsProgression20er2p5[1]=ptEGsProgression20er2p5[0]
                IndexEGsProgression20er2p5[0]=iEG
                ptEGsProgression20er2p5[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression20er2p5[1]:
                IndexEGsProgression20er2p5[1]=iEG
                ptEGsProgression20er2p5[1]=emuTree.L1Upgrade.egEt[iEG]


        if emuTree.L1Upgrade.egEt[iEG]>35:
            # single
            if filledProgression35er2p5==False:
                ptProgression35er2p5.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression35er2p5 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression35er2p5[0]:
                IndexEGsProgression35er2p5[1]=IndexEGsProgression35er2p5[0]
                ptEGsProgression35er2p5[1]=ptEGsProgression35er2p5[0]
                IndexEGsProgression35er2p5[0]=iEG
                ptEGsProgression35er2p5[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression35er2p5[1]:
                IndexEGsProgression35er2p5[1]=iEG
                ptEGsProgression35er2p5[1]=emuTree.L1Upgrade.egEt[iEG]

        if emuTree.L1Upgrade.egEt[iEG]>50:
            # single
            if filledProgression50er2p5==False:
                ptProgression50er2p5.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression50er2p5 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression50er2p5[0]:
                IndexEGsProgression50er2p5[1]=IndexEGsProgression50er2p5[0]
                ptEGsProgression50er2p5[1]=ptEGsProgression50er2p5[0]
                IndexEGsProgression50er2p5[0]=iEG
                ptEGsProgression50er2p5[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression50er2p5[1]:
                IndexEGsProgression50er2p5[1]=iEG
                ptEGsProgression50er2p5[1]=emuTree.L1Upgrade.egEt[iEG]

        if emuTree.L1Upgrade.egEt[iEG]>100:
            # single
            if filledProgression100er2p5==False:
                ptProgression100er2p5.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression100er2p5 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression100er2p5[0]:
                IndexEGsProgression100er2p5[1]=IndexEGsProgression100er2p5[0]
                ptEGsProgression100er2p5[1]=ptEGsProgression100er2p5[0]
                IndexEGsProgression100er2p5[0]=iEG
                ptEGsProgression100er2p5[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression100er2p5[1]:
                IndexEGsProgression100er2p5[1]=iEG
                ptEGsProgression100er2p5[1]=emuTree.L1Upgrade.egEt[iEG]

        if emuTree.L1Upgrade.egEt[iEG]>150:
            # single
            if filledProgression150er2p5==False:
                ptProgression150er2p5.Fill(emuTree.L1Upgrade.egEt[iEG])
                filledProgression150er2p5 = True

            # di
            if emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression150er2p5[0]:
                IndexEGsProgression150er2p5[1]=IndexEGsProgression150er2p5[0]
                ptEGsProgression150er2p5[1]=ptEGsProgression150er2p5[0]
                IndexEGsProgression150er2p5[0]=iEG
                ptEGsProgression150er2p5[0]=emuTree.L1Upgrade.egEt[iEG]
            elif emuTree.L1Upgrade.egEt[iEG]>=ptEGsProgression150er2p5[1]:
                IndexEGsProgression150er2p5[1]=iEG
                ptEGsProgression150er2p5[1]=emuTree.L1Upgrade.egEt[iEG]


        
    if IndexEGsProgression0[0]>=0 and IndexEGsProgression0[1]>=0:
        ptDiProgression0.Fill(ptEGsProgression0[0],ptEGsProgression0[1])
    
    if IndexEGsProgression20[0]>=0 and IndexEGsProgression20[1]>=0:
        ptDiProgression20.Fill(ptEGsProgression20[0],ptEGsProgression20[1])

    if IndexEGsProgression35[0]>=0 and IndexEGsProgression35[1]>=0:
        ptDiProgression35.Fill(ptEGsProgression35[0],ptEGsProgression35[1])

    if IndexEGsProgression50[0]>=0 and IndexEGsProgression50[1]>=0:
        ptDiProgression50.Fill(ptEGsProgression50[0],ptEGsProgression50[1])

    if IndexEGsProgression100[0]>=0 and IndexEGsProgression100[1]>=0:
        ptDiProgression100.Fill(ptEGsProgression100[0],ptEGsProgression100[1])

    if IndexEGsProgression150[0]>=0 and IndexEGsProgression150[1]>=0:
        ptDiProgression150.Fill(ptEGsProgression150[0],ptEGsProgression150[1])

    if IndexEGsProgression0er2p5[0]>=0 and IndexEGsProgression0er2p5[1]>=0:
        ptDiProgression0er2p5.Fill(ptEGsProgression0er2p5[0],ptEGsProgression0er2p5[1])
    
    if IndexEGsProgression20er2p5[0]>=0 and IndexEGsProgression20er2p5[1]>=0:
        ptDiProgression20er2p5.Fill(ptEGsProgression20er2p5[0],ptEGsProgression20er2p5[1])

    if IndexEGsProgression35er2p5[0]>=0 and IndexEGsProgression35er2p5[1]>=0:
        ptDiProgression35er2p5.Fill(ptEGsProgression35er2p5[0],ptEGsProgression35er2p5[1])

    if IndexEGsProgression50er2p5[0]>=0 and IndexEGsProgression50er2p5[1]>=0:
        ptDiProgression50er2p5.Fill(ptEGsProgression50er2p5[0],ptEGsProgression50er2p5[1])

    if IndexEGsProgression100er2p5[0]>=0 and IndexEGsProgression100er2p5[1]>=0:
        ptDiProgression100er2p5.Fill(ptEGsProgression100er2p5[0],ptEGsProgression100er2p5[1])

    if IndexEGsProgression150er2p5[0]>=0 and IndexEGsProgression150er2p5[1]>=0:
        ptDiProgression150er2p5.Fill(ptEGsProgression150er2p5[0],ptEGsProgression150er2p5[1])


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
    legend1.AddEntry(rateDiCurves[i],"Di-Obj rate @ p_{T}^{L1} > "+str(thresholds[i])+" GeV (both EGs)","LPE")
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
    legend1.AddEntry(rateDiCurvesEr2p5[i],"Di-Obj rate @ p_{T}^{L1} > "+str(thresholds[i])+" GeV (both EGs)","LPE")
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

canvas2.SaveAs("PDFs/"+label+"/rateEr2p5_"+label+".pdf")
canvas2.SaveAs("PNGs/"+label+"/rateEr2p5_"+label+".png")

####################

print("saving histograms and efficiencies in root file for later plotting if desired")
fileout = ROOT.TFile("ROOTs/rate_graphs_"+label+".root","RECREATE")
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






