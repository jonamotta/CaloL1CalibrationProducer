#librairies utiles
from re import S
import numpy as np
import sys
import os
import copy
import pandas as pd
import matplotlib.pyplot as plt
from math import *

from ModelCMS import *
import mplhep
plt.style.use(mplhep.style.CMS)

sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *

# List of plots
# a) Uncalibrated resolution
#    i) inclusive
#    ii) in bins of gen jet pT
# b) Calibrated resolution
#    i) inclusive
#    ii) in bins onf gen jet pT
#    iii) plots showing calibrated and uncalibrated
# c) Calibration constants
#    i) Calibration constants vs. ieta for different ET
#    ii) For a few ieta, ieta = 1, ieta = 10, ieta = 15, ieta = 27, show calibration constant vs. ET
# d) Scale and resolution
#    i) For a few ieta (and inclusively in ieta), show calibrated and uncalibrated <L1 ET / Gen PT> as function of Gen PT
#    ii) For a few ieta (and inclusively in eta), show calibrated and uncalibrated RMS (L1 ET / Gen PT) as function of Gen PT
#  e) Gen jet pT spectrum
#  f) ECAL fraction (E/[E+H]) - sum across 81 towers - as function of jet pT

c_uncalib = 'royalblue'
c_calib = 'darkorange'
eta_towers = list(TowersEta.keys())

def PlotSF (SF_matrix, bins, odir, v_sample):

    colors = plt.cm.viridis_r(np.linspace(0,1,len(bins)))
    plt.figure(figsize=(12,8))
    for i in range(len(bins) - 1):
        plt.plot(eta_towers, SF_matrix[:,i], 'o--', color=colors[i], label = f"{bins[i]} $\leq E_T <$ {bins[i+1]}")
    plt.xlabel('Trigger eta tower ring #')
    plt.ylabel('{} calibration constant'.format(v_sample))
    plt.legend(fontsize = 10, ncol=1, loc = 'upper right')
    plt.grid(linestyle='dotted')
    plt.title('CMS Simulation')
    savefile = odir + '/Calib_vs_Eta.pdf'
    plt.savefig(savefile)
    savefile = odir + '/Calib_vs_Eta.png'
    plt.savefig(savefile)
    print(savefile)

    eta_towers_plot = [1,5,10,15,20] # to be chosen

    colors = plt.cm.viridis_r(np.linspace(0,1,len(eta_towers)))
    plt.figure(figsize=(12,8))
    for i in range(len(eta_towers)):
        if eta_towers[i] in eta_towers_plot:
            plt.plot(bins[:-1], SF_matrix[i,:], 'o--', color=colors[i], label = f"$\eta = ${eta_towers[i]}")
    plt.xlabel('Energy [GeV]')
    plt.ylabel('{} calibration constant'.format(v_sample))
    plt.legend(fontsize = 10, ncol=1, loc = 'upper right')
    plt.grid(linestyle='dotted')
    plt.title('CMS Simulation')
    savefile = odir + '/Calib_vs_Energy.pdf'
    plt.savefig(savefile)
    savefile = odir + '/Calib_vs_Energy.png'
    plt.savefig(savefile)
    print(savefile)

    return True

# The uncalibrated energy is the sum of all the energies (check that it's not just iem), *0.5 to have units of GeV, over all the CD towers
# It returns the standard deviation of the distribution
def PlotResolution(df_uncalib,df_calib,odir,v_sample):

    bins_res = np.linspace(0,2,50)

    if v_sample == 'ECAL':
        column = 'resolution_ECAL'
    elif v_sample == 'HCAL':
        column = 'resolution_HCAL'
    
    plt.figure(figsize=(12,8))
    text_1 = r'Uncalib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_uncalib['res'].mean(), df_uncalib['res'].std())
    plt.hist(df_uncalib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_uncalib)
    plt.xlabel('Resolution')
    plt.ylabel('A.U.')
    plt.legend(fontsize=15)
    plt.title('Uncalibrated Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Resolution_uncalib_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

# It returns the standard deviation of the distribution

    plt.figure(figsize=(12,8))
    text_1 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib['res'].mean(), df_calib['res'].std())
    plt.hist(df_calib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_calib)
    plt.xlabel('Resolution')
    plt.ylabel('A.U.')
    plt.legend(fontsize=15)
    plt.title('Calibrated Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Resolution_calib_{}.png'.format(v_sample)
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
    savefile = odir + '/Resolution_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    return True

def PlotResolution_bins(df_uncalib,df_calib,odir,v_sample,energy_bins):
    
    data = []
    
    labels_text = []
    for i in range(len(bins_energy)-1):
        labels_text.append('{}-{}'.format(bins_energy[i], bins_energy[i+1]))
    df_uncalib['bins'] = pd.cut(df_uncalib['jetPt'], bins = bins_energy, labels = labels_text)
    df_calib['bins']   = pd.cut(df_calib['jetPt'], bins = bins_energy, labels = labels_text)
    bins_labels = np.unique(df_uncalib['bins'])
    print(bins_labels)
    
    for bin_label in sorted(bins_labels):
        
        fig = plt.figure(figsize = [12,8])
        bins_res = np.linspace(0,2,30)
        
        df_uncalib_bin = df_uncalib[df_uncalib['bins'] == bin_label]
        df_calib_bin = df_calib[df_calib['bins'] == bin_label]
        
        data.append({'bins': bin_label, 
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
        plt.title(f'Jets of {bin_label} Gev')
        savefile = odir + '/Resolution_{}_{}.png'.format(v_sample, bin_label)
        plt.savefig(savefile)
        print(savefile)

    resolution = pd.DataFrame(data=data)
    energy = []
    for edges in resolution['bins']:
        energy.append(int(edges.split('-')[0]))
    resolution['energy'] = energy
    resolution = resolution.sort_values('energy', axis=0)

    fig = plt.figure(figsize = [18,10])
    plt.bar(resolution['bins'], resolution['uncalib_std'], width=0.4, alpha=0.7, align='center', label='Uncalib', color=c_uncalib)
    plt.bar(resolution['bins'], resolution['calib_std'], width=0.4, alpha=0.7, align='edge', label='Calib', color=c_calib)
    plt.xlabel('Energy bins')
    plt.ylabel('Standard Deviation')
    plt.legend(loc='upper left')
    savefile = odir + '/Resolution_std_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    return resolution

def PlotGenJetPtSpectrum(df_uncalib,df_calib,odir,v_sample):
    
    plt.figure(figsize=(12,8))
    text_1 = r'Uncalib: $\mu = {:.1f}, \sigma = {:.1f}$'.format(df_uncalib['jetPt'].mean(), df_uncalib['jetPt'].std())
    plt.hist(df_uncalib['jetPt'], bins=100, label=text_1, histtype='step', density=True, stacked=True, linewidth=2)
    text_2 = r'Calib: $\mu = {:.1f}, \sigma = {:.1f}$'.format(df_calib['jetPt'].mean(), df_calib['jetPt'].std())
    plt.hist(df_calib['jetPt'], bins=100, label=text_2, histtype='step', density=True, stacked=True, linewidth=2)
    plt.xlabel('Jet Pt [GeV]')
    plt.ylabel('A.U.')
    plt.legend(loc='upper right',fontsize=12)
    plt.title('Jet Pt {}'.format(v_sample))
    savefile = odir + '/GenJetPt_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)


### To run:
### python3 ModelPlots.py --model /data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/ECALtraining/ECAL_coeffs --out data_ECAL_Jona/plots --SF data_ECAL_Jona/ScaleFactors_ECAL.csv

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--model",    dest="model",   help="Folder with trained model",       default=None)
    parser.add_option("--SF",       dest="SF",      help="Scale factors csv file",          default=None)
    parser.add_option("--out",      dest="odir",    help="Output folder",                   default=None)
    parser.add_option("--v",        dest="v",       help="Ntuple type ('ECAL' or 'HCAL')",  default='ECAL')
    (options, args) = parser.parse_args()
    print(options)

    # Definition of output folder
    if options.odir:
        odir = options.odir
    else:
        odir = os.getcwd() + '/data_ECAL/plots'
    os.system('mkdir -p '+ odir)
    print('\nOutput folder = {}\n'.format(odir))

    # Definition of Scale factors matrix
    if options.SF:
        SFOutFile = options.SF
    else:
        SFOutFile = 'data_ECAL/ScaleFactors_ECAL.csv'
    print('Scale factors inside {}'.format(SFOutFile))

    # Takes the matrix removing the first column (eta values), the header is commented and automatically removed
    ScaleFactors = np.loadtxt(open(SFOutFile, "rb"), delimiter=',')[:,1:]
    # Definition of bin edges from the header, 510 is always the top edge
    with open(SFOutFile) as f:
        header = f.readline().rstrip()
    bin_edges = header.split(',')[1:]
    bins_energy = [int(edge.split('-')[0]) for edge in bin_edges] + [510]
    print('\nEnergy bins = {}'.format(bins_energy))

    # Plot the scale factors
    print('\nPlot scale factors')
    PlotSF(ScaleFactors, bins_energy, odir, options.v)

    # # Plot the resolution histograms

    # Build the two pandas for the training (uncalibrated) and testing (calibrated)

    print('\nLoad data')
    indir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/ECALtraining'
    X_train = np.load(indir+'/X_train.npz')['arr_0']
    X_test = np.load(indir+'/X_test.npz')['arr_0']
    Y_train = np.load(indir+'/Y_train.npz')['arr_0']
    Y_test = np.load(indir+'/Y_test.npz')['arr_0']

    print('\nSum energy')
    # Define the uncalibrated jet energy (sum of the energies in each tower of the chuncky donut)
    X_train_energy_sum = []
    for i in range(len(X_train)):
        energy_sum = 0
        for t in X_train[i]:
            energy_sum = energy_sum + t[0]
        X_train_energy_sum.append(energy_sum)

    print('\nLoad model')
    # Definition of the trained model
    if options.model:
        modeldir = options.model
    else:
        modeldir = os.getcwd() + '/data_ECAL/Model_ECAL'

    model1 = keras.models.load_model(modeldir + '/model', compile=False)
    couche = keras.models.load_model(modeldir + '/couche', compile=False)

    # Define the calibrated jet energy (applying the model to the test samples)
    X_test_calib_sum = model1.predict(X_test)*2

    print('\nBuild pandas')
    # Produce the pandas dataframe
    df_uncalib = pd.DataFrame(data = {'jetPt': Y_train.ravel(), 'jetEnergy': X_train_energy_sum})
    df_calib   = pd.DataFrame(data = {'jetPt': Y_test.ravel(), 'jetEnergy': X_test_calib_sum.ravel()})

    # Compute resolution
    print('\nCompute resolution')
    df_uncalib['res'] = df_uncalib['jetEnergy']/df_uncalib['jetPt']*0.5
    df_calib['res']   = df_calib['jetEnergy']/df_calib['jetPt']*0.5

    PlotResolution(df_uncalib,df_calib,odir,options.v)
    PlotGenJetPtSpectrum(df_uncalib,df_calib,odir,options.v)
    resolution = PlotResolution_bins(df_uncalib,df_calib,odir,options.v,bins_energy)


############################# Complicated way of doing things, but saving eta information #############################
'''
    print('\nReshape data')
    # Flatten 3D matrix to have 2D matrix
    uncalib_towers = X_train.reshape(len(X_train)*81,41)
    uncalib_jets = pd.DataFrame(np.repeat(Y_train,81), columns=['jetPt'])
    uncalib_events = pd.DataFrame(np.repeat(list(range(len(X_train))),81), columns=['ev'])
    # Flatten 3D matrix to have 2D matrix
    calib_towers = X_test.reshape(len(X_test)*81,41)
    calib_jets = pd.DataFrame(np.repeat(Y_test,81), columns=['jetPt'])
    calib_events = pd.DataFrame(np.repeat(list(range(len(X_test))),81), columns=['ev'])

    # Define the uncalibrated pandas with all the zeros and ones
    column_names = ['iesum'] + [str(i) for i in eta_towers]
    eta_columns = column_names[1:]
    energy_columns = column_names[:1]

    df_uncalib_ones = pd.DataFrame(uncalib_towers, columns=column_names)
    df_calib_ones = pd.DataFrame(calib_towers, columns=column_names)

    # Remove the column with energy to apply the convertion
    df_uncalib_eta_ones = df_uncalib_ones[eta_columns]
    df_calib_eta_ones = df_calib_ones[eta_columns]

    print('\nConvert one hot encoder data')
    df_uncalib_eta = df_uncalib_eta_ones.idxmax(axis=1)
    df_calib_eta = df_calib_eta_ones.idxmax(axis=1)

    # Produce the pandas dataframe with index, iesum and ieta information
    df_uncalib = pd.concat([uncalib_events,uncalib_jets,df_uncalib_ones[energy_columns],df_uncalib_eta], axis=1)
    df_calib = pd.concat([calib_events,calib_jets,df_calib_ones[energy_columns],df_calib_eta], axis=1)

    # Compute resolution
    df_uncalib_res = pd.DataFrame()
    df_uncalib_res['sum'] = df_uncalib.groupby('ev').iesum.sum()
    df_uncalib_res['jetPt'] = Y_train
    df_uncalib_res['res'] = df_uncalib_res['sum']/df_uncalib_res['jetPt']*0.5

    df_calib_res = pd.DataFrame()
    df_calib_res['sum'] = df_calib.groupby('ev').iesum.sum()
    df_calib_res['jetPt'] = Y_test
    df_calib_res['res'] = df_calib_res['sum']/df_calib_res['jetPt']*0.5

    PlotResolution(df_uncalib_res,df_calib_res,odir,options.v)
'''

    # Add information about the jetPt

    # df = 
    # PlotResolution(df,df_calib,odir,v_sample)

    # # produce calibrated towers on the testing sample
    # predictions = model.predict(X_test)
    # print(predictions)
    # predictions = predictions.ravel()
    # print(predictions)
    # resolution_calibrated = predictions/Y_test
    # # [FIXME] This could be done in a more elegant way ..... Do we have to apply manually the coefficients?
    # df_calib = pd.DataFrame(np.array([predictions.T, resolution_calibrated]).T,columns=("jet_fit","calib_resolution"))
    # df_calib.to_csv('data/calib_towers_' + options.v  + '.csv')


