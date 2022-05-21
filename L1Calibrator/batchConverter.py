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
#le reseau de neurone partage par tous (inputs_dim = 2)

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

# Apply ECAL model to iem for the HCAL calibration, return a 1D vector to subtract from Y
def calibrate_iem(model_iem, X_vec):
    print('Calibrating iem')
    X = np.delete(X_vec, 2, axis=2) # delete iesum column (always start deleting from right columns)
    X = np.delete(X, 1, axis=2)     # delete ihad column
    X_iem_calib = model_iem.predict(X) # [GeV]
    del X_vec
    return X_iem_calib # [GeV]

# Apply HCAL model to ihad for the second ECAL calibration, return a 1D vector to subtract from Y
def calibrate_ihad(model_ihad, X_vec):
    print('Calibrating ihad')
    X = np.delete(X_vec, 2, axis=2) # delete iesum column (always start deleting from right columns)
    X = np.delete(X, 0, axis=2)     # delete iem column
    X_ihad_calib = model_ihad.predict(X) # [GeV]
    return X_ihad_calib # [GeV]

def convert_samples_X(X_vec, training_energy):
    # convert samples for training
    # X vector columns: iem, ihad, iesum, ieta
    if training_energy == 'iem':
        print('\nConvert X and Y vectors to keep iem')
        X = np.delete(X_vec, 2, axis=2) # delete iesum column (always start deleting from right columns)
        X = np.delete(X, 1, axis=2)     # delete ihad column

    elif training_energy == 'ihad':
        print('\nConvert X and Y vectors to keep ihad')
        X = np.delete(X_vec, 2, axis=2) # delete iesum column (always start deleting from right columns)
        X = np.delete(X, 0, axis=2)     # delete iem column

    elif training_energy == 'iesum':
        print('\nConvert X and Y vectors to keep iesum')
        X = np.delete(X_vec, 1, axis=2) # delete ihad column (always start deleting from right columns)
        X = np.delete(X, 0, axis=2)     # delete iem column
        
    return X

def convert_samples_Y(X_vec, Y_vec, training_energy, model):
    # convert samples for training
    # Y vector columns: jetPt, jetEta
    Y = Y_vec[:,0] # remove jetEta column
    del Y_vec

    # X vector columns: iem, ihad, iesum, ieta
    if training_energy == 'iem':
        print('Targeting jetPt - ihad')
        X_ihad = np.sum(X_vec, axis = 1)[:,1:2].ravel() # [ET]
        Y = Y - X_ihad*0.5 # [Gev] jetPt - HCAL_deposit
        # After calibrating HCAL we could reperform the ECAL calibration targeting jetPt - X_ihad_calib
        # if model != None:
        #     Y = Y - calibrate_ihad(model, X_vec)
        # else:
        #     X_ihad = np.sum(X_vec, axis = 1)[:,1:2].ravel() # [ET]
        #     Y = Y - X_ihad*0.5 # [Gev] jetPt - HCAL_deposit

    elif training_energy == 'ihad':
        if model != None:
            print('Targeting jetPt - calibrated iem')
            X_calib = calibrate_iem(model, X_vec)
            Y = Y - X_calib
        else: 
            print('Targeting jetPt - iem')
            X_iem = np.sum(X_vec,axis = 1)[:,0:1].ravel() # [ET]
            Y = Y - X_iem*0.5 # [Gev] jetPt - ECAL_deposit 

    elif training_energy == 'iesum':
        print('Targeting jetPt')
        
    return Y

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python batchConverter.py --indir 2022_05_09_NtuplesV12 --v ECAL --etrain iem --ECALModel /data_CMS/cms/motta/CaloL1calibraton/2022_05_09_NtuplesV12/ECALtraining/model_ECAL/

if __name__ == "__main__" :
    
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",        dest="indir",       help="Input folder with X_train.npx and Y_train.npz",   default=None)
    parser.add_option("--v",            dest="v",           help="Ntuple type ('ECAL' or 'HCAL')",                  default=None)
    parser.add_option("--etrain",       dest="etrain",      help="Trainining energy ('iem', 'ihad' or 'iesum')",    default=None)
    parser.add_option("--ECALModel",    dest="ECALModel",   help="ECAL model directory",                            default=None)
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training'

    print('Upload training vectors X and Y')
    # read testing and training datasets
    # Inside X_vec: matrix n_ev x 81 x 43 ([81 for the chucky donut towers][43 for iem, ihad, iesum, ieta])
    # Inside Y_vec: matrx n_ev x 2 (jetPt, jetEta)
    X_vec = np.load(indir+'/X_train.npz')['arr_0'][:200000]
    Y_vec = np.load(indir+'/Y_train.npz')['arr_0'][:200000]

    # upload ECAL model for HCAL training
    couche_ECAL = None
    if options.ECALModel != None:
        print('Upload ECAL model')
        model1_ECAL = keras.models.load_model(options.ECALModel + '/model', compile=False)
        couche_ECAL = keras.models.load_model(options.ECALModel + '/couche', compile=False)

    # X_train = convert_samples_X(X_vec, options.etrain)
    # print('Save X vector')
    # np.savez_compressed(indir + '/X_train_NN.npz', X_train)

    if len(Y_vec) < 50000:
        # Inside X_train: matrix n_ev x 81 x 41 ([81 for the chucky donut towers][41 for iesum, ieta])
        # Inside Y_train: vector n_ev (jetPt)
        Y_train = convert_samples_Y(X_vec, Y_vec, options.etrain, model)
        np.savez_compressed(indir + '/Y_train_NN.npz', Y_train)

    else:
        Y_train = []
        steps = int(len(Y_vec)/50000)
        scan = [int(len(Y_vec)/steps*i) for i in range(steps)] + [len(Y_vec)]
        print(scan)
        for i in range(len(scan)-1):
            print(scan[i],scan[i+1]-1)
            Y_tmp = convert_samples_Y(X_vec[scan[i]:scan[i+1]-1], Y_vec[scan[i]:scan[i+1]-1], options.etrain, model1_ECAL)
            Y_train = np.append(Y_train, Y_tmp)
            print(Y_train[:2])
            del Y_tmp

        print('Save Y vector')
        np.savez_compressed(indir + '/Y_train_NN.npz', Y_train)

    print('\nConverted vectors saved to folder: {}'.format(indir))
    print(indir + '/X_train_NN.npz')
    print(indir + '/Y_train_NN.npz')
