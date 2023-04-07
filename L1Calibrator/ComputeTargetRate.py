import numpy as np
import random
import glob
import sys
import os

import matplotlib.pyplot as plt

from NNModelTraining_FullyCustom_GPUdistributed import *
import tensorflow as tf

random.seed(7)
np.random.seed(7)
os.system('export PYTHONHASHSEED=7')


# python3 ComputeTargetRate.py --indir 2023_04_06_NtuplesV39 --v ECAL --tag TargetRateProxy
# ECAL CURR CALIBRATION : Target Rate Proxy = tf.Tensor(44.63708, shape=(), dtype=float32)

def threshold_relaxation_sigmoid(x, mean, sharpness):
    k = sharpness * (x - mean)
    return tf.sigmoid(k, name="sigmoid")

def threshold_relaxation_inverseSigmoid(x, mean, sharpness):
    k = sharpness * (x - mean)
    return tf.sigmoid(-k, name="inverse_sigmoid")

# part of the loss that controls the rate for egammas
def rateLossEgs (z, egThr):
    # no need to act on the seed (already clusterized)
    # predict jet energy and apply threshold: sum all the ihad energies z[:,:,0] of the 9x9 and all the iem energies z[:,:,1] of the 9x9
    jet_pred = tf.reduce_sum(z[:,:,0], axis=1, keepdims=True) + tf.reduce_sum(z[:,:,1], axis=1, keepdims=True)
    # for each entry of jet_pred, apply sigmoid cut at egThr (50): if jet_pred > 50 TT_eAT = 1, else 0
    TT_eAT = threshold_relaxation_sigmoid(jet_pred, egThr, 10.)
    # compute the number of clusters passing the egThr cut
    passing = tf.reduce_sum(TT_eAT, keepdims=False)

    # the rate of each single batch is computed as: (# of clusters passing egThr)/(# of clusters in the batch)
    # scale_clusters15GeV is computed in ComputeScaleClusters.py
    # python3 ComputeScaleClusters.py \
    # --LogDir /data_CMS/cms/motta/CaloL1calibraton/2023_04_06_NtuplesV39/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data/ \
    # --L1Dir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data/
    scale_clusters15GeV = 0.016549667686051477 # computed as (# clusters with EG > 15 GeV)/(# total events)
    scale_rate = 0.001*2500*11245.6 
    # reconvert the ratio to EG25GeV rate
    proxyRate = passing / z.shape[0] * scale_rate * scale_clusters15GeV

    return proxyRate

# part of the loss that controls the rate for jets
def rateLossJets(z, seedThr, jetThr): # [FIXME]
    # predict seed energy and apply threshold
    TT_seed_pred = z[:,40,1:2] + z[:,40,0:1]
    TT_seed_AT = threshold_relaxation_sigmoid(TT_seed_pred, seedThr, 100.)
    # predict jet energy and apply threshold
    jet_pred = tf.reduce_sum(z[:,:,0], axis=1, keepdims=True) + tf.reduce_sum(z[:,:,1], axis=1, keepdims=True)
    jet_AT = threshold_relaxation_sigmoid(jet_pred, jetThr, 10.)
    
    passing = tf.reduce_sum(TT_seed_AT * jet_AT, keepdims=False) # do logical AND between z_seeds_AT and z_jet_AT
    scale_rate = 0.001*2500*11245.6 
    # the rate should already be consistent but some studies have to be performed as for the ECAL case
    proxyRate = passing / z.shape[0] * scale_rate

    return proxyRate


##############################################################################
################################## MAIN BODY #################################
##############################################################################

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--indir",          dest="indir",          help="Input folder with X_train.npx and Y_train.npz", default=None                       )
parser.add_option("--v",              dest="v",              help="Which training to perform: ECAL or HCAL?",      default=None                       )
parser.add_option("--tag",            dest="tag",            help="Tag of the training folder",                    default=""                         )
(options, args) = parser.parse_args()

indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
if options.v == 'ECAL':                      batch_size = 256
if options.v == 'HCAL' or options.v == 'HF': batch_size = 2048

# description of the features for reading out
feature_description = {
    'chuncky_donut': tf.io.FixedLenFeature([], tf.string, default_value=''), # byteslist to be read as string 
    'trainingPt'   : tf.io.FixedLenFeature([], tf.float32, default_value=0)  # single float values
}

# parse proto input based on description
def parse_function(example_proto):
    example = tf.io.parse_single_example(example_proto, feature_description)
    chuncky_donut = tf.io.parse_tensor(example['chuncky_donut'], out_type=tf.float32) # decode byteslist to original 81x43 tensor
    return chuncky_donut, example['trainingPt']

# read raw rate dataset and parse it 
InRateRecords = glob.glob(indir+'/rateTFRecords/record_*.tfrecord')
raw_rate_dataset = tf.data.TFRecordDataset(InRateRecords)
rate_dataset = raw_rate_dataset.map(parse_function)
rate_dataset = rate_dataset.batch(batch_size, drop_remainder=True)
del InRateRecords, raw_rate_dataset

num_batches = 0
rateLoss_value = 0
for rate_batch in rate_dataset:
    if not num_batches%100: print('at batch', num_batches)
    num_batches += 1
    z, _ = rate_batch
    if options.v == 'ECAL':                      rateLoss_value += rateLossEgs(z, 50) # remember the thresholds are in HW units!
    if options.v == 'HCAL' or options.v == 'HF': rateLoss_value += rateLossJets(z, 8, 100)  # remember the thresholds are in HW units!

if options.v == 'ECAL':
    print( options.v, 'CURR CALIBRATION : Target Rate Proxy =', rateLoss_value/num_batches, \
          '(computed as: (# clusters passing 25 GeV) / (# clusters) * 0.001*2500*11245.6) * (# clusters)/(# total events)')


