import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import random
import mplhep
import json
import time
import glob
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

def makePlots(HISTORY, odir):
    plt.style.use(mplhep.style.CMS)
    cmap = matplotlib.cm.get_cmap('Set1')

    plt.plot(HISTORY['x'], HISTORY['train_loss'], label='Training', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_loss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/loss.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['train_RMSE'], label='Training', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_RMSE'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('RMSE')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/RootMeanSquaredError.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['train_regressionLoss'], label='Training', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_regressionLoss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Regression loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/regressionLoss.pdf')
    plt.close()

    plt.plot(HISTORY['x'][1:], HISTORY['train_regressionLoss'][1:], label='Training', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'][1:], HISTORY['test_regressionLoss'][1:], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
    plt.ylabel('Regression loss')
    plt.xlabel('Epoch')
    plt.grid()
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    mplhep.cms.label('Preliminary', data=True, rlabel=r'')
    plt.savefig(odir+'/plots/regressionLoss_zoom.pdf')
    plt.close()

    plt.plot(HISTORY['x'], HISTORY['train_rateLoss'], label='Training', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['test_rateLoss'], label='Testing', lw=2, ls='-', marker='o', color=cmap(1))
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

    plt.plot(HISTORY['x'], HISTORY['train_regressionLoss'], label='Regression loss', lw=2, ls='-', marker='o', color=cmap(0))
    plt.plot(HISTORY['x'], HISTORY['train_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(1))
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
    plt.plot(HISTORY['x'], HISTORY['test_rateLoss'], label='Rate loss', lw=2, ls='-', marker='o', color=cmap(1))
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

def create_model(version, seedThr=None):

    ####################### TTP #######################
    # The TTP_input is a vector of 9x9 chunky donuts before calibration
    TTP_input = keras.Input(shape=(81,42), dtype=tf.float32, name='chunky_donut')
    
    layer1 = Dense(82,  name='nn1', input_dim=41, activation='relu', kernel_initializer=RN(mean=1.0, seed=7), use_bias=False)
    layer2 = Dense(256, name='nn2',               activation='relu', kernel_initializer=RN(mean=1.0, seed=7), use_bias=False)
    layer3 = Dense(1,   name='nn3',               activation='relu', kernel_initializer=RN(mean=1.0, seed=7), use_bias=False)
    layer4 = lay.Lambda(Fgrad)

    TTP = Sequential(name="ttp")
    TTP.add(layer1)
    TTP.add(layer2)
    TTP.add(layer3)
    TTP.add(layer4)

    MainPredictionList = make_AddList(TTP, TTP_input)
    TTP_output = lay.Add(name="main_predicted_energy")(MainPredictionList)
    # The TTP_output is a vector of calibrated L1 jet energies, after the summation layer
    
    ####################### RATE #######################
    # The rate_input is a vector of 9x9 chunky donuts before calibration
    rate_input = keras.Input(shape=(81,42), dtype=tf.float32, name='rate_proxy')

    seedThr = seedThr - 0.1
    numThr = 1 - 0.1

    # for each jet, compute the iesum
    if version == 'HCAL' or version == 'HF':

        # for each tower apply sigmoid cut on the seed at seedThr (8): if tower energy > 8 jet_seed_found = 1, else 0
        jet_em  = lay.Lambda(lambda x : tf.reduce_sum(x, axis=1, keepdims=True)[:,:,0], name='jet_em_deposit')(rate_input)
        jet_had = make_AddList(TTP, rate_input, name="jet_had_deposit")
        jet_iesum = lay.Lambda(lambda x : x[0] + x[1], name="seed_tot_energy")((jet_em, jet_had))
        
        # for each tower apply sigmoid cut on the seed at seedThr (8): if tower energy > 8 jet_seed_found = 1, else 0
        jet_seed_found = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, seedThr, 1000.), name="apply_seed_threshold")(jet_iesum)
        # for each jet compute how many seeds were found
        jet_seed_number = lay.Lambda(lambda x : tf.reduce_sum(x, axis=1, keepdims=True), name='seed_numbers')(jet_seed_found)
        # for each jet check the presence of at least one seed
        jet_seed_passing = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, numThr, 1000.), name="pass_seed_threshold")(jet_seed_number)

        rate_output = lay.Lambda(lambda x : x[0] * x[1], name="thresholds_or")((jet_seed_passing, jet_iesum))
        # The rate_output is a vector of calibrated L1 jet energies !!! only for jets passing the seed threshold !!!, after the summation layer

    # [FIXME] HERE WE NEED TO CHANGE THE WAY OF COMPUTING THE RATE PROXY
    if version == 'ECAL':
        # # 'hardcoded' threshold on hcal over ecal deposit
        # hasEBthr = lay.Lambda(lambda x : tf.reduce_sum(x[:,2:30], axis=1, keepdims=True) * pow(2, -hoeThrEB), name='has_hoe_eb_thr')(rate_input)
        # hasEEthr = lay.Lambda(lambda x : tf.reduce_sum(x[:,30:], axis=1, keepdims=True) * pow(2, -hoeThrEE), name='has_hoe_ee_thr')(rate_input)
        # hoeThr = lay.Lambda(lambda x : x[0] + x[1], name="has_hoe_thr")((hasEBthr, hasEEthr))

        # # hadronic deposit behind the ecal one
        # TT_had = lay.Lambda(lambda x : x[:,0:1], name='tt_had_deposit')(rate_input)

        # # # predict TT energy, add correspondong non-calibrated had part, and apply threshold
        # TT_em_pred = TTP(lay.Lambda(lambda x : x[:,1:], name="tt_em_pred")(rate_input))
        # TT_pred = lay.Lambda(lambda x : x[0] + x[1], name="tt_tot_energy")((TT_em_pred, TT_had))
        # TT_eAT = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, egThr, 10.), name="apply_eg_threshold")(TT_pred) # sharpness 10. means +/-0.5 GeV tunron region

        # # # calculate HoE for each TT and apply threshold (this is a <= threshold so need 1-sigmoid)
        # TT_hoe = lay.Lambda(lambda x : tf.math.divide_no_nan(x[0], x[1]), name="compute_tt_hoe")((TT_had, TT_em_pred))
        # TT_hoeAT = lay.Lambda(lambda x : threshold_relaxation_inverseSigmoid(x[0], x[1], 1000.), name="apply_hoe_threshold")((TT_hoe,hoeThr)) # sharpness 1000. means +/-0.005 tunron region

        # # do logical AND between TT_eAT and TT_hoeAT
        # rate_output = lay.Lambda(lambda x : x[0] * x[1], name="thresholds_or")((TT_eAT, TT_hoeAT))

        # no need to apply the hoe cut anymore, since it's intrinsically included in the cluster
        # new structure of the rate input for ECAL

        egThr = 10
        # predict jet energy and apply threshold: sum all the ihad energies z[:,:,0] of the 9x9 and all the iem energies z[:,:,1] of the 9x9
        # sum hadronic deposit behind the ecal one
        eg_had = lay.Lambda(lambda x : tf.reduce_sum(x, axis=1, keepdims=True)[:,:,0], name='eg_had_deposit')(rate_input)
        # apply model to the em component
        RatePredictionList = make_AddList(TTP, rate_input, name="rate_")
        eg_em_pred = lay.Add(name="rate_predicted_energy")(RatePredictionList)
        # sum had energy and calibrated em energy
        eg_pred = lay.Lambda(lambda x : x[0] + x[1], name="eg_tot_energy")((eg_em_pred, eg_had))
        # apply threshold
        eg_AT = lay.Lambda(lambda x : threshold_relaxation_sigmoid(x, egThr, 10.), name="apply_eg_threshold")(eg_pred) # sharpness 10. means +/-0.5 GeV tunron region
        rate_output = eg_AT

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
    parser.add_option("--indir",            dest="indir",            help="Base input and output folder",                  default=None                       )
    parser.add_option("--tag",              dest="tag",              help="Tag of the training folder",                    default=""                         )
    parser.add_option("--v",                dest="v",                help="Which training to perform: ECAL or HCAL?",      default=None                       )
    parser.add_option("--ngpus",            dest="ngpus",            help="Number of GPUs on which to distribute",         default=4,     type=int            )
    parser.add_option("--epochs",           dest="epochs",           help="Number of epochs for the training",             default=20,    type=int            )
    parser.add_option("--batch_size",       dest="batch_size",       help="Batch size for the training",                   default=2048,  type=int            )
    parser.add_option("--no-verbose",       dest="verbose",          help="Deactivate verbose training",                   default=True,  action='store_false')
    parser.add_option("--makeOnlyPlots",    dest="makeOnlyPlots",    help="Do not do the training, just make the plots",   default=False, action='store_true' )
    parser.add_option("--addtag",           dest="addtag",           help="Add tag to distinguish different trainings",    default="",                        )
    parser.add_option("--MaxLR",            dest="MaxLR",            help="Maximum learning rate",                         default='1E-3')
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/model_' + options.v + options.addtag
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
    MAX_LEARNING_RATE = float(options.MaxLR)
    HISTORY = { 'x'        : [],
                'learning_rate': [[]],
                'train_loss' : [], 'train_regressionLoss' : [], 'train_rateLoss' : [], 'train_RMSE' : [],
                'test_loss'  : [], 'test_regressionLoss'  : [], 'test_rateLoss'  : [], 'test_RMSE'  : []
              }
    # new method to change learning rate over time (not to miss local minima)
    lr_schedule = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=MAX_LEARNING_RATE, decay_steps=5, decay_rate=0.1)

    ##############################################################################
    ################################# LOAD INPUTS ################################
    ##############################################################################

    with tf.device('/CPU:0'):
        # description of the features for reading out
        feature_description = {
            'chuncky_donut': tf.io.FixedLenFeature([], tf.string, default_value=''), # byteslist to be read as string 
            'trainingPt'   : tf.io.FixedLenFeature([], tf.float32, default_value=0)  # single float values
        }

        # parse proto input based on description
        def parse_function(example_proto):
            example = tf.io.parse_single_example(example_proto, feature_description)
            chuncky_donut = tf.io.parse_tensor(example['chuncky_donut'], out_type=tf.float32) # decode byteslist to original 81x43 tensor
            return chuncky_donut, example['trainingPt']

        # read raw training dataset and parse it 
        InTrainRecords = glob.glob(indir+'/trainTFRecords/record_*.tfrecord')
        raw_train_dataset = tf.data.TFRecordDataset(InTrainRecords)
        train_dataset = raw_train_dataset.map(parse_function)
        del InTrainRecords, raw_train_dataset

        # read raw testing dataset and parse it 
        InTestRecords = glob.glob(indir+'/testTFRecords/record_*.tfrecord')
        raw_test_dataset = tf.data.TFRecordDataset(InTestRecords)
        test_dataset = raw_test_dataset.map(parse_function)
        del InTestRecords, raw_test_dataset

        # read raw rate dataset and parse it 
        InRateRecords = glob.glob(indir+'/rateTFRecords/record_*.tfrecord')
        raw_rate_dataset = tf.data.TFRecordDataset(InRateRecords)
        rate_dataset = raw_rate_dataset.map(parse_function)
        del InRateRecords, raw_rate_dataset

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
    test_dist_dataset  = mirrored_strategy.experimental_distribute_dataset(test_dataset,  options=DISTRIBUTION_OPTS)
    rate_dist_dataset  = mirrored_strategy.experimental_distribute_dataset(rate_dataset,  options=DISTRIBUTION_OPTS)
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

        # part of the loss that controls the rate
        def rateLoss(z_pred, jetThr, targetRate):
            jetThr = jetThr - 0.1
            # compute fraction of passing events and multiply by rate scaling
            jets_passing_threshold = threshold_relaxation_sigmoid(z_pred, jetThr, 10.)
            proxyRate = tf.reduce_sum(jets_passing_threshold, keepdims=True) / BATCH_SIZE_PER_REPLICA
            realtive_diff = (proxyRate - targetRate)
            return tf.cosh(1.5 * realtive_diff) # FIXME: scaling to be optimized
            # sharpness of 10 corresponds to +/- 1 kHz
            # return threshold_relaxation_sigmoid(proxyRate, targetRate, 0.1) # FIXME: scaling to be optimized

        # GPU distribution friendly loss computation
        def compute_losses(y, y_pred, z_pred):
            regressionLoss_value = regressionLoss(y, y_pred)

            # normal regions computed on ZeroBias
            if VERSION == 'ECAL': 
                rateLoss_value = rateLoss(z_pred, 44.63708) # [FIXME]
            if VERSION == 'HCAL': 
                rateLoss_value_50 = rateLoss(z_pred, 100, 0.05906486977242875)
                # rateLoss_value_40 = rateLoss(z_pred, 80, 0.13216800071384716)
                # rateLoss_value_30 = rateLoss(z_pred, 60, 0.43565990767259705)
                # rateLoss_value = (rateLoss_value_50 + rateLoss_value_40 + rateLoss_value_30) * 100
                rateLoss_value = rateLoss_value_50 * 10000

            fullLoss = regressionLoss_value + rateLoss_value

            return [tf.nn.compute_average_loss(fullLoss,             global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(regressionLoss_value, global_batch_size=GLOBAL_BATCH_SIZE),
                    tf.nn.compute_average_loss(rateLoss_value,       global_batch_size=GLOBAL_BATCH_SIZE)]

        # define model and related stuff
        model, TTP = create_model(VERSION, seedThr=8.)
        # optimizer = keras.optimizers.Adam(learning_rate=lr_schedule)
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

        # grads = tape.gradient([losses[1], losses[2], losses[3]], model.trainable_weights)
        # suggested by Frederic but it doesn't work
        grads = tape.gradient(losses[0], model.trainable_weights)
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
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[2], axis=None)]

    @tf.function
    def distributed_test_step(dataset_inputs, rate_inputs):
        per_replica_losses = mirrored_strategy.run(custom_test_step, args=(dataset_inputs, rate_inputs,))
        return [mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[0], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[1], axis=None),
                mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses[2], axis=None)]


    # run training loop
    for epoch in range(EPOCHS):
        start_time = time.time()
        print('\nStart of epoch %d' % (epoch+1,))

        # TRAIN LOOP
        train_losses = np.array([0., 0., 0.])
        train_losses_avg = np.array([0., 0., 0.])
        num_batches = 0
        for batch, rate_batch in zip(train_dist_dataset, rate_dist_dataset):
            train_losses = distributed_train_step(batch, rate_batch)
            train_losses_avg += train_losses
            num_batches += 1

            # Log every N batches
            if VERBOSE and num_batches % 1 == 0:
                print(
                      '    At batch %d (seen %d samples so far) : loss = %.4f ; regressionLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f'
                      %
                      (num_batches, num_batches*GLOBAL_BATCH_SIZE, float(train_losses[0]), float(train_losses[1]), float(train_losses[2]), float(train_acc_metric.result()))
                     )

        train_losses_avg = train_losses_avg / num_batches

        # TEST LOOP
        test_losses = np.array([0., 0., 0.])
        num_batches = 0
        for batch, rate_batch in zip(test_dist_dataset, rate_dist_dataset):
            test_losses += distributed_test_step(batch, rate_batch)
            num_batches += 1

        test_losses = test_losses / num_batches

        train_RMSE = train_acc_metric.result()
        test_RMSE = test_acc_metric.result()
        print('Training : loss = %.4f ; regressionLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(train_losses_avg[0]), float(train_losses_avg[1]), float(train_losses_avg[2]), float(train_RMSE)) )
        print('Testing  : loss = %.4f ; regressionLoss = %.4f ; rateLoss = %.4f ; RMSE = %.4f' % (float(test_losses[0]), float(test_losses[1]), float(test_losses[2]), float(test_RMSE)) )

        HISTORY['x'].append(epoch+1)
        if epoch < EPOCHS-1: HISTORY['learning_rate'].append([])
        HISTORY['train_loss'].append(float(train_losses_avg[0]))
        HISTORY['train_regressionLoss'].append(float(train_losses_avg[1]))
        HISTORY['train_rateLoss'].append(float(train_losses_avg[2]))
        HISTORY['train_RMSE'].append(float(train_RMSE))
        HISTORY['test_loss'].append(float(test_losses[0]))
        HISTORY['test_regressionLoss'].append(float(test_losses[1]))
        HISTORY['test_rateLoss'].append(float(train_losses[2]))
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
    
    
