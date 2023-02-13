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

        if not Z is None:
            Z = np.delete(Z, 2, axis=2)
            Z = Z[ Z[:,:,0] >= 29 ] # remove TTs that have iEM<=29 : 29 = (50-(50*0.12))/1.5 = (egThr-(egThr*hoeThrEB))/bigSF [this already reshapes so that every TT becomes an event]

            # make the rate dataset as long as the training one (usefull to batch them in the same way)
            Zdim = Z.shape[0]
            Xdim = X.shape[0]
            if Zdim < Xdim:
                times = int(Xdim / Zdim) + 1
                Z = np.repeat(Z, times, axis=0)
                Z = Z[:Xdim]

    elif version == 'HCAL':
        X = np.delete(X, 2, axis=2)
        if not Z is None:
            Z = Z[ np.sum(Z[:,:,2], axis=1) >= 50 ] # remove JETs that have E<=50 : 50 ~ (100/n)/1.66*n = (jetThr/nActiveTT)/bigSF*nActiveTT
            Z = np.delete(Z, 2, axis=2)

            # make the rate dataset as long as the training one (usefull to batch them in the same way)
            Zdim = Z.shape[0]
            Xdim = X.shape[0]
            if Zdim < Xdim:
                times = int(Xdim / Zdim) + 1
                Z = np.repeat(Z, times, axis=0)
                Z = Z[:Xdim]
        
    return X, Y, Z

def makePlots(HISTORY, odir):
    plt.style.use(mplhep.style.CMS)
    # cmap = matplotlib.cm.get_cmap('Set1')
    cmap = matplotlib.cm.get_cmap('tab20c')

    plt.plot(HISTORY['x'], HISTORY['ecal_train_loss'], label='ECAL Taining', lw=2, ls='-', marker='o', color=cmap(4))
    plt.plot(HISTORY['x'], HISTORY['ecal_test_loss'], label='ECAL Testing', lw=2, ls='--', marker='o', color=cmap(5))
    plt.plot(HISTORY['x'], HISTORY['hcal_train_loss'], label='HCAL Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['hcal_test_loss'], label='HCAL Testing', lw=2, ls='--', marker='o', color=cmap(1))
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    # plt.yscale('log')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/loss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['ecal_train_RMSE'], label='ECAL Taining', lw=2, ls='-', marker='o', color=cmap(4))
    plt.plot(HISTORY['x'], HISTORY['ecal_test_RMSE'], label='ECAL Testing', lw=2, ls='--', marker='o', color=cmap(5))
    plt.plot(HISTORY['x'], HISTORY['hcal_train_RMSE'], label='HCAL Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['hcal_test_RMSE'], label='HCAL Testing', lw=2, ls='--', marker='o', color=cmap(1))
    plt.ylabel('RMSE')
    plt.xlabel('Epoch')
    # plt.yscale('log')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/RootMeanSquaredError.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['ecal_train_regressionLoss'], label='ECAL Taining', lw=2, ls='-', marker='o', color=cmap(4))
    # plt.plot(HISTORY['x'], HISTORY['ecal_test_regressionLoss'], label='ECAL Testing', lw=2, ls='--', marker='o', color=cmap(5))
    plt.plot(HISTORY['x'], HISTORY['hcal_train_regressionLoss'], label='HCAL Taining', lw=2, ls='-', marker='o', color=cmap(0))
    # plt.plot(HISTORY['x'], HISTORY['hcal_test_regressionLoss'], label='HCAL Testing', lw=2, ls='--', marker='o', color=cmap(1))
    plt.ylabel('Regression loss')
    plt.xlabel('Epoch')
    # plt.yscale('log')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/regressionLoss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['ecal_train_weightsLoss'], label='ECAL Taining', lw=2, ls='-', marker='o', color=cmap(4))
    # plt.plot(HISTORY['x'], HISTORY['ecal_test_weightsLoss'], label='ECAL Testing', lw=2, ls='--', marker='o', color=cmap(5))
    plt.plot(HISTORY['x'], HISTORY['hcal_train_weightsLoss'], label='HCAL Taining', lw=2, ls='-', marker='o', color=cmap(0))
    # plt.plot(HISTORY['x'], HISTORY['hcal_test_weightsLoss'], label='HCAL Testing', lw=2, ls='--', marker='o', color=cmap(1))
    plt.ylabel('Weights loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='lower left', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/weightsLoss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['ecal_train_rateLoss'], label='ECAL Taining', lw=2, ls='-', marker='o', color=cmap(4))
    plt.plot(HISTORY['x'], HISTORY['ecal_test_rateLoss'], label='ECAL Testing', lw=2, ls='--', marker='o', color=cmap(5))
    plt.plot(HISTORY['x'], HISTORY['hcal_train_rateLoss'], label='HCAL Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['hcal_test_rateLoss'], label='HCAL Testing', lw=2, ls='--', marker='o', color=cmap(1))
    plt.ylabel('Rate loss')
    plt.xlabel('Epoch')
    plt.grid()
    plt.yscale('log')
    # plt.ylim(0.000475,0.0007)
    plt.subplots_adjust(left=0.17)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/rateLoss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['ecal_train_regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(8))
    plt.plot(HISTORY['x'], HISTORY['ecal_train_weightsLoss'], label='Weights loss', lw=2, ls='-', marker='o', color=cmap(12))
    plt.plot(HISTORY['x'], HISTORY['ecal_train_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(16))
    plt.ylabel('Loss breakdown')
    plt.xlabel('Epoch')
    plt.grid()
    plt.yscale('log')
    # plt.ylim(0.000475,1.05)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/trainLosses_ecal.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['hcal_train_regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(8))
    plt.plot(HISTORY['x'], HISTORY['hcal_train_weightsLoss'], label='Weights loss', lw=2, ls='-', marker='o', color=cmap(12))
    plt.plot(HISTORY['x'], HISTORY['hcal_train_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(16))
    plt.ylabel('Loss breakdown')
    plt.xlabel('Epoch')
    plt.grid()
    plt.yscale('log')
    # plt.ylim(0.000475,1.05)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/trainLosses_hcal.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['ecal_test_regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(8))
    plt.plot(HISTORY['x'], HISTORY['ecal_test_weightsLoss'], label='Weights loss', lw=2, ls='-', marker='o', color=cmap(12))
    plt.plot(HISTORY['x'], HISTORY['ecal_test_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(16))
    plt.ylabel('Loss breakdown')
    plt.xlabel('Epoch')
    plt.yscale('log')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/validLosses_ecal.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['hcal_test_regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(8))
    plt.plot(HISTORY['x'], HISTORY['hcal_test_weightsLoss'], label='Weights loss', lw=2, ls='-', marker='o', color=cmap(12))
    plt.plot(HISTORY['x'], HISTORY['hcal_test_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(16))
    plt.ylabel('Loss breakdown')
    plt.xlabel('Epoch')
    plt.yscale('log')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/validLosses_hcal.pdf')
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

def make_AddList(TTP_ecal, TTP_hcal, inputs_ecal, inputs_hcal, name=""):
    AdditionList = []
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,0,:],  name=f"{name}_ecal_tt{0}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,1,:],  name=f"{name}_ecal_tt{1}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,2,:],  name=f"{name}_ecal_tt{2}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,3,:],  name=f"{name}_ecal_tt{3}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,4,:],  name=f"{name}_ecal_tt{4}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,5,:],  name=f"{name}_ecal_tt{5}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,6,:],  name=f"{name}_ecal_tt{6}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,7,:],  name=f"{name}_ecal_tt{7}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,8,:],  name=f"{name}_ecal_tt{8}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,9,:],  name=f"{name}_ecal_tt{9}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,10,:], name=f"{name}_ecal_tt{10}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,11,:], name=f"{name}_ecal_tt{11}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,12,:], name=f"{name}_ecal_tt{12}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,13,:], name=f"{name}_ecal_tt{13}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,14,:], name=f"{name}_ecal_tt{14}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,15,:], name=f"{name}_ecal_tt{15}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,16,:], name=f"{name}_ecal_tt{16}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,17,:], name=f"{name}_ecal_tt{17}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,18,:], name=f"{name}_ecal_tt{18}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,19,:], name=f"{name}_ecal_tt{19}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,20,:], name=f"{name}_ecal_tt{20}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,21,:], name=f"{name}_ecal_tt{21}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,22,:], name=f"{name}_ecal_tt{22}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,23,:], name=f"{name}_ecal_tt{23}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,24,:], name=f"{name}_ecal_tt{24}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,25,:], name=f"{name}_ecal_tt{25}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,26,:], name=f"{name}_ecal_tt{26}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,27,:], name=f"{name}_ecal_tt{27}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,28,:], name=f"{name}_ecal_tt{28}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,29,:], name=f"{name}_ecal_tt{29}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,30,:], name=f"{name}_ecal_tt{30}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,31,:], name=f"{name}_ecal_tt{31}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,32,:], name=f"{name}_ecal_tt{32}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,33,:], name=f"{name}_ecal_tt{33}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,34,:], name=f"{name}_ecal_tt{34}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,35,:], name=f"{name}_ecal_tt{35}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,36,:], name=f"{name}_ecal_tt{36}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,37,:], name=f"{name}_ecal_tt{37}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,38,:], name=f"{name}_ecal_tt{38}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,39,:], name=f"{name}_ecal_tt{39}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,40,:], name=f"{name}_ecal_tt{40}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,41,:], name=f"{name}_ecal_tt{41}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,42,:], name=f"{name}_ecal_tt{42}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,43,:], name=f"{name}_ecal_tt{43}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,44,:], name=f"{name}_ecal_tt{44}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,45,:], name=f"{name}_ecal_tt{45}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,46,:], name=f"{name}_ecal_tt{46}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,47,:], name=f"{name}_ecal_tt{47}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,48,:], name=f"{name}_ecal_tt{48}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,49,:], name=f"{name}_ecal_tt{49}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,50,:], name=f"{name}_ecal_tt{50}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,51,:], name=f"{name}_ecal_tt{51}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,52,:], name=f"{name}_ecal_tt{52}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,53,:], name=f"{name}_ecal_tt{53}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,54,:], name=f"{name}_ecal_tt{54}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,55,:], name=f"{name}_ecal_tt{55}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,56,:], name=f"{name}_ecal_tt{56}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,57,:], name=f"{name}_ecal_tt{57}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,58,:], name=f"{name}_ecal_tt{58}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,59,:], name=f"{name}_ecal_tt{59}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,60,:], name=f"{name}_ecal_tt{60}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,61,:], name=f"{name}_ecal_tt{61}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,62,:], name=f"{name}_ecal_tt{62}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,63,:], name=f"{name}_ecal_tt{63}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,64,:], name=f"{name}_ecal_tt{64}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,65,:], name=f"{name}_ecal_tt{65}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,66,:], name=f"{name}_ecal_tt{66}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,67,:], name=f"{name}_ecal_tt{67}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,68,:], name=f"{name}_ecal_tt{68}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,69,:], name=f"{name}_ecal_tt{69}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,70,:], name=f"{name}_ecal_tt{70}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,71,:], name=f"{name}_ecal_tt{71}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,72,:], name=f"{name}_ecal_tt{72}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,73,:], name=f"{name}_ecal_tt{73}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,74,:], name=f"{name}_ecal_tt{74}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,75,:], name=f"{name}_ecal_tt{75}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,76,:], name=f"{name}_ecal_tt{76}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,77,:], name=f"{name}_ecal_tt{77}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,78,:], name=f"{name}_ecal_tt{78}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,79,:], name=f"{name}_ecal_tt{79}")(inputs_ecal)) )
    AdditionList.append( TTP_ecal(lay.Lambda(lambda x : x[:,80,:], name=f"{name}_ecal_tt{80}")(inputs_ecal)) )

    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,0,:],  name=f"{name}_hcal_tt{0}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,1,:],  name=f"{name}_hcal_tt{1}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,2,:],  name=f"{name}_hcal_tt{2}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,3,:],  name=f"{name}_hcal_tt{3}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,4,:],  name=f"{name}_hcal_tt{4}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,5,:],  name=f"{name}_hcal_tt{5}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,6,:],  name=f"{name}_hcal_tt{6}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,7,:],  name=f"{name}_hcal_tt{7}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,8,:],  name=f"{name}_hcal_tt{8}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,9,:],  name=f"{name}_hcal_tt{9}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,10,:], name=f"{name}_hcal_tt{10}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,11,:], name=f"{name}_hcal_tt{11}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,12,:], name=f"{name}_hcal_tt{12}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,13,:], name=f"{name}_hcal_tt{13}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,14,:], name=f"{name}_hcal_tt{14}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,15,:], name=f"{name}_hcal_tt{15}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,16,:], name=f"{name}_hcal_tt{16}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,17,:], name=f"{name}_hcal_tt{17}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,18,:], name=f"{name}_hcal_tt{18}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,19,:], name=f"{name}_hcal_tt{19}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,20,:], name=f"{name}_hcal_tt{20}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,21,:], name=f"{name}_hcal_tt{21}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,22,:], name=f"{name}_hcal_tt{22}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,23,:], name=f"{name}_hcal_tt{23}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,24,:], name=f"{name}_hcal_tt{24}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,25,:], name=f"{name}_hcal_tt{25}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,26,:], name=f"{name}_hcal_tt{26}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,27,:], name=f"{name}_hcal_tt{27}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,28,:], name=f"{name}_hcal_tt{28}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,29,:], name=f"{name}_hcal_tt{29}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,30,:], name=f"{name}_hcal_tt{30}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,31,:], name=f"{name}_hcal_tt{31}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,32,:], name=f"{name}_hcal_tt{32}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,33,:], name=f"{name}_hcal_tt{33}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,34,:], name=f"{name}_hcal_tt{34}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,35,:], name=f"{name}_hcal_tt{35}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,36,:], name=f"{name}_hcal_tt{36}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,37,:], name=f"{name}_hcal_tt{37}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,38,:], name=f"{name}_hcal_tt{38}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,39,:], name=f"{name}_hcal_tt{39}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,40,:], name=f"{name}_hcal_tt{40}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,41,:], name=f"{name}_hcal_tt{41}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,42,:], name=f"{name}_hcal_tt{42}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,43,:], name=f"{name}_hcal_tt{43}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,44,:], name=f"{name}_hcal_tt{44}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,45,:], name=f"{name}_hcal_tt{45}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,46,:], name=f"{name}_hcal_tt{46}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,47,:], name=f"{name}_hcal_tt{47}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,48,:], name=f"{name}_hcal_tt{48}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,49,:], name=f"{name}_hcal_tt{49}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,50,:], name=f"{name}_hcal_tt{50}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,51,:], name=f"{name}_hcal_tt{51}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,52,:], name=f"{name}_hcal_tt{52}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,53,:], name=f"{name}_hcal_tt{53}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,54,:], name=f"{name}_hcal_tt{54}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,55,:], name=f"{name}_hcal_tt{55}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,56,:], name=f"{name}_hcal_tt{56}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,57,:], name=f"{name}_hcal_tt{57}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,58,:], name=f"{name}_hcal_tt{58}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,59,:], name=f"{name}_hcal_tt{59}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,60,:], name=f"{name}_hcal_tt{60}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,61,:], name=f"{name}_hcal_tt{61}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,62,:], name=f"{name}_hcal_tt{62}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,63,:], name=f"{name}_hcal_tt{63}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,64,:], name=f"{name}_hcal_tt{64}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,65,:], name=f"{name}_hcal_tt{65}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,66,:], name=f"{name}_hcal_tt{66}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,67,:], name=f"{name}_hcal_tt{67}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,68,:], name=f"{name}_hcal_tt{68}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,69,:], name=f"{name}_hcal_tt{69}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,70,:], name=f"{name}_hcal_tt{70}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,71,:], name=f"{name}_hcal_tt{71}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,72,:], name=f"{name}_hcal_tt{72}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,73,:], name=f"{name}_hcal_tt{73}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,74,:], name=f"{name}_hcal_tt{74}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,75,:], name=f"{name}_hcal_tt{75}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,76,:], name=f"{name}_hcal_tt{76}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,77,:], name=f"{name}_hcal_tt{77}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,78,:], name=f"{name}_hcal_tt{78}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,79,:], name=f"{name}_hcal_tt{79}")(inputs_hcal)) )
    AdditionList.append( TTP_hcal(lay.Lambda(lambda x : x[:,80,:], name=f"{name}_hcal_tt{80}")(inputs_hcal)) )

    return AdditionList

def create_model(seedThr=None, jetThr=None, hoeThrEB=None, hoeThrEE=None, egThr=None):
    if not (hoeThrEB and hoeThrEE and egThr):
        print('** ERROR : model cannot be created without specifying: hoeThrEB, hoeThrEE, egThr, seedThr, jetThr')
        print('** EXITING')
        exit()

    TTP_input_ecal  = keras.Input(shape=(81,42), dtype=tf.float32, name='chunky_donut_ecal')
    TTP_input_hcal = keras.Input(shape=(81,42), dtype=tf.float32, name='chunky_donut_hcal')
    rate_input_ecal = keras.Input(shape=42, dtype=tf.float32, name='rate_proxy_ecal')
    rate_input_hcal = keras.Input(shape=(81,42), dtype=tf.float32, name='rate_proxy_hcal')

    gather_ecal = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    gather_hcal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    TTP_input_ecal_em  = lay.Lambda(lambda x : tf.gather(x, gather_ecal, axis=2), name="gather_eg_ecal")(TTP_input_ecal)
    TTP_input_ecal_had = lay.Lambda(lambda x : tf.gather(x, gather_hcal, axis=2), name="gather_eg_hcal")(TTP_input_ecal)
    TTP_input_hcal_em  = lay.Lambda(lambda x : tf.gather(x, gather_ecal, axis=2), name="gather_jet_ecal")(TTP_input_hcal)
    TTP_input_hcal_had = lay.Lambda(lambda x : tf.gather(x, gather_hcal, axis=2), name="gather_jet_hcal")(TTP_input_hcal)
    
    ecal_layer1 = Dense(82,  name='ecal_nn1', input_dim=41, activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    ecal_layer2 = Dense(256, name='ecal_nn2',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    ecal_layer3 = Dense(1,   name='ecal_nn3',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    ecal_layer4 = lay.Lambda(Fgrad)

    hcal_layer1 = Dense(82,  name='hcal_nn1', input_dim=41, activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    hcal_layer2 = Dense(256, name='hcal_nn2',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    hcal_layer3 = Dense(1,   name='hcal_nn3',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    hcal_layer4 = lay.Lambda(Fgrad)

    TTP_ecal = Sequential(name="ttp_ecal")
    TTP_ecal.add(ecal_layer1)
    TTP_ecal.add(ecal_layer2)
    TTP_ecal.add(ecal_layer3)
    TTP_ecal.add(ecal_layer4)

    TTP_hcal = Sequential(name="ttp_hcal")
    TTP_hcal.add(hcal_layer1)
    TTP_hcal.add(hcal_layer2)
    TTP_hcal.add(hcal_layer3)
    TTP_hcal.add(hcal_layer4)

    PredictionList_ecal = make_AddList(TTP_ecal, TTP_hcal, TTP_input_ecal_em, TTP_input_ecal_had, name="eg")
    PredictionList_hcal = make_AddList(TTP_ecal, TTP_hcal, TTP_input_hcal_em, TTP_input_hcal_had, name="jet")

    TTP_output_ecal = lay.Add(name="ecal_predicted")(PredictionList_ecal)
    TTP_output_hcal = lay.Add(name="hcal_predicted")(PredictionList_hcal)
    
    ## ECAL EG RATE PROXY
    rate_input_ecal_em  = lay.Lambda(lambda x : tf.gather(x, gather_ecal, axis=1), name="gather_rate_eg_ecal")(rate_input_ecal)
    rate_input_ecal_had = lay.Lambda(lambda x : tf.gather(x, gather_hcal, axis=1), name="gather_rate_eg_hcal")(rate_input_ecal)
    # 'hardcoded' threshold on hcal over ecal deposit
    hasEBthr = lay.Lambda(lambda x : tf.reduce_sum(x[:,2:30], axis=1, keepdims=True) * pow(2, -hoeThrEB), name='has_hoe_eb_thr')(rate_input_ecal)
    hasEEthr = lay.Lambda(lambda x : tf.reduce_sum(x[:,30:], axis=1, keepdims=True) * pow(2, -hoeThrEE), name='has_hoe_ee_thr')(rate_input_ecal)
    hoeThr = lay.Lambda(lambda x : x[0] + x[1], name="has_hoe_thr")((hasEBthr, hasEEthr))
    # predict TT energy and apply threshold
    TT_em_pred = TTP_ecal(lay.Lambda(lambda x : x[:], name="tt_em_pred")(rate_input_ecal_em))
    TT_had_pred = TTP_hcal(lay.Lambda(lambda x : x[:], name='tt_had_pred')(rate_input_ecal_had))
    TT_pred = lay.Lambda(lambda x : x[0] + x[1], name="tt_tot_energy")((TT_em_pred, TT_had_pred))
    TT_eAT = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, egThr, 10.), name="apply_eg_threshold")(TT_pred) # sharpness 10. means +/-0.5 GeV tunron region
    # calculate HoE for each TT and apply threshold (this is a <= threshold so need 1-sigmoid)
    TT_hoe = lay.Lambda(lambda x : tf.math.divide_no_nan(x[0], x[1]), name="compute_tt_hoe")((TT_had_pred, TT_em_pred))
    TT_hoeAT = lay.Lambda(lambda x : threshold_relaxation_inverseSigmoid(x[0], x[1], 1000.), name="apply_hoe_threshold")((TT_hoe,hoeThr)) # sharpness 1000. means +/-0.005 tunron region
    # do logical AND between TT_eAT and TT_hoeAT
    rate_output_ecal = lay.Lambda(lambda x : x[0] * x[1], name="ecal_thresholds_or")((TT_eAT, TT_hoeAT))

    ## HCAL JET RATE PROXY
    rate_input_hcal_em  = lay.Lambda(lambda x : tf.gather(x, gather_ecal, axis=2), name="gather_rate_jet_ecal")(rate_input_hcal)
    rate_input_hcal_had = lay.Lambda(lambda x : tf.gather(x, gather_hcal, axis=2), name="gather_rate_jet_hcal")(rate_input_hcal)
    # predict seed energy (including the correspondong non-calibrated TT part) and apply threshold
    TT_seed_had_pred = TTP_hcal(lay.Lambda(lambda x : x[:,40,:], name="seed_had_pred")(rate_input_hcal_em))
    TT_seed_em_pred = TTP_ecal(lay.Lambda(lambda x : x[:,40,:], name='seed_em_pred')(rate_input_hcal_had))
    TT_seed_pred = lay.Lambda(lambda x : x[0] + x[1], name="seed_tot_energy")((TT_seed_had_pred, TT_seed_em_pred))
    TT_seed_AT = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, seedThr, 100.), name="apply_seed_threshold")(TT_seed_pred) # sharpness 10. means +/-0.05 GeV tunron region
    # predict jet energy (including the correspondong non-calibrated TTs part) and apply threshold
    RatePredictionList = make_AddList(TTP_ecal, TTP_hcal, rate_input_hcal_em, rate_input_hcal_had, name="rate")
    jet_pred = lay.Add(name="rate_predicted_energy")(RatePredictionList)
    jet_AT = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, jetThr, 10.), name="apply_jet_threshold")(jet_pred) # sharpness 10. means +/-0.5 GeV tunron region
    # do logical AND between TT_eAT and TT_hoeAT
    rate_output_hcal = lay.Lambda(lambda x : x[0] * x[1], name="hcal_thresholds_or")((TT_seed_AT, jet_AT))

    model = keras.Model(inputs=[TTP_input_ecal, TTP_input_hcal, rate_input_ecal, rate_input_hcal], outputs=[TTP_output_ecal, TTP_output_hcal, rate_output_ecal, rate_output_hcal], name='Layer1Calibrator')

    return model, TTP_ecal, TTP_hcal


if __name__ == "__main__" :
    ##############################################################################
    ################################ PARSE OPTIONS ###############################
    ##############################################################################

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",            dest="indir",            help="Input folder with X_train.npx and Y_train.npz", default=None                       )
    parser.add_option("--tag",              dest="tag",              help="Tag of the training folder",                    default=""                         )
    parser.add_option("--v",                dest="v",                help="Which training to perform: ECAL or HCAL?",      default=None                       )
    parser.add_option("--ngpus",            dest="ngpus",            help="Number of GPUs on which to distribute",         default=2,     type=int            )
    parser.add_option("--epochs",           dest="epochs",           help="Number of epochs for the training",             default=20,    type=int            )
    parser.add_option("--batch_size",       dest="batch_size",       help="Batch size for the training",                   default=1024,  type=int            )
    parser.add_option("--validation_split", dest="validation_split", help="Fraction of events to be used for testing",     default=0.25,  type=float          )
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
    NGPUS = options.ngpus
    BUFFER_SIZE = int(1E5)
    BATCH_SIZE_PER_REPLICA = options.batch_size
    GLOBAL_BATCH_SIZE = BATCH_SIZE_PER_REPLICA * NGPUS
    EPOCHS = options.epochs
    MAX_LEARNING_RATE = 1E-3
    HISTORY = { 'x'        : [],
                'learning_rate': [[]],
                'ecal_train_loss' : [], 'ecal_train_regressionLoss' : [], 'ecal_train_weightsLoss' : [], 'ecal_train_rateLoss' : [], 'ecal_train_RMSE' : [],
                'ecal_test_loss'  : [], 'ecal_test_regressionLoss'  : [], 'ecal_test_weightsLoss'  : [], 'ecal_test_rateLoss'  : [], 'ecal_test_RMSE'  : [],
                'hcal_train_loss' : [], 'hcal_train_regressionLoss' : [], 'hcal_train_weightsLoss' : [], 'hcal_train_rateLoss' : [], 'hcal_train_RMSE' : [],
                'hcal_test_loss'  : [], 'hcal_test_regressionLoss'  : [], 'hcal_test_weightsLoss'  : [], 'hcal_test_rateLoss'  : [], 'hcal_test_RMSE'  : []
              }


    ##############################################################################
    ################################# LOAD INPUTS ################################
    ##############################################################################

    if not options.readTfDatasets:
        with tf.device('/CPU:0'):
            # read testing and training datasets for ECAL
            # Inside X_vec: matrix n_ev x 81 x 43 ([81 for the chucky donut towers][43 for iem, ihad, iesum, ieta])
            # Inside Y_vec: matrx n_ev x 4 (jetPt, jetPhi, jetEta, trainingPt)
            print('** INFO : loading ECAL NumPy datasets')
            X_train_ecal = np.load(indir+'/X_ecal_train.npz')['arr_0']
            Y_train_ecal = np.load(indir+'/Y_ecal_train.npz')['arr_0']
            Z_train = np.load('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/NUtraining_rateProxy/X_train.npz')['arr_0']
            print('** INFO : done loading ECAL NumPy datasets')

            print('** INFO : preprocessing ECAL NumPy datasets')
            X_train_ecal, Y_train_ecal, Z_train_ecal = convert_samples(X_train_ecal, Y_train_ecal, Z_train, "ECAL")
            
            # clean from the events that are completely outside of a 'regular' resposne
            uncalibResp = Y_train_ecal / np.sum(X_train_ecal[:,:,0], axis=1)
            X_train_ecal = X_train_ecal[(uncalibResp < 3) & (uncalibResp > 0.3)]
            Y_train_ecal = Y_train_ecal[(uncalibResp < 3) & (uncalibResp > 0.3)]
            del uncalibResp
            print('** INFO : done preprocessing ECAL NumPy datasets')
            
            print('** INFO : tensorizing ECAL NumPy datasets')
            x_train_ecal, x_test_ecal, y_train_ecal, y_test_ecal = train_test_split(X_train_ecal, Y_train_ecal, test_size=options.validation_split, random_state=7)
            del X_train_ecal, Y_train_ecal
            x_test_ecal = tf.convert_to_tensor(x_test_ecal, dtype=tf.float32)
            y_test_ecal = tf.convert_to_tensor(y_test_ecal, dtype=tf.float32)
            x_train_ecal = tf.convert_to_tensor(x_train_ecal, dtype=tf.float32)
            y_train_ecal = tf.convert_to_tensor(y_train_ecal, dtype=tf.float32)
            z_rate_ecal = tf.convert_to_tensor(Z_train_ecal, dtype=tf.float32)
            _ = tf.convert_to_tensor(np.zeros(len(Z_train_ecal)), dtype=tf.float32)
            print('** INFO : done tensorizing ECAL NumPy datasets')

            # Prepare the TensorFlow datasets
            print('** INFO : preparing ECAL TensorFlow datasets')
            train_dataset_ecal = tf.data.Dataset.from_tensor_slices((x_train_ecal, y_train_ecal))
            test_dataset_ecal = tf.data.Dataset.from_tensor_slices((x_test_ecal, y_test_ecal))
            rate_dataset_ecal = tf.data.Dataset.from_tensor_slices((z_rate_ecal, _))
            del x_test_ecal, y_test_ecal, x_train_ecal, y_train_ecal, z_rate_ecal, _
            print('** INFO : done preparing ECAL TensorFlow datasets')

            print('** INFO : saving ECAL TensorFlow datasets')
            tf.data.experimental.save(train_dataset_ecal, indir+'/train_ecal_TfDataset', compression='GZIP')
            tf.data.experimental.save(test_dataset_ecal, indir+'/test_ecal_TfDataset', compression='GZIP')
            tf.data.experimental.save(rate_dataset_ecal, indir+'/rate_ecal_TfDataset', compression='GZIP')
            print('** INFO : done saving ECAL TensorFlow datasets')

            # read testing and training datasets for HCAL
            # Inside X_vec: matrix n_ev x 81 x 43 ([81 for the chucky donut towers][43 for iem, ihad, iesum, ieta])
            # Inside Y_vec: matrx n_ev x 4 (jetPt, jetPhi, jetEta, trainingPt)
            print('** INFO : loading HCAL NumPy datasets')
            X_train_hcal = np.load(indir+'/X_hcal_train.npz')['arr_0']
            Y_train_hcal = np.load(indir+'/Y_hcal_train.npz')['arr_0']
            Z_train = np.load('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/NUtraining_rateProxy/X_train.npz')['arr_0']
            print('** INFO : done loading HCAL NumPy datasets')

            print('** INFO : preprocessing HCAL NumPy datasets')
            X_train_hcal, Y_train_hcal, Z_train_hcal = convert_samples(X_train_hcal, Y_train_hcal, Z_train, "HCAL")
            del Z_train

            # clean from the events that are completely outside of a 'regular' resposne
            uncalibResp = Y_train_hcal / np.sum(X_train_hcal[:,:,1], axis=1)
            X_train_hcal = X_train_hcal[(uncalibResp < 3) & (uncalibResp > 0.3)]
            Y_train_hcal = Y_train_hcal[(uncalibResp < 3) & (uncalibResp > 0.3)]
            del uncalibResp
            print('** INFO : done preprocessing HCAL NumPy datasets')

            print('** INFO : tensorizing HCAL NumPy datasets')
            x_train_hcal, x_test_hcal, y_train_hcal, y_test_hcal = train_test_split(X_train_hcal, Y_train_hcal, test_size=options.validation_split, random_state=7)
            del X_train_hcal, Y_train_hcal
            x_test_hcal = tf.convert_to_tensor(x_test_hcal, dtype=tf.float32)
            y_test_hcal = tf.convert_to_tensor(y_test_hcal, dtype=tf.float32)
            x_train_hcal = tf.convert_to_tensor(x_train_hcal, dtype=tf.float32)
            y_train_hcal = tf.convert_to_tensor(y_train_hcal, dtype=tf.float32)
            z_rate_hcal = tf.convert_to_tensor(Z_train_hcal, dtype=tf.float32)
            _ = tf.convert_to_tensor(np.zeros(len(Z_train_hcal)), dtype=tf.float32)
            print('** INFO : done tensorizing HCAL NumPy datasets')

            # Prepare the TensorFlow datasets
            print('** INFO : preparing HCAL TensorFlow datasets')
            train_dataset_hcal = tf.data.Dataset.from_tensor_slices((x_train_hcal, y_train_hcal))
            test_dataset_hcal = tf.data.Dataset.from_tensor_slices((x_test_hcal, y_test_hcal))
            rate_dataset_hcal = tf.data.Dataset.from_tensor_slices((z_rate_hcal, _))
            del x_test_hcal, y_test_hcal, x_train_hcal, y_train_hcal, z_rate_hcal, _
            print('** INFO : done preparing HCAL TensorFlow datasets')

            print('** INFO : saving HCAL TensorFlow datasets')
            tf.data.experimental.save(train_dataset_hcal, indir+'/train_hcal_TfDataset', compression='GZIP')
            tf.data.experimental.save(test_dataset_hcal, indir+'/test_hcal_TfDataset', compression='GZIP')
            tf.data.experimental.save(rate_dataset_hcal, indir+'/rate_hcal_TfDataset', compression='GZIP')
            print('** INFO : done saving HCAL TensorFlow datasets')
    else:
        print('** INFO : loading TensorFlow datasets')
        train_dataset_ecal = tf.data.experimental.load(indir+'/train_ecal_TfDataset', compression='GZIP')
        test_dataset_ecal = tf.data.experimental.load(indir+'/test_ecal_TfDataset', compression='GZIP')
        rate_dataset_ecal = tf.data.experimental.load(indir+'/rate_ecal_TfDataset', compression='GZIP')
        
        train_dataset_hcal = tf.data.experimental.load(indir+'/train_hcal_TfDataset', compression='GZIP')
        test_dataset_hcal = tf.data.experimental.load(indir+'/test_hcal_TfDataset', compression='GZIP')
        rate_dataset_hcal = tf.data.experimental.load(indir+'/rate_hcal_TfDataset', compression='GZIP')
        print('** INFO : done loading TensorFlow datasets')

    print('** INFO : batching TensorFlow datasets')
    train_dataset_ecal = train_dataset_ecal.shuffle(BUFFER_SIZE).batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    test_dataset_ecal = test_dataset_ecal.batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    rate_dataset_ecal = rate_dataset_ecal.shuffle(BUFFER_SIZE).batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    
    train_dataset_hcal = train_dataset_hcal.shuffle(BUFFER_SIZE).batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    test_dataset_hcal = test_dataset_hcal.batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    rate_dataset_hcal = rate_dataset_hcal.shuffle(BUFFER_SIZE).batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
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
                                                   experimental_per_replica_buffer_size=2)

    print('** INFO : distributing training datasets')
    train_dist_dataset_ecal = mirrored_strategy.experimental_distribute_dataset(train_dataset_ecal, options=DISTRIBUTION_OPTS)
    test_dist_dataset_ecal = mirrored_strategy.experimental_distribute_dataset(test_dataset_ecal, options=DISTRIBUTION_OPTS)
    rate_dist_dataset_ecal = mirrored_strategy.experimental_distribute_dataset(rate_dataset_ecal, options=DISTRIBUTION_OPTS)
    del train_dataset_ecal, test_dataset_ecal, rate_dataset_ecal

    train_dist_dataset_hcal = mirrored_strategy.experimental_distribute_dataset(train_dataset_hcal, options=DISTRIBUTION_OPTS)
    test_dist_dataset_hcal = mirrored_strategy.experimental_distribute_dataset(test_dataset_hcal, options=DISTRIBUTION_OPTS)
    rate_dist_dataset_hcal = mirrored_strategy.experimental_distribute_dataset(rate_dataset_hcal, options=DISTRIBUTION_OPTS)
    del train_dataset_hcal, test_dataset_hcal, rate_dataset_hcal
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
        def weightsLoss(version):
            modelWeights = model.trainable_weights
            if version == 'ecal':
                modelWeights_ss = float( tf.math.reduce_sum(tf.math.square(modelWeights[0]), keepdims=True) +
                                         tf.math.reduce_sum(tf.math.square(modelWeights[1]), keepdims=True) +
                                         tf.math.reduce_sum(tf.math.square(modelWeights[2]), keepdims=True)
                                       )
            if version == 'hcal':
                modelWeights_ss = float( tf.math.reduce_sum(tf.math.square(modelWeights[3]), keepdims=True) +
                                         tf.math.reduce_sum(tf.math.square(modelWeights[4]), keepdims=True) +
                                         tf.math.reduce_sum(tf.math.square(modelWeights[5]), keepdims=True)
                                       )

            return  modelWeights_ss * 1 # FIXME: scaling to be optimized

        # part of the loss that controls the rate for jets
        def rateLossJets(z_pred):
            # compute fraction of passing events and multiply by rate scaling
            proxyRate = tf.reduce_sum(z_pred, keepdims=True) / BATCH_SIZE_PER_REPLICA * 0.001*2500*11245.6
            targetRate = 191.8348 # computed from the old calibration in the same manner as here
            realtive_diff = (proxyRate - targetRate) / targetRate
            return tf.cosh(1.5 * realtive_diff) * 1 # FIXME: scaling to be optimized

        # part of the loss that controls the rate for e/gammas
        def rateLossEgs(z_pred):
            # compute fraction of passing events and multiply by rate scaling
            proxyRate = tf.reduce_sum(z_pred, keepdims=True) / BATCH_SIZE_PER_REPLICA * 0.001*2500*11245.6
            targetRate = 3756.696 # computed from the old calibration in the same manner as here
            realtive_diff = (proxyRate - targetRate) / targetRate
            return tf.cosh(1.5 * realtive_diff) * 1 # FIXME: scaling to be optimized

        # GPU distribution friendly loss computation
        def compute_losses(y, y_pred, z_pred, version):
            regressionLoss_value = regressionLoss(y, y_pred)
            if version == 'ecal':
                weightsLoss_value = weightsLoss(version)
                rateLoss_value = rateLossEgs(z_pred)
            if version == 'hcal':
                weightsLoss_value = weightsLoss(version)
                rateLoss_value = rateLossJets(z_pred)
            fullLoss = regressionLoss_value + weightsLoss_value + rateLoss_value

            return [tf.nn.compute_average_loss(fullLoss,             global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(regressionLoss_value, global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(weightsLoss_value,    global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(rateLoss_value,       global_batch_size=GLOBAL_BATCH_SIZE)]

        # define model and related stuff
        model, TTP_ecal, TTP_hcal = create_model(hoeThrEB=3., hoeThrEE=4., egThr=50., seedThr=8., jetThr=100.)
        optimizer = keras.optimizers.Adam(learning_rate=MAX_LEARNING_RATE)
        checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
        train_acc_metric_ecal = keras.metrics.RootMeanSquaredError(name='train_accuracy_ecal')
        train_acc_metric_hcal = keras.metrics.RootMeanSquaredError(name='train_accuracy_hcal')
        test_acc_metric_ecal  = keras.metrics.RootMeanSquaredError(name='test_accuracy_ecal')
        test_acc_metric_hcal  = keras.metrics.RootMeanSquaredError(name='test_accuracy_hcal')

    # print(model.summary())
    # exit()

    def custom_train_step(inputs_ecal, inputs_hcal, rate_inputs_ecal, rate_inputs_hcal):
        x_ecal, y_ecal = inputs_ecal
        x_hcal, y_hcal = inputs_hcal
        z_ecal, _ = rate_inputs_ecal
        z_hcal, _ = rate_inputs_hcal
        with tf.GradientTape() as tape:
            y_ecal_pred, y_hcal_pred, z_ecal_pred, z_hcal_pred = model([x_ecal, x_hcal, z_ecal, z_hcal], training=True)
            losses_ecal = compute_losses(y_ecal, y_ecal_pred, z_ecal_pred, 'ecal')
            losses_hcal = compute_losses(y_hcal, y_hcal_pred, z_hcal_pred, 'hcal')

        grads = tape.gradient([losses_ecal[1], losses_hcal[1], losses_ecal[2], losses_hcal[2], losses_ecal[3], losses_hcal[3]], model.trainable_weights)
        optimizer.apply_gradients(zip(grads, model.trainable_weights))
        train_acc_metric_ecal.update_state(y_ecal, y_ecal_pred)
        train_acc_metric_hcal.update_state(y_hcal, y_hcal_pred)

        return losses_ecal, losses_hcal

    def custom_test_step(inputs_ecal, inputs_hcal, rate_inputs_ecal, rate_inputs_hcal):
        x_ecal, y_ecal = inputs_ecal
        x_hcal, y_hcal = inputs_hcal
        z_ecal, _ = rate_inputs_ecal
        z_hcal, _ = rate_inputs_hcal
        y_ecal_pred, y_hcal_pred, z_ecal_pred, z_hcal_pred = model([x_ecal, x_hcal, z_ecal, z_hcal], training=False)
        losses_ecal = compute_losses(y_ecal, y_ecal_pred, z_ecal_pred, 'ecal')
        losses_hcal = compute_losses(y_hcal, y_hcal_pred, z_hcal_pred, 'hcal')
        test_acc_metric_ecal.update_state(y_ecal, y_ecal_pred)
        test_acc_metric_hcal.update_state(y_hcal, y_hcal_pred)

        return losses_ecal, losses_hcal

    @tf.function
    def distributed_train_step(ecal_dataset_inputs, hcal_dataset_inputs, ecal_rate_inputs, hcal_rate_inputs):
        per_replica_losses_ecal, per_replica_losses_hcal = mirrored_strategy.run(custom_train_step, args=(ecal_dataset_inputs, hcal_dataset_inputs, ecal_rate_inputs, hcal_rate_inputs,))
        return [
                [mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_ecal[0], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_ecal[1], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_ecal[2], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_ecal[3], axis=None)],
                [mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_hcal[0], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_hcal[1], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_hcal[2], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_hcal[3], axis=None)]
                ]

    @tf.function
    def distributed_test_step(ecal_dataset_inputs, hcal_dataset_inputs, ecal_rate_inputs, hcal_rate_inputs):
        per_replica_losses_ecal, per_replica_losses_hcal = mirrored_strategy.run(custom_test_step, args=(ecal_dataset_inputs, hcal_dataset_inputs, ecal_rate_inputs, hcal_rate_inputs,))
        return [
                [mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_ecal[0], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_ecal[1], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_ecal[2], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_ecal[3], axis=None)],
                [mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_hcal[0], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_hcal[1], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_hcal[2], axis=None),
                 mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses_hcal[3], axis=None)]
                ]


    # run training loop
    for epoch in range(EPOCHS):
        start_time = time.time()
        print('\nStart of epoch %d' % (epoch+1,))

        # TRAIN LOOP
        train_losses_avg = np.array([[0., 0., 0., 0.], [0., 0., 0., 0.]])
        num_batches = 0
        for batch_ecal, batch_hcal, rate_batch_ecal, rate_batch_hcal in zip(train_dist_dataset_ecal, train_dist_dataset_hcal, rate_dist_dataset_ecal, rate_dist_dataset_hcal):
            train_losses = distributed_train_step(batch_ecal, batch_hcal, rate_batch_ecal, rate_batch_hcal)
            train_losses_avg += train_losses
            num_batches += 1

            # Log every N batches
            if VERBOSE and num_batches % 1 == 0:
                print(
                      '    At batch %d (seen %d samples so far) : ECAL :  loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f \n\t\t\t\t\t       HCAL :  loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f'
                      %
                      (num_batches, num_batches*GLOBAL_BATCH_SIZE, float(train_losses[0][0]), float(train_losses[0][1]), float(train_losses[0][2]), float(train_losses[0][3]), float(train_acc_metric_ecal.result()),
                                                                   float(train_losses[1][0]), float(train_losses[1][1]), float(train_losses[1][2]), float(train_losses[1][3]), float(train_acc_metric_hcal.result()))
                     )

        train_losses_avg = train_losses_avg / num_batches

        # TEST LOOP
        test_losses = np.array([[0., 0., 0., 0.], [0., 0., 0., 0.]])
        num_batches = 0
        for batch_ecal, batch_hcal, rate_batch_ecal, rate_batch_hcal in zip(test_dist_dataset_ecal, test_dist_dataset_hcal, rate_dist_dataset_ecal, rate_dist_dataset_hcal):
            test_losses += distributed_test_step(batch_ecal, batch_hcal, rate_batch_ecal, rate_batch_hcal)
            num_batches += 1

        test_losses = test_losses / num_batches

        train_RMSE_ecal = train_acc_metric_ecal.result()
        test_RMSE_ecal = test_acc_metric_ecal.result()
        train_RMSE_hcal = train_acc_metric_hcal.result()
        test_RMSE_hcal = test_acc_metric_hcal.result()
        print('Training : ECAL : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(train_losses_avg[0][0]), float(train_losses_avg[0][1]), float(train_losses_avg[0][2]), float(train_losses_avg[0][3]), float(train_RMSE_ecal)) )
        print('           HCAL : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(train_losses_avg[1][0]), float(train_losses_avg[1][1]), float(train_losses_avg[1][2]), float(train_losses_avg[1][3]), float(train_RMSE_hcal)) )
        print('Testing  : ECAL : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(test_losses[0][0]), float(test_losses[0][1]), float(test_losses[0][2]), float(test_losses[0][3]), float(test_RMSE_ecal)) )
        print('           HCAL : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(test_losses[1][0]), float(test_losses[1][1]), float(test_losses[1][2]), float(test_losses[1][3]), float(test_RMSE_hcal)) )

        HISTORY['x'].append(epoch+1)
        if epoch < EPOCHS-1: HISTORY['learning_rate'].append([])
        HISTORY['ecal_train_loss'].append(           float(train_losses_avg[0][0]))
        HISTORY['ecal_train_regressionLoss'].append( float(train_losses_avg[0][1]))
        HISTORY['ecal_train_weightsLoss'].append(    float(train_losses_avg[0][2]))
        HISTORY['ecal_train_rateLoss'].append(       float(train_losses_avg[0][3]))
        HISTORY['ecal_train_RMSE'].append(           float(train_RMSE_ecal))
        HISTORY['ecal_test_loss'].append(            float(test_losses[0][0]))
        HISTORY['ecal_test_regressionLoss'].append(  float(test_losses[0][1]))
        HISTORY['ecal_test_weightsLoss'].append(     float(test_losses[0][2]))
        HISTORY['ecal_test_rateLoss'].append(        float(train_losses[0][3]))
        HISTORY['ecal_test_RMSE'].append(            float(test_RMSE_ecal))
        HISTORY['hcal_train_loss'].append(           float(train_losses_avg[1][0]))
        HISTORY['hcal_train_regressionLoss'].append( float(train_losses_avg[1][1]))
        HISTORY['hcal_train_weightsLoss'].append(    float(train_losses_avg[1][2]))
        HISTORY['hcal_train_rateLoss'].append(       float(train_losses_avg[1][3]))
        HISTORY['hcal_train_RMSE'].append(           float(train_RMSE_hcal))
        HISTORY['hcal_test_loss'].append(            float(test_losses[1][0]))
        HISTORY['hcal_test_regressionLoss'].append(  float(test_losses[1][1]))
        HISTORY['hcal_test_weightsLoss'].append(     float(test_losses[1][2]))
        HISTORY['hcal_test_rateLoss'].append(        float(train_losses[1][3]))
        HISTORY['hcal_test_RMSE'].append(            float(test_RMSE_hcal))

        # Reset metrics at the end of each epoch
        train_acc_metric_ecal.reset_states()
        test_acc_metric_ecal.reset_states()
        train_acc_metric_hcal.reset_states()
        test_acc_metric_hcal.reset_states()

        # save checkpoint
        checkpoint.save(CKPTpf)

        print('Time taken: %.2fs' % (time.time() - start_time))

    model.save(odir + '/model')
    TTP_ecal.save(odir + '/TTP_ecal')
    TTP_hcal.save(odir + '/TTP_hcal')
    print('\nTrained model saved to folder: {}'.format(odir))


    json.dump(HISTORY, open(odir+'/HISTORY.json', 'w'))
    print('Training history saved to file: {}/HISTORY.json'.format(odir))

    makePlots(HISTORY, odir)
