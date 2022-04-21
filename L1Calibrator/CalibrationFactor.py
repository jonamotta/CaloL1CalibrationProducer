#librairies utiles
import numpy as np
import os
import copy
import pandas as pd
import matplotlib.pyplot as plt

from ModelCMS import *

# Returns matrix with scale factors for the trained model (couche)
# The matrix has 40 rows, for all the eta towers, and as many columns as the number of the energy bins
def ExtractSF (model, bins):

    SF_matrix = np.zeros(((len(eta_towers)),(len(bins)-1)))

    # Scan over energy bins
    for i_bin in range(len(bins)-1):

        print('Running bin ', i_bin)
        i_energy_start = bins[i_bin]
        i_energy_stop = bins[i_bin+1]        

        # Scan over eta towers
        for i, i_eta in enumerate(eta_towers):

            predictions = []

            # Scan over all the possible energies belongin to each bin
            for i_energy in range(i_energy_start, i_energy_stop):
                # Reproduce an one-hot tower with the information required by the model, i.e. value of the tower energy and eta position
                one_hot_tower = np.array([[i_energy] + [0 if i != i_eta else 1 for i in eta_towers]])
                # Apply the model to the one-hot tower to get the expected converted energy, multiply by 2 to convert from GeV to towers energy units
                predictions.append(model.predict(one_hot_tower).ravel()/i_energy*2)

            # Compute the mean over all the energies for each bin
            SF_matrix[i,i_bin] = np.mean(predictions)

    return SF_matrix

### To run:
### python3 CalibrationFactor.py --model data_ECAL/Model_ECAL

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--model",    dest="model",   help="Folder with trained model",       default=None)
    parser.add_option("--bins",     dest="bins",    help="Comma separated energy bins",     default=None)
    parser.add_option("--out",      dest="odir",    help="Output folder",                   default=None)
    parser.add_option("--v",        dest="v",       help="Ntuple type ('ECAL' or 'HCAL')",  default='ECAL')
    (options, args) = parser.parse_args()
    print(options)

    # Definition of the trained model
    if options.model:
        modeldir = options.model
    else:
        modeldir = os.getcwd() + '/data_ECAL/Model_ECAL'
    print('\nTrained model = {}\n'.format(modeldir))

    model1 = keras.models.load_model(modeldir + '/model', compile=False)
    couche = keras.models.load_model(modeldir + '/couche', compile=False)
    
    # Definition of energy bins in units of 0.5 GeV, from 1 to 510
    if options.bins:
        bins_energy = options.bins.split(',')
    else:
        bins_energy = [1,4,6,8,10,12,16,22,38,164,244,510]
    print('\nEnergy bins = {}'.format(bins_energy))

    # Definition of the output folder
    if options.odir:
        odir = options.odir
    else:
        odir = os.getcwd() + '/data_ECAL'
    os.system('mkdir -p '+ odir)
    print('\nOutput folder = {}\n'.format(odir))

    # produce scale factors for every bin and every eta tower (matrix 40 * nbins)
    SFOutFile = odir + '/ScaleFactors_' + options.v + '.csv'
    ScaleFactors = ExtractSF(couche, bins_energy)
    # Add eta references and save to output csv file
    ScaleFactors_index = np.c_[eta_towers, ScaleFactors]
    head_text = 'ieta'
    for i in range(len(bins_energy)-1):
        head_text = head_text + ',{}-{}'.format(bins_energy[i], bins_energy[i+1])
    np.savetxt(SFOutFile, ScaleFactors_index, delimiter=",", header=head_text, fmt=','.join(['%i'] + ['%1.22f']*(len(bins_energy)-1)))

    print('\nScale Factors saved to {}'.format(SFOutFile))
