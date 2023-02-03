from sklearn.model_selection import train_test_split
import numpy as np
import sklearn
import random
import time
import copy
import sys
import os

import matplotlib.pyplot as plt

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
    print('\nConvert X, Y, and Z vectors to order iem and ihad appropriately')
    if version == 'ECAL':
        X = np.delete(X, 2, axis=2) # delete iesum column (always start deleting from right columns)
        X[:,:,[0,1]] = X[:,:,[1,0]]     # order iem and ihad to have the needed one on the right

        Z = np.delete(Z, 2, axis=2)
        Z = Z.reshape(Z.shape[0]*Z.shape[1], Z.shape[2]) # reshape so that every TT beomes an event
        Z = Z[ Z[:,0] != 0 ] # remove TTs that have iEM == 0
        Z[:,[0,1]] = Z[:,[1,0]]

    elif version == 'HCAL':
        X = np.delete(X, 2, axis=2)
        Z = np.delete(Z, 2, axis=2)
        
    return X, Y, Z


##############################################################################
############################## MODEL DEFINITION ##############################
##############################################################################

# flooring custom gradient
@tf.custom_gradient
def Fgrad(x):
    def fgrad(dy):
        return dy
    return tf.floor(x), fgrad

inputs = keras.Input(shape = (81,42), name = 'chunky_donut')
layer1 = Dense(164, name = 'NN1', input_dim=41, activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
layer2 = Dense(512, name = 'NN2',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
layer3 = Dense(1,   name = 'NN3',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
layer4 = lay.Lambda(Fgrad)

TTP = Sequential()
TTP.add(layer1)
TTP.add(layer2)
TTP.add(layer3)
TTP.add(layer4)

separation_l = []
separation_l.append( TTP(lay.Lambda(lambda x : x[:,0,1:],name=f"TT{0}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,1,1:],name=f"TT{1}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,2,1:],name=f"TT{2}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,3,1:],name=f"TT{3}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,4,1:],name=f"TT{4}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,5,1:],name=f"TT{5}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,6,1:],name=f"TT{6}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,7,1:],name=f"TT{7}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,8,1:],name=f"TT{8}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,9,1:],name=f"TT{9}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,10,1:],name=f"TT{10}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,11,1:],name=f"TT{11}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,12,1:],name=f"TT{12}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,13,1:],name=f"TT{13}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,14,1:],name=f"TT{14}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,15,1:],name=f"TT{15}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,16,1:],name=f"TT{16}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,17,1:],name=f"TT{17}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,18,1:],name=f"TT{18}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,19,1:],name=f"TT{19}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,20,1:],name=f"TT{20}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,21,1:],name=f"TT{21}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,22,1:],name=f"TT{22}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,23,1:],name=f"TT{23}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,24,1:],name=f"TT{24}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,25,1:],name=f"TT{25}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,26,1:],name=f"TT{26}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,27,1:],name=f"TT{27}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,28,1:],name=f"TT{28}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,29,1:],name=f"TT{29}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,30,1:],name=f"TT{30}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,31,1:],name=f"TT{31}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,32,1:],name=f"TT{32}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,33,1:],name=f"TT{33}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,34,1:],name=f"TT{34}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,35,1:],name=f"TT{35}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,36,1:],name=f"TT{36}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,37,1:],name=f"TT{37}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,38,1:],name=f"TT{38}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,39,1:],name=f"TT{39}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,40,1:],name=f"TT{40}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,41,1:],name=f"TT{41}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,42,1:],name=f"TT{42}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,43,1:],name=f"TT{43}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,44,1:],name=f"TT{44}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,45,1:],name=f"TT{45}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,46,1:],name=f"TT{46}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,47,1:],name=f"TT{47}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,48,1:],name=f"TT{48}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,49,1:],name=f"TT{49}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,50,1:],name=f"TT{50}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,51,1:],name=f"TT{51}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,52,1:],name=f"TT{52}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,53,1:],name=f"TT{53}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,54,1:],name=f"TT{54}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,55,1:],name=f"TT{55}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,56,1:],name=f"TT{56}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,57,1:],name=f"TT{57}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,58,1:],name=f"TT{58}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,59,1:],name=f"TT{59}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,60,1:],name=f"TT{60}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,61,1:],name=f"TT{61}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,62,1:],name=f"TT{62}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,63,1:],name=f"TT{63}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,64,1:],name=f"TT{64}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,65,1:],name=f"TT{65}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,66,1:],name=f"TT{66}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,67,1:],name=f"TT{67}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,68,1:],name=f"TT{68}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,69,1:],name=f"TT{69}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,70,1:],name=f"TT{70}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,71,1:],name=f"TT{71}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,72,1:],name=f"TT{72}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,73,1:],name=f"TT{73}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,74,1:],name=f"TT{74}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,75,1:],name=f"TT{75}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,76,1:],name=f"TT{76}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,77,1:],name=f"TT{77}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,78,1:],name=f"TT{78}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,79,1:],name=f"TT{79}")(inputs)) )
separation_l.append( TTP(lay.Lambda(lambda x : x[:,80,1:],name=f"TT{80}")(inputs)) )

outputs = keras.layers.Add()(separation_l)
model = keras.Model(inputs, outputs, name='Layer1Calibrator')


##############################################################################
######################## CUSTOM TRAINING DEFINITIONS #########################
##############################################################################

optimizer = keras.optimizers.Adam(learning_rate=1E-3)
train_acc_metric = keras.metrics.RootMeanSquaredError()
val_acc_metric   = keras.metrics.RootMeanSquaredError()

history = { 'x'                  : [],
            'loss'               : [],
            'regressionLoss'     : [],
            'weightsLoss'        : [],
            'rateLoss'           : [],
            'RMSE'               : [],
            'val_loss'           : [],
            'val_regressionLoss' : [],
            'val_weightsLoss'    : [],
            'val_rateLoss'       : [],
            'val_RMSE'           : []
          }

# part of the loss that controls the regression of teh energy
def regressionLoss(y, y_pred):
    MAPE = tf.keras.losses.MeanAbsolutePercentageError()
    return MAPE(y, y_pred)

# part of the loss that controls the weights overtraining
def weightsLoss():
    modelWeights = model.trainable_weights
    modelWeights_ss = float( tf.math.reduce_sum(tf.math.square(modelWeights[0])) + tf.math.reduce_sum(tf.math.square(modelWeights[1])) + tf.math.reduce_sum(tf.math.square(modelWeights[2])) )
    return  modelWeights_ss / 50. # FIXME: scaling to be optimized

# part of the loss that controls the rate for jets
def rateLossJets(z, seedThr, jetThr):
    # predict seed energy (including the correspondong non-calibrated TT part) and apply threshold
    z_seeds_pred = TTP(z[:,40,1:]) + tf.reshape(z[:,40,0], (-1,1))
    z_seeds_AT = tf.where(z_seeds_pred>=seedThr, 1., 0.)

    # predict jet energy (including the correspondong non-calibrated TTs part) and apply threshold
    z_jet_pred = model(z, training=False) + tf.reduce_sum(z, axis=1, keepdims=True)[:,:,0]
    z_jet_AT = tf.where(z_jet_pred>=jetThr, 1., 0.)
    
    passing = tf.reduce_sum(z_seeds_AT * z_jet_AT) # do logical AND between z_seeds_AT and z_jet_AT
    total   = z.shape[0]

    return passing / total * 100 #* 2450 * 11245.6 * 0.001 / scaling # FIXME: rate to be computed? and  scaling to be defined

# part of the loss that controls the rate for e/gammas
def rateLossEgs(z, hoeThrEB, hoeThrEE, egThr):
    # predict TT energy (including the correspondong non-calibrated TT part) and apply threshold
    z_TT_pred = TTP(z[:,1:]) + tf.reshape(z[:,0], (-1,1))
    z_TT_eAT = tf.where(z_TT_pred>=egThr, 1., 0.)

    # calculate HoE for each TT and apply threshold
    z_TT_hoe = tf.reshape(z[:,0], (-1,1)) / TTP(z[:,1:]) 
    z_TT_isEB = tf.reduce_sum(z[:,2:30], axis=1, keepdims=True) * pow(2, -hoeThrEB)
    z_TT_isEE = tf.reduce_sum(z[:,30:], axis=1, keepdims=True) * pow(2, -hoeThrEE)
    hoeThr = z_TT_isEB + z_TT_isEE
    z_TT_hoeAT = tf.where(z_TT_hoe>=hoeThr, 1., 0.)

    passing = tf.reduce_sum(z_TT_hoeAT * z_TT_eAT) # do logical AND between z_TT_eAT and z_TT_hoeAT
    total   = z.shape[0]

    return passing / total * 40000 #* 2450 * 11245.6 * 0.001 / scaling # FIXME: rate to be computed? and  scaling to be defined

@tf.function
def custom_train_step(v, x, y, z):
    with tf.GradientTape() as tape:
        y_pred = model(x, training=True)
        regressionLoss_value = regressionLoss(y, y_pred)
        weightsLoss_value = weightsLoss()
        if v == 'HCAL': rateLoss_value = rateLossJets(z, 8., 100.) # remember the thresholds are in HW units!
        if v == 'ECAL': rateLoss_value = rateLossEgs(z, 3, 4, 50.) # remember the thresholds are in HW units!
        loss = regressionLoss_value + weightsLoss_value + rateLoss_value
        grads = tape.gradient(loss, model.trainable_weights)
    
    optimizer.apply_gradients(zip(grads, model.trainable_weights))
    train_acc_metric.update_state(y, y_pred)

    return loss, regressionLoss_value, weightsLoss_value, rateLoss_value, train_acc_metric.result()

@tf.function
def custom_test_step(v, x, y, z):
    y_pred = model(x, training=False)
    regressionLoss_value = regressionLoss(y, y_pred)
    weightsLoss_value = weightsLoss()
    if v == 'HCAL': rateLoss_value = rateLossJets(z, 8., 100.) # remember the thresholds are in HW units!
    if v == 'ECAL': rateLoss_value = rateLossEgs(z, 3, 4, 50.) # remember the thresholds are in HW units!
    loss = regressionLoss_value + weightsLoss_value + rateLoss_value
    val_acc_metric.update_state(y, y_pred)

    return loss, regressionLoss_value, weightsLoss_value, rateLoss_value


#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 NNModelTraining.py --in 2022_05_02_NtuplesV9 --v HCAL

if __name__ == "__main__" :
    
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",            dest="indir",            help="Input folder with X_train.npx and Y_train.npz", default=None             )
    parser.add_option("--tag",              dest="tag",              help="tag of the training folder",                    default=""               )
    parser.add_option("--v",                dest="v",                help="Ntuple type ('ECAL' or 'HCAL')",                default=None             )
    parser.add_option("--epochs",           dest="epochs",           help="Number of epochs for the training",             default=20,   type=int   )
    parser.add_option("--batch_size",       dest="batch_size",       help="Batch size for the training",                   default=1024, type=int   )
    parser.add_option("--validation_split", dest="validation_split", help="Fraction of events to be used for testing",     default=0.25, type=float )
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/model_' + options.v
    os.system('mkdir -p '+ odir)
    os.system('mkdir -p '+ odir+'/plots')

    verbose = True
    epochs = options.epochs
    batch_size = options.batch_size
    validation_split = options.validation_split

    # read testing and training datasets
    # Inside X_vec: matrix n_ev x 81 x 43 ([81 for the chucky donut towers][43 for iem, ihad, iesum, ieta])
    # Inside Y_vec: matrx n_ev x 2 (jetPt, jetPhi, jetEta, trainingPt)
    X_train = np.load(indir+'/X_train.npz')['arr_0']
    Y_train = np.load(indir+'/Y_train.npz')['arr_0']
    Z_train = np.load('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/NUtraining_rateProxy/X_train.npz')['arr_0']

    # Inside X_train: matrix n_ev x 81 x 43 ([81 for the chucky donut towers][iem, ihad, iesum, 40*ieta])
    # Inside Y_train: vector n_ev (jetPt)
    X_train, Y_train, Z_train = convert_samples(X_train, Y_train, Z_train, options.v)

    # clean from the events that are completely pusite of a regular resposne
    uncalibResp = Y_train / np.sum(X_train[:,:,1], axis=1)
    X_train = X_train[(uncalibResp < 3) & (uncalibResp > 0.3)]
    Y_train = Y_train[(uncalibResp < 3) & (uncalibResp > 0.3)]

    Xt, Xv, Yt, Yv = train_test_split(X_train, Y_train, test_size=validation_split, random_state=7)    
    x_val = tf.convert_to_tensor(Xv, dtype=tf.int64)
    y_val = tf.convert_to_tensor(Yv, dtype=tf.float32)
    x_train = tf.convert_to_tensor(Xt, dtype=tf.int64)
    y_train = tf.convert_to_tensor(Yt, dtype=tf.float32)
    z = tf.convert_to_tensor(Z_train, dtype=tf.float32)
    del X_train, Y_train, Z_train, Xt, Xv, Yt, Yv

    print(x_val.shape)
    print(y_val.shape)
    print(x_train.shape)
    print(y_train.shape)
    print(z.shape)
    exit()

    # Prepare the training dataset.
    train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    train_dataset = train_dataset.batch(batch_size)

    # Prepare the validation dataset.
    # val_dataset = tf.data.Dataset.from_tensor_slices((x_val, y_val))
    # val_dataset = val_dataset.batch(batch_size)

    # run training loop
    for epoch in range(epochs):
        start_time = time.time()
        print("\nStart of epoch %d" % (epoch+1,))

        for step, (x_batch_train, y_batch_train) in enumerate(train_dataset):
            train_loss, train_regressionLoss, train_weightLoss, train_rateLoss, train_acc = custom_train_step(options.v, x_batch_train, y_batch_train, z)

            # Log every N batches.
            if verbose and step % 1 == 0:
                print( "At batch %d (seen %d samples so far) : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f" % (step+1, (step+1)*batch_size, float(train_loss), float(train_regressionLoss), float(train_weightLoss), float(train_rateLoss), float(train_acc)) )

        # Run a validation loop at the end of each epoch.
        # for x_batch_val, y_batch_val in val_dataset:
        val_loss, val_regressionLoss, val_weightLoss, val_rateLoss = custom_test_step(options.v, x_val, y_val, z)

        train_acc = train_acc_metric.result()
        val_acc = val_acc_metric.result()
        print( "Validation : loss %4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f" % (float(val_loss), float(val_regressionLoss), float(val_weightLoss), float(val_rateLoss), float(val_acc)) )

        history['x'].append(epoch+1)
        history['loss'].append(train_loss)
        history['regressionLoss'].append(train_regressionLoss)
        history['weightsLoss'].append(train_weightLoss)
        history['rateLoss'].append(train_rateLoss)
        history['RMSE'].append(train_acc)
        history['val_loss'].append(val_loss)
        history['val_regressionLoss'].append(val_regressionLoss)
        history['val_weightsLoss'].append(val_weightLoss)
        history['val_rateLoss'].append(val_rateLoss)
        history['val_RMSE'].append(val_acc)

        # Reset metrics at the end of each epoch
        train_acc_metric.reset_states()
        val_acc_metric.reset_states()

        print("Time taken: %.2fs" % (time.time() - start_time))

    model.save(odir + '/model')
    TTP.save(odir + '/TTP')
    print('\nTrained model saved to folder: {}'.format(odir))


    import matplotlib.pyplot as plt
    import matplotlib
    import mplhep
    plt.style.use(mplhep.style.CMS)
    cmap = matplotlib.cm.get_cmap('Set1')

    plt.plot(history['x'], history['loss'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(history['x'], history['val_loss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/loss.pdf')
    plt.close()

    plt.plot(history['x'], history['RMSE'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(history['x'], history['val_RMSE'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('RMSE')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/RootMeanSquaredError.pdf')
    plt.close()

    plt.plot(history['x'], history['regressionLoss'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(history['x'], history['val_regressionLoss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Regression loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/regressionLoss.pdf')
    plt.close()

    plt.plot(history['x'], history['weightsLoss'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(history['x'], history['val_weightsLoss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Weights loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/weightsLoss.pdf')
    plt.close()

    plt.plot(history['x'], history['rateLoss'], label='Taining', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(history['x'], history['val_rateLoss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Rate loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/rateLoss.pdf')
    plt.close()

    plt.plot(history['x'], history['regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(history['x'], history['weightsLoss'], label='Weights loss', lw=2, ls='-', marker='o', color=cmap(1))
    plt.plot(history['x'], history['rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(2))
    plt.ylabel('Loss breakdown')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/trainLosses.pdf')
    plt.close()

    plt.plot(history['x'], history['val_regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(history['x'], history['val_weightsLoss'], label='Weights loss', lw=2, ls='-', marker='o', color=cmap(1))
    plt.plot(history['x'], history['val_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(2))
    plt.ylabel('Loss breakdown')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/validLosses.pdf')
    plt.close()
