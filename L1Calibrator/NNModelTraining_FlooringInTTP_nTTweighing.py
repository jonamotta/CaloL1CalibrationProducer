#librairies utiles
import numpy as np
import copy
import os
import pandas as pd
import matplotlib.pyplot as plt
from math import *
from itertools import product

import sklearn
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers as lay

# Regression import
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from tensorflow.keras.constraints import max_norm
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.initializers import RandomNormal as RN

np.random.seed(7)

##############################################################################
############################## Model definition ##############################
##############################################################################

# flooring custom gradient
@tf.custom_gradient
def fgrad(x):
    def grad(dy):
        return dy
    return tf.floor(x), grad

inputs = keras.Input(shape = (81,41), name = 'chunky_donut')
layer1 = Dense(164, name = 'NN1', input_dim=41, activation='relu', kernel_initializer=RN(seed=7), bias_initializer='zeros', bias_constraint = max_norm(0.))
layer2 = Dense(512, name = 'NN2',               activation='relu', kernel_initializer=RN(seed=7), bias_initializer='zeros', bias_constraint = max_norm(0.))
layer3 = Dense(1,   name = 'NN3',               activation='relu', kernel_initializer=RN(seed=7), bias_initializer='zeros', bias_constraint = max_norm(0.))
layer4 = lay.Lambda(fgrad)

TTP = Sequential()
TTP.add(layer1)
TTP.add(layer2)
TTP.add(layer3)
TTP.add(layer4)

separation_l = []
separation_l.append( TTP(lay.Lambda(lambda x : x[:,0,:],name=f"TT{0}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,1,:],name=f"TT{1}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,2,:],name=f"TT{2}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,3,:],name=f"TT{3}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,4,:],name=f"TT{4}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,5,:],name=f"TT{5}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,6,:],name=f"TT{6}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,7,:],name=f"TT{7}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,8,:],name=f"TT{8}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,9,:],name=f"TT{9}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,10,:],name=f"TT{10}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,11,:],name=f"TT{11}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,12,:],name=f"TT{12}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,13,:],name=f"TT{13}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,14,:],name=f"TT{14}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,15,:],name=f"TT{15}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,16,:],name=f"TT{16}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,17,:],name=f"TT{17}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,18,:],name=f"TT{18}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,19,:],name=f"TT{19}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,20,:],name=f"TT{20}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,21,:],name=f"TT{21}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,22,:],name=f"TT{22}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,23,:],name=f"TT{23}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,24,:],name=f"TT{24}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,25,:],name=f"TT{25}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,26,:],name=f"TT{26}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,27,:],name=f"TT{27}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,28,:],name=f"TT{28}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,29,:],name=f"TT{29}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,30,:],name=f"TT{30}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,31,:],name=f"TT{31}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,32,:],name=f"TT{32}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,33,:],name=f"TT{33}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,34,:],name=f"TT{34}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,35,:],name=f"TT{35}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,36,:],name=f"TT{36}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,37,:],name=f"TT{37}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,38,:],name=f"TT{38}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,39,:],name=f"TT{39}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,40,:],name=f"TT{40}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,41,:],name=f"TT{41}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,42,:],name=f"TT{42}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,43,:],name=f"TT{43}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,44,:],name=f"TT{44}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,45,:],name=f"TT{45}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,46,:],name=f"TT{46}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,47,:],name=f"TT{47}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,48,:],name=f"TT{48}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,49,:],name=f"TT{49}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,50,:],name=f"TT{50}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,51,:],name=f"TT{51}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,52,:],name=f"TT{52}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,53,:],name=f"TT{53}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,54,:],name=f"TT{54}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,55,:],name=f"TT{55}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,56,:],name=f"TT{56}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,57,:],name=f"TT{57}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,58,:],name=f"TT{58}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,59,:],name=f"TT{59}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,60,:],name=f"TT{60}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,61,:],name=f"TT{61}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,62,:],name=f"TT{62}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,63,:],name=f"TT{63}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,64,:],name=f"TT{64}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,65,:],name=f"TT{65}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,66,:],name=f"TT{66}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,67,:],name=f"TT{67}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,68,:],name=f"TT{68}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,69,:],name=f"TT{69}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,70,:],name=f"TT{70}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,71,:],name=f"TT{71}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,72,:],name=f"TT{72}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,73,:],name=f"TT{73}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,74,:],name=f"TT{74}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,75,:],name=f"TT{75}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,76,:],name=f"TT{76}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,77,:],name=f"TT{77}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,78,:],name=f"TT{78}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,79,:],name=f"TT{79}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,80,:],name=f"TT{80}")(inputs)) )

outputs = keras.layers.Add()(separation_l)
model1 = keras.Model(inputs, outputs, name = 'CMS')

def custom_loss(y_true, y_pred):
    return tf.nn.l2_loss((y_true - y_pred)/(y_true+0.1))

model1.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss=custom_loss, metrics=['RootMeanSquaredError'])


def convert_samples(X_vec, Y_vec, version):
    # Y vector columns: jetPt, jetEta, jetPhi, trainingPt (for ECAL jetPt - hcalET, for HCAL jetPt - calib(iem))
    # keep only the trainingPt
    Y = Y_vec[:,3]

    nTT = X[:,0,0].reshape(-1,1) 
    
    # X vector columns: nTT,iem, ihad, iesum, ieta
    if version == 'ECAL':
        print('\nConvert X and Y vectors to keep iem')
        X = np.delete(X_vec, 3, axis=2) # delete iesum column (always start deleting from right columns)
        X = np.delete(X, 2, axis=2)     # delete ihad column
        X = np.delete(X, 0, axis=2)     # delete nTT column

    elif version == 'HCAL':
        print('\nConvert X and Y vectors to keep ihad')
        X = np.delete(X_vec, 3, axis=2) # delete iesum column (always start deleting from right columns)
        X = np.delete(X, 1, axis=2)     # delete iem column
        X = np.delete(X, 0, axis=2)     # delete nTT column

    return X, Y, nTT

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 NNModelTraining.py --in 2022_05_02_NtuplesV9 --v HCAL

if __name__ == "__main__" :
    
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",        dest="indir",       help="Input folder with X_train.npx and Y_train.npz",   default=None)
    parser.add_option("--tag",          dest="tag",         help="tag of the training folder",                      default="")
    parser.add_option("--v",            dest="v",           help="Ntuple type ('ECAL' or 'HCAL')",                  default=None)
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/model_' + options.v
    os.system('mkdir -p '+ odir)
    os.system('mkdir -p '+ odir+'/plots')

    # read testing and training datasets
    # Inside X_vec: matrix n_ev x 81 x 44 ([81 for the chucky donut towers][43 for nTT, iem, ihad, iesum, ieta])
    # Inside Y_vec: matrx n_ev x 2 (jetPt, jetPhi, jetEta, trainingPt)
    X_vec = np.load(indir+'/X_train.npz')['arr_0']
    Y_vec = np.load(indir+'/Y_train.npz')['arr_0']

    # Inside X_train: matrix n_ev x 81 x 41 ([81 for the chucky donut towers][41 for iesum, ieta])
    # Inside Y_train: vector n_ev (jetPt)
    # Inside nTT: vector n_ev (nTT)
    X_train, Y_train, nTT = convert_samples(X_vec, Y_vec, options.v)

    history = model1.fit([X_train,nTT], Y_train, epochs=20, batch_size=128, verbose=1, validation_split=0.1)

    model1.save(odir + '/model')
    TTP.save(odir + '/TTP')

    print(history.history.keys())

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(odir+'/plots/loss.pdf')
    plt.close()

    plt.plot(history.history['root_mean_squared_error'])
    plt.plot(history.history['val_root_mean_squared_error'])
    plt.title('model RootMeanSquaredError')
    plt.ylabel('RootMeanSquaredError')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(odir+'/plots/RootMeanSquaredError.pdf')
    plt.close()

    print('\nTrained model saved to folder: {}'.format(odir))
