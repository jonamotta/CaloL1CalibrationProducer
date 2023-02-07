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
            Z = np.delete(Z, 2, axis=2)
            Z = Z[ Z[:,:,0] != 0 ] # remove TTs that have iEM == 0 (this already reshapes so that every TT becomes an event)
            Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have iem on the right

    elif version == 'HCAL':
        X = np.delete(X, 2, axis=2)
        if not Z is None: Z = np.delete(Z, 2, axis=2)
        
    return X, Y, Z

def applyECALcalib(Z, TTP):
    xDim = Z.shape[0] ; yDim = 81 ; zDim = 42
    Z = Z.reshape(xDim*yDim, zDim) # reshape so that every TT becomes an event
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    # TT_em_pred = tf.cast(TTP.predict(Z[:,1:], batch_size=2048), dtype=tf.int16)
    TT_em_pred = TTP.predict(Z[:,1:], batch_size=2048) # CAST REMOVED
    Z[:,[0,1]] = Z[:,[1,0]] # order iem and ihad to have the needed one on the right
    Z[:,[0]] = TT_em_pred
    Z = Z.reshape(xDim, yDim, zDim) # reshape so that 81xTT becomes an event again
    return Z


##############################################################################
############################## MODEL DEFINITION ##############################
##############################################################################

# flooring custom gradient
@tf.custom_gradient
def Fgrad(x):
    def fgrad(dy):
        return dy
    return tf.floor(x), fgrad

def create_model():
    inputs = keras.Input(shape = (81,42), name = 'chunky_donut')
    layer1 = Dense(164, name = 'nn1', input_dim=41, activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    layer2 = Dense(512, name = 'nn2',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    layer3 = Dense(1,   name = 'nn3',               activation='relu', kernel_initializer=RN(seed=7), use_bias=False)
    layer4 = lay.Lambda(Fgrad)

    TTP = Sequential()
    TTP.add(layer1)
    TTP.add(layer2)
    TTP.add(layer3)
    TTP.add(layer4)

    separation_l = []
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,0,1:],  name=f"tt{0}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,1,1:],  name=f"tt{1}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,2,1:],  name=f"tt{2}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,3,1:],  name=f"tt{3}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,4,1:],  name=f"tt{4}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,5,1:],  name=f"tt{5}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,6,1:],  name=f"tt{6}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,7,1:],  name=f"tt{7}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,8,1:],  name=f"tt{8}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,9,1:],  name=f"tt{9}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,10,1:], name=f"tt{10}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,11,1:], name=f"tt{11}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,12,1:], name=f"tt{12}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,13,1:], name=f"tt{13}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,14,1:], name=f"tt{14}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,15,1:], name=f"tt{15}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,16,1:], name=f"tt{16}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,17,1:], name=f"tt{17}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,18,1:], name=f"tt{18}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,19,1:], name=f"tt{19}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,20,1:], name=f"tt{20}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,21,1:], name=f"tt{21}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,22,1:], name=f"tt{22}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,23,1:], name=f"tt{23}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,24,1:], name=f"tt{24}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,25,1:], name=f"tt{25}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,26,1:], name=f"tt{26}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,27,1:], name=f"tt{27}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,28,1:], name=f"tt{28}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,29,1:], name=f"tt{29}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,30,1:], name=f"tt{30}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,31,1:], name=f"tt{31}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,32,1:], name=f"tt{32}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,33,1:], name=f"tt{33}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,34,1:], name=f"tt{34}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,35,1:], name=f"tt{35}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,36,1:], name=f"tt{36}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,37,1:], name=f"tt{37}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,38,1:], name=f"tt{38}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,39,1:], name=f"tt{39}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,40,1:], name=f"tt{40}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,41,1:], name=f"tt{41}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,42,1:], name=f"tt{42}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,43,1:], name=f"tt{43}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,44,1:], name=f"tt{44}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,45,1:], name=f"tt{45}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,46,1:], name=f"tt{46}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,47,1:], name=f"tt{47}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,48,1:], name=f"tt{48}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,49,1:], name=f"tt{49}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,50,1:], name=f"tt{50}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,51,1:], name=f"tt{51}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,52,1:], name=f"tt{52}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,53,1:], name=f"tt{53}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,54,1:], name=f"tt{54}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,55,1:], name=f"tt{55}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,56,1:], name=f"tt{56}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,57,1:], name=f"tt{57}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,58,1:], name=f"tt{58}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,59,1:], name=f"tt{59}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,60,1:], name=f"tt{60}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,61,1:], name=f"tt{61}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,62,1:], name=f"tt{62}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,63,1:], name=f"tt{63}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,64,1:], name=f"tt{64}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,65,1:], name=f"tt{65}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,66,1:], name=f"tt{66}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,67,1:], name=f"tt{67}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,68,1:], name=f"tt{68}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,69,1:], name=f"tt{69}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,70,1:], name=f"tt{70}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,71,1:], name=f"tt{71}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,72,1:], name=f"tt{72}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,73,1:], name=f"tt{73}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,74,1:], name=f"tt{74}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,75,1:], name=f"tt{75}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,76,1:], name=f"tt{76}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,77,1:], name=f"tt{77}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,78,1:], name=f"tt{78}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,79,1:], name=f"tt{79}")(inputs)) )
    separation_l.append( TTP(lay.Lambda(lambda x : x[:,80,1:], name=f"tt{80}")(inputs)) )

    outputs = keras.layers.Add()(separation_l)
    model = keras.Model(inputs, outputs, name='Layer1Calibrator')

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
    parser.add_option("--ngpus",            dest="ngpus",            help="Number of GPUs on which to distribute",         default=2,     type=int            )
    parser.add_option("--epochs",           dest="epochs",           help="Number of epochs for the training",             default=20,    type=int            )
    parser.add_option("--batch_size",       dest="batch_size",       help="Batch size for the training",                   default=1024,  type=int            )
    parser.add_option("--validation_split", dest="validation_split", help="Fraction of events to be used for testing",     default=0.25,  type=float          )
    parser.add_option("--no-verbose",       dest="verbose",          help="Deactivate verbose training",                   default=True,  action='store_false')
    parser.add_option("--readTfDatasets",   dest="readTfDatasets",   help="Do not do pre-processing and load TF datasets", default=False, action='store_true' )
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/model_' + options.v
    CKPTdir = odir+'/training_checkpoints'
    CKPTpf = os.path.join(CKPTdir, "ckpt")
    os.system('mkdir -p '+ odir)
    os.system('mkdir -p '+ odir+'/plots')
    os.system('mkdir -p '+ CKPTdir)


    ##############################################################################
    ########################### TRAINING SETUP VARIABLES #########################
    ##############################################################################

    VERBOSE = options.verbose
    VERSION = options.v
    NGPUS = options.ngpus
    BUFFER_SIZE = int(1E7)
    BATCH_SIZE_PER_REPLICA = options.batch_size
    GLOBAL_BATCH_SIZE = BATCH_SIZE_PER_REPLICA * NGPUS
    EPOCHS = options.epochs
    MAX_LEARNING_RATE = 1E-3
    RATE_STEPIN_FQ = 5
    RATE_STEPIN_RESIDUAL = 0
    N_RATE_EVTS_xGPU = 50000 * NGPUS # for the rate select NGPUS multiple of number of events and batch by the same value to have one batch per GPU
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
            Z_train = np.load('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/NUtraining_rateProxy/X_train.npz')['arr_0']
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
                ECAL_TTPmodel = keras.models.load_model('/data_CMS/cms/motta/CaloL1calibraton/'+options.indir+'/ECALtraining_0pt500/model_ECAL/TTP', compile=False, custom_objects={'Fgrad': Fgrad})
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
    train_dataset = train_dataset.batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    test_dataset = test_dataset.batch(GLOBAL_BATCH_SIZE, drop_remainder=True)
    rate_dataset = rate_dataset.take(N_RATE_EVTS_xGPU)
    rate_dataset = rate_dataset.batch(N_RATE_EVTS_xGPU, drop_remainder=True)
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
                                                   experimental_per_replica_buffer_size=1)

    print('** INFO : distributing training datasets')
    train_dist_dataset = mirrored_strategy.experimental_distribute_dataset(train_dataset, options=DISTRIBUTION_OPTS)
    test_dist_dataset = mirrored_strategy.experimental_distribute_dataset(test_dataset, options=DISTRIBUTION_OPTS)
    rate_dist_dataset = mirrored_strategy.experimental_distribute_dataset(rate_dataset, options=DISTRIBUTION_OPTS)
    del train_dataset, test_dataset, rate_dataset
    print('** INFO : done distributing training datasets')

    '''
    ## THE FOLLOWING PART IS AN ATTEMPT TO STORE THE REPLICAS DIRECTLY ON DEVICE BUT THIS SEEMS TO JAM THE MEMORY AND IMMENSLY SLOW DOWN THE GPUs
    def create_dataset_fn_with_args(path, batch_size, truncation=None):
        def create_dataset_fn(input_context):
            dataset = tf.data.experimental.load(path, compression='GZIP')
            if truncation: dataset.take(truncation)
            dataset = dataset.batch(batch_size, drop_remainder=True)
            return dataset
        return create_dataset_fn

    DISTRIBUTION_OPTS = tf.distribute.InputOptions(experimental_fetch_to_device=False,
                                                   experimental_replication_mode=tf.distribute.InputReplicationMode.PER_REPLICA,
                                                   experimental_place_dataset_on_device=True,
                                                   experimental_per_replica_buffer_size=5)

    print('** INFO : re-loading, batching, and distributing datasets')
    create_dataset_fn = create_dataset_fn_with_args(indir+'/train_TfDataset', GLOBAL_BATCH_SIZE)
    train_dist_dataset = mirrored_strategy.distribute_datasets_from_function(create_dataset_fn, options=DISTRIBUTION_OPTS)

    create_dataset_fn = create_dataset_fn_with_args(indir+'/test_TfDataset', GLOBAL_BATCH_SIZE)
    test_dist_dataset = mirrored_strategy.distribute_datasets_from_function(create_dataset_fn, options=DISTRIBUTION_OPTS)

    create_dataset_fn = create_dataset_fn_with_args(indir+'/rate_TfDataset', N_RATE_EVTS_xGPU, N_RATE_EVTS_xGPU)
    rate_dist_dataset = mirrored_strategy.distribute_datasets_from_function(create_dataset_fn, options=DISTRIBUTION_OPTS)

    # del train_dataset, test_dataset, rate_dataset # free some memory
    print('** INFO : done re-loading, batching, and distributing datasets')
    ## THE ABOVE PART IS AN ATTEMPT TO STORE THE REPLICAS DIRECTLY ON DEVICE BUT THIS SEEMS TO JAM THE MEMORY AND IMMENSLY SLOW DOWN THE GPUs
    '''

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
            return modelWeights_ss * 1 # FIXME: scaling to be optimized

        def threshold_relaxation_sigmoid(x, mean, sharpness):
            k = sharpness * (x - mean)
            return tf.sigmoid(k)

        def threshold_relaxation_inverseSigmoid(x, mean, sharpness):
            k = sharpness * (x - mean)
            return tf.sigmoid(-k)

        #part of the loss that controls the rate for jets
        def rateLossJets(z, seedThr, jetThr):
            # predict seed energy (including the correspondong non-calibrated TT part) and apply threshold
            # TT_seed_pred = tf.cast(TTP(z[:,40,1:]), dtype=tf.int16) + tf.reshape(z[:,40,0], (-1,1))
            TT_seed_pred = TTP(z[:,40,1:]) + tf.reshape(z[:,40,0], (-1,1)) # CAST REMOVED
            TT_seed_AT = tf.where(TT_seed_pred>=seedThr, 1., 0.)

            # predict jet energy (including the correspondong non-calibrated TTs part) and apply threshold
            # jet_pred = model(z, training=False) + tf.cast(tf.reduce_sum(z, axis=1, keepdims=True)[:,:,0], dtype=tf.float32)
            jet_pred = model(z, training=False) + tf.reduce_sum(z, axis=1, keepdims=True)[:,:,0] # CAST REMOVED
            jet_AT = tf.where(jet_pred>=jetThr, 1., 0.)
            
            passing = tf.reduce_sum(TT_seed_AT * jet_AT, keepdims=True) # do logical AND between z_seeds_AT and z_jet_AT
            proxyRate = passing / z.shape[0] * 0.001*2500*11245.6
            targetRate = 30.048183 # computed from the old calibration in the smae manner as here

            return pow(proxyRate - targetRate, 6) # FIXME: scaling to be defined
            # return tf.exp(proxyRate - targetRate) # FIXME: scaling to be defined

        # part of the loss that controls the rate for e/gammas
        def rateLossEgs(z, hoeThrEB, hoeThrEE, egThr):
            # 'hardcoded' threshold on hcal over ecal deposit
            hasEBthr = tf.reduce_sum(z[:,2:30], axis=1, keepdims=True) * pow(2, -hoeThrEB)
            hasEEthr = tf.reduce_sum(z[:,30:], axis=1, keepdims=True) * pow(2, -hoeThrEE)
            hoeThr = hasEBthr + hasEEthr

            # hadronic deposit behind the ecal one
            TT_had = tf.reshape(z[:,0], (-1,1))

            # predict TT energy, add correspondong non-calibrated had part, and apply threshold
            TT_em_pred = TTP(z[:,1:])
            TT_pred = TT_em_pred + TT_had
            TT_eAT = threshold_relaxation_sigmoid(TT_pred, egThr, 5.)

            # calculate HoE for each TT and apply threshold
            TT_hoe = TT_had / TT_em_pred
            TT_hoeAT = threshold_relaxation_inverseSigmoid(TT_hoe, hoeThr, 1000.)

            passing = tf.reduce_sum(TT_hoeAT * TT_eAT, keepdims=True) # do logical AND between TT_eAT and TT_hoeAT
            proxyRate = passing / z.shape[0] * 0.001*2500*11245.6
            targetRate = 3756.696 # computed from the old calibration in the same manner as here
            realtive_diff = (proxyRate - targetRate) / targetRate * 100

            return tf.exp(realtive_diff)

        # GPU distribution friendly loss computation
        def compute_train_losses(y, y_pred, z):
            regressionLoss_value = regressionLoss(y, y_pred)
            weightsLoss_value = weightsLoss()
            if VERSION == 'HCAL': rateLoss_value = rateLossJets(z, 8, 100.) # remember the thresholds are in HW units!
            if VERSION == 'ECAL': rateLoss_value = rateLossEgs(z, 3, 4, 50) # remember the thresholds are in HW units!
            fullLoss = regressionLoss_value + weightsLoss_value + rateLoss_value

            return [tf.nn.compute_average_loss(fullLoss,             global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(regressionLoss_value, global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(weightsLoss_value,    global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(rateLoss_value,       global_batch_size=GLOBAL_BATCH_SIZE)]

        # GPU distribution friendly loss computation
        def compute_train_losses_withoutRate(y, y_pred):
            regressionLoss_value = regressionLoss(y, y_pred)
            weightsLoss_value = weightsLoss()
            rateLoss_value = tf.constant([0.0])
            fullLoss = regressionLoss_value + weightsLoss_value + rateLoss_value

            return [tf.nn.compute_average_loss(fullLoss,             global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(regressionLoss_value, global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(weightsLoss_value,    global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(rateLoss_value,       global_batch_size=GLOBAL_BATCH_SIZE)]

        # GPU distribution friendly loss computation
        def compute_test_losses(y, y_pred):
            regressionLoss_value = regressionLoss(y, y_pred)
            weightsLoss_value = weightsLoss()
            fullLoss = regressionLoss_value + weightsLoss_value

            return [tf.nn.compute_average_loss(fullLoss,             global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(regressionLoss_value, global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(weightsLoss_value,    global_batch_size=GLOBAL_BATCH_SIZE)]

        model, TTP = create_model()
        optimizer = keras.optimizers.Adam(learning_rate=MAX_LEARNING_RATE)
        checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
        train_acc_metric = keras.metrics.RootMeanSquaredError(name='train_accuracy')
        test_acc_metric  = keras.metrics.RootMeanSquaredError(name='test_accuracy')

    def custom_train_step(inputs, rate_inputs):
        x, y = inputs
        if not rate_inputs is None: z, _ = rate_inputs
        with tf.GradientTape() as tape:
            y_pred = model(x, training=True)
            if not rate_inputs is None: losses = compute_train_losses(y, y_pred, z)
            else:                       losses = compute_train_losses_withoutRate(y, y_pred)
            
        grads = tape.gradient(losses[3], model.trainable_weights)

        print(optimizer.get_gradients(losses[3], model.trainable_weights))

        optimizer.apply_gradients(zip(grads, model.trainable_weights))
        train_acc_metric.update_state(y, y_pred)

        return losses

    def custom_test_step(inputs):
        x, y = inputs
        y_pred = model(x, training=False)
        losses = compute_test_losses(y, y_pred)
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
    def distributed_test_step(dataset_inputs):
        per_replica_losses = mirrored_strategy.run(custom_test_step, args=(dataset_inputs,))
        return [mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[0], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[1], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[2], axis=None)]


    # run training loop
    for epoch in range(EPOCHS):
        start_time = time.time()
        print('\nStart of epoch %d' % (epoch+1,))

        # settings for the stepping function learning rate
        if RATE_STEPIN_RESIDUAL >= RATE_STEPIN_FQ: RATE_STEPIN_RESIDUAL = 0 

        # TRAIN LOOP
        train_losses = np.array([0., 0., 0., 0.])
        num_batches = 0
        for batch in train_dist_dataset:
            # stepping function learning rate
            LR = step_funtion_learning_rate_schedule(num_batches, MAX_LEARNING_RATE, RATE_STEPIN_FQ, RATE_STEPIN_RESIDUAL)
            optimizer.lr = LR
            HISTORY['learning_rate'][epoch].append(LR)

            if num_batches % RATE_STEPIN_FQ == RATE_STEPIN_RESIDUAL:
                for rate_batch in rate_dist_dataset:
                    train_losses = distributed_train_step(batch, rate_batch)
            else:
                train_losses = distributed_train_step(batch, None)

            num_batches += 1

            # Log every N batches
            if VERBOSE and num_batches % 1 == 0:
                print('    At batch %d (seen %d samples so far) : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f ; LR = %.4f' % (num_batches, num_batches*GLOBAL_BATCH_SIZE, float(train_losses[0]), float(train_losses[1]), float(train_losses[2]), float(train_losses[3]), float(train_acc_metric.result()), LR) )

        # settings for the stepping function learning rate
        RATE_STEPIN_RESIDUAL += 1

        # TEST LOOP
        test_losses = np.array([0., 0., 0.])
        num_batches = 0
        for batch in test_dist_dataset:
            test_losses += distributed_test_step(batch)
            num_batches += 1

        test_losses = test_losses / num_batches
        test_losses[0] += train_losses[3]

        train_RMSE = train_acc_metric.result()
        test_RMSE = test_acc_metric.result()
        print('Training : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(train_losses[0]), float(train_losses[1]), float(train_losses[2]), float(train_losses[3]), float(train_RMSE)) )
        print('Testing  : loss = %.4f ; regressionLoss = %.4f ; weightsLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(test_losses[0]), float(test_losses[1]), float(test_losses[2]), float(train_losses[3]), float(test_RMSE)) )

        HISTORY['x'].append(epoch+1)
        if epoch < EPOCHS-1: HISTORY['learning_rate'].append([])
        HISTORY['train_loss'].append(float(train_losses[0]))
        HISTORY['train_regressionLoss'].append(float(train_losses[1]))
        HISTORY['train_weightsLoss'].append(float(train_losses[2]))
        HISTORY['train_rateLoss'].append(float(train_losses[3]))
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
