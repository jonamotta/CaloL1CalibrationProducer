#librairies utiles
import numpy as np
import os
import sys
import copy
import pandas as pd
import matplotlib.pyplot as plt
# from NNModelTraining import *
# from NNModelTraining_FlooringAfterTTP import *
# from NNModelTraining_FlooringInTTP import *
from NNModelTraining_FlooringInTTP_nTTweighing import *
sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *


#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 CalibrationFactor.py --in 2022_04_21_NtuplesV1 --v ECAL 

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",    dest="indir",   help="Input folder with trained model", default=None)
    parser.add_option("--tag",      dest="tag",     help="tag of the training folder",      default="")
    parser.add_option("--out",      dest="odir",    help="Output folder",                   default=None)
    parser.add_option("--v",        dest="v",       help="Ntuple type ('ECAL' or 'HCAL')",  default='ECAL')
    parser.add_option("--maxeta",   dest="maxeta",  help="Eta tower max",                   default=None)
    parser.add_option("--padZeros", dest="padZeros", help="fill 0.0 SF to closest neighbour value", action='store_true', default=False)
    parser.add_option("--saturateAt", dest="saturateAt", help="saturate SFs at X value", type=float, default=None)
    (options, args) = parser.parse_args()
    print(options)

    label = ''
    if options.saturateAt: label = '_saturatedAt'+str(options.saturateAt).split('.')[0]+'p'+str(options.saturateAt).split('.')[1]

    # Definition of the trained model
    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    modeldir = indir + '/model_' + options.v
    print('\nModel dir = {}\n'.format(modeldir))

    model1 = keras.models.load_model(modeldir + '/model', compile=False, custom_objects={'Fgrad': Fgrad})
    TTP = keras.models.load_model(modeldir + '/TTP', compile=False, custom_objects={'Fgrad': Fgrad})

    if options.maxeta: maxeta = options.maxeta
    else:              maxeta = 41
    if maxeta>29: maxeta = maxeta - 1

    # Definition of the output folder
    if options.odir:
        odir = options.odir
    else:
        odir = indir + '/data_' + options.v
    os.system('mkdir -p '+ odir)
    print('\nOutput dir = {}\n'.format(odir))

    if options.v == "HCAL":
        ################## Energy rows and eta columns ##################
        # produce scale factors for every bin and every eta tower (matrix 40 * nbins)
        # SFOutFile = odir + '/ScaleFactors_' + options.v + label + '.csv'

        # eta_towers = [i for i in range(1,maxeta+1)]
        # input_towers = []
        # max_energy = 255
        # for i_energy in range(1, max_energy+1):
        #     for i, i_eta in enumerate(eta_towers):
        #         one_hot_tower = np.array([i_energy] + [0 if i != i_eta else 1 for i in range(1,maxeta+1)])
        #         input_towers.append(one_hot_tower)

        # input_towers = np.array(input_towers)

        # Einput = input_towers[:,0].reshape(-1,1)
        # Epredicted = TTP.predict(input_towers)

        # SFs = (Epredicted/Einput).reshape(max_energy,maxeta)
        # SFs_not_inverted = SFs.transpose()

        # head_text = 'eta = [0'
        # for i in range(1,maxeta):
        #     head_text = head_text + ' ,{}'.format(i)
        # head_text = head_text + "]"
        # np.savetxt(SFOutFile, SFs_not_inverted, delimiter=",", header=head_text, fmt=','.join(['%1.4f']*max_energy))
        # print('\nScale Factors saved to: {}'.format(SFOutFile))

        # Inverted

        SFOutFile = odir + '/ScaleFactors_' + options.v + label + '_inverted.csv'

        eta_towers_HCAL = [i for i in range(1,29)]
        input_towers = []
        max_energy = 255
        for i_energy in range(1, max_energy+1):
            for i, i_eta in enumerate(eta_towers_HCAL):
                one_hot_tower = np.array([i_energy] + [0 if i != i_eta else 1 for i in range(1,maxeta+1)])
                input_towers.append(one_hot_tower)

        input_towers = np.array(input_towers)

        Einput = input_towers[:,0].reshape(-1,1)
        Epredicted = TTP.predict(input_towers)

        SFs = (Epredicted/Einput).reshape(max_energy,28)

        head_text = 'energy bins = [0'
        for i in range(1,max_energy):
            head_text = head_text + ' ,{}'.format(i)
        head_text = head_text + " , 256]"
        np.savetxt(SFOutFile, SFs, delimiter=",", header=head_text, fmt=','.join(['%1.4f']*28))
        print('\nScale Factors saved to: {}'.format(SFOutFile))

        # HF 

        SFOutFile = odir + '/ScaleFactors_' + options.v + label + '_HF_inverted.csv'

        eta_towers_HF = [i for i in range(29,maxeta+1)]
        input_towers = []
        max_energy = 255
        for i_energy in range(1, max_energy+1):
            for i, i_eta in enumerate(eta_towers_HF):
                one_hot_tower = np.array([i_energy] + [0 if i != i_eta else 1 for i in range(1,maxeta+1)])
                input_towers.append(one_hot_tower)

        input_towers = np.array(input_towers)

        Einput = input_towers[:,0].reshape(-1,1)
        Epredicted = TTP.predict(input_towers)

        SFs = (Epredicted/Einput).reshape(max_energy,maxeta-28)

        head_text = 'energy bins = [0'
        for i in range(1,max_energy):
            head_text = head_text + ' ,{}'.format(i)
        head_text = head_text + " , 256]"
        np.savetxt(SFOutFile, SFs, delimiter=",", header=head_text, fmt=','.join(['%1.4f']*(maxeta-28)))

        print('\nScale Factors saved to: {}'.format(SFOutFile))

    else:
        ################## Energy rows and eta columns ##################
        # produce scale factors for every bin and every eta tower (matrix 40 * nbins)
        SFOutFile = odir + '/ScaleFactors_' + options.v + label + '_inverted.csv'

        eta_towers = [i for i in range(1,maxeta+1)]
        input_towers = []
        max_energy = 255
        for i_energy in range(1, max_energy+1):
            for i, i_eta in enumerate(eta_towers):
                one_hot_tower = np.array([i_energy] + [0 if i != i_eta else 1 for i in range(1,maxeta+1)])
                input_towers.append(one_hot_tower)

        input_towers = np.array(input_towers)

        Einput = input_towers[:,0].reshape(-1,1)
        Epredicted = TTP.predict(input_towers)

        SFs = (Epredicted/Einput).reshape(max_energy,maxeta)

        head_text = 'energy bins = [0'
        for i in range(1,max_energy):
            head_text = head_text + ' ,{}'.format(i)
        head_text = head_text + " , 256]"
        np.savetxt(SFOutFile, SFs, delimiter=",", header=head_text, fmt=','.join(['%1.4f']*maxeta))

        print('\nScale Factors saved to: {}'.format(SFOutFile))      








































