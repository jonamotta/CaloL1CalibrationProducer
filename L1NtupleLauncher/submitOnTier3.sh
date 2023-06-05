source /opt/exp_soft/cms/t3/t3setup

## AVAILABLE COMMAND OPTIONS
## python submitOnTier3.py --inFileList list\
##                         --outTag tag \
##                         --nJobs 100 \
##                         --queue {long, short} \
##                         --maxEvts -1 \
##                         --inJson JSON \
##                         --caloParams CP \
##                         --noL1calib \
##                         --globalTag GT \
##                         --data \
##                         --reco \
##                         --no_exec


# python submitOnTier3.py --inFileList VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM \
#                         --outTag GT130XmcRun32022realisticv2_CaloParams2022v01noL1calib_reco \
#                         --nJobs 46 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_1_noL1calib_cfi \
#                         --globalTag 130X_mcRun3_2022_realistic_v2 \
#                         --reco

# python submitOnTier3.py --inFileList VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM \
#                         --outTag GT130XmcRun32022realisticv2_CaloParams2022v01oldHCALsf_reco \
#                         --nJobs 46 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_1_oldHCALsf_cfi \
#                         --globalTag 130X_mcRun3_2022_realistic_v2 \
#                         --reco

# python submitOnTier3.py --inFileList VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM \
#                         --outTag GT130XmcRun32022realisticv2_CaloParams2022v27newCalib_reco \
#                         --nJobs 46 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v27_newCalib_cfi \
#                         --globalTag 130X_mcRun3_2022_realistic_v2 \
#                         --reco

# python submitOnTier3.py --inFileList VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM \
#                         --outTag GT130XmcRun32022realisticv2_CaloParams2022v28newCalib_reco \
#                         --nJobs 46 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v28_newCalib_cfi \
#                         --globalTag 130X_mcRun3_2022_realistic_v2 \
#                         --reco

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --noL1calib \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_6_oldHcalL1Calib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v27_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v28newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v28_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v29_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v31_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json_resubmit2 \
#                         --nJobs 1826 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --noL1calib \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json_resubmit2 \
#                         --nJobs 5515 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --noL1calib \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json_resubmit2 \
#                         --nJobs 922 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --noL1calib \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 116 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --noL1calib \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
#                         --nJobs 116 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_oldHcalL1Calib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json \
#                         --nJobs 116 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v27_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v28newCalib_data_reco_json \
#                         --nJobs 116 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v28_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json \
#                         --nJobs 116 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v29_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json \
#                         --nJobs 116 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v31_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 245 \
#                         --queue long \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --noL1calib \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
#                         --nJobs 245 \
#                         --queue long \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_oldHcalL1Calib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json \
#                         --nJobs 122 \
#                         --queue long \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v27_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v28newCalib_data_reco_json \
#                         --nJobs 122 \
#                         --queue long \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v28_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json \
#                         --nJobs 122 \
#                         --queue long \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v29_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json \
#                         --nJobs 245 \
#                         --queue long \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v31_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json \
#                         --nJobs 245 \
#                         --queue long \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v31_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD
                        
# python submitOnTier3.py --inFileList SinglePionGun_E0p2to200__Run3Winter23Digi-NoPU_126X_mcRun3_2023_forPU65_v1-v2__GEN-SIM-RAW \
#                         --outTag GT130XmcRun32022realisticv2_CaloParams2022v06_noL1calib \
#                         --nJobs 2218 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --noL1calib \
#                         --globalTag 130X_mcRun3_2022_realistic_v2 \

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v35_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v35_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v35_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# # From data training

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v33_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v33_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v33_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# # noL1Calib MUON
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --noL1calib \
#                         --data \
#                         --recoFromAOD

# # currCalib MUON
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# # oldCalib MUON
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_oldHcalL1Calib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# # currCalib EGAMMA
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# # currCalib RATE
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# # currCalib RATE full 362616 stat
# python submitOnTier3.py --inFileList EphemeralZeroBias__Run2022G-v1__Run362616__RAW \
#     --outTag GT124XdataRun3v11_CaloParams2022v06_data \
#     --nJobs 2502 \
#     --queue short \
#     --maxEvts -1 \
#     --caloParams caloParams_2022_v0_6_cfi \
#     --globalTag 124X_dataRun3_v11 \
#     --data

# # noCalib RATE full 362616 stat
# python submitOnTier3.py --inFileList EphemeralZeroBias__Run2022G-v1__Run362616__RAW \
#     --outTag GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data \
#     --nJobs 2502 \
#     --queue short \
#     --maxEvts -1 \
#     --caloParams caloParams_2022_v0_6_cfi \
#     --globalTag 124X_dataRun3_v11 \
#     --noL1calib \
#     --data

# # v39
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39newCalib_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v39_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v39_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data

# # v39 C
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39CnewCalib_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v39_C_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39CnewCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v39_C_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data

# # v39 D
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39DnewCalib_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v39_D_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39DnewCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v39_D_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data

# re-emulation v40 C3
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3v11_CaloParams2022v40C3newCalib_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v40_C3_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromAOD
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v40C3newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v40_C3_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data

# # re-emulation v40 C6
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3v11_CaloParams2022v40C6newCalib_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v40_C6_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromAOD
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v40C6newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v40_C6_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data

# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3v11_CaloParams2022v06_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromAOD

# # v39 H1
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39H1newCalib_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v39_H1_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39H1newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v39_H1_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data

# # v39 H1
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39H2newCalib_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v39_H2_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v39H2newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v39_H2_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data

# v41
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v41CnewCalib_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v41_C_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromAOD
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v41CnewCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v41_C_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --noL1calib \
#                         --recoFromAOD

# correct v41
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3v11_CaloParams2022v41CZSnewCalib_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v41_C_ZS_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromAOD
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v41CZSnewCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v41_C_ZS_newCalib_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data  
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3v11_CaloParams2022v06modZS0p5_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_modZS0p5_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data \
#                         --recoFromAOD
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3v11_CaloParams2022v06modZS0p5_data \
#                         --nJobs 2502 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_6_modZS0p5_cfi \
#                         --globalTag 124X_dataRun3_v11 \
#                         --data

# # v42
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1 \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v42_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v42_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data  

# # v43
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v43_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v43_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --noL1calib \
#                         --data \
#                         --recoFromSKIM

# latest prompt GT
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v42_newCalib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data \
#                         --noL1calib \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v42_newCalib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v06_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data

# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --noL1calib \
#                         --data

# Re-emulation on jets
# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__AOD__Olivier \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 2000 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data \
#                         --noL1calib \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__AOD__Olivier \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json \
#                         --nJobs 2000 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__AOD__Olivier \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json \
#                         --nJobs 2000 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v42_newCalib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data \
#                         --recoFromAOD

############################################################################################################
############################################################################################################
############################################################################################################

# ntuples JetMET Era F noL1Calib for input ---> NOT ON DISK
# python submitOnTier3.py --inFileList JetMET__Run2022F-PromptReco-v1__AOD \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                         --nJobs 2000 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromAOD

# # ntuples JetMET Era G Early noL1Calib for input
# python submitOnTier3.py --inFileList JetMET__Run2022G_Early-PromptReco-v1__AOD \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                         --nJobs 2055 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromAOD

# # ntuples JetMET Era G Late noL1Calib for input
# python submitOnTier3.py --inFileList JetMET__Run2022G_Late-PromptReco-v1__AOD \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                         --nJobs 4298 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromAOD

# ntuples JetMET Era G noL1Calib for input (fixed v156)
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__AOD \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
                        --nJobs 5603 \
                        --queue short \
                        --maxEvts -1 \
                        --inJson Cert_Collisions2022_355100_362760_Golden \
                        --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data \
                        --recoFromAOD

# Re-emulation
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
                        --nJobs 244 \
                        --queue short \
                        --maxEvts -1 \
                        --inJson Cert_Collisions2022_355100_362760_Golden \
                        --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data \
                        --recoFromAOD
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
                        --nJobs 244 \
                        --queue short \
                        --maxEvts -1 \
                        --inJson Cert_Collisions2022_355100_362760_Golden \
                        --caloParams caloParams_2023_v0_2_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data \
                        --recoFromAOD
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v47A_data_reco_json \
                        --nJobs 244 \
                        --queue short \
                        --maxEvts -1 \
                        --inJson Cert_Collisions2022_355100_362760_Golden \
                        --caloParams caloParams_2023_v47A_newCalib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data \
                        --recoFromAOD
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v47B_data_reco_json \
                        --nJobs 244 \
                        --queue short \
                        --maxEvts -1 \
                        --inJson Cert_Collisions2022_355100_362760_Golden \
                        --caloParams caloParams_2023_v47B_newCalib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data \
                        --recoFromAOD
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v47C_data_reco_json \
                        --nJobs 244 \
                        --queue short \
                        --maxEvts -1 \
                        --inJson Cert_Collisions2022_355100_362760_Golden \
                        --caloParams caloParams_2023_v47C_newCalib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data \
                        --recoFromAOD

python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
                        --nJobs 278 \
                        --queue short \
                        --maxEvts -1 \
                        --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v02_data \
                        --nJobs 278 \
                        --queue short \
                        --maxEvts -1 \
                        --caloParams caloParams_2023_v0_2_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v47AnewCalib_data \
                        --nJobs 278 \
                        --queue short \
                        --maxEvts -1 \
                        --caloParams caloParams_2023_v47A_newCalib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v47BnewCalib_data \
                        --nJobs 278 \
                        --queue short \
                        --maxEvts -1 \
                        --caloParams caloParams_2023_v47B_newCalib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
                        --outTag GT130XdataRun3Promptv3_CaloParams2023v47CnewCalib_data \
                        --nJobs 278 \
                        --queue short \
                        --maxEvts -1 \
                        --caloParams caloParams_2023_v47C_newCalib_cfi \
                        --globalTag 130X_dataRun3_Prompt_v3 \
                        --data

############################################################################################################
############################################################################################################

# ntuples Muon Era G
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                         --nJobs 7501 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromAOD

############################################################################################################
############################################################################################################

# ntuples EGamma Era E
# python submitOnTier3.py --inFileList EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                         --nJobs 5475 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                         --nJobs 5475 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromSKIM

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                         --nJobs 2764 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromSKIM

# re-emulation v46
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_new \
#                         --nJobs 120 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromSKIM
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json_new \
#                         --nJobs 120 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v0_2_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromSKIM
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v46newCalib_data_reco_json_new \
#                         --nJobs 120 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2023_v46_newCalib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data \
#                         --recoFromSKIM
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v02_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2023_v0_2_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
#                         --outTag GT130XdataRun3Promptv3_CaloParams2023v46newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2023_v46_newCalib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v3 \
#                         --data
# delete EphemeralZeroBias0__Run2022G-v1__Run362616__RAW_GT130XdataRun3Promptv3*

########################################################################################################
########################################################################################################

# Egamma with fixed SFs
# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v33newCalibNew_data_reco_json \
#                         --nJobs 2879 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v33_newCalib_New_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromSKIM

# fixed ECAL
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT130XdataRun3Promptv2_CaloParams2022v43fixnewCalib_data_reco_json \
#                         --nJobs 256 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v43_fix_newCalib_cfi \
#                         --globalTag 130X_dataRun3_Prompt_v2 \
#                         --data \
#                         --recoFromAOD

# found that GT v11 is wrong --> go back to Promptv10
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --noL1calib \
#                         --recoFromAOD
# python submitOnTier3.py --inFileList Muon__Run2022G-PromptReco-v1__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v41CZSnewCalib_data_reco_json \
#                         --nJobs 7745 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v41_C_ZS_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD
# python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362616__RAW \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v41CZSnewCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v41_C_ZS_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data
# export SITECONFIG_PATH=/cvmfs/cms.cern.ch/SITECONF/T2_FR_GRIF_LLR/GRIF-LLR