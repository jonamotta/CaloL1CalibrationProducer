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

feature_description = {
    'chuncky_donut': tf.io.FixedLenFeature([], tf.string, default_value=''), # byteslist to be read as string 
    'trainingPt'   : tf.io.FixedLenFeature([], tf.float32, default_value=0)  # single float values
}

# parse proto input based on description
def parse_function(example_proto):
    example = tf.io.parse_single_example(example_proto, feature_description)
    chuncky_donut = tf.io.parse_tensor(example['chuncky_donut'], out_type=tf.float32) # decode byteslist to original 81x43 tensor
    return chuncky_donut, example['trainingPt']

def threshold_relaxation_sigmoid(x, mean, sharpness):
    k = sharpness * (x - mean)
    return tf.sigmoid(k, name="sigmoid")

def RateProxyJets (cd, seedThr, jetThr):

    seedThr = seedThr - 0.1
    jetThr = jetThr - 0.1
    numThr = 1 - 0.1

    # for each tower apply sigmoid cut on the seed at seedThr (8): if tower energy > 8 jet_seed_found = 1, else 0
    TT_iesum = cd[:,:,1] + cd[:,:,0]
    jet_seed_found = threshold_relaxation_sigmoid(TT_iesum, seedThr, 1000.)
    # for each jet compute how many seeds were found
    jet_seed_number = tf.reduce_sum(jet_seed_found, axis=1, keepdims=True)
    # for each jet check the presence of at least one seed
    jet_seed_passing = threshold_relaxation_sigmoid(jet_seed_number, numThr, 1000.)

    # predict jet energy and apply threshold: sum all the ihad energies cd[:,:,1] of the 9x9 and all the iem energies cd[:,:,0] of the 9x9
    jet_sum = tf.reduce_sum(cd[:,:,1], axis=1, keepdims=True) + tf.reduce_sum(cd[:,:,0], axis=1, keepdims=True)
    # for each entry of jet, apply sigmoid cut on the sum at jetThr (50): if jet_sum > 50 jet_sum_passing = 1, else 0
    jet_sum_passing = threshold_relaxation_sigmoid(jet_sum, jetThr, 10.)
    # compute the number of jets passing both selections
    jet_passing = tf.reduce_sum(jet_seed_passing * jet_sum_passing, keepdims=False)
    # print("### INFO: " + str(jet_passing) + " / " + str(cd.shape[0]) + " = " + str(jet_passing/cd.shape[0]))

    return jet_passing / cd.shape[0]

# python3 TestRateProxy.py --indir 2023_06_08_NtuplesV50/JetMET_PuppiJet_Barrel_Pt30_HoTot95 --v HCAL --tag DataReco

##############################################################################
################################## MAIN BODY #################################
##############################################################################

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--indir",    dest="indir",    help="Input folder with TFRecords",                    default=None  )
parser.add_option("--v",        dest="v",        help="Which training to perform: ECAL or HCAL?",       default=None  )
parser.add_option("--tag",      dest="tag",      help="Tag of the training folder",                     default=""    )
parser.add_option("--filesLim", dest="filesLim", help="Maximum number of files to use",                 default=1000000, type=int)
(options, args) = parser.parse_args()

indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
if options.v == 'ECAL':                      sys.exit("Rate proxy not implemented")
if options.v == 'HCAL' or options.v == 'HF': batch_size = 500

# read raw rate dataset and parse it 
print('\n ### Reading TF records from: ' + indir + '/rateTFRecords/record_*.tfrecord')
InTrainRecords = glob.glob(indir+'/rateTFRecords/record_*.tfrecord')[:options.filesLim]
raw_train_dataset = tf.data.TFRecordDataset(InTrainRecords)
train_dataset = raw_train_dataset.map(parse_function)
train_dataset = train_dataset.batch(batch_size, drop_remainder=True)
del InTrainRecords, raw_train_dataset

num_batches = 0
rateLoss_value = 0
jet_passing_100 = 0
jet_passing_80 = 0
jet_passing_50 = 0
jet_passing_45 = 0
jet_passing_40 = 0
jet_passing_35 = 0
jet_passing_30 = 0
jet_total = 0
# remember the thresholds are in HW units!)
for train_batch in train_dataset:
    if not num_batches%100: print('at batch', num_batches)
    num_batches += 1
    cd, _ = train_batch
    jet_passing_100 += float(RateProxyJets(cd, 8, 200))
    jet_passing_80 += float(RateProxyJets(cd, 8, 160))
    jet_passing_50 += float(RateProxyJets(cd, 8, 100))
    jet_passing_45 += float(RateProxyJets(cd, 8, 90))
    jet_passing_40 += float(RateProxyJets(cd, 8, 80))
    jet_passing_35 += float(RateProxyJets(cd, 8, 70))
    jet_passing_30 += float(RateProxyJets(cd, 8, 60))

print("### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 30 GeV : ", jet_passing_30/num_batches)
print("### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 35 GeV : ", jet_passing_35/num_batches)
print("### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 40 GeV : ", jet_passing_40/num_batches)
print("### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 45 GeV : ", jet_passing_45/num_batches)
print("### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 50 GeV : ", jet_passing_50/num_batches)
print("### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 80 GeV : ", jet_passing_80/num_batches)
print("### INFO: Compute percentage of jets passing seed at 4 GeV & sum > 100 GeV : ", jet_passing_100/num_batches)


