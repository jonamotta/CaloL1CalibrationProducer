# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate.py --indir 2023_03_06_NtuplesV33 --tag DataReco_invertedOrder --v ECAL
# sleep 15

# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate.py --indir 2023_03_06_NtuplesV33 --tag DataReco_normalOrder --v HCAL
# sleep 15

# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate_C.py --indir 2023_04_18_NtuplesV41 --tag DataReco --v HCAL --addtag C
# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate_C_32Nodes.py --indir 2023_04_18_NtuplesV41 --tag DataReco50to80 --v HCAL --batch_size 512 --epochs 20 --addtag leesNodes

# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate_C.py --indir 2023_04_29_NtuplesV42 --tag DataReco --v HCAL --addtag _A --epochs 20
# python3 PrepareReEmulation.py --indir 2023_04_29_NtuplesV42 --v HCAL --tag DataReco --addtag _A
# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate_C.py --indir 2023_04_29_NtuplesV43 --tag DataReco --v HCAL --addtag _A --epochs 20
# python3 PrepareReEmulation.py --indir 2023_04_29_NtuplesV43 --v HCAL --tag DataReco --addtag _A

# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate.py --indir 2023_02_22_NtuplesV30 --tag DataReco --v ECAL --epochs 20 --batch_size 2048 --validation_split 0.2 --ngpus 4
# sleep 5

# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate.py --indir 2023_02_22_NtuplesV30 --tag DataReco --v HCAL --epochs 20 --batch_size 2048 --validation_split 0.2 --ngpus 4
# sleep 5

# python NNModelTraining_FullyCustom_GPUdistributed_batchedRate.py --indir 2023_02_22_NtuplesV30 --tag DataReco --v HF   --epochs 20 --batch_size 2048 --validation_split 0.2 --ngpus 4
# sleep 5

python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegression.py --indir 2023_05_19_NtuplesV46 --v ECAL --tag DataReco --addtag _OnlyRegression
sleep 5
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegressionAndRegularization.py --indir 2023_05_19_NtuplesV46 --v ECAL --tag DataReco --addtag _OnlyRegressionAndRegularization

python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegression.py --indir 2023_05_20_NtuplesV47/JetMET_HoTot95_puppi_barrel --v HCAL --tag DataReco \
 --addtag _OnlyRegression_LRe-3 --batch_size 256 --epochs 50
python3 NNModelTraining_FullyCustom_GPUdistributed_batchedRate_OnlyRegression.py --indir 2023_05_20_NtuplesV47/JetMET_HoTot80_puppi_barrel --v HCAL --tag DataReco \
 --addtag _OnlyRegression_LRe-4 --batch_size 1024 --epochs 20




# python NNModelTraining_FlooringInTTP.py --indir 2022_07_20_NtuplesV23 --v ECAL --tag _0pt500
# sleep 5
# python CalibrationFactor.py --indir 2022_07_20_NtuplesV23 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt500 --padZeros
# sleep 5

# python NNModelTraining_FlooringInTTP.py --indir 2022_07_20_NtuplesV23 --v HCAL --tag _30pt1000
# sleep 5
# python CalibrationFactor.py --indir 2022_07_20_NtuplesV23 --start 1 --stop 200 --v HCAL --tag _30pt1000 --padZeros
# sleep 5

# python NNModelTraining_FlooringInTTP.py --indir 2022_07_20_NtuplesV23 --v ECAL --tag _0pt200
# sleep 5
# python CalibrationFactor.py --indir 2022_07_20_NtuplesV23 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt200 --padZeros
# sleep 5

# python NNModelTraining_FlooringInTTP.py --indir 2022_07_20_NtuplesV23 --v HCAL --tag _30pt500
# sleep 5
# python CalibrationFactor.py --indir 2022_07_20_NtuplesV23 --start 1 --stop 200 --v HCAL --tag _30pt500 --padZeros
# sleep 5

# python NNModelTraining_FlooringInTTP.py --indir 2022_07_20_NtuplesV23 --v HCAL --tag _20pt1000
# sleep 5
# python CalibrationFactor.py --indir 2022_07_20_NtuplesV23 --start 1 --stop 200 --v HCAL --tag _20pt1000 --padZeros
# sleep 5



# python3 ModelPlots.py --indir 2022_07_20_NtuplesV23 --v ECAL --tag _0pt500
# python3 ModelPlots.py --indir 2022_07_20_NtuplesV23 --v HCAL --tag _30pt1000
# python3 ModelPlots.py --indir 2022_07_20_NtuplesV23 --v ECAL --tag _0pt200
# python3 ModelPlots.py --indir 2022_07_20_NtuplesV23 --v HCAL --tag _30pt500
# python3 ModelPlots.py --indir 2022_07_20_NtuplesV23 --v HCAL --tag _20pt1000

# python3 ModelPlots.py --indir 2022_06_14_NtupleV21 --v HCAL --tag _30pt1000_eta41_Lbound0p95

# python3 ModelPlots.py --indir 2022_07_12_NtupleV22 --v HCAL --tag _30pt1000_eta41_nTT





# python NNModelTraining_FlooringInTTP_SoftSaturationInTTP.py --indir 2022_07_20_NtuplesV23 --v HCAL --tag _30pt1000_softSaturInTTP --proxyMinEta 16 --proxyMaxEta 28 --proxyMinE 3 --proxyMaxE 6
# sleep 5
# python CalibrationFactor.py --indir 2022_07_20_NtuplesV23 --start 1 --stop 200 --v HCAL --tag _30pt1000_softSaturInTTP --padZeros
# sleep 5