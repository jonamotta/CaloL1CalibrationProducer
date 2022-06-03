source /opt/exp_soft/cms/t3/t3setup

# python submitOnTier3.py --njobs 5 --applyHCALpfa1p --testRun --applyNewCalib
# python submitOnTier3.py --njobs 5 --applyHCALpfa1p --testRun --applyNewCalibNoZeros
# python submitOnTier3.py --njobs 5 --applyHCALpfa1p --testRun --applyOldCalib

# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 20To30 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 30To50 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 50To80 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 80To120 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 120To170 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 20To30 --applyNewCalib # --no_exec
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 30To50 --applyNewCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 50To80 --applyNewCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 80To120 --applyNewCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCDnoPU --qcdPtBin 120To170 --applyNewCalib # --no_exec

# python submitOnTier3.py --njobs 250 --applyHCALpfa1p --doQCDnoPU --qcdPtBin PUForTRK --applyNoCalib # --no_exec

#python submitOnTier3.py --njobs 200 --applyHCALpfa1p --doPi0_200 --applyNoCalib #--no_exec


## RE-EMULATION

python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doNu --applyNewCalib
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doNu --applyNewCalibNoZeros
python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doNu --applyOldCalib
python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doNu --applyNoCalib

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCDnoPU   --applyNoCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNoCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNoCalib

python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCDnoPU   --applyNewCalib
python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNewCalib
python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNewCalib

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCDnoPU   --applyNewCalibNoZeros
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNewCalibNoZeros
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNewCalibNoZeros

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCDnoPU   --applyOldCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyOldCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyOldCalib

# python submitOnTier3.py --njobs 100 --applyHCALpfa1p --doMET --applyNoCalib --no_exec