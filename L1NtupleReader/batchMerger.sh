# python3 batchMerger.py --indir 2023_02_20_NtuplesV29 --batchdir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --v ECAL --odir DataReco --sample test
# python3 batchMerger.py --indir 2023_02_20_NtuplesV29 --batchdir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json --v ECAL --odir DataReco --sample oldCalib

# python3 batchMerger.py --indir 2023_02_20_NtuplesV29 --batchdir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json          --v HCAL --odir DataReco --sample test
# python3 batchMerger.py --indir 2023_02_20_NtuplesV29 --batchdir JetMET__Run2022G-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json --v HCAL   --odir DataReco --sample oldCalib


# python3 batchMerger.py --indir 2023_02_28_NtuplesV31 --batchdir ElectronTraining_JSON     --v ECAL --odir DataReco --sample train
# python3 batchMerger.py --indir 2023_02_28_NtuplesV31 --batchdir JetTraining_JSON          --v HCAL --odir DataReco --sample train --flattenEtaDistribution
# python3 batchMerger.py  --indir 2023_03_03_NtuplesV32 \
#                         --batchdir SinglePionGun_E0p2to200__Run3Winter23Digi-NoPU_126X_mcRun3_2023_forPU65_v1-v2__GEN-SIM-RAW__GT130XmcRun32022realisticv2_CaloParams2022v06_noL1calib \
#                         --v HCAL --odir MCGen --sample train

# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --batchdir EGamma__Run2022* --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --v ECAL --odir DataReco --filesPerRecord 50
# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --batchdir JetTraining_*    --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --v HCAL --odir DataReco --filesPerRecord 50

# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --rate_only --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --v ECAL --odir DataRecoCurrCalib --filesPerRecord 50
# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --rate_only --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --v HCAL --odir DataRecoCurrCalib --filesPerRecord 50


# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --rate_only 16000000 --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --v ECAL --odir DataReco_invertedOrder --HCALcalib4rate 2023_03_06_NtuplesV33/HCALtrainingDataReco_invertedOrder --filesPerRecord 50
# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --rate_only 9000000  --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --v HCAL --odir DataReco_normalOrder   --ECALcalib4rate 2023_03_06_NtuplesV33/ECALtrainingDataReco_normalOrder   --filesPerRecord 25

# python3 batchMerger.py --indir 2023_03_22_NtuplesV35 --batchdir L1Ntuples --v HCAL --odir MCRecoCorr --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --filesPerRecord 200

# python3 batchMerger.py --indir 2023_03_24_NtuplesV36 --batchdir L1Ntuples --v HCAL --odir MCGen --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --filesPerRecord 300

# python3 batchMerger.py --indir 2023_03_25_NtuplesV37 --batchdir L1Ntuples --v HCAL --odir MCRecoCorr --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --filesPerRecord 300

# python3 batchMerger.py --indir 2023_03_25_NtuplesV37 --batchdir L1Ntuples --v HCAL --odir MCRecoCorr_FlattenEta --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --filesPerRecord 300 --flattenEtaDistribution

# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_v33RateTest --v ECAL --odir v33RateTest --rate_only 1 --filesPerRecord 300
# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_v33RateTest0p8 --v ECAL --odir v33RateTest0p8 --rate_only 1 --filesPerRecord 300
# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_v33RateTest1p2 --v ECAL --odir v33RateTest1p2 --rate_only 1 --filesPerRecord 300

# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_v33RateTest0p8True --v ECAL --odir v33RateTest0p8True --rate_only 1 --filesPerRecord 300
# python3 batchMerger.py --indir 2023_03_06_NtuplesV33 --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_v33RateTest1p2True --v ECAL --odir v33RateTest1p2True --rate_only 1 --filesPerRecord 300

# # new rate proxy woth clusterfilter
# python3 batchMerger.py --indir 0000_00_00_NtuplesRateVunc --ratedir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_RateProxyCluster --v ECAL --odir RateProxyFilterCluster --rate_only 1 --filesPerRecord 300
# python3 batchMerger.py --indir 2023_04_06_NtuplesV39 --ratedir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data --v ECAL --odir TargetRateProxy --rate_only 1 --filesPerRecord 300

# # prepare input to NN testing with different options
# python3 batchMerger.py --indir 2023_04_06_NtuplesV39 \
#         --batchdir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#         --v ECAL --odir DataReco --filesPerRecord 300 \
#         --ratedir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data --filesLim 500

# # prepare input to NN with full ECAL stat
# python3 batchMerger.py --indir 2023_04_06_NtuplesV39 \
#         --batchdir EGamma__Run2022*-ZElectron-PromptReco-v1__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json \
#         --v ECAL --odir DataRecoFullStat --filesPerRecord 300 \
#         --ratedir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# # prepare input to NN training for HCAL
# python3 batchMerger.py --indir 2023_04_13_NtuplesV40 \
#         --batchdir L1Ntuples \
#         --v HCAL --odir MCReco --filesPerRecord 300 \
#         --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_06_NtuplesV39/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# # prepare input to NN training for HCAL with data ieta <= 15 (80K jets)
# python3 batchMerger.py --indir 2023_04_18_NtuplesV41 --batchdir JetTraining_JSON* --v HCAL --odir DataReco --filesPerRecord 1000 \
#  --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# # prepare input to NN training for HCAL with data ieta <= 15 and jetPt restriction (16K jets)
# python3 batchMerger.py --indir 2023_04_18_NtuplesV41 --batchdir JetTraining_JSON* --v HCAL --odir DataReco50to80 --ljetPtcut 50 --ujetPtcut 80 --filesPerRecord 1000 \
#  --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# prepare input to NN training for HCAL with data ieta <= 15 with ZS and suppression of one hot encoding
# python3 batchMerger.py --indir 2023_04_29_NtuplesV42 --batchdir JetTraining_JSON* --v HCAL --odir DataReco --filesPerRecord 1000 \
#  --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# prepare input to NN training for HCAL with data ieta <= 15 without ZS and suppression of one hot encoding
# python3 batchMerger.py --indir 2023_04_29_NtuplesV43 --batchdir JetTraining_JSON* --v HCAL --odir DataReco --filesPerRecord 1000 \
#  --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

python3 batchMerger.py --indir 2023_05_01_NtuplesV44 --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 1000 \
 --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

######################################################################################################################
######################################################################################################################
# New ECAL Calib (23919637)
python3 batchMerger.py --indir 2023_05_19_NtuplesV46 \
    --batchdir EGamma__Run2022*-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
    --v ECAL --odir DataReco --filesPerRecord 300 \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# New HCAL Calib (6896)
python3 batchMerger.py --indir 2023_05_20_NtuplesV47/JetMET_HoTot95_puppi_barrel \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# New HCAL Calib (299650)
python3 batchMerger.py --indir 2023_05_20_NtuplesV47/JetMET_HoTot80_puppi_barrel \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# New HCAL Calib (3022087)
python3 batchMerger.py --indir 2023_05_20_NtuplesV47/JetMET_HoTot50_puppi_barrel_MinusIem \
    --batchdir GoodNtuples --v HCAL --odir DataReco --filesPerRecord 300 --selectResp \
    --ratedir /data_CMS/cms/motta/CaloL1calibraton/2023_04_18_NtuplesV41/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data

# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir ElectronTraining_JSON --v ECAL --odir DataReco --sample train
# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir JetTraining_JSON      --v HCAL --odir DataReco --sample train
# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir JetTraining_JSON      --v HF   --odir DataReco --sample train

# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06noL1Calib_data_reco_json  --v ECAL --odir DataReco --sample test
# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06noL1Calib_data_reco_json                 --v HCAL --odir DataReco --sample test
# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06noL1Calib_data_reco_json                 --v HF   --odir DataReco --sample test

# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p_batches/paddedAndReadyToMerge_rateProxy_oldCalib --v ECAL --odir DataReco --sample targetRate --noY
# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p_batches/paddedAndReadyToMerge_rateProxy_oldCalib --v HCAL --odir DataReco --sample targetRate --noY
# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p_batches/paddedAndReadyToMerge_rateProxy_oldCalib --v HF   --odir DataReco --sample targetRate --noY

# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p_batches/paddedAndReadyToMerge_rateProxy --v ECAL --odir DataReco --sample trainRate --noY
# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p_batches/paddedAndReadyToMerge_rateProxy --v HCAL --odir DataReco --sample trainRate --noY
# python3 batchMerger.py --indir 2023_02_22_NtuplesV30 --batchdir SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p_batches/paddedAndReadyToMerge_rateProxy --v HF   --odir DataReco --sample trainRate --noY



####################################################################################################################################################################################################
####################################################################################################################################################################################################
####################################################################################################################################################################################################
## OLD COMMANDS FOR OLD VERSION OF THE MERGER

# python3 batchMerger.py --indir 2022_05_16_NtuplesVtest1 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU
# python3 batchMerger.py --indir 2022_05_16_NtuplesVtest2 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU
# python3 batchMerger.py --indir 2022_05_16_NtuplesVtest3 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU

# python3 batchMerger.py --indir 2022_05_16_NtuplesVtest1 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU
# python3 batchMerger.py --indir 2022_05_16_NtuplesVtest2 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU
# python3 batchMerger.py --indir 2022_05_16_NtuplesVtest3 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU

# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _30_150_flat_noNoisyTTcut
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _30_150_flat_noNoisyTTcut

# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _30_300_forceEtaZero
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _30_300_forceEtaZero



# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --applyOnTheFly True --doQCDnoPU --odir _30_300_flooringTrainingSFapplied
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --applyOnTheFly True --doQCDnoPU --odir _30_300_newTrainingSFapplied
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --applyOnTheFly True --doQCDnoPU --odir _30_300_noSFapplied

# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --applyOnTheFly True --doQCDnoPU --odir _30_300_flooringTrainingSFapplied
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --applyOnTheFly True --doQCDnoPU --odir _30_300_newTrainingSFapplied
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --applyOnTheFly True --doQCDnoPU --odir _30_300_noSFapplied


# python3 batchMerger.py --indir 2022_05_20_NtuplesV17 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _30_300_newCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_20_NtuplesV17 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _30_300_oldCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_20_NtuplesV17 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _30_300_noCalibration --applyOnTheFly True

# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _300_600_newCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _300_600_oldCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doQCDnoPU --odir _300_600_noCalibration --applyOnTheFly True

# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _0_100_newCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _0_100_oldCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _0_100_noCalibration --applyOnTheFly True

# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _100_300_newCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _100_300_oldCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _100_300_noCalibration --applyOnTheFly True

# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _200_500_newCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _200_500_oldCalibrationOnTheFly --applyOnTheFly True
# python3 batchMerger.py --indir 2022_05_18_NtuplesV16 --sample test --v Apply --applyHCALpfa1p --applyNoCalib --doEG --odir _200_500_noCalibration --applyOnTheFly True


# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample train --v ECAL --applyHCALpfa1p --applyNoCalib --doEG0_200   --filesLim 1000 --odir _0pt200
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample train --v ECAL --applyHCALpfa1p --applyNoCalib --doEG        --filesLim 1000 --odir _0pt500
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD       --filesLim 1000 --odir _30pt1000
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD       --filesLim 1000 --odir _30pt500
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD       --filesLim 1000 --odir _20pt1000
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample test --v ECAL --applyHCALpfa1p --applyNoCalib --doEG0_200    --filesLim 1000 --odir _0pt200
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample test --v ECAL --applyHCALpfa1p --applyNoCalib --doEG         --filesLim 1000 --odir _0pt500
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD        --filesLim 1000 --odir _30pt1000
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD        --filesLim 1000 --odir _30pt500
# sleep 5
# python3 batchMerger.py --indir 2022_07_20_NtuplesV23 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD        --filesLim 1000 --odir _20pt1000
# sleep 5

# python3 batchMerger.py --indir 2022_07_12_NtupleV22 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD       --filesLim 1 --odir _30pt1000_eta41_nTT
# sleep 5
# python3 batchMerger.py --indir 2022_07_12_NtupleV22 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD        --filesLim 1 --odir _30pt1000_eta41_nTT



# python3 batchMerger.py --indir 2023_01_16_NtuplesV27 --sample test --v ECAL --applyHCALpfa1p --applyOldCalib --doEG  --filesLim 1000 --odir _0pt500_oldCalib
# python3 batchMerger.py --indir 2023_01_16_NtuplesV27 --sample test --v HCAL --applyHCALpfa1p --applyOldCalib --doQCD  --filesLim 1000 --odir _30pt1000_oldCalib


# python3 batchMerger.py --indir 2023_01_16_NtuplesV27 --sample train --v ECAL --applyHCALpfa1p --applyNoCalib --doEG  --filesLim 1000 --odir _0pt500
# sleep 5
# python3 batchMerger.py --indir 2023_01_16_NtuplesV27 --sample train --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD --filesLim 1000 --odir _30pt1000
# sleep 5
# python3 batchMerger.py --indir 2023_01_16_NtuplesV27 --sample train --v NU --applyHCALpfa1p --applyNoCalib --doNuGun --filesLim 1000 --odir _rateProxy
# sleep 5
# python3 batchMerger.py --indir 2023_01_16_NtuplesV27 --sample train --v NU --applyHCALpfa1p --applyNoCalib --doNuGun --filesLim 1000 --odir _rateProxy_oldCalib
# sleep 5
# python3 batchMerger.py --indir 2023_01_16_NtuplesV27 --sample test --v ECAL --applyHCALpfa1p --applyNoCalib --doEG   --filesLim 1000 --odir _0pt500
# sleep 5
# python3 batchMerger.py --indir 2023_01_16_NtuplesV27 --sample test --v HCAL --applyHCALpfa1p --applyNoCalib --doQCD  --filesLim 1000 --odir _30pt1000
# sleep 5