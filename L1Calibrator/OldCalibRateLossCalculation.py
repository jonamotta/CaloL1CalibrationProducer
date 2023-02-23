import numpy as np
import random
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

def convert_samples(Z, version):
    # X vector columns: iem, ihad, iesum, ieta
    if version == 'ECAL':
        Z = np.delete(Z, 2, axis=2)
        Z = Z[ Z[:,:,0] >= 29 ] # remove TTs that have iEM<=29 : 29 ~ (50-(50*0.12))/1.5 = (egThr-(egThr*hoeThrEB))/bigSF [this already reshapes so that every TT becomes an event]
        Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have iem on the right

    elif version == 'HCAL':
        Z = Z[ np.sum(Z[:,:,2], axis=1) >= 50 ] # remove TTs that have iSUM<=50 : 50 ~ (100/n)/1.66*n = (jetThr/nActiveTT)/bigSF*nActiveTT
        Z = np.delete(Z, 2, axis=2)

    return Z

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


Z_train = np.load('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/'+options.v+'training'+options.tag+'/X_trainRate.npz')['arr_0']
Z_train = convert_samples(Z_train, options.v)
z_rate = tf.convert_to_tensor(Z_train, dtype=tf.float32)
if options.v == 'ECAL':                      rateLoss_value = rateLossEgs(z_rate, 3, 4, 50) # remember the thresholds are in HW units!
if options.v == 'HCAL' or options.v == 'HF': rateLoss_value = rateLossJets(z_rate, 8, 100)  # remember the thresholds are in HW units!
print(options.v, 'UNCALIBRATED : rateLoss_value =', rateLoss_value, '(computed as: passing / total * 0.001*2500*11245.6)')


Z_train = np.load('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/'+options.v+'training'+options.tag+'/X_targetRate.npz')['arr_0']
Z_train = convert_samples(Z_train, options.v)
z_rate = tf.convert_to_tensor(Z_train, dtype=tf.float32)
if options.v == 'ECAL':                      rateLoss_value = rateLossEgs(z_rate, 3, 4, 50) # remember the thresholds are in HW units!
if options.v == 'HCAL' or options.v == 'HF': rateLoss_value = rateLossJets(z_rate, 8, 100)  # remember the thresholds are in HW units!
print(options.v, 'OLD CALIBRATION : rateLoss_value =', rateLoss_value, '(computed as: passing / total * 0.001*2500*11245.6)')


