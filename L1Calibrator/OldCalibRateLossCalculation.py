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

        Z[:,[0,1]] = Z[:,[1,0]]

    elif version == 'HCAL':
        Z = Z[ np.sum(Z[:,:,2], axis=1) >= 50 ] # remove TTs that have iSUM<=50 : 50 ~ (100/n)/1.66*n = (jetThr/nActiveTT)/bigSF*nActiveTT
        Z = np.delete(Z, 2, axis=2)

    return Z

def applyECALcalib(Z, TTP):
    xDim = Z.shape[0] ; yDim = 81 ; zDim = 42
    Z = Z.reshape(xDim*yDim, zDim) # reshape so that every TT becomes an event
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    TT_em_pred = tf.cast(TTP.predict(Z[:,1:], batch_size=2048), dtype=tf.int16)
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    Z[:,[0]] = TT_em_pred
    Z = Z.reshape(xDim, yDim, zDim) # reshape so that 81xTT becomes an event again
    return Z

# part of the loss that controls the rate for jets
def rateLossJets(z, seedThr, jetThr):
    # predict seed energy and apply threshold
    TT_seed_pred = tf.reshape(z[:,40,1] + z[:,40,0], (-1,1))
    TT_seed_AT = tf.where(TT_seed_pred>=seedThr, 1., 0.)

    # predict jet energy and apply threshold
    jet_pred = tf.reduce_sum(z[:,:,0], axis=1, keepdims=True) + tf.reduce_sum(z[:,:,1], axis=1, keepdims=True)
    jet_AT = tf.where(jet_pred>=jetThr, 1., 0.)
    
    passing = tf.reduce_sum(TT_seed_AT * jet_AT, keepdims=False) # do logical AND between z_seeds_AT and z_jet_AT
    proxyRate = passing / z.shape[0] * 0.001*2500*11245.6

    return proxyRate

# part of the loss that controls the rate for e/gammas
def rateLossEgs(z, hoeThrEB, hoeThrEE, egThr):
    # 'hardcoded' threshold on hcal over ecal deposit
    hasEBthr = tf.cast(tf.reduce_sum(z[:,2:30], axis=1, keepdims=True), dtype=tf.float32) * pow(2, -hoeThrEB)
    hasEEthr = tf.cast(tf.reduce_sum(z[:,30:], axis=1, keepdims=True), dtype=tf.float32) * pow(2, -hoeThrEE)
    hoeThr = hasEBthr + hasEEthr

    # hadronic deposit bhind the ecal one
    TT_had = tf.reshape(z[:,0], (-1,1))

    # predict TT energy, add correspondong non-calibrated had part, and apply threshold
    TT_em_pred = tf.reshape(z[:,1], (-1,1))
    TT_pred = TT_em_pred + TT_had
    TT_eAT = tf.where(TT_pred>=egThr, 1., 0.)

    # calculate HoE for each TT and apply threshold
    TT_hoe = TT_had / TT_em_pred
    TT_hoeAT = tf.where(TT_hoe<=hoeThr, 1., 0.)

    passing = tf.reduce_sum(TT_hoeAT * TT_eAT, keepdims=False) # do logical AND between TT_eAT and TT_hoeAT
    proxyRate = passing / z.shape[0] * 0.001*2500*11245.6

    return proxyRate

# part of the loss that controls the rate for jets
def rateLossJets_fromModel(z, seedThr, jetThr, TTP, model):
    # predict seed energy (including the correspondong non-calibrated TT part) and apply threshold
    TT_seed_pred = tf.cast(TTP(z[:,40,1:]), dtype=tf.int16) + tf.reshape(z[:,40,0], (-1,1))
    TT_seed_AT = tf.where(TT_seed_pred>=seedThr, 1., 0.)

    # predict jet energy (including the correspondong non-calibrated TTs part) and apply threshold
    jet_pred = model(z, training=False) + tf.cast(tf.reduce_sum(z, axis=1, keepdims=True)[:,:,0], dtype=tf.float32)
    jet_AT = tf.where(jet_pred>=jetThr, 1., 0.)
    
    passing = tf.reduce_sum(TT_seed_AT * jet_AT, keepdims=False) # do logical AND between z_seeds_AT and z_jet_AT
    proxyRate = passing / z.shape[0] * 0.001*2500*11245.6

    return proxyRate

# part of the loss that controls the rate for e/gammas
def rateLossEgs_fromModel(z, hoeThrEB, hoeThrEE, egThr, TTP):
    # 'hardcoded' threshold on hcal over ecal deposit
    hasEBthr = tf.cast(tf.reduce_sum(z[:,2:30], axis=1, keepdims=True), dtype=tf.float32) * pow(2, -hoeThrEB)
    hasEEthr = tf.cast(tf.reduce_sum(z[:,30:], axis=1, keepdims=True), dtype=tf.float32) * pow(2, -hoeThrEE)
    hoeThr = hasEBthr + hasEEthr

    # hadronic deposit behind the ecal one
    TT_had = tf.reshape(z[:,0], (-1,1))

    # predict TT energy, add correspondong non-calibrated had part, and apply threshold
    TT_em_pred = tf.cast(TTP(z[:,1:]), dtype=tf.int16)
    TT_pred = TT_em_pred + TT_had
    TT_eAT = tf.where(TT_pred>=egThr, 1., 0.)

    # calculate HoE for each TT and apply threshold
    TT_hoe = TT_had / TT_em_pred
    TT_hoeAT = tf.where(TT_hoe<=hoeThr, 1., 0.)

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
parser.add_option("--readTfDatasets", dest="readTfDatasets", help="Do not do pre-processing and load TF datasets", default=False, action='store_true' )
(options, args) = parser.parse_args()





Z_train = np.load('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/NUtraining_rateProxy_oldCalib/X_train.npz')['arr_0']
Z_train = convert_samples(Z_train, options.v)
z_rate = tf.convert_to_tensor(Z_train, dtype=tf.int16)
_ = tf.convert_to_tensor(np.zeros(len(Z_train)), dtype=tf.int8)

if options.v == 'HCAL': rateLoss_value = rateLossJets(z_rate, 8, 100)  # remember the thresholds are in HW units!
if options.v == 'ECAL': rateLoss_value = rateLossEgs(z_rate, 3, 4, 50) # remember the thresholds are in HW units!

print(options.v, 'OLD CALIBRATION : rateLoss_value =', rateLoss_value, '(computed as: passing / total * 0.001*2500*11245.6)')




Z_train = np.load('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/NUtraining_rateProxy/X_train.npz')['arr_0']
Z_train = convert_samples(Z_train, options.v)
z_rate = tf.convert_to_tensor(Z_train, dtype=tf.int16)
if options.v == 'HCAL': rateLoss_value = rateLossJets(z_rate, 8, 100)  # remember the thresholds are in HW units!
if options.v == 'ECAL': rateLoss_value = rateLossEgs(z_rate, 3, 4, 50) # remember the thresholds are in HW units!

print(options.v, 'UNCALIBRATED : rateLoss_value =', rateLoss_value, '(computed as: passing / total * 0.001*2500*11245.6)')




if options.v == 'HCAL':
    ECAL_TTPmodel = keras.models.load_model('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/ECALtraining_0pt500/model_ECAL/TTP', compile=False, custom_objects={'Fgrad': Fgrad})
    Z_train = applyECALcalib(Z_train, ECAL_TTPmodel)
    z_rate = tf.convert_to_tensor(Z_train, dtype=tf.int16)
    del ECAL_TTPmodel
modeldir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/model_' + options.v
TTP = tf.keras.models.load_model(modeldir + '/TTP', compile=False, custom_objects={'Fgrad': Fgrad})
model = tf.keras.models.load_model(modeldir + '/model', compile=False, custom_objects={'Fgrad': Fgrad})
if options.v == 'HCAL': rateLoss_value = rateLossJets_fromModel(z_rate, 8, 100, TTP, model)  # remember the thresholds are in HW units!
if options.v == 'ECAL': rateLoss_value = rateLossEgs_fromModel(z_rate, 3, 4, 50, TTP) # remember the thresholds are in HW units!

print(options.v, 'NEW CALIBRATION : rateLoss_value =', rateLoss_value, '(computed as: passing / total * 0.001*2500*11245.6)')








