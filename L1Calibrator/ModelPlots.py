#librairies utiles
from re import S
import numpy as np
import sys
import os
import copy
import pandas as pd
import matplotlib.pyplot as plt
from math import *

from alternateModel4ECAL import *
sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *

import mplhep
plt.style.use(mplhep.style.CMS)

c_uncalib = 'royalblue'
c_calib = 'darkorange'
eta_towers = list(TowersEta.keys())

# Plot calibration constants (Scale Factors) 
# 1. Calibration constants vs ieta for different ET [jetPt binning]
# 2. Calibration constant vs ET for a few ieta
def PlotSF (SF_matrix, bins, odir, v_sample, stop):

    # Plot 1) Calibration constants vs ieta for different ET [jetPt binning]
    plt.figure(figsize=(12,8))
    colors = plt.cm.viridis_r(np.linspace(0,1,len(bins)))
    for i in range(len(bins) - 1):
        plt.plot(eta_towers[:stop], SF_matrix[:stop,i], 'o--', color=colors[i], label = f"{bins[i]} $\leq E_T <$ {bins[i+1]}")
    plt.xlabel('L1T Eta Tower')
    plt.ylabel('{} Calibration Constant'.format(v_sample))
    plt.legend(fontsize = 10, ncol=1, loc = 'upper right')
    plt.grid(linestyle='dotted')
    plt.title('Calibration vs Eta')
    savefile = odir + '/Calib_vs_Eta.png'
    plt.savefig(savefile)
    print(savefile)

    # Plot 2) Calibration constant vs ET for a few ieta

    eta_towers_plot = [1,5,10,15,20] # to be chosen

    plt.figure(figsize=(12,8))
    colors = plt.cm.viridis_r(np.linspace(0,1,len(eta_towers)))
    for i in range(len(eta_towers)):
        if eta_towers[i] in eta_towers_plot:
            plt.plot(bins[:-1], SF_matrix[i,:], 'o--', color=colors[i], label = f"$\eta = ${eta_towers[i]}")
    plt.xlabel(f'Energy [$E_T$]')
    plt.ylabel('{} calibration constant'.format(v_sample))
    plt.legend(fontsize = 10, ncol=1, loc = 'upper right')
    plt.grid(linestyle='dotted')
    plt.title('Calibration vs Energy')
    savefile = odir + '/Calib_vs_Energy.png'
    plt.savefig(savefile)
    print(savefile)

    return True

# Plot inclusive calibrated and uncalibrated resolution
# The uncalibrated energy is the sum of all the energies (check that it's not just iem), *0.5 to have units of GeV, over all the CD towers
# It returns the standard deviation of the distribution
def PlotResolution(df_uncalib,df_calib,odir,v_sample):

    bins_res = np.linspace(0,2,50)
  
    plt.figure(figsize=(12,8))
    text_1 = r'Uncalib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_uncalib['res'].mean(), df_uncalib['res'].std())
    plt.hist(df_uncalib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_uncalib)
    plt.xlabel('Resolution')
    plt.ylabel('A.U.')
    plt.legend(fontsize=15)
    plt.title('Uncalibrated Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Res_{}_uncalib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    plt.figure(figsize=(12,8))
    text_1 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib['res'].mean(), df_calib['res'].std())
    plt.hist(df_calib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_calib)
    plt.xlabel('Resolution')
    plt.ylabel('A.U.')
    plt.legend(fontsize=15)
    plt.title('Calibrated Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Res_{}_calib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    # Plot simultaneously the calibrated and uncalibrated energy distributions
    plt.figure(figsize=(12,8))
    text_1 = r'Uncalib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_uncalib['res'].mean(), df_uncalib['res'].std())
    plt.hist(df_uncalib['res'], bins=bins_res, label=text_1, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
    text_2 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib['res'].mean(), df_calib['res'].std())
    plt.hist(df_calib['res'], bins=bins_res, label=text_2, histtype='step', density=True, stacked=True, linewidth=2, color=c_calib)
    plt.xlabel('Resolution')
    plt.ylabel('A.U.')
    plt.legend(fontsize=15)
    plt.title('Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Res_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    return True

# Plot generated jets spctrum in energy
def PlotGenJetPtSpectrum(df_uncalib,df_calib,odir,v_sample):
    
    plt.figure(figsize=(12,8))
    plt.hist(df_uncalib['jetPt'], bins=100, label='Uncalib', histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
    plt.hist(df_calib['jetPt'], bins=100, label='Calib', histtype='step', density=True, stacked=True, linewidth=2, color=c_calib)
    plt.xlabel(f'Jet $p_t$ [GeV]')
    plt.ylabel('A.U.')
    plt.legend(loc='upper right',fontsize=12)
    plt.title(r'Generated Jets $p_t$ Spectrum {}'.format(v_sample))
    savefile = odir + '/GenJetPt_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

# Plot calibrated and uncalibrated resolution in bins of jetPt or jetEta (based on bin_type)
def PlotResolution_bins(df_uncalib, df_calib, odir, v_sample, bins, bin_type):
    
    if bin_type == 'energy':
        column_bin = 'bins_en'
        name = 'jetPt'
        units = '[GeV]'
    elif bin_type == 'eta':
        column_bin = 'bins_eta'
        name = 'jetEta'
        units = ''
    else:
        sys.exit('[ERROR] PlotResolution_bins: choose bin_type between energy and eta')

    data = []
    
    labels_text = []
    for i in range(len(bins)-1):
        labels_text.append('{}-{}'.format(bins[i], bins[i+1]))
    df_uncalib[column_bin] = pd.cut(df_uncalib[name], bins = bins, labels = labels_text)
    df_calib[column_bin]   = pd.cut(df_calib[name], bins = bins, labels = labels_text)
    bins_labels = np.unique(df_calib[column_bin])
    
    for bin_label in sorted(bins_labels):
        
        fig = plt.figure(figsize = [12,8])
        bins_res = np.linspace(0,2,30)
        
        df_uncalib_bin = df_uncalib[df_uncalib[column_bin] == bin_label]
        df_calib_bin = df_calib[df_calib[column_bin] == bin_label]
        
        data.append({column_bin: bin_label, 
                           'uncalib_mean': df_uncalib_bin['res'].mean(), 
                           'uncalib_std': df_uncalib_bin['res'].std(),
                           'calib_mean': df_calib_bin['res'].mean(),
                           'calib_std': df_calib_bin['res'].std()})
        
        text_1 = r'Uncalib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_uncalib_bin['res'].mean(), df_uncalib_bin['res'].std())
        plt.hist(df_uncalib_bin['res'], bins=bins_res, label=text_1, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
        text_2 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib_bin['res'].mean(), df_calib_bin['res'].std())
        plt.hist(df_calib_bin['res'], bins=bins_res, label=text_2, histtype='step', density=True, stacked=True, linewidth=2, color=c_calib)
        plt.grid(axis='y', alpha=0.5)
        plt.xlabel('Resolution')
        plt.ylabel('A.U.')
        plt.legend(loc='upper left', fontsize=15)
        plt.title('{} = {} {}'.format(name, bin_label, units))
        savefile = odir + '/Res_{}{}_{}.png'.format(name.split('jet')[1], bin_label, v_sample)
        plt.savefig(savefile)
        print(savefile)
        plt.close()

    resolution = pd.DataFrame(data=data)
    energy = []
    for edges in resolution[column_bin]:
        energy.append(float(edges.split('-')[0]))
    resolution[name] = energy
    resolution = resolution.sort_values(name, axis=0)

    fig = plt.figure(figsize = [18,10])
    plt.bar(resolution[column_bin], resolution['uncalib_std']/resolution['uncalib_mean'], width=0.4, alpha=0.7, align='center', label='Uncalib', color=c_uncalib)
    plt.bar(resolution[column_bin], resolution['calib_std']/resolution['calib_mean'], width=0.4, alpha=0.7, align='edge', label='Calib', color=c_calib)
    plt.xlabel('{} bins {}'.format(name, units))
    plt.ylabel('Standard Deviation / Mean')
    plt.title(f'Jets resolution')
    plt.legend(loc='upper left')
    savefile = odir + '/Res_vs_{}_{}.png'.format(name.split('jet')[1], v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    return resolution

### To run:
### python3 ModelPlots.py --in /data_CMS/cms/motta/CaloL1calibraton/2022_04_21_NtuplesV1/ECALtraining --out data_ECAL_V1/plots --v ECAL

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--in",       dest="indir",   help="Input folder with trained model", default=None)
    parser.add_option("--out",      dest="odir",    help="Output folder",                   default=None)
    parser.add_option("--v",        dest="v",       help="Ntuple type ('ECAL' or 'HCAL')",  default='ECAL')
    (options, args) = parser.parse_args()
    print(options)

    # Definition of the trained model
    indir = options.indir
    modeldir = indir + '/model_' + options.v
    print('\nModel dir = {}'.format(modeldir))

    model1 = keras.models.load_model(modeldir + '/model', compile=False)
    couche = keras.models.load_model(modeldir + '/couche', compile=False)

    # Definition of the Scale factors
    SF_filename = indir + '/data_' + options.v + '/ScaleFactors_' + options.v + '.csv'
    print('\nScale Factors file = {}'.format(SF_filename))

    # Definition of output folder
    if options.odir:
        odir = options.odir
    else: 
        odir = indir + '/plots'
    os.system('mkdir -p '+ odir)
    print('\nOutput dir = {}'.format(odir))

    # Takes the matrix removing the first column (eta values), the header is commented and automatically removed
    ScaleFactors = np.loadtxt(open(SF_filename, "rb"), delimiter=',')[:,1:]
    # Definition of energy bin edges from the header
    with open(SF_filename) as f:
        header = f.readline().rstrip()
    bin_edges = header.split(',')[1:]
    bins_energy = [int(edge.split('-')[0]) for edge in bin_edges] + [int(bin_edges[-1].split('-')[1])]
    # bins_energy = [1, 2, 4, 10, 20, 50, 80, 100, 120, 164, 244, 510]
    print('\nEnergy bins = {}'.format(bins_energy))

    # Definition of eta bin edges
    bins_eta = [0, 0.5, 1, 1.5, 2, 2.5, 5]
    print('\nEta bins = {}'.format(bins_eta))

    #######################################################
    ################# Scale Factors plots #################
    #######################################################

    # Plot the scale factors
    print('\nPlot scale factors')
    PlotSF(ScaleFactors, bins_energy, odir, options.v, 28)

    #######################################################
    ################## Resolution plots ###################
    #######################################################

    # Build the two pandas for the training (uncalibrated) and testing (calibrated)
    # X samples contain : iesum = iem + ihad, eta tower
    # Y samples contain : jetPt, jetEta
    print('\nLoad data')
    indir = options.indir
    X_train = np.load(indir+'/X_train.npz')['arr_0']
    X_test = np.load(indir+'/X_test.npz')['arr_0']
    Y_train = np.load(indir+'/Y_train.npz')['arr_0']
    Y_test = np.load(indir+'/Y_test.npz')['arr_0']

    # Define the uncalibrated jet energy (sum of the energies in each tower of the chuncky donut)
    X_train_iem = np.sum(X_train,axis = 1)[:,0:1].ravel() # [ET]
    X_train_ihad = np.sum(X_train,axis = 1)[:,1:2].ravel() # [ET]
    X_train_iesum = X_train_iem + X_train_ihad # [ET]

    # Define the calibrated jet energy (applying the model to the test samples)
    X_test_model, Y_test_model = convert_samples(X_test, Y_test)
    X_test_calib_sum = model1.predict(X_test_model)*2 # [ET]

    print('\nBuild pandas')
    # Produce the pandas dataframes with jetPt, jetEta and jetEnergy (sum of the deposited energy in all the towers)
    df_uncalib = pd.DataFrame(data = {'jetPt': Y_train[:,0].ravel(), 'jetEta': np.abs(Y_train[:,1].ravel()), 'jetIem': X_train_iem, 'jetIhad': X_train_ihad, 'jetEnergy': X_train_iesum})
    df_calib   = pd.DataFrame(data = {'jetPt': Y_test[:,0].ravel(),  'jetEta': np.abs(Y_test[:,1].ravel()),  'jetEnergy': X_test_calib_sum.ravel()})

    # Compute resolution
    print('\nCompute resolution')
    df_uncalib['res'] = df_uncalib['jetEnergy']/df_uncalib['jetPt']*0.5
    df_calib['res']   = df_calib['jetEnergy']/df_calib['jetPt']*0.5

    PlotResolution(df_uncalib,df_calib,odir,options.v)
    PlotGenJetPtSpectrum(df_uncalib,df_calib,odir,options.v)
    resolution = PlotResolution_bins(df_uncalib,df_calib,odir,options.v,bins_energy,'energy')
    resolution_eta = PlotResolution_bins(df_uncalib,df_calib,odir,options.v,bins_eta,'eta')

    print('\nDONE!!!\n')
