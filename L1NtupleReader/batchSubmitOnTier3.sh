source /opt/exp_soft/cms/t3/t3setup

# python batchSubmitOnTier3.py --doEG0_200 --uJetPtCut 60 --etacut 28 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib --trainPtVers ECAL 
# python batchSubmitOnTier3.py --doEG0_200 --uJetPtCut 60 --etacut 28 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib --trainPtVers ECAL
# python batchSubmitOnTier3.py --doEG0_200 --uJetPtCut 60 --etacut 28 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib --trainPtVers ECAL

# python batchSubmitOnTier3.py --doEG200_500 --jetcut 60 --etacut 24 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doEG200_500 --jetcut 60 --etacut 24 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doEG200_500 --jetcut 60 --etacut 24 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib

# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "50To80" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "50To80" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "50To80" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 30

# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "80To120" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "80To120" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "80To120" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 50

# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "120To170" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "120To170" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "120To170" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 60


# python batchSubmitOnTier3.py --doQCDpu --indir 2022_05_02_NtuplesV8 --odir --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doQCDpu --indir 2022_05_02_NtuplesV8 --odir --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doQCDpu --indir 2022_05_02_NtuplesV8 --odir --applyHCALpfa1p --applyNewECALcalib


python batchSubmitOnTier3.py --doQCDnoPU --etacut 37 --hcalcut 1 --indir 2022_05_16_NtuplesVtest1 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --lJetPtCut 15 --uJetPtCut 500 --trainPtVers HCAL
python batchSubmitOnTier3.py --doQCDnoPU --etacut 37 --hcalcut 2 --indir 2022_05_16_NtuplesVtest2 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --lJetPtCut 15 --uJetPtCut 500 --trainPtVers HCAL
python batchSubmitOnTier3.py --doQCDnoPU --etacut 37 --hcalcut 3 --indir 2022_05_16_NtuplesVtest3 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --lJetPtCut 15 --uJetPtCut 500 --trainPtVers HCAL

# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "50To80" --etacut 24 --indir 2022_05_03_NtuplesV11 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 50 --uJetPtCut 150 --trainPtVers HCAL
# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "80To120" --etacut 24 --indir 2022_05_03_NtuplesV11 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 50 --uJetPtCut 150 --trainPtVers HCAL
# python batchSubmitOnTier3.py --doQCDnoPU --qcdPtBin "120To170" --etacut 24 --indir 2022_05_03_NtuplesV11 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 60 --uJetPtCut 150 --trainPtVers HCAL
