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
from tensorflow.keras.initializers import Constant as CI

np.random.seed(7)

##############################################################################
############################## Model definition ##############################
##############################################################################

# flooring custom gradient
@tf.custom_gradient
def Fgrad(x):
    def fgrad(dy):
        return dy
    return tf.floor(x), fgrad

inputs = keras.Input(shape = (81,41), name = 'chunky_donut')
layer1 = Dense(164, name = 'NN1', input_dim=41, activation='relu', kernel_initializer=RN(seed=7), bias_initializer='zeros', bias_constraint = max_norm(0.))
layer2 = Dense(512, name = 'NN2',               activation='relu', kernel_initializer=RN(seed=7), bias_initializer='zeros', bias_constraint = max_norm(0.))
layer3 = Dense(1,   name = 'NN3',               activation='relu', kernel_initializer=RN(seed=7), bias_initializer='zeros', bias_constraint = max_norm(0.))
layer4 = lay.Lambda(Fgrad)

TTP = Sequential()
TTP.add(layer1)
TTP.add(layer2)
TTP.add(layer3)
TTP.add(layer4)

# dummy NN that takes an input and gives the same value as output
dummyLayer = Dense(1, name = 'dummyNN', input_dim=1, activation='linear', kernel_initializer=CI(1.), bias_initializer='zeros', bias_constraint = max_norm(0.), trainable=False)
dummyTTP = Sequential()
dummyTTP.add(dummyLayer)

Ubound = 20.0 # insert very large value for "disactivation"
Lbound = 0.95 # insert 0.0 for "disactivation"

separation_l = []
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,0,:],name=f"TT{0}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,0,0],(-1,1)),name=f"eLbound{0}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,0,0],(-1,1)),name=f"eUbound{0}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,1,:],name=f"TT{1}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,1,0],(-1,1)),name=f"eLbound{1}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,1,0],(-1,1)),name=f"eUbound{1}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,2,:],name=f"TT{2}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,2,0],(-1,1)),name=f"eLbound{2}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,2,0],(-1,1)),name=f"eUbound{2}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,3,:],name=f"TT{3}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,3,0],(-1,1)),name=f"eLbound{3}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,3,0],(-1,1)),name=f"eUbound{3}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,4,:],name=f"TT{4}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,4,0],(-1,1)),name=f"eLbound{4}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,4,0],(-1,1)),name=f"eUbound{4}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,5,:],name=f"TT{5}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,5,0],(-1,1)),name=f"eLbound{5}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,5,0],(-1,1)),name=f"eUbound{5}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,6,:],name=f"TT{6}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,6,0],(-1,1)),name=f"eLbound{6}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,6,0],(-1,1)),name=f"eUbound{6}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,7,:],name=f"TT{7}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,7,0],(-1,1)),name=f"eLbound{7}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,7,0],(-1,1)),name=f"eUbound{7}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,8,:],name=f"TT{8}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,8,0],(-1,1)),name=f"eLbound{8}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,8,0],(-1,1)),name=f"eUbound{8}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,9,:],name=f"TT{9}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,9,0],(-1,1)),name=f"eLbound{9}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,9,0],(-1,1)),name=f"eUbound{9}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,10,:],name=f"TT{10}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,10,0],(-1,1)),name=f"eLbound{10}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,10,0],(-1,1)),name=f"eUbound{10}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,11,:],name=f"TT{11}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,11,0],(-1,1)),name=f"eLbound{11}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,11,0],(-1,1)),name=f"eUbound{11}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,12,:],name=f"TT{12}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,12,0],(-1,1)),name=f"eLbound{12}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,12,0],(-1,1)),name=f"eUbound{12}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,13,:],name=f"TT{13}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,13,0],(-1,1)),name=f"eLbound{13}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,13,0],(-1,1)),name=f"eUbound{13}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,14,:],name=f"TT{14}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,14,0],(-1,1)),name=f"eLbound{14}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,14,0],(-1,1)),name=f"eUbound{14}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,15,:],name=f"TT{15}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,15,0],(-1,1)),name=f"eLbound{15}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,15,0],(-1,1)),name=f"eUbound{15}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,16,:],name=f"TT{16}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,16,0],(-1,1)),name=f"eLbound{16}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,16,0],(-1,1)),name=f"eUbound{16}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,17,:],name=f"TT{17}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,17,0],(-1,1)),name=f"eLbound{17}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,17,0],(-1,1)),name=f"eUbound{17}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,18,:],name=f"TT{18}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,18,0],(-1,1)),name=f"eLbound{18}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,18,0],(-1,1)),name=f"eUbound{18}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,19,:],name=f"TT{19}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,19,0],(-1,1)),name=f"eLbound{19}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,19,0],(-1,1)),name=f"eUbound{19}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,20,:],name=f"TT{20}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,20,0],(-1,1)),name=f"eLbound{20}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,20,0],(-1,1)),name=f"eUbound{20}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,21,:],name=f"TT{21}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,21,0],(-1,1)),name=f"eLbound{21}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,21,0],(-1,1)),name=f"eUbound{21}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,22,:],name=f"TT{22}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,22,0],(-1,1)),name=f"eLbound{22}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,22,0],(-1,1)),name=f"eUbound{22}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,23,:],name=f"TT{23}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,23,0],(-1,1)),name=f"eLbound{23}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,23,0],(-1,1)),name=f"eUbound{23}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,24,:],name=f"TT{24}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,24,0],(-1,1)),name=f"eLbound{24}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,24,0],(-1,1)),name=f"eUbound{24}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,25,:],name=f"TT{25}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,25,0],(-1,1)),name=f"eLbound{25}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,25,0],(-1,1)),name=f"eUbound{25}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,26,:],name=f"TT{26}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,26,0],(-1,1)),name=f"eLbound{26}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,26,0],(-1,1)),name=f"eUbound{26}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,27,:],name=f"TT{27}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,27,0],(-1,1)),name=f"eLbound{27}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,27,0],(-1,1)),name=f"eUbound{27}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,28,:],name=f"TT{28}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,28,0],(-1,1)),name=f"eLbound{28}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,28,0],(-1,1)),name=f"eUbound{28}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,29,:],name=f"TT{29}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,29,0],(-1,1)),name=f"eLbound{29}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,29,0],(-1,1)),name=f"eUbound{29}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,30,:],name=f"TT{30}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,30,0],(-1,1)),name=f"eLbound{30}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,30,0],(-1,1)),name=f"eUbound{30}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,31,:],name=f"TT{31}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,31,0],(-1,1)),name=f"eLbound{31}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,31,0],(-1,1)),name=f"eUbound{31}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,32,:],name=f"TT{32}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,32,0],(-1,1)),name=f"eLbound{32}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,32,0],(-1,1)),name=f"eUbound{32}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,33,:],name=f"TT{33}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,33,0],(-1,1)),name=f"eLbound{33}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,33,0],(-1,1)),name=f"eUbound{33}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,34,:],name=f"TT{34}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,34,0],(-1,1)),name=f"eLbound{34}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,34,0],(-1,1)),name=f"eUbound{34}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,35,:],name=f"TT{35}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,35,0],(-1,1)),name=f"eLbound{35}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,35,0],(-1,1)),name=f"eUbound{35}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,36,:],name=f"TT{36}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,36,0],(-1,1)),name=f"eLbound{36}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,36,0],(-1,1)),name=f"eUbound{36}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,37,:],name=f"TT{37}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,37,0],(-1,1)),name=f"eLbound{37}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,37,0],(-1,1)),name=f"eUbound{37}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,38,:],name=f"TT{38}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,38,0],(-1,1)),name=f"eLbound{38}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,38,0],(-1,1)),name=f"eUbound{38}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,39,:],name=f"TT{39}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,39,0],(-1,1)),name=f"eLbound{39}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,39,0],(-1,1)),name=f"eUbound{39}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,40,:],name=f"TT{40}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,40,0],(-1,1)),name=f"eLbound{40}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,40,0],(-1,1)),name=f"eUbound{40}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,41,:],name=f"TT{41}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,41,0],(-1,1)),name=f"eLbound{41}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,41,0],(-1,1)),name=f"eUbound{41}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,42,:],name=f"TT{42}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,42,0],(-1,1)),name=f"eLbound{42}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,42,0],(-1,1)),name=f"eUbound{42}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,43,:],name=f"TT{43}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,43,0],(-1,1)),name=f"eLbound{43}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,43,0],(-1,1)),name=f"eUbound{43}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,44,:],name=f"TT{44}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,44,0],(-1,1)),name=f"eLbound{44}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,44,0],(-1,1)),name=f"eUbound{44}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,45,:],name=f"TT{45}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,45,0],(-1,1)),name=f"eLbound{45}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,45,0],(-1,1)),name=f"eUbound{45}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,46,:],name=f"TT{46}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,46,0],(-1,1)),name=f"eLbound{46}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,46,0],(-1,1)),name=f"eUbound{46}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,47,:],name=f"TT{47}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,47,0],(-1,1)),name=f"eLbound{47}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,47,0],(-1,1)),name=f"eUbound{47}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,48,:],name=f"TT{48}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,48,0],(-1,1)),name=f"eLbound{48}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,48,0],(-1,1)),name=f"eUbound{48}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,49,:],name=f"TT{49}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,49,0],(-1,1)),name=f"eLbound{49}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,49,0],(-1,1)),name=f"eUbound{49}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,50,:],name=f"TT{50}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,50,0],(-1,1)),name=f"eLbound{50}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,50,0],(-1,1)),name=f"eUbound{50}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,51,:],name=f"TT{51}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,51,0],(-1,1)),name=f"eLbound{51}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,51,0],(-1,1)),name=f"eUbound{51}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,52,:],name=f"TT{52}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,52,0],(-1,1)),name=f"eLbound{52}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,52,0],(-1,1)),name=f"eUbound{52}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,53,:],name=f"TT{53}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,53,0],(-1,1)),name=f"eLbound{53}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,53,0],(-1,1)),name=f"eUbound{53}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,54,:],name=f"TT{54}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,54,0],(-1,1)),name=f"eLbound{54}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,54,0],(-1,1)),name=f"eUbound{54}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,55,:],name=f"TT{55}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,55,0],(-1,1)),name=f"eLbound{55}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,55,0],(-1,1)),name=f"eUbound{55}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,56,:],name=f"TT{56}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,56,0],(-1,1)),name=f"eLbound{56}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,56,0],(-1,1)),name=f"eUbound{56}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,57,:],name=f"TT{57}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,57,0],(-1,1)),name=f"eLbound{57}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,57,0],(-1,1)),name=f"eUbound{57}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,58,:],name=f"TT{58}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,58,0],(-1,1)),name=f"eLbound{58}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,58,0],(-1,1)),name=f"eUbound{58}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,59,:],name=f"TT{59}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,59,0],(-1,1)),name=f"eLbound{59}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,59,0],(-1,1)),name=f"eUbound{59}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,60,:],name=f"TT{60}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,60,0],(-1,1)),name=f"eLbound{60}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,60,0],(-1,1)),name=f"eUbound{60}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,61,:],name=f"TT{61}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,61,0],(-1,1)),name=f"eLbound{61}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,61,0],(-1,1)),name=f"eUbound{61}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,62,:],name=f"TT{62}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,62,0],(-1,1)),name=f"eLbound{62}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,62,0],(-1,1)),name=f"eUbound{62}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,63,:],name=f"TT{63}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,63,0],(-1,1)),name=f"eLbound{63}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,63,0],(-1,1)),name=f"eUbound{63}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,64,:],name=f"TT{64}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,64,0],(-1,1)),name=f"eLbound{64}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,64,0],(-1,1)),name=f"eUbound{64}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,65,:],name=f"TT{65}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,65,0],(-1,1)),name=f"eLbound{65}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,65,0],(-1,1)),name=f"eUbound{65}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,66,:],name=f"TT{66}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,66,0],(-1,1)),name=f"eLbound{66}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,66,0],(-1,1)),name=f"eUbound{66}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,67,:],name=f"TT{67}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,67,0],(-1,1)),name=f"eLbound{67}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,67,0],(-1,1)),name=f"eUbound{67}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,68,:],name=f"TT{68}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,68,0],(-1,1)),name=f"eLbound{68}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,68,0],(-1,1)),name=f"eUbound{68}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,69,:],name=f"TT{69}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,69,0],(-1,1)),name=f"eLbound{69}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,69,0],(-1,1)),name=f"eUbound{69}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,70,:],name=f"TT{70}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,70,0],(-1,1)),name=f"eLbound{70}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,70,0],(-1,1)),name=f"eUbound{70}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,71,:],name=f"TT{71}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,71,0],(-1,1)),name=f"eLbound{71}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,71,0],(-1,1)),name=f"eUbound{71}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,72,:],name=f"TT{72}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,72,0],(-1,1)),name=f"eLbound{72}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,72,0],(-1,1)),name=f"eUbound{72}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,73,:],name=f"TT{73}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,73,0],(-1,1)),name=f"eLbound{73}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,73,0],(-1,1)),name=f"eUbound{73}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,74,:],name=f"TT{74}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,74,0],(-1,1)),name=f"eLbound{74}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,74,0],(-1,1)),name=f"eUbound{74}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,75,:],name=f"TT{75}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,75,0],(-1,1)),name=f"eLbound{75}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,75,0],(-1,1)),name=f"eUbound{75}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,76,:],name=f"TT{76}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,76,0],(-1,1)),name=f"eLbound{76}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,76,0],(-1,1)),name=f"eUbound{76}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,77,:],name=f"TT{77}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,77,0],(-1,1)),name=f"eLbound{77}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,77,0],(-1,1)),name=f"eUbound{77}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,78,:],name=f"TT{78}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,78,0],(-1,1)),name=f"eLbound{78}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,78,0],(-1,1)),name=f"eUbound{78}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,79,:],name=f"TT{79}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,79,0],(-1,1)),name=f"eLbound{79}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,79,0],(-1,1)),name=f"eUbound{79}")(inputs))*Ubound) ) )
separation_l.append( tf.clip_by_value( TTP(lay.Lambda(lambda x : x[:,80,:],name=f"TT{80}")(inputs)) , clip_value_min=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,80,0],(-1,1)),name=f"eLbound{80}")(inputs))*Lbound), clip_value_max=tf.floor(dummyTTP(lay.Lambda(lambda x : tf.reshape(x[:,80,0],(-1,1)),name=f"eUbound{80}")(inputs))*Ubound) ) )

outputs = keras.layers.Add()(separation_l)
model1 = keras.Model(inputs, outputs, name = 'CMS')

def custom_loss(y_true, y_pred):
    return tf.nn.l2_loss((y_true - y_pred)/(y_true+0.1))

model1.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss=custom_loss, metrics=['RootMeanSquaredError'])


def convert_samples(X_vec, Y_vec, version):
    # Y vector columns: jetPt, jetEta, jetPhi, trainingPt (for ECAL jetPt - hcalET, for HCAL jetPt - calib(iem))
    # keep only the trainingPt
    Y = Y_vec[:,3]

    # X vector columns: iem, ihad, iesum, ieta
    if version == 'ECAL':
        print('\nConvert X and Y vectors to keep iem')
        X = np.delete(X_vec, 2, axis=2) # delete iesum column (always start deleting from right columns)
        X = np.delete(X, 1, axis=2)     # delete ihad column

    elif version == 'HCAL':
        print('\nConvert X and Y vectors to keep ihad')
        X = np.delete(X_vec, 2, axis=2) # delete iesum column (always start deleting from right columns)
        X = np.delete(X, 0, axis=2)     # delete iem column
        
    return X, Y

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
    # Inside X_vec: matrix n_ev x 81 x 43 ([81 for the chucky donut towers][43 for iem, ihad, iesum, ieta])
    # Inside Y_vec: matrx n_ev x 2 (jetPt, jetPhi, jetEta, trainingPt)
    X_vec = np.load(indir+'/X_train.npz')['arr_0']
    Y_vec = np.load(indir+'/Y_train.npz')['arr_0']

    # Inside X_train: matrix n_ev x 81 x 41 ([81 for the chucky donut towers][41 for iesum, ieta])
    # Inside Y_train: vector n_ev (jetPt)
    X_train, Y_train = convert_samples(X_vec, Y_vec, options.v)

    history = model1.fit(X_train, Y_train, epochs=10, batch_size=128, verbose=1, validation_split=0.1)

    # print(model1.summary())
    # exit()

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

