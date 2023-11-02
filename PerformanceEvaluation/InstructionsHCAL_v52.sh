Instructions for the training of HCAL and HF (V52)

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
 --outdir 2023_06_26_NtuplesV52/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --jetPtcut 30 --do_HoTot --tag _PuppiJet_100K_Pt30_Raw
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --jetPtcut 30 --do_HoTot --tag _PuppiJet_100K_Pt30_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/TestInput_JetMET2022G --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --jetPtcut 30 --HoTotcut 0.95 --OnlyIhad --tag _PuppiJet_100K_Pt30_HoTot95_OnlyIhad_CD
'''

2) Read jets and produce inputs:

- Extract CD and target jet energy from the ntuples

'''
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 \
    --target reco --type jet --chunk_size 5000 \
    --queue short \
    --hcalcut 0.95 --lJetPtCut 30 --PuppiJet --matching
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95_HF3x3 \
    --target reco --type jet --chunk_size 5000 \
    --queue short \
    --hcalcut 0.95 --lJetPtCut 30 --PuppiJet --matching --sizeHF 3
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95_HF1x1 \
    --target reco --type jet --chunk_size 5000 \
    --queue short \
    --hcalcut 0.95 --lJetPtCut 30 --PuppiJet --matching --sizeHF 1
'''

- Extract sample for the jet rate proxy

'''
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/EphemeralZeroBias_Pt30To1000 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --lJetPtCut 30 --uJetPtCut 1000
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/EphemeralZeroBias_Pt30To1000_HF3x3 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --lJetPtCut 30 --uJetPtCut 1000 --sizeHF 3
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/EphemeralZeroBias_Pt30To1000_HF1x1 \
    --target emu --type jet --chunk_size 5000 \
    --queue short \
    --lJetPtCut 30 --uJetPtCut 1000 --sizeHF 1
'''

- Merge CD into tensorflow and save the input size:

'''
# (training 878670, rate 928326)
python3 batchMerger.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp --filesRatePerRecord 100 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/EphemeralZeroBias_Pt30To1000/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data
# (training 853827, rate 897215)
python3 batchMerger.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95_HF3x3 \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp --filesRatePerRecord 100 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/EphemeralZeroBias_Pt30To1000_HF3x3/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data
# (training 475172, rate 482108)
python3 batchMerger.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95_HF1x1 \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp --filesRatePerRecord 100 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/EphemeralZeroBias_Pt30To1000_HF1x1/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data
'''

- Plot the inputs and check that the built CD energy distribution corresponds to the previous one

''' 
python3 PlotResponseTF.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 \
    --v HCAL --tag DataReco --addtag _Uncalib --PlotRate --eventLim 100000
python3 PlotResponseTF.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95_HF3x3 \
    --v HCAL --tag DataReco --addtag _Uncalib --PlotRate --eventLim 100000
python3 PlotResponseTF.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95_HF1x1 \
    --v HCAL --tag DataReco --addtag _Uncalib --PlotRate --eventLim 100000
'''

- Compute target rate
'''
python3 TestRateProxy.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 \
    --v HCAL --tag DataReco
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 30 GeV :  0.8135712587049809
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 35 GeV :  0.7178994546612275
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 40 GeV :  0.6399986253216349
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 45 GeV :  0.5526859120883304
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 50 GeV :  0.44984522791065534
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 80 GeV :  0.04135645675053418
### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 100 GeV :  0.006935576691973832
'''

3) Training:

'''
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 \
    --v HCAL --tag DataReco --MaxLR 1E-4 --batch_size 1024 --epochs 20 --ThrRate 40 --TargetRate 0.6399986253216349
'''

4) Extract SFs, plot SFs and plot performance from testing sample:

'''
python3 PrepareReEmulation.py --indir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 \
    --v HCAL --tag DataReco --applyECAL False --modelRate

python3 ProduceCaloParams.py --name caloParams_2023_v52_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33/ECALtrainingDataReco_normalOrder/data/ScaleFactors_ECAL_energystep2iEt.csv \
    --HCAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95/HCALtrainingDataReco/data/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF   /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95/HCALtrainingDataReco/data/ScaleFactors_HF_energystep2iEt.csv
python3 ProduceCaloParams.py --name caloParams_2023_ECALv33_HCALv51_HFv52_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33/ECALtrainingDataReco_normalOrder/data/ScaleFactors_ECAL_energystep2iEt.csv \
    --HCAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF   /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95/HCALtrainingDataReco/data/ScaleFactors_HF_energystep2iEt.csv
'''

5) Re-emulate:

- Create caloParams file
- Copy the file to the src/L1Trigger/L1TCalorimeter/python/ folder
- Launche re-emulation:

'''
python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v52_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v52newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_v52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v52_HF3x3_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v52_HF3x3_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v52HF3x3newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_v52_HF3x3_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList JetMET__Run2022G-PromptReco-v1__Run362617__AOD \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv33HCALv51HFv52_data_reco_json \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv33_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromAOD
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv33HCALv51HFv52newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv33_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
'''

6) Performance evaluation:

'''
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v52_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --jetPtcut 30 --HoTotcut 0.95 --OnlyIhad --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_OnlyIhad_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v52_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --jetPtcut 30 --HoTotcut 0.95 --tag _PuppiJet_100K_Barrel_Pt30_HoTot95_CD
python3 resolutions_CD.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v52_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95 --label Muon_data_reco --reco --nEvts 100000 --target jet \
 --raw --PuppiJet --jetPtcut 30 --tag _PuppiJet_100K_Barrel_Pt30_CD

# UnCalib
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/NtuplesVunc_Raw_Puppi_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/NtuplesVunc_Raw_Puppi_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
 --outdir 2023_06_26_NtuplesV52/NtuplesVunc_Raw_Puppi_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
# OldCalib
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/NtuplesVcur_Raw_Puppi_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/NtuplesVcur_Raw_Puppi_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
 --outdir 2023_06_26_NtuplesV52/NtuplesVcur_Raw_Puppi_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305

# NewCalib 52
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v52_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v52_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/NtuplesV52new_Raw_Puppi_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v52_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/NtuplesV52new_Raw_Puppi_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v52newCalib_data \
 --outdir 2023_06_26_NtuplesV52/NtuplesV52new_Raw_Puppi_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_26_NtuplesV52/NtuplesV52new_Raw_Puppi_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
 --old 2023_06_26_NtuplesV52/NtuplesVcur_Raw_Puppi_Pt30 --unc 2023_06_26_NtuplesV52/NtuplesVunc_Raw_Puppi_Pt30 --do_HoTot --er 1.305

# NewCalib ECALv33_HCALv51_HFv52
python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023ECALv33HCALv51HFv52_data_reco_json
python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023ECALv33HCALv51HFv52_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/NtuplesECALV33_HCALV51_HFV52_Raw_Puppi_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 30 --do_HoTot
python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023ECALv33HCALv51HFv52_data_reco_json/GoodNtuples \
 --outdir 2023_06_26_NtuplesV52/NtuplesECALV33_HCALV51_HFV52_Raw_Puppi_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv33HCALv51HFv52newCalib_data \
 --outdir 2023_06_26_NtuplesV52/NtuplesECALV33_HCALV51_HFV52_Raw_Puppi_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
python3 comparisonPlots.py --indir 2023_06_26_NtuplesV52/NtuplesECALV33_HCALV51_HFV52_Raw_Puppi_Pt30 --label Muon_data_reco  --target jet --reco \
 --thrsFixRate 40 --thrsFixRate 60 --thrsFixRate 80 \
 --old 2023_06_26_NtuplesV52/NtuplesVcur_Raw_Puppi_Pt30 --unc 2023_06_26_NtuplesV52/NtuplesVunc_Raw_Puppi_Pt30 --do_HoTot --er 1.305
'''

'''
python3 comparisonPlots_old.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib --tag _normalOrder
/data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33/PerformancePlots_normalOrder_LooseElectron_raw
'''

'''
### 
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalibNew_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/NtuplesECALV33_WS --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/NtuplesECALNoCalib_WS --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/NtuplesECALCurCalib_WS --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/NtuplesECALOldCalib_WS --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot

#
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalibNew_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALV33 --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALNoCalib --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALCurCalib --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALOldCalib --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 comparisonPlots_old.py --indir 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALV33 --label EGamma_data_reco  --target ele --reco \
 --old 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALOldCalib --unc 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALNoCalib \
 --doRate False --doTurnOn False --ref _oldCalib
python3 comparisonPlots_old.py --indir 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALV33 --label EGamma_data_reco  --target ele --reco \
 --old 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALCurCalib --unc 2023_09_11_NtuplesV33/L1Workshop/NtuplesECALNoCalib \
 --doRate False --doTurnOn False --ref _curCalib
# NO

#
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv33_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362617/NtuplesECALV33 --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362617/NtuplesECALNoCalib --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362617/NtuplesECALCurCalib --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 comparisonPlots_old.py --indir 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362617/NtuplesECALV33 --label EGamma_data_reco  --target ele --reco \
 --old 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362617/NtuplesECALCurCalib --unc 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362617/NtuplesECALNoCalib \
 --doRate False --doTurnOn False
# NO

#
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v51A_ECALv33_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362616/NtuplesECALV33 --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362616/NtuplesECALNoCalib --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
 --outdir 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362616/NtuplesECALCurCalib --label EGamma_data_reco --reco --nEvts 60000 --target ele
python3 comparisonPlots_old.py --indir 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362616/NtuplesECALV33 --label EGamma_data_reco  --target ele --reco \
 --old 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362616/NtuplesECALCurCalib --unc 2023_09_11_NtuplesV33/L1Workshop_GT130X_Run362616/NtuplesECALNoCalib \
 --doRate False --doTurnOn False
#


python3 comparisonPlots_old.py --indir 2023_09_11_NtuplesV33/NtuplesECALV33_WS --label EGamma_data_reco  --target ele --reco \
 --old 2023_09_11_NtuplesV33/NtuplesECALCurCalib_WS --unc 2023_09_11_NtuplesV33/NtuplesECALNoCalib_WS --do_EoTot \
 --doRate False --doTurnOn False --ref _currCalib
python3 comparisonPlots_old.py --indir 2023_09_11_NtuplesV33/NtuplesECALV33_WS --label EGamma_data_reco  --target ele --reco \
 --old 2023_09_11_NtuplesV33/NtuplesECALOldCalib_WS --unc 2023_09_11_NtuplesV33/NtuplesECALNoCalib_WS --do_EoTot \
 --doRate False --doTurnOn False --ref _oldCalib

python3 comparisonPlots_old.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib --tag _normalOrder
'''
