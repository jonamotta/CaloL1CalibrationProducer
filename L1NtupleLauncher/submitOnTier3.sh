source /opt/exp_soft/cms/t3/t3setup

# python submitOnTier3.py --njobs 5 --applyHCALpfa1p --testRun --applyNewCalib
# python submitOnTier3.py --njobs 5 --applyHCALpfa1p --testRun --applyNewCalibNoZeros
# python submitOnTier3.py --njobs 5 --applyHCALpfa1p --testRun --applyOldCalib

# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doQCD --qcdPtBin 20To30 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doQCD --qcdPtBin 30To50 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCD --qcdPtBin 50To80 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCD --qcdPtBin 80To120 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCD --qcdPtBin 120To170 --applyNoCalib # --no_exec
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doQCD --qcdPtBin 20To30 --applyNewCalib # --no_exec
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doQCD --qcdPtBin 30To50 --applyNewCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCD --qcdPtBin 50To80 --applyNewCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCD --qcdPtBin 80To120 --applyNewCalib # --no_exec
# python submitOnTier3.py --njobs 400 --applyHCALpfa1p --doQCD --qcdPtBin 120To170 --applyNewCalib # --no_exec

# python submitOnTier3.py --njobs 250 --applyHCALpfa1p --doQCD --qcdPtBin PUForTRK --applyNoCalib # --no_exec

#python submitOnTier3.py --njobs 200 --applyHCALpfa1p --doPi0_200 --applyNoCalib #--no_exec


## RE-EMULATION

# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doNu --applyNewCalib
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doNu --applyNewCalibSaturAt 1.75
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doNu --applyOldCalib
# python submitOnTier3.py --njobs 300 --applyHCALpfa1p --doNu --applyNoCalib

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD       --applyNoCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNoCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNoCalib

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCDpu       --applyNoCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200pu   --applyNoCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500pu --applyNoCalib

#python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD       --applyNewCalib
#python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNewCalib
#python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNewCalib
#python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu        --applyNewCalib

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD       --applyNewCalibManualSatur_1
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNewCalibManualSatur_1
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNewCalibManualSatur_1
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu        --applyNewCalibManualSatur

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD       --applyNewCalibSaturAt 1.75
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNewCalibSaturAt 1.75
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNewCalibSaturAt 1.75

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD       --applyNewCalibECALsaturAt 1.2 --applyNewCalibHCALsaturAt 1.5
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNewCalibECALsaturAt 1.2 --applyNewCalibHCALsaturAt 1.5
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNewCalibECALsaturAt 1.2 --applyNewCalibHCALsaturAt 1.5
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu        --applyNewCalibECALsaturAt 1.2 --applyNewCalibHCALsaturAt 1.5

# python submitOnTier3.py --njobs 15000 --applyHCALpfa1p --doQCD       --applyOldCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyOldCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyOldCalib

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCDpu       --applyOldCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200pu   --applyOldCalib
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500pu --applyOldCalib

# python submitOnTier3.py --njobs 100 --applyHCALpfa1p --doMET --applyNoCalib --no_exec




# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD       --applyNewCalib --seedThreshold 6.0
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNewCalib --seedThreshold 6.0
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNewCalib --seedThreshold 6.0

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD       --applyNewCalib --seedThreshold 8.0
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG0_200   --applyNewCalib --seedThreshold 8.0
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doEG200_500 --applyNewCalib --seedThreshold 8.0

# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu        --applyNewCalib --seedThreshold 6.0
# python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu        --applyNewCalib --seedThreshold 8.0

python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD    --applyNewCalibManualSatur_2
python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu     --applyNewCalibManualSatur_2

python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD    --applyNewCalibManualSatur_3
python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu     --applyNewCalibManualSatur_3

python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD    --applyNewCalibManualSatur_4
python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu     --applyNewCalibManualSatur_4

python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD    --applyNewCalibManualSatur_5
python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu     --applyNewCalibManualSatur_5

python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD    --applyNewCalib_10TT
python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu     --applyNewCalib_10TT

python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doQCD    --applyNewCalib_More10TT
python submitOnTier3.py --njobs 750 --applyHCALpfa1p --doNu     --applyNewCalib_More10TT