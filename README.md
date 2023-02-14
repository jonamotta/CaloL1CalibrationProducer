# CaloL1CalibrationProducer

Package to produce CaloL1 calibration of the trigger towers.

## Installation instructions
```bash
cmsrel CMSSW_13_0_0_pre2
cd CMSSW_13_0_0_pre2/src
cmsenv
git cms-init
git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
git fetch cms-l1t-offline l1t-integration-CMSSW_13_0_0_pre2
git cms-merge-topic -u cms-l1t-offline:l1t-integration-v142
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data

git clone git@github.com:jonamotta/CaloL1CalibrationProducer.git

git cms-checkdeps -A -a

scram b -j 12
```

To produce the L1NTuples on Tier3, go in `L1NtupleLauncher` and run:
```bash
python submitOnTier3.py <options>
```
Examples of launching commands can be found in `submitOnTier3.sh`.

After the production of the L1NTuples the production of the input files to the NNs is done by going to `L1NtupleReader` and running:
```bash
python3 batchMaker.py <options>
```
this will batch the L1NTuples in `.hdf5` files containing no more then N events each (N to be specified).

After the batching, crate the taglist file and put it inside the folder `L1NtupleReader/inputBatches`

After this the Padding of the chunky donut needs to be performed with:
```bash
python batchSubmitOnTier3.py <options>
```
Examples of launching commands can be found in `batchSubmitOnTier3.sh`.


After this, need to merge the batches into one single file containing the input to the NNs, this is done with:
```bash
python3 batchMerger.py <options>
```
this will create the following four output files that are to be used for the training of the NNs:
* `X_train.npz`
* `X_test.npz`
* `Y_train.npz`
* `Y_test.npz`

When the four inputs files above are produced the model can be trained with:
```bash
python3 NNModelTraining<NNversions>.py <options>
```

To produce the Scale Factors matrix, run:
```bash
python3 CalibrationFactor<tag>.py <options>
```

To make the plots of the output of the NN, run:
```bash
python3 ModelPlots<tag>.py <options>
```