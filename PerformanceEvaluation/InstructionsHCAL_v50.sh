Instructions for the training of HCAL (V50)

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

1) Produce input jets:

- Re-emulate data (JetMET) with the current Global Tag

'''
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 5603 --queue short --maxEvts -1 --data --recoFromAOD
'''

- Re-emulate data (ZB) with the current Global Tag

'''
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
python submitOnTier3.py --inFileList EphemeralZeroBias1__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
python submitOnTier3.py --inFileList EphemeralZeroBias2__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
python submitOnTier3.py --inFileList EphemeralZeroBias3__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
python submitOnTier3.py --inFileList EphemeralZeroBias4__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
python submitOnTier3.py --inFileList EphemeralZeroBias5__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
python submitOnTier3.py --inFileList EphemeralZeroBias6__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
python submitOnTier3.py --inFileList EphemeralZeroBias7__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
python submitOnTier3.py --inFileList EphemeralZeroBias8__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
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

- Extract sample for the jet rate proxy

'''
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias0_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias1__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias1_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias2__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias2_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias3__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias3_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias4__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias4_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias5__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias5_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias6__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias6_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias7__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias7_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias8__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias8_Barrel_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
'''

- Merge CD into tensorflow and save the input size:

'''
# New HCAL Calib (training 10188) -> 12737 ?
python3 batchMerger.py --indir 2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --batchdir GoodNtuples --v HCAL --odir DataRecoV50 --filesPerRecord 300 --selectResp --filesRatePerRecord 5 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias_Barrel_Pt30To1000/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data

mkdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95
mv /data_CMS/cms/motta/CaloL1calibraton/2023_06_03_NtuplesV48/JetMET_PuppiJet_Barrel_Pt30_HoTot95/HCALtrainingDataRecoV50 \
  /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95/HCALtrainingDataReco
'''

- Plot the inputs and check that the built CD energy distribution corresponds to the previous one

'''
# 12737 events
python3 PlotResponseTF.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _Uncalib --PlotRate
'''

### Rate Proxy target at 30 GeV = 0.4133330276701589
### Rate Proxy target at 40 GeV = 0.12730107058526857
### Rate Proxy target at 50 GeV = 0.05767864102152633

- Compute target rate
'''
python3 TestRateProxy.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco
'''

### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 30 GeV :  0.4356599158939274
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 35 GeV :  0.22529068041121822
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 40 GeV :  0.13216800105640258
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 45 GeV :  0.08504652219085858
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 50 GeV :  0.05905648719134002
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 80 GeV :  0.010995664170825448
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 100 GeV :  0.004934617385247169

3) Training:

'''
A) - G)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _A --batch_size 256 --epochs 20

X*)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _X*_* --batch_size 256 --epochs 20
X) after optimization
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _X --batch_size 256 --epochs 50

Y*)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRateAndStd.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _Y* --batch_size 256 --epochs 20   
Y) after optimization (100)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRateAndStd.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _Y --batch_size 256 --epochs 50
'''

4) Extract SFs, plot SFs and plot performance from testing sample:

'''
python3 PrepareReEmulation.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _* --applyECAL False --modelRate
'''

5) Re-emulate:

- Create caloParams file
- Copy the file to the src/L1Trigger/L1TCalorimeter/python/ folder
- Launche re-emulation:

'''
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50B_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v50B_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50BnewCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v50B_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50D_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v50D_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50DnewCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v50D_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50X_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v50X_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50XnewCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v50X_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50Y_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v50Y_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50YnewCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v50Y_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
'''

6) Performance evaluation:

'''
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50B_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50B_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_OnlyIhad_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50B_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50B_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50B_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50B_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --tag _PuppiJet_100K_Barrel_Pt30_CD

# NewCalib 50B
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50B_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50B_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50B_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v50BnewCalib_data \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_08_NtuplesV50/NtuplesVnew50B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305
'''

'''
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50D_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50D_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_OnlyIhad_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50D_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50D_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50D_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50D_CD_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --tag _PuppiJet_100K_Barrel_Pt30_CD

# NewCalib 50D
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50D_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50D_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50D_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50D_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50D_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v50DnewCalib_data \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50D_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_08_NtuplesV50/NtuplesVnew50D_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305

# NewCalib 50X
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50X_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50X_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50X_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50X_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50X_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v50XnewCalib_data \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50X_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_08_NtuplesV50/NtuplesVnew50X_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305

# NewCalib 50Y
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50Y_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50Y_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50Y_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50Y_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50Y_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v50YnewCalib_data \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50Y_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_08_NtuplesV50/NtuplesVnew50Y_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305
'''

##########################################################################################################################################################################################################################
##########################################################################################################################################################################################################################
##########################################################################################################################################################################################################################
# OLD
##########################################################################################################################################################################################################################
##########################################################################################################################################################################################################################
##########################################################################################################################################################################################################################

'''
1) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 50, 0.05906486977242875) * 100 = threshold_relaxation_sigmoid(proxyRate, targetRate, 0.1)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_1 --batch_size 256 --epochs 20
2) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 50, 0.05906486977242875) * 10 = threshold_relaxation_sigmoid(proxyRate, targetRate, 0.1)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_2 --batch_size 256 --epochs 20
3) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 50, 0.05906486977242875) * 0 = threshold_relaxation_sigmoid(proxyRate, targetRate, 0.1)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_3 --batch_size 256 --epochs 20
4) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 50, 0.05906486977242875) * 100 = threshold_relaxation_sigmoid(proxyRate, targetRate, 1)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_4 --batch_size 256 --epochs 20
5) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 50, 0.05906486977242875) * 100 = threshold_relaxation_sigmoid(proxyRate, targetRate, 10)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_5 --batch_size 256 --epochs 20
6) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 50, 0.05906486977242875) * 1000 = threshold_relaxation_sigmoid(proxyRate, targetRate, 10)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_6 --batch_size 256 --epochs 20
7) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 50, 0.05906486977242875) * 10000 = threshold_relaxation_sigmoid(proxyRate, targetRate, 10)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_7 --batch_size 256 --epochs 20
8) previous ones were uncorrect because I forgot the conversion from 50 GeV to 100 iEt: -> MUCH BETTER NOW!!!!!!!!!!
regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 100, 0.05906486977242875) * 10000 = threshold_relaxation_sigmoid(proxyRate, targetRate, 10)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_8 --batch_size 256 --epochs 20
9) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 100, 0.05906486977242875) * 100 = threshold_relaxation_sigmoid(proxyRate, targetRate, 10)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_9 --batch_size 256 --epochs 20
10) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & 
    rateLoss_value_50 = rateLoss(z_pred, 100, 0.05906486977242875) & 
    rateLoss_value_40 = rateLoss(z_pred, 80, 0.13216800071384716) & 
    rateLoss_value_30 = rateLoss(z_pred, 60, 0.43565990767259705) &
    rateLoss_value = (rateLoss_value_50 + rateLoss_value_40 + rateLoss_value_30)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_10 --batch_size 256 --epochs 20
11) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & 
    rateLoss_value_50 = rateLoss(z_pred, 100, 0.05906486977242875) & 
    rateLoss_value_40 = rateLoss(z_pred, 80, 0.13216800071384716) & 
    rateLoss_value_30 = rateLoss(z_pred, 60, 0.43565990767259705) &
    rateLoss_value = (rateLoss_value_50 + rateLoss_value_40 + rateLoss_value_30) * 100
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_11 --batch_size 256 --epochs 20
12) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 100, 0.05906486977242875) * 100 = threshold_relaxation_sigmoid(proxyRate, targetRate, 1)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_12 --batch_size 256 --epochs 20
13) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 100, 0.05906486977242875) * 100 = threshold_relaxation_sigmoid(proxyRate, targetRate, 0.1)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_13 --batch_size 256 --epochs 20
14) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 100, 0.05906486977242875) * 100000 = threshold_relaxation_sigmoid(proxyRate, targetRate, 0.1)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_14 --batch_size 256 --epochs 20
15) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 100, 0.05906486977242875) * 100 = tf.cosh(1.5 * realtive_diff)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_15 --batch_size 256 --epochs 20
16) regression_loss = tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 & rate_loss = rateLoss(z_pred, 100, 0.05906486977242875) * 10000 = tf.cosh(1.5 * realtive_diff)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_16 --batch_size 256 --epochs 20
17) test only rate
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRate_LRe-3_17 --batch_size 256 --epochs 20
18) test only rate initialize weights at 1

20) new definition of rate output (not 81 towers but final energy)
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _OnlyRegressionAndRate_LRe-3_20 --batch_size 256 --epochs 20

'''

4) Extract SFs, plot SFs and plot performance from testing sample:

'''
python3 PrepareReEmulation.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _OnlyRegressionAndRate_LRe-3_* --applyECAL False --modelRate
'''

5) Re-emulate:

- Create caloParams file
- Copy the file to the src/L1Trigger/L1TCalorimeter/python/ folder
- Launche re-emulation:

'''
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50-16_data_reco_json \
    --nJobs 244 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v50-16_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v50-16newCalib_data \
    --nJobs 278 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v50-16_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
'''

6) Performance evaluation:

'''
# NewCalib
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50-16_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50-16_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50-16_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v50-16_data_reco_json/GoodNtuples \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50-16_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v50-16newCalib_data \
 --outdir 2023_06_08_NtuplesV50/NtuplesVnew50-16_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_08_NtuplesV50/NtuplesVnew50-16_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305
'''