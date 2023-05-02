# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --outdir 0000_00_00_NtuplesVunc --label EGamma_data_reco --reco --nEvts -1 --target ele
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 0000_00_00_NtuplesVold --label EGamma_data_reco --reco --nEvts -1 --target ele --unpacked
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 2023_02_28_NtuplesV31  --label EGamma_data_reco --reco --nEvts -1 --target ele


# # python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --outdir 0000_00_00_NtuplesVunc --label Muon_data_reco   --reco --nEvts -1 --target jet
# # python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 0000_00_00_NtuplesVold --label Muon_data_reco   --reco --nEvts -1 --target jet --unpacked
# # python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 2023_02_28_NtuplesV31  --label Muon_data_reco   --reco --nEvts -1 --target jet


# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --outdir 0000_00_00_NtuplesVunc --label EGamma_data_reco --reco --nEvts -1 --target ele
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 0000_00_00_NtuplesVold --label EGamma_data_reco --reco --nEvts -1 --target ele --unpacked
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 2023_02_28_NtuplesV31  --label EGamma_data_reco --reco --nEvts -1 --target ele


# # python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json     --outdir 0000_00_00_NtuplesVunc --label Muon_data_reco   --reco --nEvts -1 --target jet
# # python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 0000_00_00_NtuplesVold --label Muon_data_reco   --reco --nEvts -1 --target jet --unpacked
# # python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json       --outdir 2023_02_28_NtuplesV31  --label Muon_data_reco   --reco --nEvts -1 --target jet


# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data     --outdir 0000_00_00_NtuplesVunc --label EGamma_data_reco --nEvts -1 --target ele
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data       --outdir 0000_00_00_NtuplesVold --label EGamma_data_reco --nEvts -1 --target ele --unpacked
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data       --outdir 2023_02_28_NtuplesV31  --label EGamma_data_reco --nEvts -1 --target ele


# # python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data     --outdir 0000_00_00_NtuplesVunc --label Muon_data_reco   --nEvts -1 --target jet
# # python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data       --outdir 0000_00_00_NtuplesVold --label Muon_data_reco   --nEvts -1 --target jet --unpacked
# # python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data       --outdir 2023_02_28_NtuplesV31  --label Muon_data_reco   --nEvts -1 --target jet


# python3 comparisonPlots.py --indir 2023_02_28_NtuplesV31 --label EGamma_data_reco --target ele --reco --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40

# # python3 comparisonPlots.py --indir 2023_02_28_NtuplesV31 --label Muon_data_reco   --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100

# currCalib  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EGAMMA
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json  --outdir 0000_00_00_NtuplesVcur --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcur  --label EGamma_data_reco --reco --nEvts 500000 --target ele

# currCalib  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MUON
# find good ntuples first
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcur  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcur --label Muon_data_reco --reco --nEvts 500000 --target jet

# RATE  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_data  --outdir 0000_00_00_NtuplesVcur --label EGamma_data_reco --nEvts -1 --target ele
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_data  --outdir 0000_00_00_NtuplesVcur --label Muon_data_reco --nEvts -1 --target jet
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data  --outdir 0000_00_00_NtuplesVunc --label Muon_data_reco --nEvts -1 --target jet
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data  --outdir 0000_00_00_NtuplesVold --label Muon_data_reco --nEvts -1 --target jet

# noCalib  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MUON (419M)
# find good ntuples first
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVunc  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVunc --label Muon_data_reco --reco --nEvts 500000 --target jet

# oldCalib  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MUON
# find good ntuples first
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVold  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVold --label Muon_data_reco --reco --nEvts 500000 --target jet

# v35 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EGAMMA
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data  --outdir 2023_03_22_NtuplesV35 --label EGamma_data_reco --nEvts -1 --target ele
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data_reco_json --outdir 2023_03_22_NtuplesV35  --label EGamma_data_reco --reco --nEvts -1 --target ele
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data_reco_json --outdir 2023_03_22_NtuplesV35  --label EGamma_data_reco --reco --nEvts -1 --target ele
# python3 comparisonPlots.py --indir 2023_03_22_NtuplesV35 --label EGamma_data_reco --target ele --reco --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40
# python3 comparisonPlots.py --indir 2023_03_22_NtuplesV35 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib

# MUON
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data  --outdir 2023_03_22_NtuplesV35  --label Muon_data_reco   --nEvts -1 --target jet
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data_reco_json/GoodNtuples --outdir 2023_03_22_NtuplesV35  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v35newCalib_data_reco_json/GoodNtuples --outdir 2023_03_22_NtuplesV35 --label Muon_data_reco --reco --nEvts 500000 --target jet
# (TO DO YET) cause we are missing the noCalib and currCalib
# python3 comparisonPlots.py --indir 2023_03_22_NtuplesV35 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100
# python3 comparisonPlots.py --indir 2023_03_22_NtuplesV35 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib

# v33 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EGAMMA
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data  --outdir 2023_03_06_NtuplesV33 --label EGamma_data_reco --nEvts -1 --target ele --tag _normalOrder
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts -1 --target ele --tag _normalOrder
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts -1 --target ele --tag _normalOrder
# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco --target ele --reco --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 --tag _normalOrder
# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib --tag _normalOrder

# MUON
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data  --outdir 2023_03_06_NtuplesV33  --label Muon_data_reco   --nEvts -1 --target jet --tag _normalOrder
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v3newCalib_data_reco_json/GoodNtuples --outdir 2023_03_06_NtuplesV33  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _normalOrder
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json/GoodNtuples --outdir 2023_03_06_NtuplesV33 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _normalOrder
# (TO DO YET) cause we are missing the noCalib and currCalib
# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 --tag _normalOrder
# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib --tag _normalOrder

# v37 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data_reco_json
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data_reco_json

# EGAMMA
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data/GoodNtuples  --outdir 2023_03_25_NtuplesV37 --label EGamma_data_reco --nEvts 500000 --target ele
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data_reco_json/GoodNtuples --outdir 2023_03_25_NtuplesV37  --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data_reco_json/GoodNtuples --outdir 2023_03_25_NtuplesV37  --label EGamma_data_reco --reco --nEvts 500000 --target ele
# # python3 comparisonPlots.py --indir 2023_03_25_NtuplesV37 --label EGamma_data_reco --target ele --reco --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40r
# python3 comparisonPlots.py --indir 2023_03_25_NtuplesV37 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib

# # MUON
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data/GoodNtuples  --outdir 2023_03_25_NtuplesV37  --label Muon_data_reco   --nEvts 500000 --target jet
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data_reco_json/GoodNtuples --outdir 2023_03_25_NtuplesV37  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v37newCalib_data_reco_json/GoodNtuples --outdir 2023_03_25_NtuplesV37 --label Muon_data_reco --reco --nEvts 500000 --target jet
# # python3 comparisonPlots.py --indir 2023_03_25_NtuplesV37 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100
# python3 comparisonPlots.py --indir 2023_03_25_NtuplesV37 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib

# # v38 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data
# # python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data_reco_json
# # python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data_reco_json

# # EGAMMA
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data/GoodNtuples  --outdir 2023_03_25_NtuplesV38 --label EGamma_data_reco --nEvts 500000 --target ele
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data_reco_json/GoodNtuples --outdir 2023_03_25_NtuplesV38  --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data_reco_json/GoodNtuples --outdir 2023_03_25_NtuplesV38  --label EGamma_data_reco --reco --nEvts 500000 --target ele
# # python3 comparisonPlots.py --indir 2023_03_25_NtuplesV38 --label EGamma_data_reco --target ele --reco --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40r
# python3 comparisonPlots.py --indir 2023_03_25_NtuplesV38 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib

# # MUON
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data/GoodNtuples  --outdir 2023_03_25_NtuplesV38  --label Muon_data_reco   --nEvts 500000 --target jet
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data_reco_json/GoodNtuples --outdir 2023_03_25_NtuplesV38  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v38newCalib_data_reco_json/GoodNtuples --outdir 2023_03_25_NtuplesV38 --label Muon_data_reco --reco --nEvts 500000 --target jet
# # python3 comparisonPlots.py --indir 2023_03_25_NtuplesV38 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100
# python3 comparisonPlots.py --indir 2023_03_25_NtuplesV38 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib

# # v33 0p8 rate -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # EGAMMA
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v33Rate0p8newCalib_data  --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco   --nEvts 500000 --target ele --tag _Rate0p8
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33Rate0p8newCalib_data_reco_json
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33Rate0p8newCalib_data_reco_json/GoodNtuples --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _Rate0p8
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33Rate0p8newCalib_data_reco_json/GoodNtuples --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _Rate0p8
# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib --tag _Rate0p8

# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v33Rate1p2newCalib_data  --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco   --nEvts 500000 --target ele --tag _Rate1p2
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33Rate1p2newCalib_data_reco_json
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33Rate0p8newCalib_data_reco_json/GoodNtuples --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _Rate1p2
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33Rate0p8newCalib_data_reco_json/GoodNtuples --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _Rate1p2
# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --ref _currCalib --tag _Rate1p2

# # v39 
# mv /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v39_data /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v39newCalib_data
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v39newCalib_data  --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco   --nEvts 500000 --target ele --tag _NewRateProxy

# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39newCalib_data_reco_json
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39newCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _NewRateProxy
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39newCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _NewRateProxy
# python3 comparisonPlots.py --indir 2023_04_06_NtuplesV39 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --tag _NewRateProxy

# # v39 C
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v39CnewCalib_data  --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --nEvts 500000 --target ele --tag C
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39CnewCalib_data_reco_json
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39CnewCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag C
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39CnewCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag C
# python3 comparisonPlots.py --indir 2023_04_06_NtuplesV39 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --tag C

# v39 D
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v39DnewCalib_data  --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --nEvts 500000 --target ele --tag D
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39DnewCalib_data_reco_json
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39DnewCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag D
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39DnewCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag D
# python3 comparisonPlots.py --indir 2023_04_06_NtuplesV39 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --tag D

# find rate target HCAL
# python3 rate.py --indir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data  --outdir 0000_00_00_NtuplesVcurGT  --label EGamma_data_reco --nEvts 500000 --target ele --er 2.5
# python3 rate.py --indir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data  --outdir 0000_00_00_NtuplesVcurGT  --label Muon_data_reco --nEvts 500000 --target jet --er 2.5
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurGT  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurGT  --label Muon_data_reco --reco --nEvts 500000 --target jet

# v40 C3
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v40C3DnewCalib_data  --outdir 2023_04_13_NtuplesV40  --label Muon_data_reco --nEvts 500000 --target jet --tag C3
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v40C3newCalib_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v40C3newCalib_data_reco_json/GoodNtuples --outdir 2023_04_13_NtuplesV40  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag C3
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v40C3newCalib_data_reco_json/GoodNtuples --outdir 2023_04_13_NtuplesV40  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag C3
# python3 comparisonPlots.py --indir 2023_04_13_NtuplesV40 --label Muon_data_reco --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurGT --unc 0000_00_00_NtuplesVunc --tag C3

# v40 C6
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v40C6DnewCalib_data  --outdir 2023_04_13_NtuplesV40  --label Muon_data_reco --nEvts 500000 --target jet --tag C6
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v40C6newCalib_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v40C6newCalib_data_reco_json/GoodNtuples --outdir 2023_04_13_NtuplesV40  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag C6
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v40C6newCalib_data_reco_json/GoodNtuples --outdir 2023_04_13_NtuplesV40  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag C6
# python3 comparisonPlots.py --indir 2023_04_13_NtuplesV40 --label Muon_data_reco --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurGT --unc 0000_00_00_NtuplesVunc --tag C6

# v39 H1
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v39H1newCalib_data  --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --nEvts 500000 --target ele --tag H1
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39H1newCalib_data_reco_json
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39H1newCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag H1
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39H1newCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag H1
# python3 comparisonPlots.py --indir 2023_04_06_NtuplesV39 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --tag H1

# v39 H2
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v39H2newCalib_data  --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --nEvts 500000 --target ele --tag H2
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39H2newCalib_data_reco_json
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39H1newCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag H1
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39H2newCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag H2
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json       --outdir 0000_00_00_NtuplesVunc --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json   --outdir 0000_00_00_NtuplesVcur --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3v11_CaloParams2022v39H2newCalib_data_reco_json/GoodNtuples --outdir 2023_04_06_NtuplesV39  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag H2
# python3 comparisonPlots.py --indir 2023_04_06_NtuplesV39 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --tag H1
# python3 comparisonPlots.py --indir 2023_04_06_NtuplesV39 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcur --unc 0000_00_00_NtuplesVunc --tag H2

# v41 C
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v41CnewCalib_data  --outdir 2023_04_18_NtuplesV41  --label Muon_data_reco --nEvts 500000 --target jet --tag C --raw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v41CnewCalib_data_reco_json
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v41CnewCalib_data_reco_json/GoodNtuples --outdir 2023_04_18_NtuplesV41  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag C --raw
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v41CnewCalib_data_reco_json/GoodNtuples --outdir 2023_04_18_NtuplesV41 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag C --raw

# python3 rate.py --indir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data  --outdir 0000_00_00_NtuplesVcurRaw  --label Muon_data_reco --nEvts 500000 --target jet --raw
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurRaw  --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurRaw --label Muon_data_reco --reco --nEvts 500000 --target jet --raw

# python3 rate.py --indir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data --outdir 0000_00_00_NtuplesVuncRaw  --label Muon_data_reco --nEvts 500000 --target jet --raw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncRaw  --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncRaw --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 comparisonPlots.py --indir 2023_04_18_NtuplesV41 --label Muon_data_reco --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurRaw --unc 0000_00_00_NtuplesVuncRaw --tag C

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # v41 C correct
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v41CZSnewCalib_data  --outdir 2023_04_18_NtuplesV41  --label Muon_data_reco --nEvts 500000 --target jet --tag C_cor_v10 --raw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v41CZSnewCalib_data_reco_json
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v41CZSnewCalib_data_reco_json/GoodNtuples --outdir 2023_04_18_NtuplesV41  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag C_cor_v10 --raw
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v41CZSnewCalib_data_reco_json/GoodNtuples --outdir 2023_04_18_NtuplesV41 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag C_cor_v10 --raw
# # old calib with ZS
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06modZS0p5_data  --outdir 0000_00_00_NtuplesVcurRawZS  --label Muon_data_reco --nEvts 500000 --target jet --raw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06modZS0p5_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06modZS0p5_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurRawZS  --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3v11_CaloParams2022v06modZS0p5_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurRawZS --label Muon_data_reco --reco --nEvts 500000 --target jet --raw

# python3 comparisonPlots.py --indir 2023_04_18_NtuplesV41 --label Muon_data_reco --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurRawZS --unc 0000_00_00_NtuplesVuncRaw_v10 --tag C_cor_v10

# v33 raw -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EGAMMA
# python3 rate.py --indir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data  --outdir 0000_00_00_NtuplesVcurRaw  --label EGamma_data_reco --nEvts 500000 --target ele --raw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurRaw  --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurRaw --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw

# python3 rate.py --indir EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_noL1Calib_data  --outdir 0000_00_00_NtuplesVuncRaw  --label EGamma_data_reco --nEvts 500000 --target ele --raw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncRaw  --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncRaw --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw

# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data  --outdir 2023_03_06_NtuplesV33 --label EGamma_data_reco --nEvts 500000 --target ele --tag _normalOrder_raw --raw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_raw --raw 
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_raw --raw
# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcurRaw --unc 0000_00_00_NtuplesVuncRaw --ref _currCalibRaw --tag _normalOrder_raw

# MUON
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data  --outdir 2023_03_06_NtuplesV33  --label Muon_data_reco   --nEvts 500000 --target jet --tag _normalOrder_raw --raw
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json/GoodNtuples --outdir 2023_03_06_NtuplesV33  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _normalOrder_raw --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json/GoodNtuples --outdir 2023_03_06_NtuplesV33 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _normalOrder_raw --raw

# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVunc_v10  --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVunc_v10 --label Muon_data_reco --reco --nEvts 500000 --target jet --raw

# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncRaw_v10  --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncRaw_v10 --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurRaw --unc 0000_00_00_NtuplesVuncRaw_v10 --ref _currCalibRaw --tag _normalOrder_raw \
#         --doTurnOn False --doRate False

# 1)
# # No Calibration muons Et
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncNew  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncNew --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --outdir 0000_00_00_NtuplesVuncNew --label Muon_data_reco --nEvts 500000 --target jet
# # No Calibration muons EtRaw
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncNewRaw  --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncNewRaw --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --outdir 0000_00_00_NtuplesVuncNewRaw --label Muon_data_reco --nEvts 500000 --target jet --raw
# # No Calibration egamma Et
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNew  --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNew --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --outdir 0000_00_00_NtuplesVuncNew --label EGamma_data_reco --nEvts 500000 --target ele
# # No Calibration egamma EtRaw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNewRaw  --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNewRaw --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --outdir 0000_00_00_NtuplesVuncNewRaw --label EGamma_data_reco --nEvts 500000 --target ele --raw

# # 2)
# # Current Calibration (w/ ZS) muons Et
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurNew  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurNew --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_data --outdir 0000_00_00_NtuplesVcurNew --label Muon_data_reco --nEvts 500000 --target jet
# # Current Calibration (w/ ZS) muons EtRaw
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurNewRaw  --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurNewRaw --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_data --outdir 0000_00_00_NtuplesVcurNewRaw --label Muon_data_reco --nEvts 500000 --target jet --raw
# # Current Calibration (w/ ZS) egamma Et
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurNew  --label Muon_data_reco --reco --nEvts 500000 --target jet
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurNew --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_data--outdir 0000_00_00_NtuplesVcurNew --label EGamma_data_reco --nEvts 500000 --target ele
# # Current Calibration (w/ ZS) egamma EtRaw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurNewRaw  --label Muon_data_reco --reco --nEvts 500000 --target jet --raw
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurNewRaw --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_data --outdir 0000_00_00_NtuplesVcurNewRaw --label EGamma_data_reco --nEvts 500000 --target ele --raw

# v42 EtRaw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data  --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco  --nEvts 500000 --target jet --tag _A_raw --raw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1
python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1/GoodNtuples --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A_raw --raw
python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1/GoodNtuples --outdir 2023_04_29_NtuplesV42 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A_raw --raw
python3 comparisonPlots.py --indir 2023_04_29_NtuplesV42 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
        --old 0000_00_00_NtuplesVcurNewRaw --unc 0000_00_00_NtuplesVuncNewRaw --tag _A_raw
# v42 Et
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data  --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco  --nEvts 500000 --target jet --tag _A
python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1/GoodNtuples --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A
python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1/GoodNtuples --outdir 2023_04_29_NtuplesV42 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A
python3 comparisonPlots.py --indir 2023_04_29_NtuplesV42 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
        --old 0000_00_00_NtuplesVcurNew --unc 0000_00_00_NtuplesVuncNew --tag _A

# v43 EtRaw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data  --outdir 2023_04_29_NtuplesV43  --label Muon_data_reco  --nEvts 500000 --target jet --tag _A_raw --raw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data_reco_json/GoodNtuples --outdir 2023_04_29_NtuplesV43  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A_raw --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data_reco_json/GoodNtuples --outdir 2023_04_29_NtuplesV43 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A_raw --raw
# python3 comparisonPlots.py --indir 2023_04_29_NtuplesV43 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurNewRaw --unc 0000_00_00_NtuplesVuncNewRaw --tag _A_raw
# v43 Et
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data  --outdir 2023_04_29_NtuplesV43  --label Muon_data_reco  --nEvts 500000 --target jet --tag _A
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data_reco_json/GoodNtuples --outdir 2023_04_29_NtuplesV43  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v43newCalib_data_reco_json/GoodNtuples --outdir 2023_04_29_NtuplesV43 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A
# python3 comparisonPlots.py --indir 2023_04_29_NtuplesV43 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurNew --unc 0000_00_00_NtuplesVuncNew --tag _A



###############################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################
## OLD COMMANDS FOR OLD SCRIPTS



###############################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################
## MONTE CARLO

# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v01noL1calib_reco/ -1 HCAL_MC_noCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v01oldHCALsf_reco/ -1 HCAL_MC_oldCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v27newCalib_reco/ -1 HCAL_MC_v27newCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v28newCalib_reco/ -1 HCAL_MC_v28newCalibReco ./

# python3 turnOn.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p/ 100000 ECAL_uncalib
# python3 turnOn.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_oldCalib_applyHCALpfa1p/ 100000 ECAL_oldCalib
# python3 turnOn.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_newCalib_applyHCALpfa1p/ 100000 ECAL_newCalib


# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v01noL1calib_reco/ -1 HCAL_MC_noCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v01oldHCALsf_reco/ -1 HCAL_MC_oldCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v27newCalib_reco/ -1 HCAL_MC_v27newCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v3__AODSIM__GT130XmcRun32022realisticv2_CaloParams2022v28newCalib_reco/ -1 HCAL_MC_v28newCalibReco ./

# python3 resolutions.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p/ 100000 ECAL_uncalib
# python3 resolutions.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_oldCalib_applyHCALpfa1p/ 100000 ECAL_oldCalib
# python3 resolutions.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_newCalib_applyHCALpfa1p/ 100000 ECAL_newCalib

# python3 rate_HCAL_TandP.py /data_CMS/cms/davignon/Layer1SFsNtuples/Rate/Run362616_noCalib/Tot_Ntuple_Rate_Run362616_noCalib.root -1 HCAL_MC_noCalibReco 1 pt95eff
# python3 rate_HCAL_TandP.py /data_CMS/cms/davignon/Layer1SFsNtuples/Rate/Run362616_noCalib/Tot_Ntuple_Rate_Run362616_noCalib.root -1 HCAL_MC_oldCalibReco 0 pt95eff
# python3 rate_HCAL_TandP.py /data_CMS/cms/davignon/Layer1SFsNtuples/Rate/Run362616_newLayer1SFs/Tot_Ntuple_Rate_Run362616_newL1SFs.root -1 HCAL_MC_v27newCalibReco 1 pt95eff
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT130XdataRun3Promptv10_CaloParams2022v28newCalib_data -1 HCAL_MC_v28newCalibReco pt95eff

# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_uncalib_applyHCALpfa1p/ 500000 ECAL_uncalib
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_oldCalib_applyHCALpfa1p/ 500000 ECAL_oldCalib
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW_newCalib_applyHCALpfa1p/ 500000 ECAL_newCalib

# python3 comparisonPlots.py HCAL_MC_v27newCalibReco ./ pt95eff
# python3 comparisonPlots.py HCAL_MC_v28newCalibReco ./ Reco pt95eff

# python3 comparisonPlots.py ECAL_newCalib

###############################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################
## DATA

# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ 50000 HCAL_Data_noCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ 50000 HCAL_Data_oldCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ 50000 HCAL_Data_currCalibReco ./ unpacked
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ 50000 HCAL_Data_v31newCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ 50000 HCAL_Data_v27newCalibReco ./

# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ -1 ECAL_Data_noCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ -1 ECAL_Data_oldCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ -1 ECAL_Data_currCalibReco ./ unpacked
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ -1 ECAL_Data_v31newCalibReco ./
# python3 turnOn_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ -1 ECAL_Data_v27newCalibReco ./

# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ 50000 HCAL_Data_noCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ 50000 HCAL_Data_oldCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ 50000 HCAL_Data_currCalibReco ./ unpacked
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ 50000 HCAL_Data_v31newCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ 50000 HCAL_Data_v27newCalibReco ./

# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ -1 ECAL_Data_noCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ -1 ECAL_Data_oldCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ -1 ECAL_Data_currCalibReco ./ unpacked
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ -1 ECAL_Data_v31newCalibReco ./
# python3 resolutions_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ -1 ECAL_Data_v27newCalibReco ./

# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ 500000 HCAL_Data_noCalibReco
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ 500000 HCAL_Data_oldCalibReco
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ 500000 HCAL_Data_currCalibReco unpacked
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data/ 500000 HCAL_Data_v31newCalibReco
# python3 rate_HCAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data/ 500000 HCAL_Data_v27newCalibReco

# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ -1 ECAL_Data_noCalibReco
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ -1 ECAL_Data_oldCalibReco
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ -1 ECAL_Data_currCalibReco unpacked
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data/ -1 ECAL_Data_v31newCalibReco
# python3 rate_ECAL.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data/ -1 ECAL_Data_v27newCalibReco

# python3 comparisonPlots.py HCAL_Data_v27newCalib currCalib ./ Reco
# python3 comparisonPlots.py ECAL_Data_v27newCalib currCalib ./ Reco
# python3 comparisonPlots.py HCAL_Data_v29newCalib currCalib ./ Reco
# python3 comparisonPlots.py ECAL_Data_v29newCalib currCalib ./ Reco
# python3 comparisonPlots.py HCAL_Data_v31newCalib currCalib ./ Reco
# python3 comparisonPlots.py ECAL_Data_v31newCalib currCalib ./ Reco



# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ 50000 HCAL_Data_noCalibReco ./
# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ 50000 HCAL_Data_oldCalibReco ./
# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ 50000 HCAL_Data_currCalibReco ./ unpacked
# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v31newCalib_data_reco_json/ 50000 HCAL_Data_v31newCalibReco ./
# python3 turnOn_MET_reco.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ 50000 HCAL_Data_v27newCalibReco ./



# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ HCAL_Data_noCalibReco_off 50000 -1
# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ HCAL_Data_oldCalibReco_off 50000 -1
# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ HCAL_Data_currCalibReco_off 50000 -1 unpacked
# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ HCAL_Data_v29newCalibReco_off 50000 -1
# python3 rate_HCAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data/ HCAL_Data_v27newCalibReco_off 50000 -1

# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json/ ECAL_Data_noCalibReco_off -1 -1
# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json/ ECAL_Data_oldCalibReco_off -1 -1
# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ ECAL_Data_currCalibReco_off -1 -1 unpacked
# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v29newCalib_data/ ECAL_Data_v29newCalibReco_off -1 -1
# python3 rate_ECAL_JB.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data_reco_json/ /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v27newCalib_data/ ECAL_Data_v27newCalibReco_off -1 -1

# python3 comparisonPlots_JB.py HCAL_Data_noCalibReco_currCalibReco_v29newCalibReco_off HCAL_Data_noCalibReco_off HCAL_Data_currCalibReco_off HCAL_Data_v29newCalibReco_off
# python3 comparisonPlots_JB.py ECAL_Data_noCalibReco_currCalibReco_v29newCalibReco_off ECAL_Data_noCalibReco_off ECAL_Data_currCalibReco_off ECAL_Data_v29newCalibReco_off
# python3 comparisonPlots_JB.py HCAL_Data_noCalibReco_currCalibReco_v27newCalibReco_off HCAL_Data_noCalibReco_off HCAL_Data_currCalibReco_off HCAL_Data_v27newCalibReco_off
# python3 comparisonPlots_JB.py ECAL_Data_noCalibReco_currCalibReco_v27newCalibReco_off ECAL_Data_noCalibReco_off ECAL_Data_currCalibReco_off ECAL_Data_v27newCalibReco_off

