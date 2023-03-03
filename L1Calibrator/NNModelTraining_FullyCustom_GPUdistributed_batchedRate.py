from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import sklearn
import random
import mplhep
import json
import time
import copy
import sys
import os

from tensorflow.keras.initializers import RandomNormal as RN
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers as lay
from tensorflow.keras.layers import Dense
from tensorflow import keras
import tensorflow as tf

random.seed(7)
np.random.seed(7)
tf.random.set_seed(7)
tf.compat.v1.set_random_seed(7)
os.system('export PYTHONHASHSEED=7')


##############################################################################
############################## HELPER FUNCTIONS ##############################
##############################################################################

def convert_samples(X, Y, Z, version):
    # Y vector columns: jetPt, jetEta, jetPhi, trainingPt
    # keep only the trainingPt
    Y = Y[:,3]

    # X vector columns: iem, ihad, iesum, ieta
    if version == 'ECAL':
        X = np.delete(X, 2, axis=2) # delete iesum column (always start deleting from right columns)
        X[:,:,[0,1]] = X[:,:,[1,0]] # order iem and ihad to have iem on the right

        if not Z is None:
            Z = np.delete(Z, 2, axis=2) # delete iesum column (always start deleting from right columns)
            Z = Z[ Z[:,:,0] >= 29 ] # remove TTs that have iEM<=29 : 29 = (50-(50*0.12))/1.5 = (egThr-(egThr*hoeThrEB))/bigSF [this already reshapes so that every TT becomes an event]
            Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have iem on the right

            # make the rate dataset as long as the training one (usefull to batch them in the same way)
            Zdim = Z.shape[0]
            Xdim = X.shape[0]
            if Zdim < Xdim:
                times = int(Xdim / Zdim) + 1
                Z = np.repeat(Z, times, axis=0)
                Z = Z[:Xdim]

    elif version == 'HCAL' or version == 'HF':
        X = np.delete(X, 2, axis=2) # delete iesum column (always start deleting from right columns)
        if not Z is None:
            Z = Z[ np.sum(Z[:,:,2], axis=1) >= 50 ] # remove JETs that have E<=50 : 50 ~ (100/n)/1.66*n = (jetThr/nActiveTT)/bigSF*nActiveTT
            Z = np.delete(Z, 2, axis=2) # delete iesum column (always start deleting from right columns)

            # make the rate dataset as long as the training one (usefull to batch them in the same way)
            Zdim = Z.shape[0]
            Xdim = X.shape[0]
            if Zdim < Xdim:
                times = int(Xdim / Zdim) + 1
                Z = np.repeat(Z, times, axis=0)
                Z = Z[:Xdim]
        
    return X, Y, Z

def applyECALcalib(Z, TTP):
    xDim = Z.shape[0] ; yDim = 81 ; zDim = 42
    Z = Z.reshape(xDim*yDim, zDim) # reshape so that every TT becomes an event
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    TT_em_pred = TTP.predict(Z[:,1:], batch_size=2048)
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    Z[:,[0]] = TT_em_pred
    Z = Z.reshape(xDim, yDim, zDim) # reshape so that 81xTT becomes an event again
    return Z

def makePlots(HISTORY, odir):
    plt.style.use(mplhep.style.CMS)
    cmap = matplotlib.cm.get_cmap('Set1')

    plt.plot(HISTORY['x'], HISTORY['train_loss'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_loss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/loss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['train_RMSE'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_RMSE'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('RMSE')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/RootMeanSquaredError.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['train_regressionLoss'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_regressionLoss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Regression loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/regressionLoss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['train_weightsLoss'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_weightsLoss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Weights loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/weightsLoss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['train_rateLoss'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_rateLoss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Rate loss')
    plt.xlabel('Epoch')
    plt.grid()
    plt.yscale('log')
    plt.ylim(0.000475,0.0007)
    plt.subplots_adjust(left=0.17)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/rateLoss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['train_regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['train_weightsLoss'], label='Weights loss', lw=2, ls='-', marker='o', color=cmap(1))
    plt.plot(HISTORY['x'], HISTORY['train_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(2))
    plt.ylabel('Loss breakdown')
    plt.xlabel('Epoch')
    plt.grid()
    plt.yscale('log')
    plt.ylim(0.000475,1.05)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/trainLosses.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['test_regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_weightsLoss'], label='Weights loss', lw=2, ls='-', marker='o', color=cmap(1))
    plt.plot(HISTORY['x'], HISTORY['test_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(2))
    plt.ylabel('Loss breakdown')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/validLosses.pdf')
    plt.close()


##############################################################################
############################## MODEL DEFINITION ##############################
##############################################################################

# flooring custom gradient
@tf.custom_gradient
def Fgrad(x):
    def fgrad(dy):
        return dy
    return tf.floor(x), fgrad

def threshold_relaxation_sigmoid(x, mean, sharpness):
    k = sharpness * (x - mean)
    return tf.sigmoid(k, name="sigmoid")

def threshold_relaxation_inverseSigmoid(x, mean, sharpness):
    k = sharpness * (x - mean)
    return tf.sigmoid(-k, name="inverse_sigmoid")

def make_AddList(TTP, inputs, name=""):
    AdditionList = []
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,0,1:],  name=f"{name}tt{0}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,1,1:],  name=f"{name}tt{1}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,2,1:],  name=f"{name}tt{2}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,3,1:],  name=f"{name}tt{3}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,4,1:],  name=f"{name}tt{4}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,5,1:],  name=f"{name}tt{5}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,6,1:],  name=f"{name}tt{6}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,7,1:],  name=f"{name}tt{7}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,8,1:],  name=f"{name}tt{8}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,9,1:],  name=f"{name}tt{9}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,10,1:], name=f"{name}tt{10}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,11,1:], name=f"{name}tt{11}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,12,1:], name=f"{name}tt{12}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,13,1:], name=f"{name}tt{13}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,14,1:], name=f"{name}tt{14}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,15,1:], name=f"{name}tt{15}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,16,1:], name=f"{name}tt{16}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,17,1:], name=f"{name}tt{17}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,18,1:], name=f"{name}tt{18}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,19,1:], name=f"{name}tt{19}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,20,1:], name=f"{name}tt{20}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,21,1:], name=f"{name}tt{21}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,22,1:], name=f"{name}tt{22}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,23,1:], name=f"{name}tt{23}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,24,1:], name=f"{name}tt{24}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,25,1:], name=f"{name}tt{25}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,26,1:], name=f"{name}tt{26}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,27,1:], name=f"{name}tt{27}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,28,1:], name=f"{name}tt{28}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,29,1:], name=f"{name}tt{29}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,30,1:], name=f"{name}tt{30}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,31,1:], name=f"{name}tt{31}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,32,1:], name=f"{name}tt{32}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,33,1:], name=f"{name}tt{33}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,34,1:], name=f"{name}tt{34}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,35,1:], name=f"{name}tt{35}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,36,1:], name=f"{name}tt{36}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,37,1:], name=f"{name}tt{37}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,38,1:], name=f"{name}tt{38}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,39,1:], name=f"{name}tt{39}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,40,1:], name=f"{name}tt{40}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,41,1:], name=f"{name}tt{41}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,42,1:], name=f"{name}tt{42}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,43,1:], name=f"{name}tt{43}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,44,1:], name=f"{name}tt{44}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,45,1:], name=f"{name}tt{45}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,46,1:], name=f"{name}tt{46}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,47,1:], name=f"{name}tt{47}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,48,1:], name=f"{name}tt{48}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,49,1:], name=f"{name}tt{49}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,50,1:], name=f"{name}tt{50}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,51,1:], name=f"{name}tt{51}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,52,1:], name=f"{name}tt{52}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,53,1:], name=f"{name}tt{53}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,54,1:], name=f"{name}tt{54}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,55,1:], name=f"{name}tt{55}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,56,1:], name=f"{name}tt{56}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,57,1:], name=f"{name}tt{57}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,58,1:], name=f"{name}tt{58}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,59,1:], name=f"{name}tt{59}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,60,1:], name=f"{name}tt{60}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,61,1:], name=f"{name}tt{61}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,62,1:], name=f"{name}tt{62}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,63,1:], name=f"{name}tt{63}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,64,1:], name=f"{name}tt{64}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,65,1:], name=f"{name}tt{65}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,66,1:], name=f"{name}tt{66}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,67,1:], name=f"{name}tt{67}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,68,1:], name=f"{name}tt{68}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,69,1:], name=f"{name}tt{69}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,70,1:], name=f"{name}tt{70}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,71,1:], name=f"{name}tt{71}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,72,1:], name=f"{name}tt{72}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,73,1:], name=f"{name}tt{73}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,74,1:], name=f"{name}tt{74}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,75,1:], name=f"{name}tt{75}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,76,1:], name=f"{name}tt{76}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,77,1:], name=f"{name}tt{77}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,78,1:], name=f"{name}tt{78}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,79,1:], name=f"{name}tt{79}")(inputs)) )
    AdditionList.append( TTP(lay.Lambda(lambda x : x[:,80,1:], name=f"{name}tt{80}")(inputs)) )
    return AdditionList

def create_model(version, seedThr=None, jetThr=None, hoeThrEB=None, hoeThrEE=None, egThr=None):
    if version == 'ECAL' and not (hoeThrEB and hoeThrEE and egThr):
        print('** ERROR : model cannot be created without specifying: hoeThrEB, hoeThrEE, egThr')
        print('** EXITING')
        exit()
    if (version == 'HCAL' or version == 'HF') and not (seedThr and jetThr):
        print('** ERROR : model cannot be created without specifying: seedThr, jetThr')
        print('** EXITING')
        exit()

    TTP_input = keras.Input(shape=(81,42), dtype=tf.float32, name='chunky_donut')
    if version == 'ECAL':                    rate_input = keras.Input(shape=42, dtype=tf.float32, name='rate_proxy')
    if version == 'HCAL' or version == 'HF': rate_input = keras.Input(shape=(81,42), dtype=tf.float32, name='rate_proxy')
    
    layer1 = Dense(82,  name='nn1', input_dim=41, activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    layer2 = Dense(256, name='nn2',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    layer3 = Dense(1,   name='nn3',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    layer4 = lay.Lambda(Fgrad)

    TTP = Sequential(name="ttp")
    TTP.add(layer1)
    TTP.add(layer2)
    TTP.add(layer3)
    TTP.add(layer4)

    MainPredictionList = make_AddList(TTP, TTP_input)
    TTP_output = lay.Add(name="main_predicted_energy")(MainPredictionList)
    
    if version == 'ECAL':
        # 'hardcoded' threshold on hcal over ecal deposit
        hasEBthr = lay.Lambda(lambda x : tf.reduce_sum(x[:,2:30], axis=1, keepdims=True) * pow(2, -hoeThrEB), name='has_hoe_eb_thr')(rate_input)
        hasEEthr = lay.Lambda(lambda x : tf.reduce_sum(x[:,30:], axis=1, keepdims=True) * pow(2, -hoeThrEE), name='has_hoe_ee_thr')(rate_input)
        hoeThr = lay.Lambda(lambda x : x[0] + x[1], name="has_hoe_thr")((hasEBthr, hasEEthr))

        # hadronic deposit behind the ecal one
        TT_had = lay.Lambda(lambda x : x[:,0:1], name='tt_had_deposit')(rate_input)

        # # predict TT energy, add correspondong non-calibrated had part, and apply threshold
        TT_em_pred = TTP(lay.Lambda(lambda x : x[:,1:], name="tt_em_pred")(rate_input))
        TT_pred = lay.Lambda(lambda x : x[0] + x[1], name="tt_tot_energy")((TT_em_pred, TT_had))
        TT_eAT = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, egThr, 10.), name="apply_eg_threshold")(TT_pred) # sharpness 10. means +/-0.5 GeV tunron region

        # # calculate HoE for each TT and apply threshold (this is a <= threshold so need 1-sigmoid)
        TT_hoe = lay.Lambda(lambda x : tf.math.divide_no_nan(x[0], x[1]), name="compute_tt_hoe")((TT_had, TT_em_pred))
        TT_hoeAT = lay.Lambda(lambda x : threshold_relaxation_inverseSigmoid(x[0], x[1], 1000.), name="apply_hoe_threshold")((TT_hoe,hoeThr)) # sharpness 1000. means +/-0.005 tunron region

        # do logical AND between TT_eAT and TT_hoeAT
        rate_output = lay.Lambda(lambda x : x[0] * x[1], name="thresholds_or")((TT_eAT, TT_hoeAT))

    if version == 'HCAL' or version == 'HF':
        # predict seed energy (including the correspondong EM TT part) and apply threshold
        TT_seed_had_pred = TTP(lay.Lambda(lambda x : x[:,40,1:], name="seed_had_pred")(rate_input))
        TT_seed_em = lay.Lambda(lambda x : x[:,40,0:1], name='seed_em_deposit')(rate_input)
        TT_seed_pred = lay.Lambda(lambda x : x[0] + x[1], name="seed_tot_energy")((TT_seed_had_pred, TT_seed_em))
        TT_seed_AT = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, seedThr, 100.), name="apply_seed_threshold")(TT_seed_pred) # sharpness 10. means +/-0.05 GeV tunron region

        # predict jet energy (including the correspondong non-calibrated TTs part) and apply threshold
        jet_em = lay.Lambda(lambda x : tf.reduce_sum(x, axis=1, keepdims=True)[:,:,0], name='jet_em_deposit')(rate_input)
        RatePredictionList = make_AddList(TTP, rate_input, name="rate_")
        jet_had_pred = lay.Add(name="rate_predicted_energy")(RatePredictionList)
        jet_pred = lay.Lambda(lambda x : x[0] + x[1], name="jet_tot_energy")((jet_had_pred, jet_em))
        jet_AT = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, jetThr, 10.), name="apply_jet_threshold")(jet_pred) # sharpness 10. means +/-0.5 GeV tunron region
        
        # do logical AND between TT_eAT and TT_hoeAT
        rate_output = lay.Lambda(lambda x : x[0] * x[1], name="thresholds_or")((TT_seed_AT, jet_AT))

    model = keras.Model(inputs=[TTP_input, rate_input], outputs=[TTP_output, rate_output], name='Layer1Calibrator')

    return model, TTP

def step_funtion_learning_rate_schedule(batch_nmbr, max_learning_rate, stepping_frequency, residual):
    if batch_nmbr % stepping_frequency == residual: return max_learning_rate
    else:                                           return max_learning_rate / 10

if __name__ == "__main__" :
    ##############################################################################
    ################################ PARSE OPTIONS ###############################
    ##############################################################################

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",            dest="indir",            help="Input folder with X_train.npx and Y_train.npz", default=None                       )
    parser.add_option("--tag",              dest="tag",              help="Tag of the training folder",                    default=""                         )
    parser.add_option("--v",                dest="v",                help="Which training to perform: ECAL or HCAL?",      default=None                       )
    parser.add_option("--ngpus",            dest="ngpus",            help="Number of GPUs on which to distribute",         default=4,     type=int            )
    parser.add_option("--epochs",           dest="epochs",           help="Number of epochs for the training",             default=20,    type=int            )
    parser.add_option("--batch_size",       dest="batch_size",       help="Batch size for the training",                   default=2048,  type=int            )
    parser.add_option("--validation_split", dest="validation_split", help="Fraction of events to be used for testing",     default=0.20,  type=float          )
    parser.add_option("--no-verbose",       dest="verbose",          help="Deactivate verbose training",                   default=True,  action='store_false')
    parser.add_option("--readTfDatasets",   dest="readTfDatasets",   help="Do not do pre-processing and load TF datasets", default=False, action='store_true' )
    parser.add_option("--makeOnlyPlots",    dest="makeOnlyPlots",    help="Do not do the training, just make the plots",   default=False, action='store_true' )
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/model_' + options.v
    CKPTdir = odir+'/training_checkpoints'
    CKPTpf = os.path.join(CKPTdir, "ckpt")
    os.system('mkdir -p '+ odir)
    os.system('mkdir -p '+ odir+'/plots')
    os.system('mkdir -p '+ CKPTdir)

    if options.makeOnlyPlots:
        HISTORY = json.load(open(odir+'/HISTORY.json', 'r'))
        makePlots(HISTORY, odir)
        print('** INFO : made the plots, exiting')
        exit()


    ##############################################################################
    ########################### TRAINING SETUP VARIABLES #########################
    ##############################################################################

    VERBOSE = options.verbose
    VERSION = options.v
    NGPUS = options.ngpus
    BUFFER_SIZE = int(1E5)
    BATCH_SIZE_PER_REPLICA = options.batch_size
    GLOBAL_BATCH_SIZE = BATCH_SIZE_PER_REPLICA * NGPUS
    EPOCHS = options.epochs
    MAX_LEARNING_RATE = 1E-3
    HISTORY = { 'x'        : [],
                'learning_rate': [[]],
                'train_loss' : [], 'train_regressionLoss' : [], 'train_weightsLoss' : [], 'train_rateLoss' : [], 'train_RMSE' : [],
                'test_loss'  : [], 'test_regressionLoss'  : [], 'test_weightsLoss'  : [], 'test_rateLoss'  : [], 'test_RMSE'  : []
              }


    ##############################################################################
    ################################# LOAD INPUTS ################################
    ##############################################################################

    if not options.readTfDatasets:
        with tf.device('/CPU:0'):
            # read testing and training datasets
            # Inside X_vec: matrix n_ev x 81 x 43 ([81 for the chucky donut towers][43 for iem, ihad, iesum, ieta])
            # Inside Y_vec: matrx n_ev x 4 (jetPt, jetPhi, jetEta, trainingPt)
            print('** INFO : loading NumPy datasets')
            X_train = np.load(indir+'/X_train.npz')['arr_0']
            Y_train = np.load(indir+'/Y_train.npz')['arr_0']
            Z_train = np.load(indir+'/X_trainRate.npz')['arr_0']
            print('** INFO : done loading NumPy datasets')

            print('** INFO : preprocessing NumPy datasets')
            X_train, Y_train, Z_train = convert_samples(X_train, Y_train, Z_train, VERSION)
            
            # clean from the events that are completely outside of a 'regular' resposne
            uncalibResp = Y_train / np.sum(X_train[:,:,1], axis=1)
            X_train = X_train[(uncalibResp < 3) & (uncalibResp > 0.3)]
            Y_train = Y_train[(uncalibResp < 3) & (uncalibResp > 0.3)]
            del uncalibResp

            # in the case of HCAL, apply the calibration of the ECAL energy deposits so that the predicted TT sums will include that effect
            if VERSION == 'HCAL':
                ECAL_TTPmodel = keras.models.load_model('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/ECALtrainingDataReco/model_ECAL/TTP', compile=False, custom_objects={'Fgrad': Fgrad})
                Z_train = applyECALcalib(Z_train, ECAL_TTPmodel)
                del ECAL_TTPmodel
            print('** INFO : done preprocessing NumPy datasets')
            
            print('** INFO : tensorizing NumPy datasets')
            x_train, x_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=options.validation_split, random_state=7)
            del X_train, Y_train
            x_test = tf.convert_to_tensor(x_test, dtype=tf.float32)
            y_test = tf.convert_to_tensor(y_test, dtype=tf.float32)
            x_train = tf.convert_to_tensor(x_train, dtype=tf.float32)
            y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)
            z_rate = tf.convert_to_tensor(Z_train, dtype=tf.float32)
            _ = tf.convert_to_tensor(np.zeros(len(Z_train)), dtype=tf.float32)
            del Z_train
            print('** INFO : done tensorizing NumPy datasets')

            # Prepare the TensorFlow datasets
            print('** INFO : preparing TensorFlow datasets')
            train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
            test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
            rate_dataset = tf.data.Dataset.from_tensor_slices((z_rate, _))
            del x_test, y_test, x_train, y_train, z_rate, _
            print('** INFO : done preparing TensorFlow datasets')

            print('** INFO : saving TensorFlow datasets')
            tf.data.experimental.save(train_dataset, indir+'/train_TfDataset', compression='GZIP')
            tf.data.experimental.save(test_dataset, indir+'/test_TfDataset', compression='GZIP')
            tf.data.experimental.save(rate_dataset, indir+'/rate_TfDataset', compression='GZIP')
            print('** INFO : done saving TensorFlow datasets')
    else:
        print('** INFO : loading TensorFlow datasets')
        train_dataset = tf.data.experimental.load(indir+'/train_TfDataset', compression='GZIP')
        test_dataset = tf.data.experimental.load(indir+'/test_TfDataset', compression='GZIP')
        rate_dataset = tf.data.experimental.load(indir+'/rate_TfDataset', compression='GZIP')
        print('** INFO : done loading TensorFlow datasets')

    print('** INFO : batching TensorFlow datasets')
    train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    test_dataset = test_dataset.batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    rate_dataset = rate_dataset.shuffle(BUFFER_SIZE).batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    print('** INFO : done batching TensorFlow datasets')


    ##############################################################################
    ########################### GPU DISTRIBUTION SETUP ###########################
    ##############################################################################

    GPUS = [tf.config.LogicalDevice(name='/device:GPU:0', device_type='GPU'),
            tf.config.LogicalDevice(name='/device:GPU:1', device_type='GPU'),
            tf.config.LogicalDevice(name='/device:GPU:2', device_type='GPU'),
            tf.config.LogicalDevice(name='/device:GPU:3', device_type='GPU')]
    GPUS = GPUS[:NGPUS]
    mirrored_strategy = tf.distribute.MirroredStrategy(devices=GPUS, cross_device_ops=tf.distribute.NcclAllReduce())

    DISTRIBUTION_OPTS = tf.distribute.InputOptions(experimental_fetch_to_device=True,
                                                   experimental_replication_mode=tf.distribute.InputReplicationMode.PER_WORKER,
                                                   experimental_place_dataset_on_device=False,
                                                   experimental_per_replica_buffer_size=5)

    print('** INFO : distributing training datasets')
    train_dist_dataset = mirrored_strategy.experimental_distribute_dataset(train_dataset, options=DISTRIBUTION_OPTS)
    test_dist_dataset = mirrored_strategy.experimental_distribute_dataset(test_dataset, options=DISTRIBUTION_OPTS)
    rate_dist_dataset = mirrored_strategy.experimental_distribute_dataset(rate_dataset, options=DISTRIBUTION_OPTS)
    del train_dataset, test_dataset, rate_dataset
    print('** INFO : done distributing training datasets')


    ##############################################################################
    ########################## GPU DISTRIBUTED TRAINING ##########################
    ##############################################################################

    with mirrored_strategy.scope():
        # part of the loss that controls the regression of teh energy
        def regressionLoss(y, y_pred):
            MAPE = tf.keras.losses.MeanAbsolutePercentageError(reduction=tf.keras.losses.Reduction.NONE)
            return tf.reshape(MAPE(y, y_pred), (1, 1)) * 100 # FIXME: scaling to be defined

        # part of the loss that controls the weights overtraining
        def weightsLoss():
            modelWeights = model.trainable_weights
            modelWeights_ss = float( tf.math.reduce_sum(tf.math.square(modelWeights[0]), keepdims=True) +
                                     tf.math.reduce_sum(tf.math.square(modelWeights[1]), keepdims=True) +
                                     tf.math.reduce_sum(tf.math.square(modelWeights[2]), keepdims=True)
                                    )
            return  modelWeights_ss * 1 # FIXME: scaling to be optimized

        # part of the loss that controls the rate
        def rateLoss(z_pred, targetRate):
            # compute fraction of passing events and multiply by rate scaling
            proxyRate = tf.reduce_sum(z_pred, keepdims=True) / BATCH_SIZE_PER_REPLICA * 0.001*2500*11245.6
            realtive_diff = (proxyRate - targetRate) / targetRate
            return tf.cosh(1.5 * realtive_diff) * 1 # FIXME: scaling to be optimized

        # GPU distribution friendly loss computation
        def compute_losses(y, y_pred, z_pred):
            regressionLoss_value = regressionLoss(y, y_pred)
            weightsLoss_value = weightsLoss()
            
            # if VERSION == 'ECAL': rateLoss_value = rateLoss(z_pred, 3636.454)
            # if VERSION == 'HCAL': rateLoss_value = rateLoss(z_pred, 150.26064)
            # if VERSION == 'HF':   rateLoss_value = rateLoss(z_pred, 175.66269)
            
            if VERSION == 'ECAL': rateLoss_value = rateLoss(z_pred, 3756.696)
            if VERSION == 'HCAL': rateLoss_value = rateLoss(z_pred, 191.8348)

            fullLoss = regressionLoss_value + weightsLoss_value + rateLoss_value

            return [tf.nn.compute_average_loss(fullLoss,             global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(regressionLoss_value, global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(weightsLoss_value,    global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(rateLoss_value,       global_batch_size=GLOBAL_BATCH_SIZE)]

        # define model and related stuff
        if VERSION == 'ECAL':                    model, TTP = create_model(VERSION, hoeThrEB=3., hoeThrEE=4., egThr=50.)
        if VERSION == 'HCAL' or VERSION == 'HF': model, TTP = create_model(VERSION, seedThr=8., jetThr=100.)
        optimizer = keras.optimizers.Adam(learning_rate=MAX_LEARNING_RATE)
        checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
        train_acc_metric = keras.metrics.RootMeanSquaredError(name='train_accuracy')
        test_acc_metric  = keras.metrics.RootMeanSquaredError(name='test_accuracy')

    # print(model.summary())
    # exit()

    def custom_train_step(inputs, rate_inputs):
        x, y = inputs
        z, _ = rate_inputs
        with tf.GradientTape() as tape:
            y_pred, z_pred = model([x, z], training=True)
            losses = compute_losses(y, y_pred, z_pred)

        grads = tape.gradient([losses[1], losses[2], losses[3]], model.trainable_weights)
        optimizer.apply_gradients(zip(grads, model.trainable_weights))
        train_acc_metric.update_state(y, y_pred)

        return losses

    def custom_test_step(inputs, rate_inputs):
        x, y = inputs
        z, _ = rate_inputs
        y_pred, z_pred = model([x, z], training=False)
        losses = compute_losses(y, y_pred, z_pred)
        test_acc_metric.update_state(y, y_pred)

        return losses

    @tf.function
    def distributed_train_step(dataset_inputs, rate_inputs):
        per_replica_losses = mirrored_strategy.run(custom_train_step, args=(dataset_inputs, rate_inputs,))
        return [mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[0], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[1], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[2], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[3], axis=None)]

    @tf.function
    def distributed_test_step(dataset_inputs, rate_inputs):
        per_replica_losses = mirrored_strategy.run(custom_test_step, args=(dataset_inputs, rate_inputs,))
        return [mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[0], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[1], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[2], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[3], axis=None)]


    # run training loop
    for epoch in range(EPOCHS):
        start_time = time.time()
        print('\nStart of epoch %d' % (epoch+1,))

        # TRAIN LOOP
        train_losses = np.array([0., 0., 0., 0.])
        train_losses_avg = np.array([0., 0., 0., 0.])
        num_batches = 0
        for batch, rate_batch in zip(train_dist_dataset, rate_dist_dataset):
            train_losses = distributed_train_step(batch, rate_batch)
            train_losses_avg += train_losses
            num_batches += 1

            # Log every N batches
            if VERBOSE and num_batches % 1 == 0:
                print(
                      '    At batch %d (seen %d samples so far) : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f'
                      %
                      (num_batches, num_batches*GLOBAL_BATCH_SIZE, float(train_losses[0]), float(train_losses[1]), float(train_losses[2]), float(train_losses[3]), float(train_acc_metric.result()))
                     )

        train_losses_avg = train_losses_avg / num_batches

        # TEST LOOP
        test_losses = np.array([0., 0., 0., 0.])
        num_batches = 0
        for batch, rate_batch in zip(test_dist_dataset, rate_dist_dataset):
            test_losses += distributed_test_step(batch, rate_batch)
            num_batches += 1

        test_losses = test_losses / num_batches

        train_RMSE = train_acc_metric.result()
        test_RMSE = test_acc_metric.result()
        print('Training : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(train_losses_avg[0]), float(train_losses_avg[1]), float(train_losses_avg[2]), float(train_losses_avg[3]), float(train_RMSE)) )
        print('Testing  : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(test_losses[0]), float(test_losses[1]), float(test_losses[2]), float(test_losses[3]), float(test_RMSE)) )

        HISTORY['x'].append(epoch+1)
        if epoch < EPOCHS-1: HISTORY['learning_rate'].append([])
        HISTORY['train_loss'].append(float(train_losses_avg[0]))
        HISTORY['train_regressionLoss'].append(float(train_losses_avg[1]))
        HISTORY['train_weightsLoss'].append(float(train_losses_avg[2]))
        HISTORY['train_rateLoss'].append(float(train_losses_avg[3]))
        HISTORY['train_RMSE'].append(float(train_RMSE))
        HISTORY['test_loss'].append(float(test_losses[0]))
        HISTORY['test_regressionLoss'].append(float(test_losses[1]))
        HISTORY['test_weightsLoss'].append(float(test_losses[2]))
        HISTORY['test_rateLoss'].append(float(train_losses[3]))
        HISTORY['test_RMSE'].append(float(test_RMSE))

        # Reset metrics at the end of each epoch
        train_acc_metric.reset_states()
        test_acc_metric.reset_states()

        # save checkpoint
        checkpoint.save(CKPTpf)

        print('Time taken: %.2fs' % (time.time() - start_time))

    model.save(odir + '/model')
    TTP.save(odir + '/TTP')
    print('\nTrained model saved to folder: {}'.format(odir))


    json.dump(HISTORY, open(odir+'/HISTORY.json', 'w'))
    print('Training history saved to file: {}/HISTORY.json'.format(odir))

    makePlots(HISTORY, odir)
    
    
