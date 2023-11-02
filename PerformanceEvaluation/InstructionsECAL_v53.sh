Instructions for the training of ECAL (V53)

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

1) Produce input egammas:

- Re-emulate data (EGamma) with the current Global Tag

'''
python submitOnTier3.py --inFileList EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --nJobs 5475 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --nJobs 5475 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --nJobs 5475 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
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
python3 resolutions.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/TestInput_EGamma2022E --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --do_EoTot --tag _LooseEle_100K_Raw

python3 resolutions_CD.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/TestInput_EGamma2022E --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --do_EoTot --tag _LooseEle_100K_CD

python3 resolutions_CD.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/TestInput_EGamma2022E --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --do_EoTot --OnlyIem --EoTotcut 0.80 --tag _LooseEle_100K_EoTot80_CDIem
'''

2) Read egammas and produce inputs:

- Extract CD and target egamma energy from the ntuples

'''
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80 \
    --target reco --type ele --chunk_size 5000 \
    --queue short \
    --ecalcut 0.80 --applyCut_3_6_9 True --LooseEle --matching

python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --target reco --type ele --chunk_size 5000 \
    --queue short \
    --ecalcut 0.80 --applyCut_3_6_9 True --LooseEle --matching --ClusterFilter
'''

- Extract sample for the eg rate proxy

'''
(0,1,2,3)
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EphemeralZeroBias \
    --target emu --type ele --chunk_size 5000 \
    --queue short \
    --applyCut_3_6_9 True
(0,1,2,3)
python3 batchSubmitOnTier3.py \
    --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EphemeralZeroBias_ClusterFilter \
    --target emu --type ele --chunk_size 5000 \
    --queue short \
    --applyCut_3_6_9 True --ClusterFilter
'''

- Merge CD into tensorflow and save the input size:

'''
# (training 2100208, rate 2212965)
python3 batchMerger.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80 \
    --batchdir EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --v ECAL --odir DataReco --filesPerRecord 150 --selectResp --filesRatePerRecord 150 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EphemeralZeroBias/EphemeralZeroBias*__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data
# (training 2037258, rate 2142177)
python3 batchMerger.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --batchdir EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --v ECAL --odir DataReco --filesPerRecord 150 --selectResp --filesRatePerRecord 150 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EphemeralZeroBias_ClusterFilter/EphemeralZeroBias*__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data
'''

- Plot the inputs and check that the built CD energy distribution corresponds to the previous one

''' 
python3 PlotResponseTF.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --addtag _Uncalib --PlotRate --eventLim 100000 --filesLim 1
python3 PlotResponseTF.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --addtag _Uncalib --PlotRate --eventLim 100000 --filesLim 1
'''

- Compute target rate
'''
python3 TestRateProxy.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco
### INFO: Compute percentage of jets passing sum > 10 GeV :  0.07387914043847851
### INFO: Compute percentage of jets passing sum > 15 GeV :  0.015907818222017735
### INFO: Compute percentage of jets passing sum > 20 GeV :  0.004388947481312848
### INFO: Compute percentage of jets passing sum > 25 GeV :  0.001552178331611424

python3 TestRateProxy.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco
### INFO: Compute percentage of jets passing sum > 10 GeV :  0.0001276690477036096
### INFO: Compute percentage of jets passing sum > 15 GeV :  3.9554379876283344e-05
### INFO: Compute percentage of jets passing sum > 20 GeV :  3.4544733934349886e-05
### INFO: Compute percentage of jets passing sum > 25 GeV :  3.407791320554254e-05

(after fixing ECAL+HCAL)
python3 TestRateProxy.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco
### INFO: Compute percentage of jets passing sum > 10 GeV :  0.09334999406117471
### INFO: Compute percentage of jets passing sum > 15 GeV :  0.019813952140379967
### INFO: Compute percentage of jets passing sum > 20 GeV :  0.005333998668550897
### INFO: Compute percentage of jets passing sum > 25 GeV :  0.002604428290296369
'''

# FIX RATE TERM in the loss
3) Training:

'''
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --MaxLR 1E-4 --batch_size 4096 --epochs 20 --ThrRate 10 --TargetRate 0.07387914043847851
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRate.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --MaxLR 1E-4 --batch_size 4096 --epochs 20 --ThrRate 10 --TargetRate 0.0001276690477036096
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_Full.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --MaxLR 1E-5 --batch_size 4096 --epochs 20 --ThrRate 10 --TargetRate 0.0001276690477036096 --addtag _Full
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_Full.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --MaxLR 1E-4 --batch_size 4096 --epochs 20 --ThrRate 10 --TargetRate 0.0001276690477036096 --addtag _Full_LRE-4
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_Full.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --MaxLR 1E-3 --batch_size 4096 --epochs 20 --ThrRate 25 --TargetRate 0.002604428290296369 --addtag _Full_LRE-4_Regression100_NewRateProxy
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_Full.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --MaxLR 1E-2 --batch_size 4096 --epochs 10 --ThrRate 25 --TargetRate 0.002604428290296369 --addtag _Full_LRE-2_Regression500_NewRateProxy

python3 NNModel_v33.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --epochs 20

python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegression.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --MaxLR 1E-4 --batch_size 4096 --epochs 10 --addtag _OnlyRegression_LRE-4

'''

4) Extract SFs, plot SFs and plot performance from testing sample:

'''
python3 PrepareReEmulation.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --applyHCAL False --modelRate --filesLim 5 --eventLim 100000
python3 PrepareReEmulation.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --applyHCAL False --modelRate --filesLim 5 --eventLim 100000
python3 PrepareReEmulation.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --applyHCAL False --modelRate --addtag _Full --filesLim 5 --eventLim 100000
python3 PrepareReEmulation.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --applyHCAL False --modelRate --addtag _Full_LRE-4 --filesLim 5 --eventLim 100000
python3 PrepareReEmulation.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --applyHCAL False --modelRate --addtag _Full_LRE-4_Regression100_NewRateProxy --filesLim 5 --eventLim 100000
python3 PrepareReEmulation.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --applyHCAL False --modelRate --addtag _Full_LRE-2_Regression500_NewRateProxy --filesLim 5 --eventLim 100000

python3 PrepareReEmulation.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --applyHCAL False --modelRate --addtag _v33 --filesLim 5 --eventLim 100000

python3 PrepareReEmulation.py --indir 2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter \
    --v ECAL --tag DataReco --applyHCAL False --addtag _OnlyRegression_LRE-4 --filesLim 5 --eventLim 100000

python3 ProduceCaloParams.py --name caloParams_2023_ECALv53_HCALv51_HFv52_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80/ECALtrainingDataReco/data/ScaleFactors_ECAL_energystep2iEt.csv \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF   /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95/HCALtrainingDataReco/data/ScaleFactors_HF_energystep2iEt.csv

python3 ProduceCaloParams.py --name caloParams_2023_ECALv53_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80/ECALtrainingDataReco/data/ScaleFactors_ECAL_energystep2iEt.csv

python3 ProduceCaloParams.py --name caloParams_2023_ECALv53Cluster_HCALv51_HFv52_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter/ECALtrainingDataReco/data/ScaleFactors_ECAL_energystep2iEt.csv \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF   /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95/HCALtrainingDataReco/data/ScaleFactors_HF_energystep2iEt.csv

python3 ProduceCaloParams.py --name caloParams_2023_ECALv53Cluster_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80_ClusterFilter/ECALtrainingDataReco/data/ScaleFactors_ECAL_energystep2iEt.csv


python3 ProduceCaloParams.py --name caloParams_2023_ECALv53A_HCALv51_HFv52_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80/ECALtrainingDataReco/data_Full_LRE-4_Regression100_NewRateProxy/ScaleFactors_ECAL_energystep2iEt.csv \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF   /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95/HCALtrainingDataReco/data/ScaleFactors_HF_energystep2iEt.csv

python3 ProduceCaloParams.py --name caloParams_2023_ECALv53B_HCALv51_HFv52_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80/ECALtrainingDataReco/data_Full_LRE-2_Regression500_NewRateProxy/ScaleFactors_ECAL_energystep2iEt.csv \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF   /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95/HCALtrainingDataReco/data/ScaleFactors_HF_energystep2iEt.csv

python3 ProduceCaloParams.py --name caloParams_2023_ECALv53C_HCALv51_HFv52_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80/ECALtrainingDataReco/data_v33/ScaleFactors_ECAL_energystep2iEt.csv \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF   /data_CMS/cms/motta/CaloL1calibraton/2023_06_26_NtuplesV52/JetMET_PuppiJet_Pt30_HoTot95/HCALtrainingDataReco/data/ScaleFactors_HF_energystep2iEt.csv

python3 ProduceCaloParams.py --name caloParams_2023_ECALv53C_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_27_NtuplesV53/EGamma_LooseEle_EoTot80/ECALtrainingDataReco/data_v33/ScaleFactors_ECAL_energystep2iEt.csv

python3 ProduceCaloParams.py --name caloParams_2023_ECALv33_newCalib_cfi \
    --base caloParams_2023_v0_2_noL1Calib_cfi.py \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33/ECALtrainingDataReco_normalOrder/data/ScaleFactors_ECAL_energystep2iEt.csv

'''

5) Re-emulate:

- Create caloParams file
- Copy the file to the src/L1Trigger/L1TCalorimeter/python/ folder
- Launche re-emulation:

'''
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53HCALv51HFv52_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv53_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53HCALv51HFv52newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv53_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v53_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv53_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v53newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv53_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53ClusterHCALv51HFv52_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv53Cluster_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53ClusterHCALv51HFv52newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv53Cluster_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v53Cluster_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv53Cluster_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v53ClusternewCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv53Cluster_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53AHCALv51HFv52_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv53A_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53AHCALv51HFv52newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv53A_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53BHCALv51HFv52_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv53B_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53BHCALv51HFv52newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv53B_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53CHCALv51HFv52_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv53C_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53CHCALv51HFv52newCalib_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv53C_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53C_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv53C_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53C_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv53C_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv53CHCALv51HFv52_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv33_HCALv51_HFv52_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM

python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv33_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_ECALv33_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023ECALv33_data \
    --nJobs 31 \
    --queue short \
    --maxEvts 5000 \
    --caloParams caloParams_2023_ECALv33_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
'''

6) Performance evaluation:

'''
python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53HCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53_CD_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --EoTotcut 0.80 --OnlyIem --tag _LooseEle_100K_EoTot80_OnlyIem_CD
python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53HCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53_CD_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --tag _LooseEle_100K_CD

# UnCalib
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
# OldCalib
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw

# NewCalib 53
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53HCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53HCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv53HCALv51HFv52newCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew53_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle --do_EoTot
# NewCalib 53 ECAL Only
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v53_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53ECALOnly_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v53_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53ECALOnly_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v53newCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53ECALOnly_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew53ECALOnly_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle --do_EoTot

# NewCalib 53 Cluster
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53ClusterHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53Cluster_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53ClusterHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53Cluster_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv53ClusterHCALv51HFv52newCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53Cluster_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew53Cluster_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle --do_EoTot
# NewCalib 53 Cluster ECAL Only
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v53Cluster_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53ClusterECALOnly_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v53Cluster_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53ClusterECALOnly_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v53ClusternewCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53ClusterECALOnly_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew53ClusterECALOnly_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle --do_EoTot


# NewCalib 53A
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53AHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53A_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53AHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53A_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv53AHCALv51HFv52newCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53A_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew53A_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle

# NewCalib 53B
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53BHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53B_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53BHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53B_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv53BHCALv51HFv52newCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53B_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew53B_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle

# NewCalib 53C
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53CHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53C_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53CHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53C_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv53CHCALv51HFv52newCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53C_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew53C_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle

# NewCalib 53C ECAL Only
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53C_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53CECALOnly_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53C_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53CECALOnly_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv53C_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew53CECALOnly_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew53CECALOnly_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle

# Golden v33
# NewCalib 33
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53CHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew33_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv53CHCALv51HFv52_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew33_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv33HCALv51HFv52newCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew33_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew33_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle

# NewCalib 33 ECAL Only
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv33_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew33ECALOnly_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023ECALv33_data_reco_json \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew33ECALOnly_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023ECALv33newCalib_data \
 --outdir 2023_06_27_NtuplesV53/NtuplesVnew33ECALOnly_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
python3 comparisonPlots.py --indir 2023_06_27_NtuplesV53/NtuplesVnew33ECALOnly_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_27_NtuplesV53/NtuplesVcur_Raw_LooseEle --unc 2023_06_27_NtuplesV53/NtuplesVunc_Raw_LooseEle

'''

