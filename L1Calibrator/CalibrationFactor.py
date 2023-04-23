#librairies utiles
import numpy as np
import os
import sys
import copy
import pandas as pd
import matplotlib.pyplot as plt
from NNModelTraining_FullyCustom_GPUdistributed_batchedRate import *
sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *
import warnings
warnings.simplefilter(action='ignore')

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 CalibrationFactor.py --in 2022_04_21_NtuplesV1 --v ECAL 

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",      dest="indir",      help="Input folder with trained model",             default=None                       )
    parser.add_option("--tag",        dest="tag",        help="tag of the training folder",                  default=""                         )
    parser.add_option("--out",        dest="odir",       help="Output folder",                               default=None                       )
    parser.add_option("--v",          dest="v",          help="Ntuple type ('ECAL' or 'HCAL')",              default='ECAL'                     )
    parser.add_option("--reg",        dest="reg",        help="Ntuple type ('ECAL' or 'HCAL' or 'HF'')",     default='ECAL'                     )
    parser.add_option("--minenergy",  dest="minenergy",  help="Energy tower min",                type=int,   default=1                          )
    parser.add_option("--maxenergy",  dest="maxenergy",  help="Energy tower max",                type=int,   default=200                        )
    parser.add_option("--energystep", dest="energystep", help="Energy steps",                    type=int,   default=1                          )
    parser.add_option("--addtag",     dest="addtag",     help="Add tag to distinguish different trainings",  default="",                        )
    (options, args) = parser.parse_args()
    print(options)

    # Definition of the trained model
    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    modeldir = indir + '/model_' + options.v + options.addtag
    print('\nModel dir = {}\n'.format(modeldir))

    TTP = keras.models.load_model(modeldir + '/TTP', compile=False, custom_objects={'Fgrad': Fgrad})

    # Definition of the output folder
    if options.odir:
        odir = options.odir
    else:
        odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag
    os.system('mkdir -p '+ odir)
    print('\nOutput dir = {}\n'.format(odir))

    ################## ECAL/HCAL ##################
    if options.reg == "HCAL" or options.reg == "ECAL":
        eta_towers = [i for i in range(1,28+1)]
        input_towers = []
        max_energy = options.maxenergy
        min_energy = options.minenergy
        energy_step = options.energystep

        i_step = 0
        if energy_step > 1: i_step = energy_step / 2

        for i_energy in range(min_energy, max_energy+1, energy_step):
            for i_eta in eta_towers:
                one_hot_tower = np.array([i_energy+i_step] + [0 if j != i_eta else 1 for j in range(1,40+1)])
                if options.reg == "ECAL":    
                    # apply 3/6/9 zero-suppression by inputing energy = 0.0
                    if i_eta == 26 and i_energy+i_step <=  6: one_hot_tower = np.array([0.0] + [0 if j != i_eta else 1 for j in range(1,40+1)])
                    if i_eta == 27 and i_energy+i_step <= 12: one_hot_tower = np.array([0.0] + [0 if j != i_eta else 1 for j in range(1,40+1)])
                    if i_eta == 28 and i_energy+i_step <= 18: one_hot_tower = np.array([0.0] + [0 if j != i_eta else 1 for j in range(1,40+1)])
                input_towers.append(one_hot_tower)

        input_towers = np.array(input_towers)

        Einput = input_towers[:,0].reshape(-1,1)
        Epredicted = TTP.predict(input_towers)

        SFs = (Epredicted/Einput).reshape(int((max_energy-min_energy)/energy_step)+1,28)
        SFs[np.isinf(SFs)] = 0.0000 # replace the infs form the 3/6/9 zero suppression trick with zeros
        SFs[np.isnan(SFs)] = 0.0000 # replace the infs form the 3/6/9 zero suppression trick with zeros

        head_text = 'energy bins iEt       = [0'
        for i in range(min_energy, max_energy, energy_step):
            head_text = head_text + ' ,{}'.format(i)
        head_text = head_text + " , 256]\n"
        
        head_text = head_text + 'energy bins GeV       = [0'
        for i in range(min_energy, max_energy, energy_step):
            head_text = head_text + ' ,{}'.format(i/2)
        head_text = head_text + " , 256]\n"

        head_text = head_text + 'energy bins GeV (int) = [0'
        for i in range(min_energy, max_energy, energy_step):
            head_text = head_text + ' ,{}'.format(int(i/2))
        head_text = head_text + " , 256]\n"

        SFOutFile = odir + '/ScaleFactors_' + options.reg + '_energystep'+str(energy_step)+'iEt.csv'
        np.savetxt(SFOutFile, SFs, delimiter=",", newline=',\n', header=head_text, fmt=','.join(['%1.4f']*28))
        print('\nScale Factors saved to: {}'.format(SFOutFile))

    ################## HF ##################
    if options.reg == "HF":
        eta_towers = [i for i in range(29,40+1)]
        input_towers = []
        max_energy = options.maxenergy
        min_energy = options.minenergy
        energy_step = options.energystep

        i_step = 0
        if energy_step > 1: i_step = energy_step / 2

        for i_energy in range(min_energy, max_energy+1, energy_step):
            for i_eta in eta_towers:
                one_hot_tower = np.array([i_energy+i_step] + [0 if j != i_eta else 1 for j in range(1,40+1)])
                input_towers.append(one_hot_tower)

        input_towers = np.array(input_towers)

        Einput = input_towers[:,0].reshape(-1,1)
        Epredicted = TTP.predict(input_towers)

        SFs = (Epredicted/Einput).reshape(int((max_energy-min_energy)/energy_step)+1,12)
        SFs[np.isinf(SFs)] = 0.0000 # replace the infs form the 3/6/9 zero suppression trick with zeros
        SFs[np.isnan(SFs)] = 0.0000 # replace the infs form the 3/6/9 zero suppression trick with zeros

        head_text = 'energy bins iEt       = [0'
        for i in range(min_energy, max_energy, energy_step):
            head_text = head_text + ' ,{}'.format(i)
        head_text = head_text + " , 256]\n"
        
        head_text = head_text + 'energy bins GeV       = [0'
        for i in range(min_energy, max_energy, energy_step):
            head_text = head_text + ' ,{}'.format(i/2)
        head_text = head_text + " , 256]\n"

        head_text = head_text + 'energy bins GeV (int) = [0'
        for i in range(min_energy, max_energy, energy_step):
            head_text = head_text + ' ,{}'.format(int(i/2))
        head_text = head_text + " , 256]\n"

        SFOutFile = odir + '/ScaleFactors_' + options.reg + '_energystep'+str(energy_step)+'iEt.csv'
        np.savetxt(SFOutFile, SFs, delimiter=",", newline=',\n', header=head_text, fmt=','.join(['%1.4f']*12))
        print('\nScale Factors saved to: {}'.format(SFOutFile))

