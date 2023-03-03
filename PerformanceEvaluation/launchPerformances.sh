python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --outdir 0000_00_00_NtuplesVunc --label EGamma_data_reco --reco --nEvts -1 --target ele
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 0000_00_00_NtuplesVold --label EGamma_data_reco --reco --nEvts -1 --target ele --unpacked
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 2023_02_28_NtuplesV31  --label EGamma_data_reco --reco --nEvts -1 --target ele


# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --outdir 0000_00_00_NtuplesVunc --label Muon_data_reco   --reco --nEvts -1 --target jet
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 0000_00_00_NtuplesVold --label Muon_data_reco   --reco --nEvts -1 --target jet --unpacked
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 2023_02_28_NtuplesV31  --label Muon_data_reco   --reco --nEvts -1 --target jet


python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --outdir 0000_00_00_NtuplesVunc --label EGamma_data_reco --reco --nEvts -1 --target ele
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 0000_00_00_NtuplesVold --label EGamma_data_reco --reco --nEvts -1 --target ele --unpacked
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 2023_02_28_NtuplesV31  --label EGamma_data_reco --reco --nEvts -1 --target ele


# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --outdir 0000_00_00_NtuplesVunc --label Muon_data_reco   --reco --nEvts -1 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 0000_00_00_NtuplesVold --label Muon_data_reco   --reco --nEvts -1 --target jet --unpacked
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 2023_02_28_NtuplesV31  --label Muon_data_reco   --reco --nEvts -1 --target jet


python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data     --outdir 0000_00_00_NtuplesVunc --label EGamma_data_reco --nEvts -1 --target ele
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data       --outdir 0000_00_00_NtuplesVold --label EGamma_data_reco --nEvts -1 --target ele --unpacked
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data       --outdir 2023_02_28_NtuplesV31  --label EGamma_data_reco --nEvts -1 --target ele


# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data     --outdir 0000_00_00_NtuplesVunc --label Muon_data_reco   --nEvts -1 --target jet
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data       --outdir 0000_00_00_NtuplesVold --label Muon_data_reco   --nEvts -1 --target jet --unpacked
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data       --outdir 2023_02_28_NtuplesV31  --label Muon_data_reco   --nEvts -1 --target jet


python3 comparisonPlots.py --indir 2023_02_28_NtuplesV31 --label EGamma_data_reco --target ele --reco --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40

# python3 comparisonPlots.py --indir 2023_02_28_NtuplesV31 --label Muon_data_reco   --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100












###############################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################
## OLD COMMANDS FOR OLD SCRIPTS



###############################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################
## MONTE CARLO

# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v01noL1calib_reco/ -1 HCAL_MC_noCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v01oldHCALsf_reco/ -1 HCAL_MC_oldCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v27newCalib_reco/ -1 HCAL_MC_v27newCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v28newCalib_reco/ -1 HCAL_MC_v28newCalibReco ./

# python3 turnOn.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p/ 100000 ECAL_uncalib
# python3 turnOn.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_oldCalib_applyHCALpfa1p/ 100000 ECAL_oldCalib
# python3 turnOn.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_newCalib_applyHCALpfa1p/ 100000 ECAL_newCalib


# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v01noL1calib_reco/ -1 HCAL_MC_noCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v01oldHCALsf_reco/ -1 HCAL_MC_oldCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v27newCalib_reco/ -1 HCAL_MC_v27newCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v28newCalib_reco/ -1 HCAL_MC_v28newCalibReco ./

# python3 resolutions.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p/ 100000 ECAL_uncalib
# python3 resolutions.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_oldCalib_applyHCALpfa1p/ 100000 ECAL_oldCalib
# python3 resolutions.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_newCalib_applyHCALpfa1p/ 100000 ECAL_newCalib

# python3 rate_HCAL_TandP.py /data_CMS/cms/davignon/Layer1SFsNtuples/Rate/Run362616_noCalib/Tot_Ntuple_Rate_Run362616_noCalib.root -1 HCAL_MC_noCalibReco 1 pt95eff
# python3 rate_HCAL_TandP.py /data_CMS/cms/davignon/Layer1SFsNtuples/Rate/Run362616_noCalib/Tot_Ntuple_Rate_Run362616_noCalib.root -1 HCAL_MC_oldCalibReco 0 pt95eff
# python3 rate_HCAL_TandP.py /data_CMS/cms/davignon/Layer1SFsNtuples/Rate/Run362616_newLayer1SFs/Tot_Ntuple_Rate_Run362616_newL1SFs.root -1 HCAL_MC_v27newCalibReco 1 pt95eff
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT130XdataRun3Promptv10_CaloParams2022v28newCalib_data -1 HCAL_MC_v28newCalibReco pt95eff

# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p/ 500000 ECAL_uncalib
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_oldCalib_applyHCALpfa1p/ 500000 ECAL_oldCalib
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_newCalib_applyHCALpfa1p/ 500000 ECAL_newCalib

# python3 comparisonPlots.py HCAL_MC_v27newCalibReco ./ pt95eff
# python3 comparisonPlots.py HCAL_MC_v28newCalibReco ./ Reco pt95eff

# python3 comparisonPlots.py ECAL_newCalib

###############################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################
## DATA

# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ 50000 HCAL_Data_noCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ 50000 HCAL_Data_oldCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ 50000 HCAL_Data_currCalibReco ./ unpacked
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ 50000 HCAL_Data_v31newCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ 50000 HCAL_Data_v27newCalibReco ./

# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ -1 ECAL_Data_noCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ -1 ECAL_Data_oldCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ -1 ECAL_Data_currCalibReco ./ unpacked
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ -1 ECAL_Data_v31newCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ -1 ECAL_Data_v27newCalibReco ./

# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ 50000 HCAL_Data_noCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ 50000 HCAL_Data_oldCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ 50000 HCAL_Data_currCalibReco ./ unpacked
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ 50000 HCAL_Data_v31newCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ 50000 HCAL_Data_v27newCalibReco ./

# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ -1 ECAL_Data_noCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ -1 ECAL_Data_oldCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ -1 ECAL_Data_currCalibReco ./ unpacked
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ -1 ECAL_Data_v31newCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ -1 ECAL_Data_v27newCalibReco ./

# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ 500000 HCAL_Data_noCalibReco
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ 500000 HCAL_Data_oldCalibReco
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ 500000 HCAL_Data_currCalibReco unpacked
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data/ 500000 HCAL_Data_v31newCalibReco
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data/ 500000 HCAL_Data_v27newCalibReco

# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ -1 ECAL_Data_noCalibReco
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ -1 ECAL_Data_oldCalibReco
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ -1 ECAL_Data_currCalibReco unpacked
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data/ -1 ECAL_Data_v31newCalibReco
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data/ -1 ECAL_Data_v27newCalibReco

# python3 comparisonPlots.py HCAL_Data_v27newCalib currCalib ./ Reco
# python3 comparisonPlots.py ECAL_Data_v27newCalib currCalib ./ Reco
# python3 comparisonPlots.py HCAL_Data_v29newCalib currCalib ./ Reco
# python3 comparisonPlots.py ECAL_Data_v29newCalib currCalib ./ Reco
# python3 comparisonPlots.py HCAL_Data_v31newCalib currCalib ./ Reco
# python3 comparisonPlots.py ECAL_Data_v31newCalib currCalib ./ Reco



# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ 50000 HCAL_Data_noCalibReco ./
# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ 50000 HCAL_Data_oldCalibReco ./
# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ 50000 HCAL_Data_currCalibReco ./ unpacked
# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ 50000 HCAL_Data_v31newCalibReco ./
# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ 50000 HCAL_Data_v27newCalibReco ./



# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ HCAL_Data_noCalibReco_off 50000 -1
# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ HCAL_Data_oldCalibReco_off 50000 -1
# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ HCAL_Data_currCalibReco_off 50000 -1 unpacked
# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ HCAL_Data_v29newCalibReco_off 50000 -1
# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data/ HCAL_Data_v27newCalibReco_off 50000 -1

# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ ECAL_Data_noCalibReco_off -1 -1
# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ ECAL_Data_oldCalibReco_off -1 -1
# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ ECAL_Data_currCalibReco_off -1 -1 unpacked
# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ ECAL_Data_v29newCalibReco_off -1 -1
# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data/ ECAL_Data_v27newCalibReco_off -1 -1

# python3 comparisonPlots_JB.py HCAL_Data_noCalibReco_currCalibReco_v29newCalibReco_off HCAL_Data_noCalibReco_off HCAL_Data_currCalibReco_off HCAL_Data_v29newCalibReco_off
# python3 comparisonPlots_JB.py ECAL_Data_noCalibReco_currCalibReco_v29newCalibReco_off ECAL_Data_noCalibReco_off ECAL_Data_currCalibReco_off ECAL_Data_v29newCalibReco_off
# python3 comparisonPlots_JB.py HCAL_Data_noCalibReco_currCalibReco_v27newCalibReco_off HCAL_Data_noCalibReco_off HCAL_Data_currCalibReco_off HCAL_Data_v27newCalibReco_off
# python3 comparisonPlots_JB.py ECAL_Data_noCalibReco_currCalibReco_v27newCalibReco_off ECAL_Data_noCalibReco_off ECAL_Data_currCalibReco_off ECAL_Data_v27newCalibReco_off

