#librairies utiles
import numpy as np
import os
import sys
import copy
import pandas as pd
import matplotlib.pyplot as plt
# from NNModelTraining import *
# from NNModelTraining_FlooringAfterTTP import *
from NNModelTraining_FlooringInTTP import *
# from NNModelTraining_FlooringInTTP_RateProxyInLoss import *
sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *

real_eta_towers = list(TowersEta.keys())

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
    parser.add_option("--proxyMinEta",  dest="proxyMinEta", help="Min Eta for NN soft saturation", type=int,        default=1)
    parser.add_option("--proxyMaxEta",  dest="proxyMaxEta", help="Max Eta for NN soft saturation", type=int,        default=41)
    parser.add_option("--proxyMinE",    dest="proxyMinE",   help="Min E for NN soft saturation",   type=int,        default=1)
    parser.add_option("--proxyMaxE",    dest="proxyMaxE",   help="Max E for NN soft saturation",   type=int,        default=6)
    (options, args) = parser.parse_args()
    print(options)

    # Definition of the trained model
    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    modeldir = indir + '/model_' + options.v
    print('\nModel dir = {}\n'.format(modeldir))

    model1 = keras.models.load_model(modeldir + '/model', compile=False, custom_objects={'Fgrad': Fgrad})
    TTP = keras.models.load_model(modeldir + '/TTP', compile=False, custom_objects={'Fgrad': Fgrad})

    real_eta_towers = list(TowersEta.keys())
    eta_towers = [i for i in range(1,42)]
    eta_range = [i for i in range(options.proxyMinEta, options.proxyMaxEta+1)]
    if options.proxyMinEta<29 and options.proxyMaxEta>29: eta_range.remove(29) # remove TT 29
    proxy_towers = []
    min_energy = options.proxyMinE
    max_energy = options.proxyMaxE
    energy_range = max_energy - min_energy + 1
    for i_energy in range(min_energy, max_energy+1):
        for i, i_eta in enumerate(eta_towers):
            if not i_eta in eta_range: continue # skip TTs outside of the range we want to tackle
            one_hot_tower = np.array([i_energy] + [0 if i != i_eta else 1 for i in real_eta_towers])
            proxy_towers.append(one_hot_tower)

    proxy_towers = np.array(proxy_towers)

    Epredicted = TTP.predict(proxy_towers)

    k = 0
    for i in Epredicted:
        if i[0] >= 8: k += 1

        print(i)

    for i in proxy_towers:
        print(i)

    print("\n\n#####################################")
    print("input length =", len(Epredicted))
    print("output OT =", k)
    print("fraction OT =", k/len(Epredicted))








































