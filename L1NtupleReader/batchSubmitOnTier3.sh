source /opt/exp_soft/cms/t3/t3setup


# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNtuples/ElectronTraining_JSON \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_02_20_NtuplesV29 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True 

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNtuples/JetTraining_JSON \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_02_28_NtuplesV31 \
#                               --target reco --type jet --chunk_size 5000 \
#                               --queue short \
#                               --etacut 41 --hcalcut True --lJetPtCut 30 --uJetPtCut 1000

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_02_20_NtuplesV29 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_02_20_NtuplesV29 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_02_20_NtuplesV29 \
#                               --target reco --type jet --chunk_size 5000 \
#                               --queue short \
#                               --etacut 41 --hcalcut True --lJetPtCut 30 --uJetPtCut 1000

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_02_20_NtuplesV29 \
#                               --target reco --type jet --chunk_size 5000 \
#                               --queue short \
#                               --etacut 41 --hcalcut True --lJetPtCut 30 --uJetPtCut 1000

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePionGun_E0p2to200__Run3Winter23Digi-NoPU_126X_mcRun3_2023_forPU65_v1-v2__GEN-SIM-RAW__GT130XmcRun32022realisticv2_CaloParams2022v06_noL1calib \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_03_NtuplesV32 \
#                               --target gen --type jet --chunk_size 5000 \
#                               --queue short \
#                               --etacut 41 --hcalcut True --lJetPtCut 30 --uJetPtCut 1000

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True #--resubmit_failed

# python3 batchSubmitOnTier3_resubmit.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True #--resubmit_failed

# python3 batchSubmitOnTier3_resubmit.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True #--resubmit_failed

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target reco --type jet --chunk_size 5000 \
#                               --queue short \
#                               --etacut 41 --hcalcut True --lJetPtCut 30 --uJetPtCut 1000 \
#                               --resubmit_failed

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON_Early_G_Era \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target reco --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --hcalcut True --lJetPtCut 30 --uJetPtCut 1000 \
#                               --resubmit_failed

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON_Late_G_Era \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target reco --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --hcalcut True --lJetPtCut 30 --uJetPtCut 1000 \
#                               --resubmit_failed

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target emu --type jet --chunk_size 400 \
#                               --queue short \
#                               --etacut 41 \
#                               --resubmit_failed

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 --addtag _currCalib \
#                               --target emu --type jet --chunk_size 400 \
#                               --queue short \
#                               --etacut 41 --calibECALOnTheFly currCalib --calibHCALOnTheFly currCalib \
#                               --resubmit_failed

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_22_NtuplesV35 \
#                               --target reco_corr --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --HoTotcut 0.3

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_7000_10000/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_22_NtuplesV35 \
#                               --target reco_corr --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --HoTotcut 0.3

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_15000_20000/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_22_NtuplesV35 \
#                               --target reco_corr --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --HoTotcut 0.3

# # Training wrt GenPt
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_24_NtuplesV36 \
#                               --target gen --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_7000_10000/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_24_NtuplesV36 \
#                               --target gen --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_15000_20000/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_24_NtuplesV36 \
#                               --target gen --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True

# # Training with 3M events
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_10000_15000/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_25_NtuplesV37 \
#                               --target reco_corr --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --HoTotcut 0.3

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_20000_25000/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_25_NtuplesV37 \
#                               --target reco_corr --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --HoTotcut 0.3

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/FromOlivier_March23/QCD_30_500_692488_to_694487/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_25_NtuplesV37 \
#                               --target reco_corr --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --HoTotcut 0.3

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/FromOlivier_March23/QCD_30_500_694488_to_696487/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_25_NtuplesV37 \
#                               --target reco_corr --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --HoTotcut 0.3

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/FromOlivier_March23/QCD_30_500_696488_to_698487/L1Ntuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_25_NtuplesV37 \
#                               --target reco_corr --type jet --chunk_size 2500 \
#                               --queue short \
#                               --etacut 41 --lJetPtCut 30 --uJetPtCut 1000 --HoTotcut 0.3

# # test rate
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target emu --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True --calibECALOnTheFly v33_newCalib \
#                               --addtag _v33RateTest

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target emu --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True --calibECALOnTheFly v33Rate0p8_newCalib \
#                               --addtag _v33RateTest0p8

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target emu --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True --calibECALOnTheFly v33Rate1p2_newCalib \
#                               --addtag _v33RateTest1p2

# # correct rate
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target emu --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True --calibECALOnTheFly v33Rate0p8True_newCalib \
#                               --addtag _v33RateTest0p8True

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33 \
#                               --target emu --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True --calibECALOnTheFly v33Rate1p2True_newCalib \
#                               --addtag _v33RateTest1p2True

# rate studies
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/0000_00_00_NtuplesRateVunc \
#                               --target rate --type ele --chunk_size 1000 --ClusterFilter True \
#                               --queue short \
#                               --etacut 28 --lJetPtCut 15 --applyCut_3_6_9 True \
#                               --addtag _RateProxyCluster

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/0000_00_00_NtuplesRateVcurr \
#                               --target rate --type ele --chunk_size 5000 --ClusterFilter True \
#                               --queue short \
#                               --etacut 28 --ecalcut True --lJetPtCut 15 --applyCut_3_6_9 True \
#                               --addtag _RateProxyCluster 

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_06_NtuplesV39 \
#                               --target rate --type ele --chunk_size 5000 --ClusterFilter True \
#                               --queue short \
#                               --etacut 28 --lJetPtCut 15 --applyCut_3_6_9 True

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_06_NtuplesV39 \
#                               --target rate --type ele --chunk_size 5000 --ClusterFilter True \
#                               --queue short \
#                               --etacut 28 --lJetPtCut 15 --applyCut_3_6_9 True

# New training on MC after talking to Mariarosaria
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_7000_10000/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_10000_15000/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_15000_20000/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_20000_25000/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_25000_30000/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/FromOlivier_March23/QCD_30_500_692488_to_694487/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/FromOlivier_March23/QCD_30_500_694488_to_696487/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/FromOlivier_March23/QCD_30_500_696488_to_698487/L1Ntuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 50 --uJetPtCut 1000 --hcalcut True --applyZS True

# removed the shuffle in order to keep track of the position of the seed
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target emu --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40 --target emu --type jet --chunk_size 2500 \
#     --queue short --etacut 28 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True

# # training on data in the barrel: BUGGED!!!!!!!!! ZS is applied in the wrong way
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON_Early_G_Era \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON_Late_G_Era \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41 --target reco --type jet --chunk_size 2500 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True --applyZS True
# # not sure about these cuts but for v41 we don't use the rate
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41 --target emu --type jet --chunk_size 2500 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True

# training on data in the barrel with ZS
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV42 --target reco --type jet --chunk_size 5000 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON_Early_G_Era \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV42 --target reco --type jet --chunk_size 5000 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True --applyZS True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON_Late_G_Era \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV42 --target reco --type jet --chunk_size 5000 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True --applyZS True

# # training on data in the barrel without ZS
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV43 --target reco --type jet --chunk_size 5000 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON_Early_G_Era \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV43 --target reco --type jet --chunk_size 5000 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON_Late_G_Era \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV43 --target reco --type jet --chunk_size 5000 \
#     --queue short --etacut 15 --lJetPtCut 30 --uJetPtCut 1000 --hcalcut True

# # test!!!
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples//Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_05_01_NtuplesV44 --target reco --type jet --chunk_size 100 \
#     --queue short
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/davignon/Layer1SFsNTPLS/JetTraining_JSON \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_05_01_NtuplesV45 --target reco --type jet --chunk_size 100 \
#     --queue short

########################################################################################################################
########################################################################################################################
# New training with EGamma GT130
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_05_19_NtuplesV46 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True --LooseEle

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_05_19_NtuplesV46 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True --LooseEle

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_05_19_NtuplesV46 \
#                               --target reco --type ele --chunk_size 5000 \
#                               --queue short \
#                               --etacut 28 --ecalcut True --applyCut_3_6_9 True --LooseEle

########################################################################################################################
########################################################################################################################
# New training with Jets GT130
# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_05_20_NtuplesV47/JetMET_HoTot95_puppi_barrel \
#                               --target reco --type jet --chunk_size 5000 \
#                               --queue short \
#                               --etacut 15 --hcalcut 0.95 --lJetPtCut 30 --PuppiJet

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_05_20_NtuplesV47/JetMET_HoTot80_puppi_barrel \
#                               --target reco --type jet --chunk_size 5000 \
#                               --queue short \
#                               --etacut 15 --hcalcut 0.8 --lJetPtCut 30 --PuppiJet

# python3 batchSubmitOnTier3.py --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
#                               --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_05_20_NtuplesV47/JetMET_HoTot50_puppi_barrel_MinusIem \
#                               --target reco --type jet --chunk_size 5000 \
#                               --queue short \
#                               --etacut 15 --hcalcut 0.5 --lJetPtCut 30 --PuppiJet --trainPtVers HCAL

# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias0_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias1__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias1_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias2__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias2_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias3__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias3_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias4__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias4_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias5__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias5_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias6__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias6_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias7__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias7_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000
# python3 batchSubmitOnTier3.py \
#     --indir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias8__Run2022G-v1__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#     --outdir /data_CMS/cms/motta/CaloL1calibraton/2023_06_08_NtuplesV50/EphemeralZeroBias8_Barrel_Pt30To1000 \
#     --target emu --type jet --chunk_size 5000 \
#     --queue short \
#     --etacut 15 --lJetPtCut 30 --uJetPtCut 1000

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


####################################################################################################################################################################################################
####################################################################################################################################################################################################
####################################################################################################################################################################################################
## OLD COMMANDS FOR OLD VERSION OF THE SUBMITTER


# python batchSubmitOnTier3.py --doEG0_200 --uJetPtCut 60 --etacut 28 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib --trainPtVers ECAL 
# python batchSubmitOnTier3.py --doEG0_200 --uJetPtCut 60 --etacut 28 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib --trainPtVers ECAL
# python batchSubmitOnTier3.py --doEG0_200 --uJetPtCut 60 --etacut 28 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib --trainPtVers ECAL

# python batchSubmitOnTier3.py --doEG200_500 --jetcut 60 --etacut 24 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doEG200_500 --jetcut 60 --etacut 24 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doEG200_500 --jetcut 60 --etacut 24 --ecalcut True --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib

# python batchSubmitOnTier3.py --doQCD --qcdPtBin "50To80" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doQCD --qcdPtBin "50To80" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doQCD --qcdPtBin "50To80" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 30

# python batchSubmitOnTier3.py --doQCD --qcdPtBin "80To120" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doQCD --qcdPtBin "80To120" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doQCD --qcdPtBin "80To120" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 50

# python batchSubmitOnTier3.py --doQCD --qcdPtBin "120To170" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doQCD --qcdPtBin "120To170" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doQCD --qcdPtBin "120To170" --etacut 37 --indir 2022_05_02_NtuplesV8 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 60


# python batchSubmitOnTier3.py --doQCDpu --indir 2022_05_02_NtuplesV8 --odir --applyHCALpfa1p --applyNoCalib
# python batchSubmitOnTier3.py --doQCDpu --indir 2022_05_02_NtuplesV8 --odir --applyHCALpfa1p --applyOldCalib
# python batchSubmitOnTier3.py --doQCDpu --indir 2022_05_02_NtuplesV8 --odir --applyHCALpfa1p --applyNewECALcalib


# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut 1 --indir 2022_05_16_NtuplesVtest1 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --lJetPtCut 15 --uJetPtCut 500 --trainPtVers HCAL
# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut 2 --indir 2022_05_16_NtuplesVtest2 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --lJetPtCut 15 --uJetPtCut 500 --trainPtVers HCAL
# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut 3 --indir 2022_05_16_NtuplesVtest3 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --lJetPtCut 15 --uJetPtCut 500 --trainPtVers HCAL

# python batchSubmitOnTier3.py --doQCD --qcdPtBin "50To80" --etacut 24 --indir 2022_05_03_NtuplesV11 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 50 --uJetPtCut 150 --trainPtVers HCAL
# python batchSubmitOnTier3.py --doQCD --qcdPtBin "80To120" --etacut 24 --indir 2022_05_03_NtuplesV11 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 50 --uJetPtCut 150 --trainPtVers HCAL
# python batchSubmitOnTier3.py --doQCD --qcdPtBin "120To170" --etacut 24 --indir 2022_05_03_NtuplesV11 --applyHCALpfa1p --applyNewECALcalib --lJetPtCut 60 --uJetPtCut 150 --trainPtVers HCAL

# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --lJetPtCut 30 --uJetPtCut 300 --odir _30_300_forceEtaZero

# python batchSubmitOnTier3.py --doPi0_200 --etacut 37 --hcalcut True --indir 2022_05_23_NtuplesV18 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --uJetPtCut 200

# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --calibHCALOnTheFly newCalib --applyOnTheFly True --lJetPtCut 30 --uJetPtCut 300 --odir _30_300_newCalibrationOnTheFly
# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_20_NtuplesV17 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly oldCalib --calibHCALOnTheFly oldCalib --applyOnTheFly True --lJetPtCut 30 --uJetPtCut 300 --odir _30_300_oldCalibrationOnTheFly
# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_20_NtuplesV17 --applyHCALpfa1p --applyNoCalib                                                           --applyOnTheFly True --lJetPtCut 30 --uJetPtCut 300 --odir _30_300_noCalibration

# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --calibHCALOnTheFly newCalib --applyOnTheFly True --lJetPtCut 300 --uJetPtCut 600 --odir _300_600_newCalibrationOnTheFly
# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly oldCalib --calibHCALOnTheFly oldCalib --applyOnTheFly True --lJetPtCut 300 --uJetPtCut 600 --odir _300_600_oldCalibrationOnTheFly
# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib                                                           --applyOnTheFly True --lJetPtCut 300 --uJetPtCut 600 --odir _300_600_noCalibration

# python batchSubmitOnTier3.py --doEG0_200 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --calibHCALOnTheFly newCalib --applyOnTheFly True --uJetPtCut 100 --odir _0_100_newCalibrationOnTheFly
# python batchSubmitOnTier3.py --doEG0_200 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly oldCalib --calibHCALOnTheFly oldCalib --applyOnTheFly True --uJetPtCut 100 --odir _0_100_oldCalibrationOnTheFly
# python batchSubmitOnTier3.py --doEG0_200 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib                                                           --applyOnTheFly True --uJetPtCut 100 --odir _0_100_noCalibration

# python batchSubmitOnTier3.py --doEG0_200 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --calibHCALOnTheFly newCalib --applyOnTheFly True --lJetPtCut 100 --uJetPtCut 300 --odir _100_300_newCalibrationOnTheFly
# python batchSubmitOnTier3.py --doEG0_200 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly oldCalib --calibHCALOnTheFly oldCalib --applyOnTheFly True --lJetPtCut 100 --uJetPtCut 300 --odir _100_300_oldCalibrationOnTheFly
# python batchSubmitOnTier3.py --doEG0_200 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib                                                           --applyOnTheFly True --lJetPtCut 100 --uJetPtCut 300 --odir _100_300_noCalibration

# python batchSubmitOnTier3.py --doEG200_500 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --calibHCALOnTheFly newCalib --applyOnTheFly True --lJetPtCut 200 --uJetPtCut 500 --odir _200_500_newCalibrationOnTheFly
# python batchSubmitOnTier3.py --doEG200_500 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly oldCalib --calibHCALOnTheFly oldCalib --applyOnTheFly True --lJetPtCut 200 --uJetPtCut 500 --odir _200_500_oldCalibrationOnTheFly
# python batchSubmitOnTier3.py --doEG200_500 --etacut 28 --ecalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib                                                           --applyOnTheFly True --lJetPtCut 200 --uJetPtCut 500 --odir _200_500_noCalibration


# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --calibHCALOnTheFly newCalib --applyOnTheFly True --lJetPtCut 30 --uJetPtCut 300 --odir _30_300_flooringTrainingSFapplied
# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib --calibECALOnTheFly newCalib --calibHCALOnTheFly newCalib --applyOnTheFly True --lJetPtCut 30 --uJetPtCut 300 --odir _30_300_newTrainingSFapplied
# python batchSubmitOnTier3.py --doQCD --etacut 37 --hcalcut True --indir 2022_05_18_NtuplesV16 --applyHCALpfa1p --applyNoCalib                                                           --applyOnTheFly True --lJetPtCut 30 --uJetPtCut 300 --odir _30_300_noSFapplied



# python batchSubmitOnTier3.py --doEG0_200   --etacut 28 --ecalcut True --indir 2022_06_01_NtuplesV19 --applyHCALpfa1p --applyNoCalib                                 --applyCut_3_6_9 True --odir _0pt200
# python batchSubmitOnTier3.py --doEG200_500 --etacut 28 --ecalcut True --indir 2022_06_01_NtuplesV19 --applyHCALpfa1p --applyNoCalib                                 --applyCut_3_6_9 True --odir _200pt500
# python batchSubmitOnTier3.py --doQCD   --etacut 37 --hcalcut True --indir 2022_06_01_NtuplesV19 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 1000                       --odir _30pt1000
# python batchSubmitOnTier3.py --doQCD   --etacut 37 --hcalcut True --indir 2022_06_01_NtuplesV19 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 500                        --odir _30pt500
# python batchSubmitOnTier3.py --doQCD   --etacut 37 --hcalcut True --indir 2022_06_01_NtuplesV19 --applyHCALpfa1p --applyNoCalib --lJetPtCut 20 --uJetPtCut 1000                       --odir _20pt1000

# python batchSubmitOnTier3.py --doQCD   --etacut 41 --hcalcut True --indir 2022_06_01_NtuplesV19 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 1000                       --odir _30pt1000_eta41

# python batchSubmitOnTier3.py --doQCD   --etacut 41 --hcalcut True --indir 2022_06_01_NtuplesV19 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 1000                       --odir _30pt1000_eta41_newFeat


# python batchSubmitOnTier3.py --doEG0_200pu   --etacut 28 --ecalcut True --indir 2022_06_10_NtuplesV20 --applyHCALpfa1p --applyNoCalib                                 --applyCut_3_6_9 True --odir _0pt200
# python batchSubmitOnTier3.py --doEG200_500pu --etacut 28 --ecalcut True --indir 2022_06_10_NtuplesV20 --applyHCALpfa1p --applyNoCalib                                 --applyCut_3_6_9 True --odir _200pt500
# python batchSubmitOnTier3.py --doQCDpu       --etacut 41 --hcalcut True --indir 2022_06_10_NtuplesV20 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 1000                       --odir _30pt1000
# python batchSubmitOnTier3.py --doQCDpu       --etacut 41 --hcalcut True --indir 2022_06_10_NtuplesV20 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 500                        --odir _30pt500
# python batchSubmitOnTier3.py --doQCDpu       --etacut 41 --hcalcut True --indir 2022_06_10_NtuplesV20 --applyHCALpfa1p --applyNoCalib --lJetPtCut 20 --uJetPtCut 1000                       --odir _20pt1000

# python batchSubmitOnTier3.py --doQCD       --etacut 41 --hcalcut True --indir 2022_07_12_NtupleV22 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 1000                       --odir _30pt1000_eta41_nTT



# python batchSubmitOnTier3.py --doEG0_200   --etacut 28 --ecalcut True --indir 2022_07_20_NtuplesV23 --applyHCALpfa1p --applyNoCalib                                 --applyCut_3_6_9 True --odir _0pt200
# python batchSubmitOnTier3.py --doEG200_500 --etacut 28 --ecalcut True --indir 2022_07_20_NtuplesV23 --applyHCALpfa1p --applyNoCalib                                 --applyCut_3_6_9 True --odir _200pt500
# python batchSubmitOnTier3.py --doQCD       --etacut 41 --hcalcut True --indir 2022_07_20_NtuplesV23 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 1000                       --odir _30pt1000
# python batchSubmitOnTier3.py --doQCD       --etacut 41 --hcalcut True --indir 2022_07_20_NtuplesV23 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 500                        --odir _30pt500
# python batchSubmitOnTier3.py --doQCD       --etacut 41 --hcalcut True --indir 2022_07_20_NtuplesV23 --applyHCALpfa1p --applyNoCalib --lJetPtCut 20 --uJetPtCut 1000                       --odir _20pt1000

# Elena
# python batchSubmitOnTier3.py --doQCD       --etacut 41 --hcalcut True --TTNumberCut True --indir 2022_09_05_NtuplesV25 --applyHCALpfa1p --applyNoCalib --lJetPtCut 30 --uJetPtCut 1000

# python batchSubmitOnTier3.py --doNuGun --etacut 41 --indir 2023_01_16_NtuplesV27 --applyHCALpfa1p --applyNoCalib --applyCut_3_6_9 True --odir _rateProxy
# python batchSubmitOnTier3.py --doNuGun --etacut 41 --indir 2023_01_16_NtuplesV27 --applyHCALpfa1p --applyNoCalib --applyCut_3_6_9 True --odir _rateProxy_oldCalib --calibECALOnTheFly oldCalib --calibHCALOnTheFly oldCalib

# python batchSubmitOnTier3.py --doEG0_200   --etacut 28 --ecalcut True --indir 2022_07_20_NtuplesV27 --applyHCALpfa1p --applyOldCalib                                 --applyCut_3_6_9 True --odir _0pt200_oldCalib
# python batchSubmitOnTier3.py --doEG200_500 --etacut 28 --ecalcut True --indir 2022_07_20_NtuplesV27 --applyHCALpfa1p --applyOldCalib                                 --applyCut_3_6_9 True --odir _200pt500_oldCalib
# python batchSubmitOnTier3.py --doQCD       --etacut 41 --hcalcut True --indir 2022_07_20_NtuplesV27 --applyHCALpfa1p --applyOldCalib --lJetPtCut 30 --uJetPtCut 1000                       --odir _30pt1000_oldCalib

# python batchSubmitOnTier3.py --doNuGun --etacut 41 --indir 2023_01_16_NtuplesV27 --applyHCALpfa1p --applyOldCalib --applyCut_3_6_9 True --odir _rateProxy

# python batchSubmitOnTier3.py --doNuGun --etacut 41 --indir 2023_01_16_NtuplesV27 --applyHCALpfa1p --applyNewECALpHCALcalib --applyCut_3_6_9 True --odir _v23_rateProxy

