python NNModelTraining_FlooringInTTP.py --indir 2022_06_01_NtuplesV19 --v ECAL --tag _0pt200
sleep 5
python NNModelTraining_FlooringInTTP.py --indir 2022_06_01_NtuplesV19 --v ECAL --tag _0pt500
sleep 5
python NNModelTraining_FlooringInTTP.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _30pt1000
sleep 5
python NNModelTraining_FlooringInTTP.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _30pt1000_eta41
sleep 5
python NNModelTraining_FlooringInTTP.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _30pt500
sleep 5
python NNModelTraining_FlooringInTTP.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _20pt1000
sleep 5

python CalibrationFactor.py --indir 2022_06_01_NtuplesV19 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt200 --padZeros
sleep 5
python CalibrationFactor.py --indir 2022_06_01_NtuplesV19 --start 1 --stop 200 --maxeta 28 --v ECAL --tag _0pt500 --padZeros
sleep 5
python CalibrationFactor.py --indir 2022_06_01_NtuplesV19 --start 1 --stop 200 --v HCAL --tag _30pt1000 --padZeros
sleep 5
python CalibrationFactor.py --indir 2022_06_01_NtuplesV19 --start 1 --stop 200 --v HCAL --tag _30pt1000_eta41 --padZeros
sleep 5
python CalibrationFactor.py --indir 2022_06_01_NtuplesV19 --start 1 --stop 200 --v HCAL --tag _30pt500 --padZeros
sleep 5
python CalibrationFactor.py --indir 2022_06_01_NtuplesV19 --start 1 --stop 200 --v HCAL --tag _20pt1000 --padZeros
sleep 5

python ModelPlots.py --indir 2022_06_01_NtuplesV19 --v ECAL --tag _0pt200
sleep 5
python ModelPlots.py --indir 2022_06_01_NtuplesV19 --v ECAL --tag _0pt500
sleep 5
python ModelPlots.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _30pt1000
sleep 5
python ModelPlots.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _30pt1000_eta41
sleep 5
python ModelPlots.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _30pt1000_eta41_newFeat
sleep 5
python ModelPlots.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _30pt500
sleep 5
python ModelPlots.py --indir 2022_06_01_NtuplesV19 --v HCAL --tag _20pt1000
sleep 5