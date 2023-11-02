Instructions for the training of ECAL (V49)

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

- Plot the jets and check that the CD energy distribution is the same as the RawEt energy distribution

'''
python3 resolutions.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/TestInput_EGamma2022E --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --do_EoTot --tag _LooseEle_100K_Raw

python3 resolutions_CD.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/TestInput_EGamma2022E --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --do_EoTot --tag _LooseEle_100K_CD

python3 resolutions_CD.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/TestInput_EGamma2022E --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --do_EoTot --OnlyIem --tag _LooseEle_100K_CDIem

python3 resolutions_CD.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/TestInput_EGamma2022E --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --do_EoTot --OnlyIem --EoTotcut 0.80 --tag _LooseEle_100K_EoTot80_CDIem
'''

2) Read egammas and produce inputs:

- Extract CD and target egamma energy from the ntuples

'''
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_06_NtuplesV49/EGamma_LooseEle_EoTot80 \
    --target reco --type ele --chunk_size 5000 \
    --queue short \
    --etacut 28 --ecalcut 0.80 --applyCut_3_6_9 True --LooseEle
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_06_NtuplesV49/EGamma_LooseEle_EoTot80 \
    --target reco --type ele --chunk_size 5000 \
    --queue short \
    --etacut 28 --ecalcut 0.80 --applyCut_3_6_9 True --LooseEle
python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_06_NtuplesV49/EGamma_LooseEle_EoTot80 \
    --target reco --type ele --chunk_size 5000 \
    --queue short \
    --etacut 28 --ecalcut 0.80 --applyCut_3_6_9 True --LooseEle
'''

- Merge CD into tensorflow and save the input size:

'''
# New ECAL Calib 23.6M
loadGPUtf
python3 batchMerger.py --indir 2023_06_06_NtuplesV49/EGamma_LooseEle_EoTot80 \
    --batchdir EGamma__Run2022* --v ECAL --odir DataReco --filesPerRecord 100 --selectResp --noRate
'''

- Plot the inputs and check that the built CD energy distribution corresponds to the previous one

'''
python3 PlotResponseTF.py --indir 2023_06_06_NtuplesV49/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --filesLim 50 --eventLim 50000 --addtag _Uncalib
'''

3) Training:

''' 5M events (300s per epoch)
python3 NNModelTraining_FullyCustom_GPUdistributed_OnlyRegression.py --indir 2023_06_06_NtuplesV49/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --MaxLR 1E-5 --addtag _50Files_OnlyRegression_LRe-5 --batch_size 2048 --epochs 20 --filesLim 50
'''
''' 19M events (1000s per epoch)
python3 NNModelTraining_FullyCustom_GPUdistributed_OnlyRegression.py --indir 2023_06_06_NtuplesV49/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --MaxLR 1E-5 --addtag _OnlyRegression_LRe-5 --batch_size 2048 --epochs 20 --filesLim 100
'''

4) Extract SFs, plot SFs and plot performance from testing sample:

'''
python3 PrepareReEmulation.py --indir 2023_06_06_NtuplesV49/EGamma_LooseEle_EoTot80 \
    --v ECAL --tag DataReco --addtag _50Files_OnlyRegression_LRe-5 --applyHCAL False --eventLim 50000
'''

5) Re-emulate:

- Create caloParams file
- Copy the file to the src/L1Trigger/L1TCalorimeter/python/ folder
- Launche re-emulation:
'''
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_noL1Calib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v0_2_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v49_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v49_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM

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
    --outTag GT130XdataRun3Promptv3_CaloParams2023v49newCalib_data \
    --nJobs 278 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v49_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data
'''

6) Performance evaluation:

'''
python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v49_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_CD_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --EoTotcut 0.80 --OnlyIem --tag _LooseEle_100K_EoTot80_OnlyIem_CD
python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v49_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_CD_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --EoTotcut 0.80 --tag _LooseEle_100K_EoTot80_CD
python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v49_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_CD_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele \
 --raw --LooseEle --tag _LooseEle_100K_CD

# UnCalib
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
 --outdir 2023_06_06_NtuplesV49/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
# OldCalib
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
 --outdir 2023_06_06_NtuplesV49/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw

# NewCalib
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v49_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v49_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v49newCalib_data \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw

python3 comparisonPlots.py --indir 2023_06_06_NtuplesV49/NtuplesVnew49_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_06_NtuplesV49/NtuplesVcur_Raw_LooseEle --unc 2023_06_06_NtuplesV49/NtuplesVunc_Raw_LooseEle --do_EoTot
'''

7) Re-emulate with new HCAL v48 calibration:

'''
python submitOnTier3.py --inFileList EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v49_HCALv48C_data_reco_json \
    --nJobs 115 \
    --queue short \
    --maxEvts -1 \
    --inJson Cert_Collisions2022_355100_362760_Golden \
    --caloParams caloParams_2023_v49_HCALv48C_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data \
    --recoFromSKIM

python submitOnTier3.py --inFileList EphemeralZeroBias0__Run2022G-v1__Run362617__RAW \
    --outTag GT130XdataRun3Promptv3_CaloParams2023v49_HCALv48CnewCalib_data \
    --nJobs 278 \
    --queue short \
    --maxEvts -1 \
    --caloParams caloParams_2023_v49_HCALv48C_newCalib_cfi \
    --globalTag 130X_dataRun3_Prompt_v3 \
    --data

# NewCalib
python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v49_HCALv48C_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_HCALv48C_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --do_EoTot
python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v49_HCALv48C_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_HCALv48C_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v49_HCALv48C_data_reco_json \
 --outdir 2023_06_06_NtuplesV49/NtuplesVnew49_HCALv48C_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw

python3 comparisonPlots.py --indir 2023_06_06_NtuplesV49/NtuplesVnew49_HCALv48C_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
 --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
 --old 2023_06_06_NtuplesV49/NtuplesVcur_Raw_LooseEle --unc 2023_06_06_NtuplesV49/NtuplesVunc_Raw_LooseEle --do_EoTot

'''