#librairies utiles
from re import S
import numpy as np
import sys
import os
import copy
import pandas as pd
import matplotlib.pyplot as plt
from math import *
from matplotlib.transforms import Affine2D

# from NNModelTraining import *
# from NNModelTraining_FlooringAfterTTP import *
from NNModelTraining_FlooringInTTP import *
sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *

import mplhep
plt.style.use(mplhep.style.CMS)
#plt.style.use(mplhep.style.CMSTex)

def export_legend(legend, filename="legend.png", expand=[-5,-5,5,5]):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent()
    bbox = bbox.from_extents(*(bbox.extents + np.array(expand)))
    bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)

c_uncalib = 'royalblue'
c_calib = 'darkorange'
eta_towers = list(TowersEta.keys())

# Plot calibration constants (Scale Factors) 
# 1. Calibration constants vs ieta for different ET [jetPt binning]
# 2. Calibration constant vs ET for a few ieta
def PlotSF (SF_matrix, bins, odir, v_sample, eta_towers):

    # Plot 1) Calibration constants vs ieta for different ET [jetPt binning]
    plt.figure(figsize=(18,12))
    colors = plt.cm.viridis_r(np.linspace(0,1,len(bins)))
    for i in range(len(bins) - 1):
        plt.plot(eta_towers, SF_matrix[:,i], 'o--', color=colors[i], label = f"{bins[i]} $\leq E_T <$ {bins[i+1]}")
    plt.xlabel('i$\eta$')
    plt.ylabel('{} Calibration Constant'.format(v_sample))
    plt.grid(linestyle='dotted')
    #plt.title('Calibration vs Eta')
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    savefile = odir + '/Calib_vs_Eta.png'
    plt.savefig(savefile)
    print(savefile)
    plt.ylim(0,13)
    legend = plt.legend(fontsize = 8, ncol=8, loc = 'upper center')
    savefile = odir + '/Calib_vs_Eta_legend.png'
    export_legend(legend, savefile)
    print(savefile)
    
    # Plot 2) Calibration constant vs ET for a few ieta

    # eta_towers_plot = [1,5,10,15,20] # to be chosen
    eta_towers_plot = eta_towers

    plt.figure(figsize=(12,8))
    colors = plt.cm.viridis_r(np.linspace(0,1,len(eta_towers)))
    for i in range(len(eta_towers)):
        if eta_towers[i] in eta_towers_plot:
            plt.plot(bins[:-1], SF_matrix[i,:], 'o--', color=colors[i], label = f"$\eta = ${eta_towers[i]}")
    plt.xlabel(f'i$E_T$')
    plt.ylabel('{} calibration constant'.format(v_sample))
    plt.legend(fontsize = 9, ncol=2, loc = 'upper right')
    plt.grid(linestyle='dotted')
    # plt.title('Calibration vs Energy')
    savefile = odir + '/Calib_vs_Energy.png'
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
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
    plt.xlabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$')
    plt.ylabel('a.u.')
    plt.legend(fontsize=15)
    # plt.title('Uncalibrated Jets Resolution {}'.format(v_sample))
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    savefile = odir + '/Res_{}_uncalib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    plt.figure(figsize=(12,8))
    text_1 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib['res'].mean(), df_calib['res'].std())
    plt.hist(df_calib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_calib)
    plt.xlabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$')
    plt.ylabel('a.u.')
    plt.legend(fontsize=15)
    # plt.title('Calibrated Jets Resolution {}'.format(v_sample))
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    savefile = odir + '/Res_{}_calib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    # Plot simultaneously the calibrated and uncalibrated energy distributions
    plt.figure(figsize=(12,8))
    text_1 = r'Uncalib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_uncalib['res'].mean(), df_uncalib['res'].std())
    plt.hist(df_uncalib['res'], bins=bins_res, label=text_1, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
    text_2 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib['res'].mean(), df_calib['res'].std())
    plt.hist(df_calib['res'], bins=bins_res, label=text_2, histtype='step', density=True, stacked=True, linewidth=2, color=c_calib)
    plt.xlabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$')
    plt.ylabel('a.u.')
    plt.legend(fontsize=15)
    # plt.title('Jets Resolution {}'.format(v_sample))
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
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
    plt.xlabel('$p_T^{gen}(jet)$ [GeV]')
    plt.ylabel('a.u.')
    plt.legend(loc='upper right',fontsize=12)
    # plt.title(r'Generated Jets $p_t$ Spectrum {}'.format(v_sample))
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    savefile = odir + '/GenJetPt_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

# Plot calibrated and uncalibrated resolution in bins of jetPt or jetEta (based on bin_type)
def PlotResolution_bins(df_uncalib, df_calib, odir, v_sample, bin_type, steps):
    
    if bin_type == 'energy':
        column_bin = 'bins_en'
        name = 'jetPt'
        label = '$p_{T}^{gen}(jet)$'
        units = '[GeV]'
    elif bin_type == 'eta':
        column_bin = 'bins_eta'
        name = 'jetEta'
        label = '$\eta^{gen}(jet)$'
        units = ''
    else:
        sys.exit('[ERROR] PlotResolution_bins: choose bin_type between energy and eta')

    data = []

    values = np.unique(df_calib[name])
    min_value = int(values.min())
    max_value = int(values.max())+1
    bins = np.arange(min_value, max_value, steps)
    bins = np.append(bins, max_value)

    labels_text = []
    for i in range(len(bins)-1):
        labels_text.append('{}-{}'.format(bins[i], bins[i+1]))
    print(bins)
    df_uncalib[column_bin] = pd.cut(df_uncalib[name], bins = bins, labels = labels_text)
    df_calib[column_bin]   = pd.cut(df_calib[name], bins = bins, labels = labels_text)
    bins_labels = np.unique(df_calib[column_bin])
    
    for bin_label in sorted(bins_labels):
        
        fig = plt.figure(figsize = [24,8])
        bins_res = np.linspace(0,2,30)
        
        df_uncalib_bin = df_uncalib[df_uncalib[column_bin] == bin_label]
        df_calib_bin = df_calib[df_calib[column_bin] == bin_label]
        
        data.append({column_bin: bin_label, 
                     'uncalib_mean': df_uncalib_bin['res'].mean(), 
                     'uncalib_std' : df_uncalib_bin['res'].std(),
                     'calib_mean'  : df_calib_bin['res'].mean(),
                     'calib_std'   : df_calib_bin['res'].std()})
        
        text_1 = r'Uncalib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_uncalib_bin['res'].mean(), df_uncalib_bin['res'].std())
        plt.hist(df_uncalib_bin['res'], bins=bins_res, label=text_1, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
        text_2 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib_bin['res'].mean(), df_calib_bin['res'].std())
        plt.hist(df_calib_bin['res'], bins=bins_res, label=text_2, histtype='step', density=True, stacked=True, linewidth=2, color=c_calib)
        plt.grid(axis='y', alpha=0.5)
        plt.xlabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$')
        plt.ylabel('a.u.')
        plt.legend(loc='upper left', fontsize=15, title='{} = {} {}'.format(label, bin_label, units))
        # plt.title('{} = {} {}'.format(name, bin_label, units))
        mplhep.cms.label('', data=False, rlabel='(14 TeV)')
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

    fig = plt.figure(figsize = [24,15])
    plt.bar(resolution[column_bin], resolution['uncalib_std']/resolution['uncalib_mean'], width=0.4, alpha=0.7, align='center', label='Uncalib', color=c_uncalib)
    plt.bar(resolution[column_bin], resolution['calib_std']/resolution['calib_mean'], width=0.4, alpha=0.7, align='edge', label='Calib', color=c_calib)
    plt.xticks(rotation=45)
    plt.ylim(0.0,0.5)
    plt.xlabel('{} {}'.format(label, units))
    plt.ylabel('$p_{T}^{gen}(jet)$ resolution')
    # plt.title(f'Jets resolution')
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    plt.legend(loc='upper right')
    savefile = odir + '/Res_vs_{}_{}.png'.format(name.split('jet')[1], v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    fig, ax = plt.subplots(figsize = [24,15])
    trans1 = Affine2D().translate(-0.05, 0.0) + ax.transData
    trans2 = Affine2D().translate(+0.05, 0.0) + ax.transData
    plt.errorbar(resolution[column_bin], resolution['uncalib_mean'], yerr=resolution['uncalib_std'], fmt='o', alpha=1, label='Uncalib', color=c_uncalib, markersize=15, capsize=8, elinewidth=3, capthick=5, transform=trans1)
    plt.errorbar(resolution[column_bin], resolution['calib_mean'], yerr=resolution['calib_std'], fmt='o', alpha=1, label='Calib', color=c_calib, markersize=15, capsize=8, elinewidth=3, capthick=5, transform=trans2)
    plt.xticks(rotation=45)
    plt.axhline(y=1., color='black', linestyle='--')
    plt.ylim(0.4,1.6)
    plt.xlabel('{} {}'.format(label, units))
    plt.ylabel('$p_{T}^{gen}(jet)$ scale')
    # plt.title(f'Jets resolution')
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    plt.legend(loc='upper right')
    savefile = odir + '/Res_vs_{}_{}_bars.png'.format(name.split('jet')[1], v_sample)
    plt.savefig(savefile)
    print(savefile)

    return resolution

def PlotResolution_vs_Pt_Etabin(df, odir, v_sample, ieta_values, calib):

    plt.figure(figsize=(15,10))
    # ieta_values = df['jetIeta'].unique()
    colors = plt.cm.viridis(np.linspace(0,1,len(ieta_values)))
    for i_eta, eta in enumerate(ieta_values):
        prof = df[df['jetIeta']==eta].groupby('jetPt')['res'].mean()
        plt.plot(prof.index, prof.values, '.', color=colors[i_eta], label=f'$\eta$ tower = {eta_towers[i_eta]}')
        plt.xlabel('$p_T^{gen}(jet)$ [GeV]')
        plt.ylabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$')
        #if calib == 'uncalib':  title = 'Uncalibrated'
        #else:                   title = 'Calibrated'
        #plt.title(title)
        mplhep.cms.label('', data=False, rlabel='(14 TeV)')
        plt.legend(fontsize = 15, ncol=1, loc = 'upper right')
    savefile = odir + '/Res_vs_Pt_Etabin_{}_{}.png'.format(calib, v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

def PlotResolution_vs_Eta_Ptbin(df, odir, v_sample, pt_values, calib):

    plt.figure(figsize=(15,10))
    colors = plt.cm.viridis(np.linspace(0,1,len(pt_values)))
    for i_pt in range(len(pt_values)-1):
        prof = df[(df['jetPt']>pt_values[i_pt]) & (df['jetPt']<pt_values[i_pt+1])].groupby('jetEta')['res'].mean()
        plt.plot(prof.index, prof.values, '.', color=colors[i_pt], label=f'${pt_values[i_pt]}<p_t<${pt_values[i_pt+1]}')
        plt.xlabel('$\eta^{gen}(jet)$')
        plt.ylabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$')
        # if calib == 'uncalib':  title = 'Uncalibrated'
        # else:                   title = 'Calibrated'
        # plt.title(title)
        mplhep.cms.label('', data=False, rlabel='(14 TeV)')
        plt.legend(fontsize = 15, ncol=1, loc = 'upper right')
    savefile = odir + '/Res_vs_Eta_Ptbin_{}_{}.png'.format(calib, v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

def PlotResolution_vs_Pt_Etavalue(df_uncalib, df_calib, odir, v_sample, eta_values):

    plt.figure(figsize=(15,10))
    prof_uncalib = df_uncalib[(df_uncalib['jetEta']>eta_values[0]) & (df_uncalib['jetEta']<eta_values[1])].groupby('jetPt')['res'].mean()
    prof_calib = df_calib[(df_calib['jetEta']>eta_values[0]) & (df_calib['jetEta']<eta_values[1])].groupby('jetPt')['res'].mean()
    plt.plot(prof_uncalib.index, prof_uncalib.values, '.', color=c_uncalib, alpha=0.7, label='Uncalib')
    plt.plot(prof_calib.index, prof_calib.values, '.', color=c_calib, alpha=0.7, label='Calib')
    plt.xlabel('$p_{T}^{gen}(jet)$ [GeV]')
    plt.ylabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$')
    # plt.title('Eta {}-{}'.format(eta_values[0], eta_values[1]))
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    plt.legend(fontsize = 15, ncol=1, loc = 'upper right', title=str(eta_values[0])+'<$|\eta^{gen}(jet)|$<'+str(eta_values[1]))
    savefile = odir + '/Res_vs_Pt_Eta{}-{}_{}.png'.format(eta_values[0], eta_values[1], v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

def PlotResolution_vs_Eta_Ptvalue(df_uncalib, df_calib, odir, v_sample, pt_values):

    plt.figure(figsize=(15,10))
    prof_uncalib = df_uncalib[(df_uncalib['jetPt']>pt_values[0]) & (df_uncalib['jetPt']<pt_values[1])].groupby('jetEta')['res'].mean()
    prof_calib = df_calib[(df_calib['jetPt']>pt_values[0]) & (df_calib['jetPt']<pt_values[1])].groupby('jetEta')['res'].mean()
    plt.plot(prof_uncalib.index, prof_uncalib.values, '.', color=c_uncalib, alpha=0.7, label='Uncalib')
    plt.plot(prof_calib.index, prof_calib.values, '.', color=c_calib, alpha=0.7, label='Calib')
    plt.xlabel('$\eta^{gen}(jet)$')
    plt.ylabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$')
    # plt.title('Pt {}-{}'.format(pt_values[0], pt_values[1]))
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    plt.legend(fontsize = 15, ncol=1, loc = 'upper right', title=str(pt_values[0])+'<$p_{T}^{gen}(jet)$<'+str(pt_values[1]))
    savefile = odir + '/Res_vs_Eta_Pt{}-{}_{}.png'.format(pt_values[0], pt_values[1], v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

def PlotECALratio(df_uncalib):

    df_uncalib['iem_ratio'] = df_uncalib['jetIem']/df_uncalib['jetEnergy']
    plt.figure(figsize=(14,8))
    plt.plot(df_uncalib['jetPt'], df_uncalib['iem_ratio'], '.')
    plt.xlabel('$p_T^{gen}(jet)$ [GeV]')
    plt.ylabel('$\sum iem/(\sum iem + \sum ihad$)')
    # plt.title('ECAL energy fraction')
    mplhep.cms.label('', data=False, rlabel='(14 TeV)')
    savefile = odir + '/Ecal_fraction_{}.png'.format(options.v)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    print('E/(E+H) > 0.8 = {}'.format(len(df_uncalib[df_uncalib['iem_ratio'] > 0.8])/len(df_uncalib)))


### To run:
### python3 ModelPlots.py --in 2022_05_02_NtuplesV9 --v HCAL --out data_ECAL_V1/plots

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",    dest="indir",   help="Input folder with trained model",     default=None)
    parser.add_option("--tag",      dest="tag",     help="tag of the training folder",      default="")
    parser.add_option("--out",      dest="odir",    help="Output folder",                       default=None)
    parser.add_option("--v",        dest="v",       help="Ntuple type ('ECAL' or 'HCAL')",      default='ECAL')
    parser.add_option("--maxeta",   dest="maxeta",  help="Eta max in the SF plot (None or 28)", default=None)
    (options, args) = parser.parse_args()
    print(options)

    # Definition of the trained model
    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    modeldir = indir + '/model_' + options.v
    print('\nModel dir = {}'.format(modeldir))

    # model1 = keras.models.load_model(modeldir + '/model', compile=False)
    # TTP = keras.models.load_model(modeldir + '/TTP', compile=False)
    model1 = keras.models.load_model(modeldir + '/model', compile=False, custom_objects={'fgrad': fgrad})
    TTP = keras.models.load_model(modeldir + '/TTP', compile=False, custom_objects={'fgrad': fgrad})

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

    eta_towers = np.loadtxt(open(SF_filename, "rb"), delimiter=',')[:,0]
    print('\nEta Trigger Towers = {}'.format(eta_towers))

    # Takes the matrix removing the first column (eta values), the header is commented and automatically removed
    ScaleFactors = np.loadtxt(open(SF_filename, "rb"), delimiter=',')[:,1:]
    # Definition of energy bin edges from the header
    with open(SF_filename) as f:
        header = f.readline().rstrip()
    bin_edges = header.split(',')[1:]
    bins_energy = [int(edge.split('-')[0].split('.')[0]) for edge in bin_edges] + [int(bin_edges[-1].split('-')[1].split('.')[0])] # [IET]
    # bins_energy = np.linspace(1,120,120) # [IET]
    print('\nEnergy bins for Scale Factors = {}'.format(bins_energy))

    #######################################################
    ################# Scale Factors plots #################
    #######################################################

    # Plot the scale factors
    print('\nPlot scale factors')
    PlotSF(ScaleFactors, bins_energy, odir, options.v, eta_towers)

    #######################################################
    ################## Resolution plots ###################
    #######################################################

    # Definition of eta bin edges
    # bins_eta = [0, 0.5, 1, 1.5, 2, 2.5, 5]
    # print('\nEta bins = {}'.format(bins_eta))
    # bins_energy = [0.5] + [ x for x in range(1,61) if x%4==0] # [GeV]

    # Build the two pandas for the training (uncalibrated) and testing (calibrated)
    # X samples contain : iesum = iem + ihad, eta tower
    # Y samples contain : jetPt, jetEta
    print('\nLoad data')
    # X_train = np.load(indir+'/X_train.npz')['arr_0']
    X_test = np.load(indir+'/X_test.npz')['arr_0']
    # Y_train = np.load(indir+'/Y_train.npz')['arr_0']
    Y_test = np.load(indir+'/Y_test.npz')['arr_0']

    # Define the uncalibrated jet energy (sum of the energies in each tower of the chuncky donut)
    X_test_iem = np.sum(X_test,axis = 1)[:,0:1].ravel() # [ET]
    X_test_ihad = np.sum(X_test,axis = 1)[:,1:2].ravel() # [ET]
    X_test_iesum = np.sum(X_test,axis = 1)[:,2:3].ravel() # [ET]

    # Define the calibrated jet energy (applying the model to the test samples)
    X_test_model, Y_test_model = convert_samples(X_test, Y_test, options.v)
    X_test_calib_sum = model1.predict(X_test_model) # [ET]

    print('\nBuild pandas')
    # Produce the pandas dataframes with jetPt, jetEta and jetEnergy (sum of the deposited energy in all the towers)
    df_uncalib = pd.DataFrame(data = {'jetPt': Y_test[:,0].ravel(), 'jetEta': np.abs(Y_test[:,1].ravel()), 'jetIem': X_test_iem, 'jetIhad': X_test_ihad, 'jetEnergy': X_test_iesum})
    df_calib   = pd.DataFrame(data = {'jetPt': Y_test[:,0].ravel(), 'jetEta': np.abs(Y_test[:,1].ravel()), 'jetIem': X_test_iem, 'jetIhad': X_test_ihad, 'jetEnergy': X_test_calib_sum.ravel()})

    # sum together the 'other' part of the enrgy to have a meaningful comparison with uncalib
    if options.v=='ECAL':
        df_calib['jetEnergy'] = df_calib['jetEnergy'] + df_calib['jetIhad']
    elif options.v=='HCAL':
        df_calib['jetEnergy'] = df_calib['jetEnergy'] + df_calib['jetIem']

    # Compute resolution
    print('\nCompute resolution')
    df_uncalib['res'] = df_uncalib['jetEnergy']/df_uncalib['jetPt']*0.5
    df_calib['res']   = df_calib['jetEnergy']/df_calib['jetPt']*0.5

    PlotResolution(df_uncalib,df_calib,odir,options.v)
    PlotGenJetPtSpectrum(df_uncalib,df_calib,odir,options.v)
    resolution = PlotResolution_bins(df_uncalib,df_calib,odir,options.v,'energy',15)
    resolution_eta = PlotResolution_bins(df_uncalib,df_calib,odir,options.v,'eta',0.5)

    ### New plots ###

    FindIeta_vctd = np.vectorize(FindIeta)
    df_uncalib['jetIeta'] = FindIeta_vctd(df_uncalib['jetEta'])
    df_calib['jetIeta'] = FindIeta_vctd(df_calib['jetEta'])

    ieta_values = [1,2,3,4,5,6]
    PlotResolution_vs_Pt_Etabin(df_uncalib, odir, options.v, ieta_values, 'uncalib')
    PlotResolution_vs_Pt_Etabin(df_calib,   odir, options.v, ieta_values, 'calib')

    pt_values = [1,5,10,15,20,25,30,35,40,60]
    PlotResolution_vs_Eta_Ptbin(df_uncalib, odir, options.v, pt_values, 'uncalib')
    PlotResolution_vs_Eta_Ptbin(df_calib,   odir, options.v, pt_values, 'calib')

    eta_values = [1,1.5]
    PlotResolution_vs_Pt_Etavalue(df_uncalib, df_calib, odir, options.v, eta_values)

    pt_values = [50,100]
    PlotResolution_vs_Eta_Ptvalue(df_uncalib, df_calib, odir, options.v, pt_values)

    PlotECALratio(df_uncalib)

    #df_uncalib.to_csv('df_uncalib.csv')
    #df_calib.to_csv('df_calib.csv')

    print('\nDONE!!!\n')