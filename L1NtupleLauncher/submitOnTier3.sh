source /opt/exp_soft/cms/t3/t3setup

## AVAILABLE COMMAND OPTIONS
## python submitOnTier3.py --inFileList list\
##                         --outTag tag \
##                         --nJobs 100 \
##                         --queue {long, short} \
##                         --maxEvts -1 \
##                         --inJson JSON \
##                         --caloParams CP \
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
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v28newCalib_data \
#                         --nJobs 278 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --caloParams caloParams_2022_v28_newCalib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data

# python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06noL1Calib_data_reco_json \
#                         --nJobs 116 \
#                         --queue short \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_noL1Calib_cfi \
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

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
                        --outTag GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json \
                        --nJobs 116 \
                        --queue short \
                        --maxEvts -1 \
                        --inJson Cert_Collisions2022_355100_362760_Golden \
                        --caloParams caloParams_2022_v29_newCalib_cfi \
                        --globalTag 124X_dataRun3_Prompt_v10 \
                        --data \
                        --recoFromSKIM

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06noL1Calib_data_reco_json \
#                         --nJobs 122 \
#                         --queue long \
#                         --maxEvts -1 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden \
#                         --caloParams caloParams_2022_v0_6_noL1Calib_cfi \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --data \
#                         --recoFromAOD

# python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
#                         --outTag GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
#                         --nJobs 122 \
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
