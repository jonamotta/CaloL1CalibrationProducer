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

After the production of the L1NTuples the production of the `.csv`/`.hdf5` files is done by going to `L1NtupleReader` and running:
```bash
python basicReader.py
```

**STILL UNDER DEVELOPMENT**
Whe the inputs are produced the model can be trained with:
```bash
python Model4.py
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