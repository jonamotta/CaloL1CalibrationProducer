# python NNModelTraining_FlooringInTTP.py --indir 2022_06_10_NtuplesV20 --v ECAL --tag _0pt500
# sleep 5
# python CalibrationFactor.py --indir 2022_06_10_NtuplesV20 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt500 --padZeros
# sleep 5

# python NNModelTraining_FlooringInTTP.py --indir 2022_06_10_NtuplesV20 --v HCAL --tag _30pt1000
# sleep 5
# python CalibrationFactor.py --indir 2022_06_10_NtuplesV20 --start 1 --stop 200 --v HCAL --tag _30pt1000 --padZeros
# sleep 5

# python NNModelTraining_FlooringInTTP.py --indir 2022_06_10_NtuplesV20 --v ECAL --tag _0pt200
# sleep 5
# python CalibrationFactor.py --indir 2022_06_10_NtuplesV20 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt200 --padZeros
# sleep 5

# python NNModelTraining_FlooringInTTP.py --indir 2022_06_10_NtuplesV20 --v HCAL --tag _30pt500
# sleep 5
# python CalibrationFactor.py --indir 2022_06_10_NtuplesV20 --start 1 --stop 200 --v HCAL --tag _30pt500 --padZeros
# sleep 5

# python NNModelTraining_FlooringInTTP.py --indir 2022_06_10_NtuplesV20 --v HCAL --tag _20pt1000
# sleep 5
# python CalibrationFactor.py --indir 2022_06_10_NtuplesV20 --start 1 --stop 200 --v HCAL --tag _20pt1000 --padZeros
# sleep 5


# python NNModelTraining_FlooringInTTP_SaturationAfterTTP.py --indir 2022_06_14_NtupleV21 --v HCAL --tag _30pt1000_eta41_satur1p45
# sleep 5
# python CalibrationFactor_mod.py --indir 2022_06_14_NtupleV21 --start 1 --stop 200 --v HCAL --tag _30pt1000_eta41_satur1p45 --padZeros
# sleep 5

python NNModelTraining_FlooringInTTP_SaturationAfterTTP.py --indir 2022_06_14_NtupleV21 --v ECAL --tag _0pt500_satur1p2
sleep 5
python CalibrationFactor_mod.py --indir 2022_06_14_NtupleV21 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt500_satur1p2 --padZeros
sleep 5

python NNModelTraining_FlooringInTTP_SaturationAfterTTP.py --indir 2022_06_14_NtupleV21 --v ECAL --tag _0pt500_satur1p3
sleep 5
python CalibrationFactor_mod.py --indir 2022_06_14_NtupleV21 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt500_satur1p3 --padZeros
sleep 5

python NNModelTraining_FlooringInTTP_SaturationAfterTTP.py --indir 2022_06_14_NtupleV21 --v ECAL --tag _0pt500_satur1p4
sleep 5
python CalibrationFactor_mod.py --indir 2022_06_14_NtupleV21 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt500_satur1p4 --padZeros
sleep 5

python NNModelTraining_FlooringInTTP_SaturationAfterTTP.py --indir 2022_06_14_NtupleV21 --v ECAL --tag _0pt500_satur1p5
sleep 5
python CalibrationFactor_mod.py --indir 2022_06_14_NtupleV21 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt500_satur1p5 --padZeros
sleep 5

python NNModelTraining_FlooringInTTP_SaturationAfterTTP.py --indir 2022_06_14_NtupleV21 --v ECAL --tag _0pt500_satur1p6
sleep 5
python CalibrationFactor_mod.py --indir 2022_06_14_NtupleV21 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt500_satur1p6 --padZeros
sleep 5


# python3 ModelPlots.py --indir 2022_06_10_NtuplesV20 --v ECAL --tag _0pt500
# python3 ModelPlots.py --indir 2022_06_10_NtuplesV20 --v HCAL --tag _30pt1000
# python3 ModelPlots.py --indir 2022_06_10_NtuplesV20 --v ECAL --tag _0pt200
# python3 ModelPlots.py --indir 2022_06_10_NtuplesV20 --v HCAL --tag _30pt500
# python3 ModelPlots.py --indir 2022_06_10_NtuplesV20 --v HCAL --tag _20pt1000
