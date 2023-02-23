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

sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *
from NNModelTraining_FullyCustom_GPUdistributed_batchedRate import *

import mplhep
plt.style.use(mplhep.style.CMS)

c_uncalib = 'royalblue'
c_oldcalib = 'darkorange'
c_newcalib = 'green'
eta_towers = list(TowersEta.keys())

leg_uncalib = 'Uncalib.'
leg_oldcalib = 'Old calib.'
leg_newcalib = 'New calib.'

# leg_uncalib = 'Uncalib.'
# leg_oldcalib = 'Post-train floor calib.'
# leg_newcalib = 'In-train floor calib.'


# Plot inclusive calibrated and uncalibrated resolution
# The uncalibrated energy is the sum of all the energies (check that it's not just iem), *0.5 to have units of GeV, over all the CD towers
# It returns the standard deviation of the distribution
def PlotResolution(df_newCalib, df_oldCalib, df_unCalib,odir,v_sample):

    bins_res = np.linspace(0,2,50)
  
    plt.figure(figsize=(10,10))
    text_1 = leg_uncalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_unCalib['res'].mean(), df_unCalib['res'].std())
    plt.hist(df_unCalib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_uncalib)
    plt.xlabel('Resolution')
    plt.ylabel('a.u.')
    plt.grid(linestyle='dotted')
    plt.legend(fontsize=20)
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    # plt.title(leg_uncalib+' Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Res_{}_unCalib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    plt.figure(figsize=(10,10))
    text_1 = leg_oldcalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_oldCalib['res'].mean(), df_oldCalib['res'].std())
    plt.hist(df_oldCalib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_oldcalib)
    plt.xlabel('Resolution')
    plt.ylabel('a.u.')
    plt.grid(linestyle='dotted')
    plt.legend(fontsize=20)
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    # plt.title(leg_oldcalib+' Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Res_{}_oldCalib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    plt.figure(figsize=(10,10))
    text_1 = leg_newcalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_newCalib['res'].mean(), df_newCalib['res'].std())
    plt.hist(df_newCalib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_newcalib)
    plt.xlabel('Resolution')
    plt.ylabel('a.u.')
    plt.grid(linestyle='dotted')
    plt.legend(fontsize=20)
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    # plt.title(leg_newcalib+' Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Res_{}_newCalib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    # Plot simultaneously the calibrated and uncalibrated energy distributions
    plt.figure(figsize=(10,10))
    text_1 = leg_uncalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_unCalib['res'].mean(), df_unCalib['res'].std())
    plt.hist(df_unCalib['res'], bins=bins_res, label=text_1, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
    text_2 = leg_oldcalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_oldCalib['res'].mean(), df_oldCalib['res'].std())
    plt.hist(df_oldCalib['res'], bins=bins_res, label=text_2, histtype='step', density=True, stacked=True, linewidth=2, color=c_oldcalib)
    text_3 = leg_newcalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_newCalib['res'].mean(), df_newCalib['res'].std())
    plt.hist(df_newCalib['res'], bins=bins_res, label=text_3, histtype='step', density=True, stacked=True, linewidth=2, color=c_newcalib)
    plt.xlabel('Resolution')
    plt.ylabel('a.u.')
    plt.grid(linestyle='dotted')
    plt.legend(fontsize=15, loc='upper left')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    # plt.title('Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Res_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    return True

# Plot generated jets spctrum in energy
def PlotGenJetPtSpectrum(df_newCalib, df_oldCalib, df_unCalib,odir,v_sample):
    
    plt.figure(figsize=(10,10))
    plt.hist(df_unCalib['jetPt'], bins=100, label=leg_uncalib, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
    plt.hist(df_newCalib['jetPt'], bins=100, label=leg_newcalib, histtype='step', density=True, stacked=True, linewidth=2, color=c_newcalib)
    plt.hist(df_oldCalib['jetPt'], bins=100, label=leg_oldcalib, histtype='step', density=True, stacked=True, linewidth=2, color=c_oldcalib)
    plt.xlabel(f'Jet $p_t$ [GeV]')
    plt.ylabel('a.u.')
    plt.grid(linestyle='dotted')
    plt.legend(loc='upper right',fontsize=20)
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    # plt.title(r'Generated Jets $p_t$ Spectrum {}'.format(v_sample))
    savefile = odir + '/GenJetPt_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

# Plot calibrated and uncalibrated resolution in bins of jetPt or jetEta (based on bin_type)
def PlotResolution_bins(df_newCalib, df_oldCalib, df_unCalib, odir, v_sample, bin_type, steps):
    
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

    values = np.unique(df_newCalib[name])
    min_value = int(values.min())
    max_value = int(values.max())+1
    bins = np.arange(min_value, max_value, steps)
    bins = np.append(bins, max_value)
    if v_sample == 'ECAL' and bin_type == 'energy': bins = np.append([0, 5, 10], bins[1:])

    labels_text = []
    for i in range(len(bins)-1):
        labels_text.append('{}-{}'.format(bins[i], bins[i+1]))
    print(bins)
    df_newCalib[column_bin] = pd.cut(df_newCalib[name], bins = bins, labels = labels_text)
    df_oldCalib[column_bin] = pd.cut(df_oldCalib[name], bins = bins, labels = labels_text)
    df_unCalib[column_bin]   = pd.cut(df_unCalib[name], bins = bins, labels = labels_text)
    bins_labels = np.unique(df_newCalib[column_bin])
    
    for bin_label in sorted(bins_labels):
        
        fig = plt.figure(figsize=(10,10))
        bins_res = np.linspace(0,2,30)
        
        df_newCalib_bin = df_newCalib[df_newCalib[column_bin] == bin_label]
        df_oldCalib_bin = df_oldCalib[df_oldCalib[column_bin] == bin_label]
        df_unCalib_bin = df_unCalib[df_unCalib[column_bin] == bin_label]
        
        data.append({column_bin: bin_label, 
                     'uncalib_mean': df_unCalib_bin['res'].mean(), 
                     'uncalib_std' : df_unCalib_bin['res'].std(),
                     'oldcalib_mean'  : df_oldCalib_bin['res'].mean(),
                     'oldcalib_std'   : df_oldCalib_bin['res'].std(),
                     'newcalib_mean'  : df_newCalib_bin['res'].mean(),
                     'newcalib_std'   : df_newCalib_bin['res'].std()})
        
        text_1 = leg_uncalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_unCalib_bin['res'].mean(), df_unCalib_bin['res'].std())
        plt.hist(df_unCalib_bin['res'], bins=bins_res, label=text_1, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
        text_2 = leg_oldcalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_oldCalib_bin['res'].mean(), df_oldCalib_bin['res'].std())
        plt.hist(df_oldCalib_bin['res'], bins=bins_res, label=text_2, histtype='step', density=True, stacked=True, linewidth=2, color=c_oldcalib)
        text_3 = leg_newcalib+r': $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_newCalib_bin['res'].mean(), df_newCalib_bin['res'].std())
        plt.hist(df_newCalib_bin['res'], bins=bins_res, label=text_3, histtype='step', density=True, stacked=True, linewidth=2, color=c_newcalib)
        
        plt.grid(axis='y', alpha=0.5)
        plt.xlabel('Resolution')
        plt.ylabel('a.u.')
        plt.grid(linestyle='dotted')
        if name.split('jet')[1] == 'Pt': leg = plt.legend(loc='upper left', fontsize=15, title=r'$%s<p_{T}<%s$' % (bin_label.split('-')[0], bin_label.split('-')[1]))
        else:                            leg = plt.legend(loc='upper left', fontsize=15, title=r'$%s<\eta<%s$' % (bin_label.split('-')[0], bin_label.split('-')[1]))
        leg._legend_box.align = "left"
        mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
        # plt.title('{} = {} {}'.format(name, bin_label, units))
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
    plt.bar(resolution[column_bin], resolution['uncalib_std']/resolution['uncalib_mean'], width=-0.4, alpha=0.7, align='edge',  label=leg_uncalib, color=c_uncalib)
    plt.bar(resolution[column_bin], resolution['oldcalib_std']/resolution['oldcalib_mean'], width=0.4, alpha=0.7, align='center',  label=leg_oldcalib, color=c_oldcalib)
    plt.bar(resolution[column_bin], resolution['newcalib_std']/resolution['newcalib_mean'], width=0.4, alpha=0.7, align='edge', label=leg_newcalib, color=c_newcalib)
    plt.xticks(rotation=45)
    # if options.v == "HCAL": plt.ylim(0.0,0.8)
    # else:                   plt.ylim(0.0,0.5)
    if name.split('jet')[1] == "Pt": plt.xlim(-0.5,14.5)
    plt.xlabel('{} bins {}'.format(name, units))
    plt.ylabel('Resolution')
    plt.grid(linestyle='dotted')
    plt.subplots_adjust(bottom=0.20)
    plt.legend(loc='upper right')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    savefile = odir + '/Res_vs_{}_{}.png'.format(name.split('jet')[1], v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    fig, ax = plt.subplots(figsize = [18,10])
    trans1 = Affine2D().translate(-0.05, 0.0) + ax.transData
    trans2 = Affine2D().translate(+0.05, 0.0) + ax.transData
    trans3 = Affine2D().translate(+0.1, 0.0) + ax.transData
    plt.errorbar(resolution[column_bin], resolution['uncalib_mean'], yerr=resolution['uncalib_std'], fmt='o', alpha=1, label=leg_uncalib, color=c_uncalib, markersize=8, capsize=8, linewidth=3, elinewidth=3, capthick=3, transform=trans1)
    plt.errorbar(resolution[column_bin], resolution['oldcalib_mean'], yerr=resolution['oldcalib_std'], fmt='o', alpha=1, label=leg_oldcalib, color=c_oldcalib, markersize=8, capsize=8, linewidth=3, elinewidth=3, capthick=3, transform=trans2)
    plt.errorbar(resolution[column_bin], resolution['newcalib_mean'], yerr=resolution['newcalib_std'], fmt='o', alpha=1, label=leg_newcalib, color=c_newcalib, markersize=8, capsize=8, linewidth=3, elinewidth=3, capthick=3, transform=trans3)
    plt.axhline(y=1., color='black', linestyle='--')
    plt.xticks(rotation=45)
    # if options.v == "HCAL": plt.ylim(0.2,1.6)
    # else:                   plt.ylim(0.4,1.6)
    if name.split('jet')[1] == "Pt": plt.xlim(-0.5,14.5)
    plt.xlabel('{} bins {}'.format(name, units))
    plt.ylabel(r'Scale')
    plt.grid(linestyle='dotted')
    plt.subplots_adjust(bottom=0.20)
    plt.legend(loc='upper right')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
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
        plt.plot(prof.index, prof.values, '.', color=colors[i_eta], label=f'$\eta$ tower = {eta}')
        plt.xlabel('Jet Pt')
        plt.ylabel('Resolution')
        plt.grid(linestyle='dotted')
        if calib == 'uncalib':  title = leg_uncalib
        elif calib == 'newCalib': title = leg_newcalib
        else: title = leg_oldcalib
        # plt.title(title)
        plt.legend(fontsize = 15, ncol=1, loc = 'upper right')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
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
        plt.xlabel('Jet Eta')
        plt.ylabel('Resolution')
        plt.grid(linestyle='dotted')
        if calib == 'uncalib':  title = leg_uncalib
        elif calib == 'newCalib': title = leg_newcalib
        else: title = leg_oldcalib
        # plt.title(title)
        plt.legend(fontsize = 15, ncol=1, loc = 'upper right')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    savefile = odir + '/Res_vs_Eta_Ptbin_{}_{}.png'.format(calib, v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

def PlotResolution_vs_Pt_Etavalue(df_newCalib, df_oldCalib, df_unCalib, odir, v_sample, eta_values):

    plt.figure(figsize=(15,10))
    prof_newCalib = df_newCalib[(df_newCalib['jetEta']>eta_values[0]) & (df_newCalib['jetEta']<eta_values[1])].groupby('jetPt')['res'].mean()
    prof_oldCalib = df_oldCalib[(df_oldCalib['jetEta']>eta_values[0]) & (df_oldCalib['jetEta']<eta_values[1])].groupby('jetPt')['res'].mean()
    prof_unCalib = df_unCalib[(df_unCalib['jetEta']>eta_values[0]) & (df_unCalib['jetEta']<eta_values[1])].groupby('jetPt')['res'].mean()
    plt.plot(prof_newCalib.index, prof_newCalib.values, '.', color=c_newcalib, alpha=0.7, label=leg_newcalib)
    plt.plot(prof_oldCalib.index, prof_oldCalib.values, '.', color=c_oldcalib, alpha=0.7, label=leg_oldcalib)
    plt.plot(prof_unCalib.index, prof_unCalib.values, '.', color=c_uncalib, alpha=0.7, label=leg_uncalib)
    plt.xlabel('Jet Pt')
    plt.ylabel('Resolution')
    plt.grid(linestyle='dotted')
    # plt.title('Eta {}-{}'.format(eta_values[0], eta_values[1]))
    plt.legend(fontsize = 15, ncol=1, loc = 'upper right')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    savefile = odir + '/Res_vs_Pt_Eta{}-{}_{}.png'.format(eta_values[0], eta_values[1], v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

def PlotResolution_vs_Eta_Ptvalue(df_newCalib, df_oldCalib, df_unCalib, odir, v_sample, pt_values):

    plt.figure(figsize=(15,10))
    prof_newCalib = df_newCalib[(df_newCalib['jetPt']>pt_values[0]) & (df_newCalib['jetPt']<pt_values[1])].groupby('jetEta')['res'].mean()
    prof_oldCalib = df_oldCalib[(df_oldCalib['jetPt']>pt_values[0]) & (df_oldCalib['jetPt']<pt_values[1])].groupby('jetEta')['res'].mean()
    prof_unCalib = df_unCalib[(df_unCalib['jetPt']>pt_values[0]) & (df_unCalib['jetPt']<pt_values[1])].groupby('jetEta')['res'].mean()
    plt.plot(prof_newCalib.index, prof_newCalib.values, '.', color=c_newcalib, alpha=0.7, label=leg_newcalib)
    plt.plot(prof_oldCalib.index, prof_oldCalib.values, '.', color=c_oldcalib, alpha=0.7, label=leg_oldcalib)
    plt.plot(prof_unCalib.index, prof_unCalib.values, '.', color=c_uncalib, alpha=0.7, label=leg_uncalib)
    plt.xlabel('Jet Eta')
    plt.ylabel('Resolution')
    plt.grid(linestyle='dotted')
    # plt.title('Pt {}-{}'.format(pt_values[0], pt_values[1]))
    plt.legend(fontsize = 15, ncol=1, loc = 'upper right')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    savefile = odir + '/Res_vs_Eta_Pt{}-{}_{}.png'.format(pt_values[0], pt_values[1], v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()


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

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/AppliedTraining_' + options.v + '_' + options.tag

    # Definition of output folder
    if options.odir:
        odir = options.odir
    else: 
        odir = indir + '/plots'
    os.system('mkdir -p '+ odir)
    print('\nOutput dir = {}'.format(odir))

    eta_towers = np.arange(1,29,1)
    if options.v == "HCAL": eta_towers = np.arange(1,41,1)
    print('\nEta Trigger Towers = {}'.format(eta_towers))

    #######################################################
    ################## Resolution plots ###################
    #######################################################

    # X samples contain : ieta, iem, ihad, iesum
    # Y samples contain : jetPt, jetEta, jetPhi, trainingPt
    print('\nLoad data')

    # X_newCalib = np.load(indir+'/X_newCalib.npz')['arr_0']
    # Y_newCalib = np.load(indir+'/Y_newCalib.npz')['arr_0']
    # X_newCalib_iem = np.sum(X_newCalib,axis = 1)[:,1:2].ravel() # [ET]
    # X_newCalib_ihad = np.sum(X_newCalib,axis = 1)[:,2:3].ravel() # [ET]
    # X_newCalib_iesum = np.sum(X_newCalib,axis = 1)[:,3:4].ravel() # [ET]

    X_oldCalib = np.load(indir+'/X_oldCalib.npz')['arr_0']
    Y_oldCalib = np.load(indir+'/Y_oldCalib.npz')['arr_0']
    X_oldCalib_iem = np.sum(X_oldCalib,axis = 1)[:,0:1].ravel() # [ET]
    X_oldCalib_ihad = np.sum(X_oldCalib,axis = 1)[:,1:2].ravel() # [ET]
    X_oldCalib_iesum = np.sum(X_oldCalib,axis = 1)[:,2:3].ravel() # [ET]

    X_unCalib = np.load(indir+'/X_unCalib.npz')['arr_0']
    Y_unCalib = np.load(indir+'/Y_unCalib.npz')['arr_0']
    X_unCalib_iem = np.sum(X_unCalib,axis = 1)[:,0:1].ravel() # [ET]
    X_unCalib_ihad = np.sum(X_unCalib,axis = 1)[:,1:2].ravel() # [ET]
    X_unCalib_iesum = np.sum(X_unCalib,axis = 1)[:,2:3].ravel() # [ET]

    modeldir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/model_' + options.v
    model = keras.models.load_model(modeldir + '/model', compile=False, custom_objects={'Fgrad': Fgrad})
    X_test_model, Y_test_model, _ = convert_samples(X_unCalib, Y_unCalib, None, options.v)
    if options.v == "ECAL": dummy_rateProxy_input = np.repeat([np.zeros(42)], len(X_test_model), axis=0)
    if options.v == "HCAL": dummy_rateProxy_input = np.repeat([np.repeat([np.zeros(42)], 81, axis=0)], len(X_test_model), axis=0)
    X_test_calib_sum, _ = model.predict([X_test_model, dummy_rateProxy_input]) # [ET]
    if options.v == "ECAL": X_newCalib_iesum = X_test_calib_sum + X_unCalib_ihad.reshape(-1,1)
    if options.v == "HCAL": X_newCalib_iesum = X_test_calib_sum + X_unCalib_iem.reshape(-1,1)
    X_newCalib_iesum = tf.make_ndarray(tf.make_tensor_proto(X_newCalib_iesum)).reshape(1,-1)[0]

    print('\nBuild pandas')
    # Produce the pandas dataframes with jetPt, jetEta and jetEnergy (sum of the deposited energy in all the towers)
    df_newCalib = pd.DataFrame(data = {'jetPt': Y_unCalib[:,0].ravel(), 'jetEta': np.abs(Y_unCalib[:,1].ravel()), 'jetEnergy': X_newCalib_iesum}) # 'jetIem': X_newCalib_iem, 'jetIhad': X_newCalib_ihad,
    df_oldCalib = pd.DataFrame(data = {'jetPt': Y_oldCalib[:,0].ravel(), 'jetEta': np.abs(Y_oldCalib[:,1].ravel()), 'jetEnergy': X_oldCalib_iesum}) # 'jetIem': X_oldCalib_iem, 'jetIhad': X_oldCalib_ihad,
    df_unCalib  = pd.DataFrame(data = {'jetPt': Y_unCalib[:,0].ravel(), 'jetEta': np.abs(Y_unCalib[:,1].ravel()), 'jetEnergy': X_unCalib_iesum}) # 'jetIem': X_unCalib_iem, 'jetIhad': X_unCalib_ihad,

    # Compute resolution
    print('\nCompute resolution')
    df_newCalib['res'] = df_newCalib['jetEnergy']/(df_newCalib['jetPt']*2) # need *2 cause reading the GeV version of Pt
    df_oldCalib['res'] = df_oldCalib['jetEnergy']/(df_oldCalib['jetPt']*2)
    df_unCalib['res']  = df_unCalib['jetEnergy']/(df_unCalib['jetPt']*2)

    PlotResolution(df_newCalib, df_oldCalib, df_unCalib,odir,options.v)
    PlotGenJetPtSpectrum(df_newCalib, df_oldCalib, df_unCalib,odir,options.v)
    resolution = PlotResolution_bins(df_newCalib, df_oldCalib, df_unCalib,odir,options.v,'energy',15)
    resolution_eta = PlotResolution_bins(df_newCalib, df_oldCalib, df_unCalib,odir,options.v,'eta',0.5)

    ### New plots ###

    FindIeta_vctd = np.vectorize(FindIeta)
    df_newCalib['jetIeta'] = FindIeta_vctd(df_newCalib['jetEta'])
    df_oldCalib['jetIeta'] = FindIeta_vctd(df_oldCalib['jetEta'])
    df_unCalib['jetIeta'] = FindIeta_vctd(df_unCalib['jetEta'])

    #ieta_values = [1,2,3,4,5,6]
    ieta_values = [24,25,26,27,28,29,30]
    PlotResolution_vs_Pt_Etabin(df_newCalib, odir, options.v, ieta_values, 'newCalib')
    PlotResolution_vs_Pt_Etabin(df_oldCalib,   odir, options.v, ieta_values, 'oldCalib')
    PlotResolution_vs_Pt_Etabin(df_unCalib,   odir, options.v, ieta_values, 'unCalib')

    pt_values = [1,5,10,15,20,25,30,35,40,60]
    PlotResolution_vs_Eta_Ptbin(df_newCalib, odir, options.v, ieta_values, 'newCalib')
    PlotResolution_vs_Eta_Ptbin(df_oldCalib,   odir, options.v, ieta_values, 'oldCalib')
    PlotResolution_vs_Eta_Ptbin(df_unCalib,   odir, options.v, ieta_values, 'unCalib')

    eta_values = [1,1.5]
    PlotResolution_vs_Pt_Etavalue(df_newCalib, df_oldCalib, df_unCalib, odir, options.v, eta_values)

    pt_values = [50,100]
    PlotResolution_vs_Eta_Ptvalue(df_newCalib, df_oldCalib, df_unCalib, odir, options.v, pt_values)

    print('\nDONE!!!\n')