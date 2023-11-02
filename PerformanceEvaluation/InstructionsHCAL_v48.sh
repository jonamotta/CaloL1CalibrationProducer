Instructions for the training of HCAL (V48)

cmsrel CMSSW_13_1_0_pre4
cd CMSSW_13_1_0_pre4/src
cmsenv
git cms-init
git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
git fetch cms-l1t-offline l1t-integration-CMSSW_13_1_0_pre4
git cms-merge-topic -u cms-l1t-offline:l1t-integration-v156
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data

git cms-checkdeps -A -a

scram b -j 8

git clone git@github.com:jonamotta/calol1calibrationproducer.git

# inside L1Trigger/L1TNtuples/python/L1NtupleEMU_cff.py change the "simCaloStage2Digis" to ("simCaloStage2Digis","MP") in order to have MP units
# stage2L1Trigger.toModify(l1UpgradeEmuTree,
#     egToken = ("simCaloStage2Digis","MP"),
#     tauTokens = [("simCaloStage2Digis","MP")],
#     jetToken = ("simCaloStage2Digis","MP"),
#     muonToken = "simGmtStage2Digis",
#     #muonToken = "muonLegacyInStage2FormatDigis",
#     sumToken = "simCaloStage2Digis", # DO NOT USE MP HERE
# )

cp CaloL1CalibrationProducer/caloParams/caloParams_2023_v48C_newCalib_cfi.py L1Trigger/L1TCalorimeter/python/

1) Produce input jets:

- Re-emulate data (JetMET or EGamma) with the current Global Tag

'''
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
'''

- Plot the jets and check that the CD energy distribution is the same as the RawEt energy distribution

'''
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot --tag _PuppiJet_100K_Barrel_Pt30_Raw
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot --tag _PuppiJet_100K_Barrel_Pt30_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_CDIhad

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_OnlyIhad_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.8 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot80_OnlyIhad_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.5 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot50_OnlyIhad_CD
'''

2) Read jets and produce inputs:

- Extract CD and target jet energy from the ntuples

'''
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --target reco --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --hcalcut 0.95 --lJetPtCut 30 --PuppiJet

python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot80 \
    --target reco --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --hcalcut 0.8 --lJetPtCut 30 --PuppiJet

python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot50_MinusIem \
    --target reco --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --hcalcut 0.5 --lJetPtCut 30 --PuppiJet --trainPtVers HCAL
'''

- Merge CD into tensorflow and save the input size:

'''
# New HCAL Calib (training 10188) -> 12737 ?
python3 batchMerger.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# New HCAL Calib (training 412913)
python3 batchMerger.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot80 \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# New HCAL Calib (training 4184564)
python3 batchMerger.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot50_MinusIem \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 100 --selectResp \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data
'''

- Plot the inputs and check that the built CD energy distribution corresponds to the previous one

'''
# 12737 events
python3 PlotResponseTF.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _Uncalib

# 146534 events
python3 PlotResponseTF.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot80 \
    --v HCAL --tag DataReco --filesLim 2 --addtag _Uncalib

# 258213 events
python3 PlotResponseTF.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot50_MinusIem \
    --v HCAL --tag DataReco --filesLim 1 --addtag _Uncalib
'''

3) Training:

'''
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegression.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegression_LRe-3 --batch_size 256 --epochs 50

python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegression.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot80 \
    --v HCAL --tag DataReco --MaxLR 1E-4 --addtag _OnlyRegression_LRe-4 --batch_size 1024 --epochs 20

python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegression.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot50_MinusIem \
    --v HCAL --tag DataReco --MaxLR 1E-5 --addtag _OnlyRegression_LRe-5 --epochs 20
'''

4) Extract SFs, plot SFs and plot performance from testing sample:

'''
python3 PrepareReEmulation.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _OnlyRegression_LRe-3 --applyECAL False

python3 PrepareReEmulation.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot80 \
    --v HCAL --tag DataReco --addtag _OnlyRegression_LRe-4 --applyECAL False --filesLim 2

python3 PrepareReEmulation.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot50_MinusIem \
    --v HCAL --tag DataReco --addtag _OnlyRegression_LRe-5 --applyECAL False --filesLim 1
'''

5) Re-emulate:

- Create caloParams file
- Copy the file to the src/L1Trigger/L1TCalorimeter/python/ folder
- Launche re-emulation:

'''
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --nJobs 244 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
    --nJobs 244 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json \
    --nJobs 244 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v48A_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json \
    --nJobs 244 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v48B_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json \
    --nJobs 244 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v48C_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD

# To resend!!!!!!!!!! with a subset of the sample
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
    --outTag GT130XdataRun3Promptv3_CaloParams2023v48AnewCalib_data \
    --nJobs 278 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v48A_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v48BnewCalib_data \
    --nJobs 278 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v48B_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v48CnewCalib_data \
    --nJobs 278 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v48C_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
'''

6) Performance evaluation:

'''
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_OnlyIhad_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --tag _PuppiJet_100K_Barrel_Pt30_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.80 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot80_OnlyIhad_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.80 --tag _PuppiJet_100K_Barrel_Pt30_HoTot80_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --tag _PuppiJet_100K_Barrel_Pt30_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.50 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot50_OnlyIhad_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.50 --tag _PuppiJet_100K_Barrel_Pt30_HoTot50_CD

python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --tag _PuppiJet_100K_Barrel_Pt30_CD

# UnCalib
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
 --outdir 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
# OldCalib
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
 --outdir 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305

# NewCalib A
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v48AnewCalib_data \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_03_NtuplesV48/NtuplesVnew48A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305

# NewCalib B
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v48BnewCalib_data \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_03_NtuplesV48/NtuplesVnew48B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305

# NewCalib C
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v48CnewCalib_data \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_03_NtuplesV48/NtuplesVnew48C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305
'''

7) Re-emulate with new ECAL v33 calibration:

- Create caloParams file 
- Copy the file to the src/L1Trigger/L1TCalorimeter/python/ folder
- Launche re-emulation:

'''
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v48C_ECALv33_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v48C_ECALv33_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD

python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v48C_ECALv33_newCalib_data \
    --nJobs 278 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v48C_ECALv33_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
'''

'''
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_ECALv33_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_ECALv33_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_ECALv33_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_ECALv33_data_reco_json/GoodNtuples \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_ECALv33_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v48C_ECALv33_newCalib_data \
 --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_ECALv33_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_03_NtuplesV48/NtuplesVnew48C_ECALv33_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305
'''
