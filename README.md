# L1NtupleProducer

Folder to produce the NTuples and the csv/hdf5 files to be used as input for the CaloL1 calibration of the trigger towers.

## Installation instructions
```bash
cmsrel CMSSW_12_3_0_pre6
cd CMSSW_12_3_0_pre6/src
cmsenv
git cms-init
git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
git fetch cms-l1t-offline l1t-integration-CMSSW_12_3_0_pre6
git cms-merge-topic -u cms-l1t-offline:l1t-integration-v124.0
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data
git clone git@github.com:jonamotta/L1NtupleProducer.git

git cms-checkdeps -A -a

scram b -j 12
```

To produce the L1NTuples on Tier3, go in `L1NtupleLauncher` and run:
```bash
python submitOnTier3.py
```

After the production of the L1NTuples the production of the input files to the NNs is done by going to `L1NtupleReader` and running:
-> Change the name of the output folder at L70 of batchMaker.py (ex. 2022_05_03_NtuplesV10)
```bash
python3 batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG0_200 --applyNoCalib
```
this will batch the L1NTuples in `.hdf5` files containing no more then 5000 events each. After this bacthing the Padding of the chunky donut needs to be performed with:
-> Crate the taglist file (Jona did it for me) and put it inside this folder '/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/'
```bash
module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7
module load python/3.7.0
python batchSubmitOnTier3.py --doEG0_200 --jetcut 60 --etacut 24 --ecalcut True --indir 2022_05_03_NtuplesV10 --applyHCALpfa1p --applyNoCalib
```
this will run the padding of the chunky donut on the Tier3 so that it will fast. It will produce the same number of output files as the number of input ones.
After this we need to merge the batches into one single file containing the input to the NNs, this is one with:
```bash
python3 batchMerger.py --applyHCALpfa1 --indir 2022_05_03_NtuplesV10 --v ECAL --applyNoCalib --doEG --sample {train or test}
```
this will create the following four output files that are to be used for the training of the NNs:
* `X_train.npz`
* `X_test.npz`
* `Y_train.npz`
* `Y_test.npz`

When the four inputs files above are produced the model can be trained with:
```bash
python3 alternateModel4ECAL.py --in /data_CMS/cms/motta/CaloL1calibraton/2022_04_26_NtuplesV4/ECALtraining --v ECAL
```

To produce the Scale Factors matrix:
```bash
python3 CalibrationFactor.py --in /data_CMS/cms/motta/CaloL1calibraton/2022_04_26_NtuplesV4/ECALtraining --v ECAL
```

To make plots:
```bash
python3 ModelPlots.py --in /data_CMS/cms/motta/CaloL1calibraton/2022_04_26_NtuplesV4/ECALtraining --v ECAL
```


## Pyhton version
All of this should work with the Python version already given by the CMSSW environment.
In case that does not work, a compatible version can be loaded via:
```bash
module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7
module load python/3.7.0
```

In case this version is being used for a Jupyter Notebook, then the fiollowing is also suggested:
```bash
source /opt/exp_soft/llr/root/v6.14.04-el7-gcc71-py37/bin/thisroot.sh
unset JUPYTER_CONFIG_DIR
unset JUPYTER_PATH
```