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
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1/GoodNtuples --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A_raw --raw
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1/GoodNtuples --outdir 2023_04_29_NtuplesV42 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A_raw --raw
# python3 comparisonPlots.py --indir 2023_04_29_NtuplesV42 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurNewRaw --unc 0000_00_00_NtuplesVuncNewRaw --tag _A_raw
# v42 Et
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data  --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco  --nEvts 500000 --target jet --tag _A
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1/GoodNtuples --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v42newCalib_data_reco_json_1/GoodNtuples --outdir 2023_04_29_NtuplesV42 --label Muon_data_reco --reco --nEvts 500000 --target jet --tag _A
# python3 comparisonPlots.py --indir 2023_04_29_NtuplesV42 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurNew --unc 0000_00_00_NtuplesVuncNew --tag _A

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

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################

# GT130X

# No Calibration muons EtRaw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncNewRaw_130  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --jetPtcut 30 --etacut 1.305
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncNewRaw_130 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data --outdir 0000_00_00_NtuplesVuncNewRaw_130 --label Muon_data_reco --nEvts 100000 --target jet --raw

# Current Calibration (w/ ZS) muons EtRaw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurNewRaw_130  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --jetPtcut 30 --etacut 1.305
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurNewRaw_130 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT130XdataRun3Promptv2_CaloParams2022v06_data --outdir 0000_00_00_NtuplesVcurNewRaw_130 --label Muon_data_reco --nEvts 100000 --target jet --raw

# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data  --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco  --nEvts 100000 --target jet --tag _A_raw_130 --raw
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json/GoodNtuples --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco --reco --nEvts 100000 --target jet --tag _A_raw_130 --raw --jetPtcut 30 --etacut 1.305
# python3 turnOn.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json/GoodNtuples --outdir 2023_04_29_NtuplesV42 --label Muon_data_reco --reco --nEvts 100000 --target jet --tag _A_raw_130 --raw
# python3 comparisonPlots.py --indir 2023_04_29_NtuplesV42 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurNewRaw_130 --unc 0000_00_00_NtuplesVuncNewRaw_130 --tag _A_raw_130

# re-emulation on jets
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncNewRaw_130_JetMET  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --jetPtcut 30 --etacut 1.305
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v06_noL1Calib_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVuncNewRaw_130_JetMET --label Muon_data_reco --reco --nEvts 100000 --target jet --raw

# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurNewRaw_130_JetMET  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --jetPtcut 30 --etacut 1.305
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v06_data_reco_json/GoodNtuples --outdir 0000_00_00_NtuplesVcurNewRaw_130_JetMET --label Muon_data_reco --reco --nEvts 100000 --target jet --raw

# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json/GoodNtuples --outdir 2023_04_29_NtuplesV42  --label Muon_data_reco --reco --nEvts 100000 --target jet --tag _A_raw_130_JetMET --raw --jetPtcut 30 --etacut 1.305
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__AOD__Olivier__GT130XdataRun3Promptv2_CaloParams2022v42newCalib_data_reco_json/GoodNtuples --outdir 2023_04_29_NtuplesV42 --label Muon_data_reco --reco --nEvts 100000 --target jet --tag _A_raw_130_JetMET --raw
# python3 comparisonPlots.py --indir 2023_04_29_NtuplesV42 --label Muon_data_reco  --target jet --reco --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#         --old 0000_00_00_NtuplesVcurNewRaw_130_JetMET --unc 0000_00_00_NtuplesVuncNewRaw_130_JetMET --tag _A_raw_130_JetMET


# ###########################################################################################################################################
# ###########################################################################################################################################
# ###########################################################################################################################################

# # LooseElectron
# # No Calibration egamma Et
# # python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNew/LooseElectron  --label EGamma_data_reco --reco --nEvts 500000 --target ele --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNew/LooseElectron --label EGamma_data_reco --reco --nEvts 500000 --target ele --LooseEle
# # No Calibration egamma EtRaw
# # python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNewRaw/LooseElectron  --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNewRaw/LooseElectron --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw --LooseEle

# # Current Calibration (w/ ZS) egamma Et
# # python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurNew/LooseElectron  --label EGamma_data_reco --reco --nEvts 500000 --target ele --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurNew/LooseElectron --label EGamma_data_reco --reco --nEvts 500000 --target ele --LooseEle
# # Current Calibration (w/ ZS) egamma EtRaw
# # python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurNewRaw/LooseElectron  --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json --outdir 0000_00_00_NtuplesVcurNewRaw/LooseElectron --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw --LooseEle

# # New Calibration (w/ ZS) egamma Et
# # python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_LooseElectron --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_LooseElectron --LooseEle
# # New Calibration (w/ ZS) egamma EtRaw
# # python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_LooseElectron_raw --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalib_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_LooseElectron_raw --raw --LooseEle

# # do the rate somehow

# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco  --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcurNew/LooseElectron --unc 0000_00_00_NtuplesVuncNew/LooseElectron --tag _normalOrder_LooseElectron

# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco  --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcurNewRaw/LooseElectron --unc 0000_00_00_NtuplesVuncNewRaw/LooseElectron --tag _normalOrder_LooseElectron_raw

# # NEW SFs

# # New Calibration (w/ ZS) egamma Et
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalibNew_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_New_LooseElectron --LooseEle
# # python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalibNew_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_New_LooseElectron --LooseEle
# # New Calibration (w/ ZS) egamma EtRaw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalibNew_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_New_LooseElectron_raw --raw --LooseEle
# # python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v33newCalibNew_data_reco_json --outdir 2023_03_06_NtuplesV33  --label EGamma_data_reco --reco --nEvts 500000 --target ele --tag _normalOrder_New_LooseElectron_raw --raw --LooseEle

# # do the rate somehow

# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco  --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcurNew/LooseElectron --unc 0000_00_00_NtuplesVuncNew/LooseElectron --tag _normalOrder_New_LooseElectron

# python3 comparisonPlots.py --indir 2023_03_06_NtuplesV33 --label EGamma_data_reco  --target ele --reco --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#         --old 0000_00_00_NtuplesVcurNewRaw/LooseElectron --unc 0000_00_00_NtuplesVuncNewRaw/LooseElectron --tag _normalOrder_New_LooseElectron_raw

# ###############################################################################################################################################################################################################################################################################################

# # Check input samples resolution EGamma
# # Era E -> 4282499 events
# python3 resolutions.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_E_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --tag _100K --do_EoTot
# python3 resolutions.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_E_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --tag _Raw_100K --do_EoTot
# python3 resolutions.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_E_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --tag _Raw_LooseEle_100K --do_EoTot
# python3 resolutions_CD.py --indir EGamma__Run2022E-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_E_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --tag _CD_LooseEle_100K_EtaFromOffline --do_EoTot

# # Era F -> 12224809 events
# python3 resolutions.py --indir EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_F_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --tag _100K --do_EoTot
# python3 resolutions.py --indir EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_F_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --tag _Raw_100K --do_EoTot
# python3 resolutions.py --indir EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_F_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --tag _Raw_LooseEle_100K --do_EoTot
# python3 resolutions_CD.py --indir EGamma__Run2022F-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_F_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --tag _CD_LooseEle_100K_EtaFromOffline --do_EoTot

# # Era G -> 1653808 events
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_G_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --tag _100K --do_EoTot
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_G_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --tag _Raw_100K --do_EoTot
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_G_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --tag _Raw_LooseEle_100K --do_EoTot
# python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json --outdir 2023_05_19_NtuplesV46/TestInput_EGamma2022_G_MPUnits  --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle --tag _CD_LooseEle_100K_EtaFromOffline --do_EoTot

# ###############################################################################################################################################################################################################################################################################################

# # Check input samples resolution Jets
# # Era G Early (max) -> 4730257 events
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --tag _100K --do_HoTot
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _Raw_100K --do_HoTot
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _Raw_PuppiJet_100K --do_HoTot
# python3 resolutions_CD.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _CD_PuppiJet_100K_EtaFromOffline --do_HoTot
# python3 resolutions_CD.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _CD_100K_EtaFromOffline --do_HoTot

# # Check input samples resolution Muon
# # Era G (wait resubmission) -> 115158 events
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --tag _100K --do_HoTot
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _Raw_100K --do_HoTot
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _Raw_PuppiJet_100K --do_HoTot
# python3 resolutions_CD.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _CD_PuppiJet_100K_EtaFromOffline --do_HoTot
# python3 resolutions_CD.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _CD_100K_EtaFromOffline --do_HoTot

# # Everything the same but just in the barrel
# # Check input samples resolution Jets
# # Era G Early (max) -> 4730257 events
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --tag _100K --do_HoTot --etacut 1.305
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _Raw_100K --do_HoTot --etacut 1.305
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _Raw_PuppiJet_100K --do_HoTot --etacut 1.305
# python3 resolutions_CD.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _CD_PuppiJet_100K_EtaFromOffline --do_HoTot --etacut 1.305
# python3 resolutions_CD.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _CD_100K_EtaFromOffline --do_HoTot --etacut 1.305

# # Check input samples resolution Muon
# # Era G (wait resubmission) -> 115158 events
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --tag _100K --do_HoTot --etacut 1.305
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _Raw_100K --do_HoTot --etacut 1.305
# python3 resolutions.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _Raw_PuppiJet_100K --do_HoTot --etacut 1.305
# python3 resolutions_CD.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _CD_PuppiJet_100K_EtaFromOffline --do_HoTot --etacut 1.305
# python3 resolutions_CD.py --indir Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json_old --outdir 2023_05_20_NtuplesV47/TestInput_Muon2022_G_MPUnits_Barrel  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _CD_100K_EtaFromOffline --do_HoTot --etacut 1.305

# Check input samples resolution Jets
# Era G Early (max) -> 4730257 events (347 files) # ------------------> Redo for 100000 events 
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel_Pt30  --label Muon_data_reco --reco --nEvts 10000 --target jet --tag _100K --do_HoTot --etacut 1.305 --jetPtcut 30
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel_Pt30  --label Muon_data_reco --reco --nEvts 10000 --target jet --raw --tag _Raw_100K --do_HoTot --etacut 1.305 --jetPtcut 30
# python3 resolutions.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel_Pt30  --label Muon_data_reco --reco --nEvts 10000 --target jet --raw --PuppiJet --tag _Raw_PuppiJet_100K --do_HoTot --etacut 1.305 --jetPtcut 30
# python3 resolutions_CD.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel_Pt30  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _CD_PuppiJet_100K_EtaFromOffline --do_HoTot --etacut 1.305 --jetPtcut 30
# python3 resolutions_CD.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel_Pt30  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --tag _CD_PuppiJet_100K_EtaFromOffline_OnlyIhad --do_HoTot --etacut 1.305 --jetPtcut 30 --OnlyIhad
# python3 resolutions_CD.py --indir JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples --outdir 2023_05_20_NtuplesV47/TestInput_JetMET2022_G_MPUnits_Barrel_Pt30  --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --tag _CD_100K_EtaFromOffline --do_HoTot --etacut 1.305 --jetPtcut 30

###############################################################################################################################################################################################################################################################################################

# NoCalib Raw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --do_EoTot --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVunc_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
# NoCalib CD
# python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVunc_CD_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --do_EoTot --raw --LooseEle

# OldCalib Raw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --do_EoTot --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVcur_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
# # OldCalib CD
# # python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json \
# #  --outdir 2023_05_19_NtuplesV46/NtuplesVcur_CD_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --do_EoTot --raw --LooseEle

# # NewCalib Raw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v46newCalib_data_reco_json \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVnew_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --do_EoTot --raw --LooseEle
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v46newCalib_data_reco_json \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVnew_Raw_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --raw --LooseEle
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v46newCalib_data \
#  --outdir 2023_05_19_NtuplesV46/NtuplesVnew_Raw_LooseEle --label EGamma_data_reco --nEvts 100000 --target ele --raw
# # NewCalib CD
# # python3 resolutions_CD.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362617__RAW-RECO__GT130XdataRun3Promptv3_CaloParams2023v46newCalib_data_reco_json \
# #  --outdir 2023_05_19_NtuplesV46/NtuplesVnew_CD_LooseEle --label EGamma_data_reco --reco --nEvts 100000 --target ele --do_EoTot --raw --LooseEle

# python3 comparisonPlots.py --indir 2023_05_19_NtuplesV46/NtuplesVnew_Raw_LooseEle --label EGamma_data_reco  --target ele --reco \
#  --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#  --old 2023_05_19_NtuplesV46/NtuplesVcur_Raw_LooseEle --unc 2023_05_19_NtuplesV46/NtuplesVunc_Raw_LooseEle --do_EoTot

# python3 comparisonPlots.py --indir 2023_05_19_NtuplesV46/NtuplesVnew_CD_LooseEle --label EGamma_data_reco  --target ele --reco \
#  --thrsFixRate 10 --thrsFixRate 12 --thrsFixRate 15 --thrsFixRate 30 --thrsFixRate 36 --thrsFixRate 40 \
#  --old 2023_05_19_NtuplesV46/NtuplesVcur_CD_LooseEle --unc 2023_05_19_NtuplesV46/NtuplesVunc_CD_LooseEle --do_EoTot --doTurnOn False --doRate False

# # No Calibration egamma Et
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNew  --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNew --label EGamma_data_reco --reco --nEvts 500000 --target ele
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --outdir 0000_00_00_NtuplesVuncNew --label EGamma_data_reco --nEvts 500000 --target ele
# # No Calibration egamma EtRaw
# python3 resolutions.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNewRaw  --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw
# python3 turnOn.py --indir EGamma__Run2022G-ZElectron-PromptReco-v1__Run362616__RAW-RECO__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json --outdir 0000_00_00_NtuplesVuncNewRaw --label EGamma_data_reco --reco --nEvts 500000 --target ele --raw
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data --outdir 0000_00_00_NtuplesVuncNewRaw --label EGamma_data_reco --nEvts 500000 --target ele --raw

###############################################################################################################################################################################################################################################################################################
# UnCalib
# # python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
# #  --outdir 2023_05_20_NtuplesV47/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw
# # OldCalib
# # python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
# #  --outdir 2023_05_20_NtuplesV47/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw
# NewCalib A
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v47A_data_reco_json/GoodNtuples \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v47A_data_reco_json/GoodNtuples \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v47AnewCalib_data \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw
# python3 comparisonPlots.py --indir 2023_05_20_NtuplesV47/NtuplesVnew47A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
#  --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#  --old 2023_05_20_NtuplesV47/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_05_20_NtuplesV47/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot

# NewCalib B
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v47B_data_reco_json/GoodNtuples \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v47B_data_reco_json/GoodNtuples \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v47BnewCalib_data \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw
# python3 comparisonPlots.py --indir 2023_05_20_NtuplesV47/NtuplesVnew47B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
#  --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#  --old 2023_05_20_NtuplesV47/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_05_20_NtuplesV47/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot

# NewCalib C
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v47C_data_reco_json/GoodNtuples \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v47C_data_reco_json/GoodNtuples \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v47CnewCalib_data \
#  --outdir 2023_05_20_NtuplesV47/NtuplesVnew47C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw
# python3 comparisonPlots.py --indir 2023_05_20_NtuplesV47/NtuplesVnew47C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
#  --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#  --old 2023_05_20_NtuplesV47/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_05_20_NtuplesV47/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot

# # UnCalib
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
# # OldCalib
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v02_data \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305

# # NewCalib A
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48A_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v48AnewCalib_data \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
# python3 comparisonPlots.py --indir 2023_06_03_NtuplesV48/NtuplesVnew48A_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
#  --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#  --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305

# # NewCalib B
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48B_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v48BnewCalib_data \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
# python3 comparisonPlots.py --indir 2023_06_03_NtuplesV48/NtuplesVnew48B_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
#  --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#  --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305

# # NewCalib C
# python3 RemoveBadNtuples_Muon.py /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json
# python3 resolutions.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --etacut 1.305 --jetPtcut 30 --do_HoTot
# python3 turnOn.py --indir JetMET__Run2022G-PromptReco-v1__Run362617__AOD__GT130XdataRun3Promptv3_CaloParams2023v48C_data_reco_json/GoodNtuples \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --reco --nEvts 100000 --target jet --raw --PuppiJet --jetPtcut 15 --er 1.305
# python3 rate.py --indir EphemeralZeroBias0__Run2022G-v1__Run362617__RAW__GT130XdataRun3Promptv3_CaloParams2023v48CnewCalib_data \
#  --outdir 2023_06_03_NtuplesV48/NtuplesVnew48C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco --nEvts 100000 --target jet --raw --er 1.305
# python3 comparisonPlots.py --indir 2023_06_03_NtuplesV48/NtuplesVnew48C_Raw_Puppi_Barrel_Pt30 --label Muon_data_reco  --target jet --reco \
#  --thrsFixRate 60 --thrsFixRate 80 --thrsFixRate 100 \
#  --old 2023_06_03_NtuplesV48/NtuplesVcur_Raw_Puppi_Barrel_Pt30 --unc 2023_06_03_NtuplesV48/NtuplesVunc_Raw_Puppi_Barrel_Pt30 --do_HoTot --er 1.305


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

