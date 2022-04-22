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
```bash
python batchMaker.py --v {ECAL/HCAL}
```
this will batch the L1NTuples in `.hdf5` files containing no more then 5000 events each. After this bacthing the Padding of the chunky donut needs to be performed with:
```bash
module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7
module load python/3.7.0
python batchSubmitOnTier3.py --v {gamma1/gamma2/qcd} {--jetcut 60} {--etacut 24}
```
this will run the padding of the chunky donut on the Tier3 so that it will fast. It will produce the same number of output files as the number of input ones.
After this we need to merge the batches into one single file containing the input to the NNs, this is one with:
```bash
python3 batchMerger.py {--dir /data_CMS/cms/motta/CaloL1calibraton/2022_04_21_NtuplesV1}
```
this will create the following four output files that are to be used for the training of the NNs:
* `X_train.npz`
* `X_test.npz`
* `Y_train.npz`
* `Y_test.npz`

When the four inputs files above are produced the model can be trained with:
```bash
python3 alternateModel4ECAL.py --in /data_CMS/cms/motta/CaloL1calibraton/2022_04_21_NtuplesV1/ECALtraining --out /data_CMS/cms/motta/CaloL1calibraton/2022_04_21_NtuplesV1/ECALtraining/model_ECAL --v ECAL
```

To produce the Scale Factors matrix:
```bash
python3 CalibrationFactor.py --model /data_CMS/cms/motta/CaloL1calibraton/2022_04_21_NtuplesV1/ECALtraining/model_ECAL --out data_ECAL
```

To make plots:
```bash
python3 ModelPlots.py --model /data_CMS/cms/motta/CaloL1calibraton/2022_04_21_NtuplesV1/ECALtraining/model_ECAL --out data_ECAL/plots --SF data_ECAL/ScaleFactors_ECAL.csv
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