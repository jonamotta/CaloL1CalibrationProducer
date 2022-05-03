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

# Regression import
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from tensorflow.keras.constraints import max_norm
from sklearn.model_selection import train_test_split

##############################################################################
############################## Model definition ##############################
##############################################################################

inputs = keras.Input(shape = (81,41), name = 'chunky_donut')

layer1 = Dense(164, name = 'NN1',   input_dim=41,   activation = 'softplus', kernel_initializer = 'normal', bias_initializer='zeros', bias_constraint = max_norm(0.))
cache =  Dense(512, name = 'cache',                 activation = 'softplus', kernel_initializer = 'normal', bias_initializer='zeros', bias_constraint = max_norm(0.))
layer2 = Dense(1,   name = 'NN2',                   activation = 'softplus', kernel_initializer = 'normal', bias_initializer='zeros', bias_constraint = max_norm(0.))
#layer1 = Dense(128, input_dim=2, activation='softplus', name = 'NN1', kernel_initializer='normal',bias_initializer='zeros')
#layer2 = Dense(1, activation='softplus', name = 'NN2',kernel_initializer='normal',bias_initializer='zeros')

couche = Sequential()
couche.add(layer1)
couche.add(cache)
#couche.add(Dense(256, activation = 'relu', name = 'cache_2',kernel_initializer='ones',bias_initializer='zeros'))
couche.add(layer2)
#le reseau de neurone partagé par tous (inputs_dim = 2)

separation_l = []
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,0,:],name=f"tour_{0}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,1,:],name=f"tour_{1}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,2,:],name=f"tour_{2}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,3,:],name=f"tour_{3}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,4,:],name=f"tour_{4}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,5,:],name=f"tour_{5}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,6,:],name=f"tour_{6}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,7,:],name=f"tour_{7}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,8,:],name=f"tour_{8}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,9,:],name=f"tour_{9}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,10,:],name=f"tour_{10}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,11,:],name=f"tour_{11}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,12,:],name=f"tour_{12}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,13,:],name=f"tour_{13}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,14,:],name=f"tour_{14}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,15,:],name=f"tour_{15}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,16,:],name=f"tour_{16}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,17,:],name=f"tour_{17}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,18,:],name=f"tour_{18}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,19,:],name=f"tour_{19}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,20,:],name=f"tour_{20}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,21,:],name=f"tour_{21}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,22,:],name=f"tour_{22}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,23,:],name=f"tour_{23}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,24,:],name=f"tour_{24}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,25,:],name=f"tour_{25}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,26,:],name=f"tour_{26}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,27,:],name=f"tour_{27}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,28,:],name=f"tour_{28}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,29,:],name=f"tour_{29}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,30,:],name=f"tour_{30}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,31,:],name=f"tour_{31}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,32,:],name=f"tour_{32}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,33,:],name=f"tour_{33}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,34,:],name=f"tour_{34}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,35,:],name=f"tour_{35}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,36,:],name=f"tour_{36}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,37,:],name=f"tour_{37}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,38,:],name=f"tour_{38}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,39,:],name=f"tour_{39}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,40,:],name=f"tour_{40}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,41,:],name=f"tour_{41}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,42,:],name=f"tour_{42}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,43,:],name=f"tour_{43}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,44,:],name=f"tour_{44}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,45,:],name=f"tour_{45}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,46,:],name=f"tour_{46}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,47,:],name=f"tour_{47}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,48,:],name=f"tour_{48}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,49,:],name=f"tour_{49}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,50,:],name=f"tour_{50}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,51,:],name=f"tour_{51}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,52,:],name=f"tour_{52}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,53,:],name=f"tour_{53}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,54,:],name=f"tour_{54}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,55,:],name=f"tour_{55}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,56,:],name=f"tour_{56}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,57,:],name=f"tour_{57}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,58,:],name=f"tour_{58}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,59,:],name=f"tour_{59}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,60,:],name=f"tour_{60}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,61,:],name=f"tour_{61}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,62,:],name=f"tour_{62}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,63,:],name=f"tour_{63}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,64,:],name=f"tour_{64}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,65,:],name=f"tour_{65}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,66,:],name=f"tour_{66}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,67,:],name=f"tour_{67}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,68,:],name=f"tour_{68}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,69,:],name=f"tour_{69}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,70,:],name=f"tour_{70}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,71,:],name=f"tour_{71}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,72,:],name=f"tour_{72}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,73,:],name=f"tour_{73}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,74,:],name=f"tour_{74}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,75,:],name=f"tour_{75}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,76,:],name=f"tour_{76}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,77,:],name=f"tour_{77}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,78,:],name=f"tour_{78}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,79,:],name=f"tour_{79}")(inputs)))
separation_l.append(couche(keras.layers.Lambda(lambda x : x[:,80,:],name=f"tour_{80}")(inputs)))

outputs = keras.layers.Add()(separation_l)
model1 = keras.Model(inputs, outputs, name = 'CMS')

def custom_loss(y_true, y_pred):
    return tf.nn.l2_loss((y_true - y_pred)/(y_true+0.1))

model1.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss=custom_loss)


def convert_samples(X_train, Y_train, version='ECALpHCAL'):
    # convert samples for training
    print('\nConvert samples to X_train and Y_train')
    if version=="ECAL":
        X_train = np.delete(X_train, 2, axis=2)   # delete iesum column
        X_train = np.delete(X_train, 1, axis=2)   # delete ihad column
    elif version=="HCAL":
        X_train = np.delete(X_train, 2, axis=2)   # delete iesum column
        X_train = np.delete(X_train, 0, axis=2)   # delete iem column
    else:
        X_train = np.delete(X_train, 1, axis=2)   # delete ihad column
        X_train = np.delete(X_train, 0, axis=2)   # delete iem column
    
    # Need to remove the second entry in the Y vectors with [:,0] (eta information)
    Y_train = Y_train[:,0]
    return X_train, Y_train


#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 NNModelTraining.py --in 2022_04_21_NtuplesV1 --v ECAL

if __name__ == "__main__" :
    
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",       dest="indir",   help="Input folder with csv",           default=None)
    parser.add_option("--v",        dest="v",       help="Ntuple type ('ECAL' or 'HCAL')",  default='ECAL')
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training'
    odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + '/model_' + options.v
    os.system('mkdir -p '+ odir)

    # read testing and training datasets
    # Inside X_vec: matrix n_ev x 81 x 43 ([81 for the chucky donut towers][43 for iem, ihad, iesum, ieta])
    # Inside Y_vec: matrx n_ev x 2 (jetPt, jetEta)
    X_vec = np.load(indir+'/X_train.npz')['arr_0']
    Y_vec = np.load(indir+'/Y_train.npz')['arr_0']

    # Inside X_train: matrix n_ev x 81 x 41 ([81 for the chucky donut towers][41 for iesum, ieta])
    # Inside Y_train: vector n_ev (jetPt)
    X_train, Y_train = convert_samples(X_vec, Y_vec)

    model1.fit(X_train, Y_train, epochs=20, batch_size=128,verbose=1)

    model1.save(odir + '/model')
    couche.save(odir + '/couche')

    print('\nTrained model saved to folder: {}'.format(odir))

