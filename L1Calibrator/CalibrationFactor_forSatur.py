#librairies utiles
import numpy as np
import os
import sys
import copy
import pandas as pd
import matplotlib.pyplot as plt
# from NNModelTraining import *
# from NNModelTraining_FlooringAfterTTP import *
from NNModelTraining_FlooringInTTP_SaturationAfterTTP import *
sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *

real_eta_towers = list(TowersEta.keys())

# Returns matrix with scale factors for the trained model (TTP)
# The matrix has 40 rows, for all the eta towers, and as many columns as the number of the energy bins
def ExtractSF (model, bins, eta_towers, padZeros, saturateAt):

    SF_matrix = np.zeros(((len(eta_towers)),(len(bins)-1)))

    # Scan over energy bins
    for i_bin in range(len(bins)-1):

        print('Running bin ', i_bin)
        i_energy_start = int(bins[i_bin])
        i_energy_stop = int(bins[i_bin+1])

        # Scan over eta towers
        for i, i_eta in enumerate(eta_towers):

            predictions = []

            # Scan over all the possible energies belongin to each bin
            for i_energy in range(i_energy_start, i_energy_stop):
                # Reproduce an one-hot tower with the information required by the model, i.e. value of the tower energy and eta position
                one_hot_tower = np.array([np.concatenate([np.array([[i_energy] + [0 if i != i_eta else 1 for i in list(TowersEta.keys())]]) , np.repeat(0,3280).reshape(80,41)])])
                # Apply the model to the one-hot tower to get the expected converted energy
                predictions.append(model.predict(one_hot_tower).ravel()/i_energy) # [ET]

            # Compute the mean over all the energies for each bin
            SF_matrix[i,i_bin] = np.mean(predictions)

            if padZeros:
                if SF_matrix[i,i_bin] == 0.:
                    if i == 0: SF_matrix[i,i_bin] = 1.0             # if first ieta bin just set to 1.0 the SF
                    else: SF_matrix[i,i_bin] = SF_matrix[i-1,i_bin] # else set it to to the previous ieta value
                    
            if saturateAt:
                if SF_matrix[i,i_bin] > saturateAt: SF_matrix[i,i_bin] = saturateAt

    return SF_matrix

# Same as before but ieta columns and energy rows
def ExtractSF_inverted (model, bins, eta_towers, padZeros, saturateAt):

    SF_matrix = np.zeros(((len(bins)-1),(len(eta_towers))))

    # Scan over energy bins
    for i_bin in range(len(bins)-1):

        print('Running bin ', i_bin)
        i_energy_start = int(bins[i_bin])
        i_energy_stop = int(bins[i_bin+1])

        # Scan over eta towers
        for i, i_eta in enumerate(eta_towers):

            predictions = []

            # Scan over all the possible energies belongin to each bin
            for i_energy in range(i_energy_start, i_energy_stop):
                # Reproduce an one-hot tower with the information required by the model, i.e. value of the tower energy and eta position
                one_hot_tower = np.array([np.concatenate([np.array([[i_energy] + [0 if i != i_eta else 1 for i in list(TowersEta.keys())]]) , np.repeat(0,3280).reshape(80,41)])])
                # Apply the model to the one-hot tower to get the expected converted energy
                predictions.append(model.predict(one_hot_tower).ravel()/i_energy) # [ET]

            # Compute the mean over all the energies for each bin
            SF_matrix[i_bin,i] = np.mean(predictions)

            if padZeros:
                if SF_matrix[i_bin,i] == 0.:
                    if i == 0: SF_matrix[i_bin,i] = 1.0             # if first ieta bin just set to 1.0 the SF
                    else: SF_matrix[i_bin,i] = SF_matrix[i_bin,i-1] # else set it to to the previous ieta value

            if saturateAt:
                if SF_matrix[i_bin,i] > saturateAt: SF_matrix[i_bin,i] = saturateAt

    return SF_matrix

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
    parser.add_option("--start",    dest="start",   help="Initial energy",                  default=None)
    parser.add_option("--stop",     dest="stop",    help="Final energy",                    default=None)
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

    # model1 = keras.models.load_model(modeldir + '/model', compile=False)
    # TTP = keras.models.load_model(modeldir + '/TTP', compile=False)
    model1 = keras.models.load_model(modeldir + '/model', compile=False, custom_objects={'Fgrad': Fgrad})
    TTP = keras.models.load_model(modeldir + '/TTP', compile=False, custom_objects={'Fgrad': Fgrad})
    
    # Definition of energy bins in units of 0.5 GeV, from 1 to 510
    # It will be optimized by a separated script
    if options.start and options.stop:
        start_energy = int(options.start)
        stop_energy = int(options.stop)
        bins_number = stop_energy - start_energy + 1
        bins_energy = np.linspace(start_energy,stop_energy,bins_number)
    else:
        # bins_energy = np.linspace(1,120,120)
        bins_energy = [1,4,8,12,16,20,30,50,70,90,110,130,150,170,200]
    print('\nEnergy bins = {}'.format(bins_energy))

    if options.maxeta != None:
        eta_towers = [i for i in range(1,int(options.maxeta)+1)]
    else:
        eta_towers = real_eta_towers

    # Definition of the output folder
    if options.odir:
        odir = options.odir
    else:
        odir = indir + '/data_' + options.v
    os.system('mkdir -p '+ odir)
    print('\nOutput dir = {}\n'.format(odir))

    ################## Energy columns and eta rows ##################
    # produce scale factors for every bin and every eta tower (matrix 40 * nbins)
    SFOutFile = odir + '/ScaleFactors_' + options.v + label +'.csv'

    # eta rows and energy columns
    ScaleFactors = ExtractSF(model1, bins_energy, eta_towers, options.padZeros, options.saturateAt)

    # # Add eta references and save to output csv file
    ScaleFactors_index = np.c_[eta_towers, ScaleFactors]
    head_text = 'ieta'
    for i in range(len(bins_energy)-1):
        head_text = head_text + ',{}-{}'.format(bins_energy[i], bins_energy[i+1])
    np.savetxt(SFOutFile, ScaleFactors_index, delimiter=",", header=head_text, fmt=','.join(['%i'] + ['%1.4f']*(len(bins_energy)-1)))
    # Units of scale factor is [ET] since the LUT will convert ET to ET, not GeV

    ################## Energy columns and eta rows ##################
    # produce scale factors for every bin and every eta tower (matrix 40 * nbins)
    SFOutFile = odir + '/ScaleFactors_' + options.v + label + '_inverted.csv'

    # eta columns and energy rows
    ScaleFactors = ExtractSF_inverted(model1, bins_energy, eta_towers, options.padZeros, options.saturateAt)

    # Add eta references and save to output csv file
    # edges_energy = ','.join('{}-{}'.format(int(bins_energy[i]), int(bins_energy[i+1])) for i in range(len(bins_energy)-1))
    ScaleFactors_index = np.c_[bins_energy[1:], ScaleFactors]
    head_text = 'en'
    for i in range(len(eta_towers)):
        head_text = head_text + ',{}'.format(eta_towers[i])
    np.savetxt(SFOutFile, ScaleFactors_index, delimiter=",", header=head_text, fmt=','.join(['%i'] + ['%1.4f']*(len(eta_towers))))
    # Units of scale factor is [ET] since the LUT will convert ET to ET, not GeV

    print('\nScale Factors saved to: {}'.format(SFOutFile))