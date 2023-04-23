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


##############################################################################
############################## HELPER FUNCTIONS ##############################
##############################################################################

# def convert_samples(Z, version):
#     # X vector columns: iem, ihad, iesum, ieta
#     if version == 'ECAL':
#         Z = np.delete(Z, 2, axis=2)
#         Z = Z[ Z[:,:,0] >= 29 ] # remove TTs that have iEM<=29 : 29 ~ (50-(50*0.12))/1.5 = (egThr-(egThr*hoeThrEB))/bigSF [this already reshapes so that every TT becomes an event]
#         Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have iem on the right

#     elif version == 'HCAL':
#         Z = Z[ np.sum(Z[:,:,2], axis=1) >= 50 ] # remove TTs that have iSUM<=50 : 50 ~ (100/n)/1.66*n = (jetThr/nActiveTT)/bigSF*nActiveTT
#         Z = np.delete(Z, 2, axis=2)

#     return Z

def threshold_relaxation_sigmoid(x, mean, sharpness):
    k = sharpness * (x - mean)
    return tf.sigmoid(k, name="sigmoid")

def threshold_relaxation_inverseSigmoid(x, mean, sharpness):
    k = sharpness * (x - mean)
    return tf.sigmoid(-k, name="inverse_sigmoid")

# part of the loss that controls the rate for jets
def rateLossJets(z, seedThr, jetThr):
    # predict seed energy and apply threshold
    TT_seed_pred = z[:,40,1:2] + z[:,40,0:1]
    TT_seed_AT = threshold_relaxation_sigmoid(TT_seed_pred, seedThr, 100.)

    # predict jet energy and apply threshold
    jet_pred = tf.reduce_sum(z[:,:,0], axis=1, keepdims=True) + tf.reduce_sum(z[:,:,1], axis=1, keepdims=True)
    jet_AT = threshold_relaxation_sigmoid(jet_pred, jetThr, 10.)
    
    passing = tf.reduce_sum(TT_seed_AT * jet_AT, keepdims=False) # do logical AND between z_seeds_AT and z_jet_AT
    proxyRate = passing / z.shape[0] * 0.001*2500*11245.6

    return proxyRate

def SimpleRateLossEgs (z, egThr):
    # no need to act on the seed (already clusterized)
    # predict jet energy and apply threshold: sum all the ihad energies z[:,:,0] of the 9x9 and all the iem energies z[:,:,1] of the 9x9
    jet_pred = tf.reduce_sum(z[:,:,0], axis=1, keepdims=True) + tf.reduce_sum(z[:,:,1], axis=1, keepdims=True)
    # for each entry of jet_pred, apply sigmoid cut at egThr (50): if jet_pred > 50 TT_eAT = 1, else 0
    TT_eAT = threshold_relaxation_sigmoid(jet_pred, egThr, 10.)
    # compute the number of clusters passing the egThr cut
    passing = tf.reduce_sum(TT_eAT, keepdims=False)

    # the rate of each single batch is computed as: (# of clusters passing egThr)/(# of clusters in the batch)
    proxyRate = passing / z.shape[0] * 0.001*2500*11245.6

    # apply cut on eoh !!!!

    return proxyRate


# part of the loss that controls the rate for e/gammas
def rateLossEgs(z, hoeThrEB, hoeThrEE, egThr):

    # 'hardcoded' threshold on hcal over ecal deposit
    hasEBthr = tf.reduce_sum(z[:,2:30], axis=1, keepdims=True) * pow(2, -hoeThrEB)
    hasEEthr = tf.reduce_sum(z[:,30:], axis=1, keepdims=True) * pow(2, -hoeThrEE)
    hoeThr = hasEBthr + hasEEthr

    # hadronic deposit bhind the ecal one
    TT_had = z[:,0:1]

    # predict TT energy, add correspondong non-calibrated had part, and apply threshold
    TT_em_pred = z[:,1:2]
    TT_pred = TT_em_pred + TT_had
    TT_eAT = threshold_relaxation_sigmoid(TT_pred, egThr, 10.)

    # calculate HoE for each TT and apply threshold
    TT_hoe = tf.math.divide_no_nan(TT_had, TT_em_pred)
    TT_hoeAT = threshold_relaxation_inverseSigmoid(TT_hoe, hoeThr, 1000.)

    passing = tf.reduce_sum(TT_hoeAT * TT_eAT, keepdims=False) # do logical AND between TT_eAT and TT_hoeAT
    proxyRate = passing / z.shape[0] * 0.001*2500*11245.6

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
    # for the new version of the Rate Proxy we have defined a 9x9 also for ECAL
    if options.v == 'ECAL':                      rateLoss_value += SimpleRateLossEgs(z, 50) # remember the thresholds are in HW units!
    # if options.v == 'ECAL':                      rateLoss_value += rateLossEgs(z, 3, 4, 50) # remember the thresholds are in HW units!
    if options.v == 'HCAL' or options.v == 'HF': rateLoss_value += rateLossJets(z, 8, 100)  # remember the thresholds are in HW units!

print(options.v, 'OLD CALIBRATION : rateLoss_value =', rateLoss_value/num_batches, '(computed as: passing / total * 0.001*2500*11245.6)')


