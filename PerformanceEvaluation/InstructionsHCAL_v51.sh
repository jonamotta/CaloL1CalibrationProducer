Instructions for the training of HCAL (V51) for HE

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
python submitOnTier3.py --inFileList EphemeralZeroBias*__Run2022G-v1__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --nJobs 946 --queue short --maxEvts -1 --data
'''

- Plot the jets and check that the CD energy distribution is the same as the RawEt energy distribution

'''
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 3. --jetPtcut 30 --do_HoTot --tag _PuppiJet_100K_BarrelEndcap_Pt30_Raw
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 3. --jetPtcut 30 --do_HoTot --tag _PuppiJet_100K_BarrelEndcap_Pt30_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 3. --jetPtcut 30 --HoTotcut 0.95 --OnlyIhad --tag _PuppiJet_100K_BarrelEndcap_Pt30_HoTot95_OnlyIhad_CD
'''

2) Read jets and produce inputs:

- Extract CD and target jet energy from the ntuples

'''
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 \
    --target reco --type jet --chunk_size 5000 \
    --queue short \
    --etacut 28 --hcalcut 0.95 --lJetPtCut 30 --PuppiJet

python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 \
    --target reco --type jet --chunk_size 5000 \
    --queue short \
    --etacut 28 --hcalcut 0.95 --lJetPtCut 30 --PuppiJet --etacutmin 15
'''

- Extract sample for the jet rate proxy

'''
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/EphemeralZeroBias_BarrelEndcap_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 28 --lJetPtCut 30 --uJetPtCut 1000

python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/EphemeralZeroBias_Endcap_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --etacut 28 --lJetPtCut 30 --uJetPtCut 1000 --etacutmin 15
'''

- Merge CD into tensorflow and save the input size:

'''
# New HCAL Calib (training 51812, rate 52613)
python3 batchMerger.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp --filesRatePerRecord 10 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/EphemeralZeroBias_BarrelEndcap_Pt30To1000/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data

# New HCAL Calib (training 43236, rate 43806)
python3 batchMerger.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp --filesRatePerRecord 5 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/EphemeralZeroBias_Endcap_Pt30To1000/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data

mkdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_Barrel_Pt30_HoTot95
mv /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_Barrel_Pt30_HoTot95/HCALtrainingDataRecoV50 \
  /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_Barrel_Pt30_HoTot95/HCALtrainingDataReco
'''

- Plot the inputs and check that the built CD energy distribution corresponds to the previous one

'''
python3 PlotResponseTF.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _Uncalib --PlotRate
python3 PlotResponseTF.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _Uncalib --PlotRate
'''

- Compute target rate
'''
python3 TestRateProxy.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 \
    --v HCAL --tag DataReco
'''
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 30 GeV :  0.6388787576130458
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 35 GeV :  0.4584420158749535
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 40 GeV :  0.33569892616499036
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 45 GeV :  0.23435025030658357
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 50 GeV :  0.15403136263291042
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 80 GeV :  0.01044917149213837
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 100 GeV :  0.0038967587975078594
'''
python3 TestRateProxy.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 \
    --v HCAL --tag DataReco
'''
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 30 GeV :  0.8260907948702231
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 35 GeV :  0.6781031670926632
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 40 GeV :  0.5260419533855614
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 45 GeV :  0.37612064850741417
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 50 GeV :  0.2477685117173469
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 80 GeV :  0.010895850072646963
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 100 GeV :  0.0030972673960419006

3) Training:

'''
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _A --batch_size 256 --epochs 20 --ThrRate 40 --TargetRate 0.33569892616499036
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-3 --addtag _A --batch_size 256 --epochs 20 --ThrRate 40 --TargetRate 0.5260419533855614
'''

4) Extract SFs, plot SFs and plot performance from testing sample:

'''
python3 PrepareReEmulation.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _A --applyECAL False --modelRate
python3 ProduceCaloParams.py --name caloParams_2023_v51A_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --HCAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HF_energystep2iEt.csv

python3 PrepareReEmulation.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _A --applyECAL False --modelRate
python3 ProduceCaloParams.py --name caloParams_2023_v51B_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --HCAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HF_energystep2iEt.csv

python3 ProduceCaloParams.py --name caloParams_2023_v51A_ECALv33_newCalib_cfi \
    --HCAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HF_energystep2iEt.csv \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33/ECALtrainingDataReco_normalOrder/data/ScaleFactors_ECAL_energystep2iEt.csv
'''

5) Re-emulate:

- Create caloParams file
- Copy the file to the src/L1Trigger/L1TCalorimeter/python/ folder
- Launche re-emulation:

'''
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v51A_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v51A_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v51AnewCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v51A_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v51B_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v51B_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v51BnewCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v51B_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
'''

6) Performance evaluation:

'''
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_OnlyIhad_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --HoTotcut 0.95 --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --tag _PuppiJet_100K_Barrel_Pt30_CD

# UnCalib
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/NtuplesVunc_Raw_Puppi_BarrelEndcap_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 3 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/NtuplesVunc_Raw_Puppi_BarrelEndcap_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
 --outdir 2023_06_21_NtuplesV51/NtuplesVunc_Raw_Puppi_BarrelEndcap_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
# OldCalib
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/NtuplesVcur_Raw_Puppi_BarrelEndcap_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 3 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/NtuplesVcur_Raw_Puppi_BarrelEndcap_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
 --outdir 2023_06_21_NtuplesV51/NtuplesVcur_Raw_Puppi_BarrelEndcap_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305

# NewCalib 51A
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 3 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v51AnewCalib_data \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_21_NtuplesV51/NtuplesVcur_Raw_Puppi_BarrelEndcap_Pt30 --unc 2023_06_21_NtuplesV51/NtuplesVunc_Raw_Puppi_BarrelEndcap_Pt30 --do_HoTot --er 1.305

# NewCalib 51B
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51B_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51B_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 3 --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51B_data_reco_json/GoodNtuples \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v51BnewCalib_data \
 --outdir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_21_NtuplesV51/JetMET_PuppiJet_Endcap_Pt30_HoTot95 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_21_NtuplesV51/NtuplesVcur_Raw_Puppi_BarrelEndcap_Pt30 --unc 2023_06_21_NtuplesV51/NtuplesVunc_Raw_Puppi_BarrelEndcap_Pt30 --do_HoTot --er 1.305
'''

Put together best ECAL and HCAL calibrations: v33 and v51A for barrel and endcap (up to TT 28)
'''
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --nJobs 300 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
    --nJobs 300 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v51A_ECALv33_data_reco_json \
    --nJobs 300 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v51A_ECALv33_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM

python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v51AECALv33newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_v51A_ECALv33_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v51A_ECALv33_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v51A_ECALv33_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
'''

Produce performance plots:
'''
# ECAL UnCalib 124X
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc_124X --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc_124X --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc_124X --label EGamma_data_reco_Raw_LooseEle --nEvts 100000 --target ele --raw --er 1.305
# ECAL OldCalib 124X
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur_124X --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur_124X --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_data \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur_124X --label EGamma_data_reco_Raw_LooseEle --nEvts 100000 --target ele --raw --er 1.305
# ECAL NewCalib ECAL_33 124X
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/Ntuples_V33_124X --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/Ntuples_V33_124X --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data \
#  --outdir 2023_06_26_BestPhDJona/Ntuples_V33_124X --label EGamma_data_reco_Raw_LooseEle --nEvts 100000 --target ele --raw --er 1.305

python3 comparisonPlots.py --indir 2023_06_26_BestPhDJona/Ntuples_V33_124X --label EGamma_data_reco_Raw_LooseEle  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 15 --thrsFixRate 20 --thrsFixRate 25 --thrsFixRate 30 --thrsFixRate 35 --thrsFixRate 40 \
 --old 2023_06_26_BestPhDJona/NtuplesVcur_124X --unc 2023_06_26_BestPhDJona/NtuplesVunc_124X --er 1.305

##################################################################################################################################################################


# ECAL UnCalib
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc --label EGamma_data_reco_Raw_LooseEle --nEvts 100000 --target ele --raw --er 1.305
# ECAL OldCalib
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur --label EGamma_data_reco_Raw_LooseEle --nEvts 100000 --target ele --raw --er 1.305
# ECAL NewCalib HCAL_51A ECAL_33
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v51A_ECALv33_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesV51A_V33 --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v51A_ECALv33_data_reco_json \
#  --outdir 2023_06_26_BestPhDJona/NtuplesV51A_V33 --label EGamma_data_reco_Raw_LooseEle --reco --nEvts 150000 --target ele --raw --LooseEle --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v51AECALv33newCalib_data \
#  --outdir 2023_06_26_BestPhDJona/NtuplesV51A_V33 --label EGamma_data_reco_Raw_LooseEle --nEvts 100000 --target ele --raw --er 1.305

python3 comparisonPlots.py --indir 2023_06_26_BestPhDJona/NtuplesV51A_V33 --label EGamma_data_reco_Raw_LooseEle  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 15 --thrsFixRate 20 --thrsFixRate 25 --thrsFixRate 30 --thrsFixRate 35 --thrsFixRate 40 \
 --old 2023_06_26_BestPhDJona/NtuplesVcur --unc 2023_06_26_BestPhDJona/NtuplesVunc --er 1.305

##################################################################################################################################################################

# HCAL UnCalib
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 3 --jetPtcut 30
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVunc --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --nEvts 100000 --target jet --raw --er 1.305
# HCAL OldCalib
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 3 --jetPtcut 30
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
#  --outdir 2023_06_26_BestPhDJona/NtuplesVcur --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --nEvts 100000 --target jet --raw --er 1.305
# HCAL NewCalib HCAL_51A ECAL_33
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_ECALv33_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_ECALv33_data_reco_json/GoodNtuples \
#  --outdir 2023_06_26_BestPhDJona/NtuplesV51A_V33 --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 3 --jetPtcut 30
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v51A_ECALv33_data_reco_json/GoodNtuples \
#  --outdir 2023_06_26_BestPhDJona/NtuplesV51A_V33 --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v51AECALv33newCalib_data \
#  --outdir 2023_06_26_BestPhDJona/NtuplesV51A_V33 --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30 --nEvts 100000 --target jet --raw --er 1.305

# python3 comparisonPlots.py --indir 2023_06_26_BestPhDJona/NtuplesV51A_V33 --label Jet_data_reco_Raw_Puppi_BarrelEndcap_Pt30  --target jet --reco \
#  --thrsFixRate 30 --thrsFixRate 35 --thrsFixRate 40 --thrsFixRate 45 --thrsFixRate 50 --thrsFixRate 55 --thrsFixRate 60 --thrsFixRate 80 \
#  --old 2023_06_26_BestPhDJona/NtuplesVcur --unc 2023_06_26_BestPhDJona/NtuplesVunc --er 1.305

'''