# OLD COMMAND FROM OLIVIER
    cmsDriver.py l1Ntuple -s RAW2DIGI --python_filename=mc.py -n 240 --no_output --era=Run2_2018 --mc --conditions=110X_mcRun3_2021_realistic_v6 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMUGEN_MC --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4 --filein=/store/mc/Run3Winter20DRMiniAOD/SinglePion_PT0to200/GEN-SIM-RAW/NoPU_110X_mcRun3_2021_realistic_v6-v3/10000/FFBA3DAA-9A9E-8442-958B-90F1490B66F9.root --no_exec



# NEW COMMAND FROM STAGE2 PAGE
    cmsDriver.py l1Ntuple -s RAW2DIGI --python_filename=mc.py -n 303 --no_output --era=Run3 --mc --conditions=123X_mcRun3_2021_realistic_v11 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimHcalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMUGEN_MC --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2022_v0_1 --filein=/store/mc/Run3Summer21DRPremix/SingleNeutrino_Pt-2To20-gun/GEN-SIM-DIGI-RAW/SNB_120X_mcRun3_2021_realistic_v6-v2/2540000/e7186f9d-8dfb-480f-bcba-ead981805f87.root --no_exec





# NEW COMMANDS FOR US --> OLD CALIBRATION (ECAL ONLY)
    cmsDriver.py l1Ntuple -s RAW2DIGI --python_filename=L1Ntuple_oldCalib_cfg.py -n 300 --no_output --era=Run3 --mc --conditions=123X_mcRun3_2021_realistic_v11 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimHcalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMUGEN_MC --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2022_v0_1 --filein=/store/mc/Run3Summer21DR/SinglePhoton_Pt-0To200-gun/GEN-SIM-DIGI-RAW/NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2/30000/24ceed17-25ac-4fba-a275-0821ad765052.root --no_exec

# NEW COMMANDS FOR US --> NEW CALIBRATION (ECAL ONLY)
    cmsDriver.py l1Ntuple -s RAW2DIGI --python_filename=L1Ntuple_newECALcalib_cfg.py -n 300 --no_output --era=Run3 --mc --conditions=123X_mcRun3_2021_realistic_v11 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimHcalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMUGEN_MC --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2022_newECALcalib --filein=/store/mc/Run3Summer21DR/SinglePhoton_Pt-0To200-gun/GEN-SIM-DIGI-RAW/NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2/30000/24ceed17-25ac-4fba-a275-0821ad765052.root --no_exec

# NEW COMMANDS FOR US --> UNCALIBRATED
    cmsDriver.py l1Ntuple -s RAW2DIGI --python_filename=L1Ntuple_uncalib_cfg.py -n 300 --no_output --era=Run3 --mc --conditions=123X_mcRun3_2021_realistic_v11 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimHcalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMUGEN_MC --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2022_noL1calib --filein=/store/mc/Run3Summer21DR/SinglePhoton_Pt-200to500-gun/GEN-SIM-DIGI-RAW/NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2/2550000/eae83b49-986c-43e1-bb72-12208a96d928.root --no_exec






# LINES TO ADD TO TURN ON THE HCAL PFA1P

    # settings of the HCAL PFA1p
    process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")

    process.simHcalTriggerPrimitiveDigis.overrideDBweightsAndFilterHB = cms.bool(True)
    process.simHcalTriggerPrimitiveDigis.overrideDBweightsAndFilterHE = cms.bool(True)

    process.HcalTPGCoderULUT.overrideDBweightsAndFilterHB = cms.bool(True)
    process.HcalTPGCoderULUT.overrideDBweightsAndFilterHE = cms.bool(True)

    process.simHcalTriggerPrimitiveDigis.numberOfFilterPresamplesHBQIE11 = 1
    process.simHcalTriggerPrimitiveDigis.numberOfFilterPresamplesHEQIE11 = 1
    process.simHcalTriggerPrimitiveDigis.weightsQIE11 = {
        "ieta1" :  [-0.47, 1.0],
        "ieta2" :  [-0.47, 1.0],
        "ieta3" :  [-0.47, 1.0],
        "ieta4" :  [-0.47, 1.0],
        "ieta5" :  [-0.47, 1.0],
        "ieta6" :  [-0.47, 1.0],
        "ieta7" :  [-0.47, 1.0],
        "ieta8" :  [-0.47, 1.0],
        "ieta9" :  [-0.47, 1.0],
        "ieta10" : [-0.47, 1.0],
        "ieta11" : [-0.47, 1.0],
        "ieta12" : [-0.47, 1.0],
        "ieta13" : [-0.47, 1.0],
        "ieta14" : [-0.47, 1.0],
        "ieta15" : [-0.47, 1.0],
        "ieta16" : [-0.47, 1.0],
        "ieta17" : [-0.47, 1.0],
        "ieta18" : [-0.47, 1.0],
        "ieta19" : [-0.47, 1.0],
        "ieta20" : [-0.47, 1.0],
        "ieta21" : [-0.43, 1.0],
        "ieta22" : [-0.43, 1.0],
        "ieta23" : [-0.43, 1.0],
        "ieta24" : [-0.43, 1.0],
        "ieta25" : [-0.43, 1.0],
        "ieta26" : [-0.43, 1.0],
        "ieta27" : [-0.43, 1.0],
        "ieta28" : [-0.43, 1.0]
    }

    process.HcalTPGCoderULUT.contain1TSHB = True
    process.HcalTPGCoderULUT.contain1TSHE = True

