#librairies utiles
from re import S
from math import *
import pandas as pd
from matplotlib.transforms import Affine2D
from NNModelTraining_FullyCustom_GPUdistributed_oneGo_noRate import *
sys.path.insert(0,'..')
from L1NtupleReader.TowerGeometry import *

import mplhep
plt.style.use(mplhep.style.CMS)

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
        plt.plot(eta_towers, SF_matrix[i,:], 'o--', color=colors[i], label = f"{bins[i]} $\leq E_T <$ {bins[i+1]}")
    plt.xlabel('i$\eta$', fontsize=20)
    plt.ylabel('{} Calibration Constant'.format(v_sample), fontsize=20)
    plt.grid(linestyle='dotted')
    #plt.title('Calibration vs Eta')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    savefile = odir + '/Calib_vs_Eta_'+v_sample+'.png'
    plt.savefig(savefile)
    print(savefile)
    plt.ylim(0,13)
    legend = plt.legend(fontsize=10, ncol=8, loc = 'upper center')
    savefile = odir + '/Calib_vs_Eta_'+v_sample+'_legend.png'
    export_legend(legend, savefile)
    print(savefile)
    
    # Plot 2) Calibration constant vs ET for a few ieta

    # eta_towers_plot = [1,5,10,15,20] # to be chosen
    eta_towers_plot = eta_towers

    plt.figure(figsize=(12,8))
    colors = plt.cm.viridis_r(np.linspace(0,1,len(eta_towers)))
    for i in range(len(eta_towers)):
        if eta_towers[i] in eta_towers_plot:
            plt.plot(bins[:-1], SF_matrix[:-1,i], 'o--', color=colors[i], label = f"$\eta = ${eta_towers[i]}")
    plt.xlabel(f'i$E_T$', fontsize=20)
    plt.ylabel('{} calibration constant'.format(v_sample), fontsize=20)
    plt.legend(fontsize=10, ncol=4, loc = 'upper right')
    plt.grid(linestyle='dotted')
    # plt.title('Calibration vs Energy')
    savefile = odir + '/Calib_vs_Energy_'+v_sample+'.png'
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    plt.savefig(savefile)
    print(savefile)

    plt.figure(figsize=(12,8))
    colors = plt.cm.viridis_r(np.linspace(0,1,len(eta_towers)))
    for i in range(len(eta_towers)):
        if eta_towers[i] in eta_towers_plot:
            plt.plot(bins[:-1], [SF*IE for SF,IE in zip(SF_matrix[:-1,i],bins[:-1])], 'o--', color=colors[i], label = f"$\eta = ${eta_towers[i]}")
    plt.xlabel(f'i$E_T$', fontsize=20)
    plt.ylabel('i$E_T$ calibrated', fontsize=20)
    plt.legend(fontsize=10, ncol=3, loc = 'upper left')
    plt.grid(linestyle='dotted')
    # plt.title('Calibration vs Energy')
    savefile = odir + '/CalibratedIet_vs_Energy_'+v_sample+'.png'
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
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
    plt.xlabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$', fontsize=20)
    plt.ylabel('a.u.', fontsize=20)
    plt.legend(fontsize=20)
    # plt.title('Uncalibrated Jets Resolution {}'.format(v_sample))
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    savefile = odir + '/Res_{}_uncalib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    plt.figure(figsize=(12,8))
    text_1 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib['res'].mean(), df_calib['res'].std())
    plt.hist(df_calib['res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_calib)
    plt.xlabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$', fontsize=20)
    plt.ylabel('a.u.', fontsize=20)
    plt.legend(fontsize=20)
    # plt.title('Calibrated Jets Resolution {}'.format(v_sample))
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    savefile = odir + '/Res_{}_calib.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)

    # Plot simultaneously the calibrated and uncalibrated energy distributions
    plt.figure(figsize=(12,8))
    text_1 = r'Uncalib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_uncalib['res'].mean(), df_uncalib['res'].std())
    plt.hist(df_uncalib['res'], bins=bins_res, label=text_1, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
    text_2 = r'Calib: $\mu = {:.3f}, \sigma = {:.3f}$'.format(df_calib['res'].mean(), df_calib['res'].std())
    plt.hist(df_calib['res'], bins=bins_res, label=text_2, histtype='step', density=True, stacked=True, linewidth=2, color=c_calib)
    plt.xlabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$', fontsize=20)
    plt.ylabel('a.u.', fontsize=20)
    plt.legend(fontsize=20)
    # plt.title('Jets Resolution {}'.format(v_sample))
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
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
    plt.xlabel('$p_T^{gen}(jet)$ [GeV]', fontsize=20)
    plt.ylabel('a.u.', fontsize=20)
    plt.legend(loc='upper right',fontsize=20)
    # plt.title(r'Generated Jets $p_t$ Spectrum {}'.format(v_sample))
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
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
        plt.xlabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$', fontsize=20)
        plt.ylabel('a.u.', fontsize=20)
        plt.legend(loc='upper left', fontsize=20, title='{} = {} {}'.format(label, bin_label, units))
        # plt.title('{} = {} {}'.format(name, bin_label, units))
        mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
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
    if name.split('jet')[1] == "Pt": plt.xlim(-0.5,14.5)
    plt.xlabel('{} {}'.format(label, units), fontsize=20)
    plt.ylabel('$p_{T}^{gen}(jet)$ resolution', fontsize=20)
    # plt.title(f'Jets resolution')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    plt.legend(loc='upper right', fontsize=20)
    savefile = odir + '/Res_vs_{}_{}.png'.format(name.split('jet')[1], v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    fig, ax = plt.subplots(figsize = [24,15])
    trans1 = Affine2D().translate(-0.05, 0.0) + ax.transData
    trans2 = Affine2D().translate(+0.05, 0.0) + ax.transData
    plt.errorbar(resolution[column_bin], resolution['uncalib_mean'], yerr=resolution['uncalib_std'], fmt='o', alpha=1, label='Uncalib', color=c_uncalib, markersize=15, capsize=8, linewidth=2, elinewidth=2, capthick=2, transform=trans1)
    plt.errorbar(resolution[column_bin], resolution['calib_mean'], yerr=resolution['calib_std'], fmt='o', alpha=1, label='Calib', color=c_calib, markersize=15, capsize=8, linewidth=2, elinewidth=2, capthick=2, transform=trans2)
    plt.xticks(rotation=45)
    plt.axhline(y=1., color='black', linestyle='--')
    plt.ylim(0.4,1.6)
    if name.split('jet')[1] == "Pt": plt.xlim(-0.5,14.5)
    plt.xlabel('{} {}'.format(label, units), fontsize=20)
    plt.ylabel('$p_{T}^{gen}(jet)$ scale', fontsize=20)
    # plt.title(f'Jets resolution')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    plt.legend(loc='upper right', fontsize=20)
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
        plt.xlabel('$p_T^{gen}(jet)$ [GeV]', fontsize=20)
        plt.ylabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$', fontsize=20)
        #if calib == 'uncalib':  title = 'Uncalibrated'
        #else:                   title = 'Calibrated'
        #plt.title(title)
        mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
        plt.legend(fontsize=20, ncol=1, loc = 'upper right')
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
        plt.xlabel('$\eta^{gen}(jet)$', fontsize=20)
        plt.ylabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$', fontsize=20)
        # if calib == 'uncalib':  title = 'Uncalibrated'
        # else:                   title = 'Calibrated'
        # plt.title(title)
        mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
        plt.legend(fontsize=20, ncol=1, loc = 'upper right')
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
    plt.xlabel('$p_{T}^{gen}(jet)$ [GeV]', fontsize=20)
    plt.ylabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$', fontsize=20)
    # plt.title('Eta {}-{}'.format(eta_values[0], eta_values[1]))
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    plt.legend(fontsize=20, ncol=1, loc = 'upper right', title=str(eta_values[0])+'<$|\eta^{gen}(jet)|$<'+str(eta_values[1]))
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
    plt.xlabel('$\eta^{gen}(jet)$', fontsize=20)
    plt.ylabel('$E_{T}^{L1}(jet)/p_{T}^{gen}(jet)$', fontsize=20)
    # plt.title('Pt {}-{}'.format(pt_values[0], pt_values[1]))
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    plt.legend(fontsize=20, ncol=1, loc = 'upper right', title=str(pt_values[0])+'<$p_{T}^{gen}(jet)$<'+str(pt_values[1]))
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
    parser.add_option("--energystep", dest="energystep", help="Energy steps",                    type=int,   default=1)
    (options, args) = parser.parse_args()
    print(options)
 
    # Definition of the trained model
    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    modeldir = indir + '/model_' + options.v
    # Definition of output folder
    if options.odir:
       odir = options.odir
    else: 
       odir = indir + '/plots'
    os.system('mkdir -p '+ odir)
 
    #######################################################
    ################# Scale Factors plots #################
    #######################################################

    energy_step = options.energystep

    ## ECAL
    # Read the Scale factors
    SF_filename = indir + '/data/ScaleFactors_ECAL_energystep'+str(energy_step)+'iEt.csv'
    ScaleFactors = np.loadtxt(open(SF_filename, "rb"), delimiter=',')
    eta_towers = range(1, len(ScaleFactors[1])+1)

    # Definition of energy bin edges from the header
    with open(SF_filename) as f:
        header = f.readline().rstrip()
    bin_edges = header.split(',')[1:]
    bin_edges[-1] = bin_edges[-1][:-1]
    if bin_edges[-1] == '256': bin_edges[-1] = '200'
    bin_edges = [ int(x) for x in bin_edges ]

    PlotSF(ScaleFactors, bin_edges, odir, "ECAL", eta_towers)

    ## HCAL
    # Read the Scale factors
    SF_filename = indir + '/data/ScaleFactors_HCAL_energystep'+str(energy_step)+'iEt.csv'
    ScaleFactors = np.loadtxt(open(SF_filename, "rb"), delimiter=',')
    eta_towers = range(1, len(ScaleFactors[1])+1)

    # Definition of energy bin edges from the header
    with open(SF_filename) as f:
        header = f.readline().rstrip()
    bin_edges = header.split(',')[1:]
    bin_edges[-1] = bin_edges[-1][:-1]
    if bin_edges[-1] == '256': bin_edges[-1] = '200'
    bin_edges = [ int(x) for x in bin_edges ]

    PlotSF(ScaleFactors, bin_edges, odir, "HCAL", eta_towers)

    ## HF
    # Read the Scale factors
    SF_filename = indir + '/data/ScaleFactors_HF_energystep'+str(energy_step)+'iEt.csv'
    ScaleFactors = np.loadtxt(open(SF_filename, "rb"), delimiter=',')
    eta_towers = range(30, 30+len(ScaleFactors[1]))

    # Definition of energy bin edges from the header
    with open(SF_filename) as f:
        header = f.readline().rstrip()
    bin_edges = header.split(',')[1:]
    bin_edges[-1] = bin_edges[-1][:-1]
    if bin_edges[-1] == '256': bin_edges[-1] = '200'
    bin_edges = [ int(x) for x in bin_edges ]

    PlotSF(ScaleFactors, bin_edges, odir, "HF", eta_towers)

    #######################################################
    ################## Resolution plots ###################
    #######################################################

    model = keras.models.load_model(modeldir + '/model', compile=False, custom_objects={'Fgrad': Fgrad})

    # Build the two pandas for the training (uncalibrated) and testing (calibrated)
    # X samples contain : iesum = iem + ihad, eta tower
    # Y samples contain : jetPt, jetEta
    print('\nLoad data')
    X_ecal_test = np.load(indir+'/X_ecal_test.npz')['arr_0']
    Y_ecal_test = np.load(indir+'/Y_ecal_test.npz')['arr_0']
    X_hcal_test = np.load(indir+'/X_hcal_test.npz')['arr_0']
    Y_hcal_test = np.load(indir+'/Y_hcal_test.npz')['arr_0']
    # make the datasets the smae length to avoid tensorflow data cardinality errors
    X_ecal_test = X_ecal_test[ :X_hcal_test.shape[0] ]
    Y_ecal_test = Y_ecal_test[ :Y_hcal_test.shape[0] ]

    # Define the uncalibrated jet energy (sum of the energies in each tower of the chuncky donut)
    X_ecal_test_iesum = np.sum(X_ecal_test,axis = 1)[:,2:3].ravel()
    X_hcal_test_iesum = np.sum(X_hcal_test,axis = 1)[:,2:3].ravel()

    # Define the calibrated jet energy (applying the model to the test samples)
    X_ecal_test_model, Y_ecal_test_model = convert_samples(X_ecal_test, Y_ecal_test, "ECAL")
    X_hcal_test_model, Y_hcal_test_model = convert_samples(X_hcal_test, Y_hcal_test, "HCAL")

    X_ecal_test_calib, X_hcal_test_calib = model.predict([X_ecal_test_model, X_hcal_test_model])

    print('\nBuild pandas')
    # Produce the pandas dataframes with jetPt, jetEta and jetEnergy (sum of the deposited energy in all the towers)
    df_ecal_uncalib = pd.DataFrame(data = {'jetPt': Y_ecal_test[:,0].ravel(), 'jetEta': np.abs(Y_ecal_test[:,1].ravel()), 'jetEnergy': X_ecal_test_iesum})
    df_ecal_calib   = pd.DataFrame(data = {'jetPt': Y_ecal_test[:,0].ravel(), 'jetEta': np.abs(Y_ecal_test[:,1].ravel()), 'jetEnergy': X_ecal_test_calib.ravel()})
    df_hcal_uncalib = pd.DataFrame(data = {'jetPt': Y_hcal_test[:,0].ravel(), 'jetEta': np.abs(Y_hcal_test[:,1].ravel()), 'jetEnergy': X_hcal_test_iesum})
    df_hcal_calib   = pd.DataFrame(data = {'jetPt': Y_hcal_test[:,0].ravel(), 'jetEta': np.abs(Y_hcal_test[:,1].ravel()), 'jetEnergy': X_hcal_test_calib.ravel()})

    # Compute resolution
    print('\nCompute resolution')
    df_ecal_uncalib['res'] = df_ecal_uncalib['jetEnergy']/df_ecal_uncalib['jetPt']*0.5
    df_ecal_calib['res']   = df_ecal_calib['jetEnergy']/df_ecal_calib['jetPt']*0.5
    df_hcal_uncalib['res'] = df_hcal_uncalib['jetEnergy']/df_hcal_uncalib['jetPt']*0.5
    df_hcal_calib['res']   = df_hcal_calib['jetEnergy']/df_hcal_calib['jetPt']*0.5


    ## ECAL PLOTS
    PlotResolution(df_ecal_uncalib,df_ecal_calib,odir,"ECAL")
    PlotGenJetPtSpectrum(df_ecal_uncalib,df_ecal_calib,odir,"ECAL")
    resolution = PlotResolution_bins(df_ecal_uncalib,df_ecal_calib,odir,"ECAL",'energy',15)
    resolution_eta = PlotResolution_bins(df_ecal_uncalib,df_ecal_calib,odir,"ECAL",'eta',0.5)

    FindIeta_vctd = np.vectorize(FindIeta)
    df_ecal_uncalib['jetIeta'] = FindIeta_vctd(df_ecal_uncalib['jetEta'])
    df_ecal_calib['jetIeta'] = FindIeta_vctd(df_ecal_calib['jetEta'])

    ieta_values = [1,2,3,4,5,6]
    PlotResolution_vs_Pt_Etabin(df_ecal_uncalib, odir, "ECAL", ieta_values, 'uncalib')
    PlotResolution_vs_Pt_Etabin(df_ecal_calib,   odir, "ECAL", ieta_values, 'calib')

    pt_values = [1,5,10,15,20,25,30,35,40,60]
    PlotResolution_vs_Eta_Ptbin(df_ecal_uncalib, odir, "ECAL", pt_values, 'uncalib')
    PlotResolution_vs_Eta_Ptbin(df_ecal_calib,   odir, "ECAL", pt_values, 'calib')

    eta_values = [1,1.5]
    PlotResolution_vs_Pt_Etavalue(df_ecal_uncalib, df_ecal_calib, odir, "ECAL", eta_values)

    pt_values = [50,100]
    PlotResolution_vs_Eta_Ptvalue(df_ecal_uncalib, df_ecal_calib, odir, "ECAL", pt_values)


    ## HCAL PLOTS
    PlotResolution(df_hcal_uncalib,df_hcal_calib,odir,"HCAL")
    PlotGenJetPtSpectrum(df_hcal_uncalib,df_hcal_calib,odir,"HCAL")
    resolution = PlotResolution_bins(df_hcal_uncalib,df_hcal_calib,odir,"HCAL",'energy',15)
    resolution_eta = PlotResolution_bins(df_hcal_uncalib,df_hcal_calib,odir,"HCAL",'eta',0.5)

    FindIeta_vctd = np.vectorize(FindIeta)
    df_hcal_uncalib['jetIeta'] = FindIeta_vctd(df_hcal_uncalib['jetEta'])
    df_hcal_calib['jetIeta'] = FindIeta_vctd(df_hcal_calib['jetEta'])

    ieta_values = [1,2,3,4,5,6]
    PlotResolution_vs_Pt_Etabin(df_hcal_uncalib, odir, "HCAL", ieta_values, 'uncalib')
    PlotResolution_vs_Pt_Etabin(df_hcal_calib,   odir, "HCAL", ieta_values, 'calib')

    pt_values = [1,5,10,15,20,25,30,35,40,60]
    PlotResolution_vs_Eta_Ptbin(df_hcal_uncalib, odir, "HCAL", pt_values, 'uncalib')
    PlotResolution_vs_Eta_Ptbin(df_hcal_calib,   odir, "HCAL", pt_values, 'calib')

    eta_values = [1,1.5]
    PlotResolution_vs_Pt_Etavalue(df_hcal_uncalib, df_hcal_calib, odir, "HCAL", eta_values)

    pt_values = [50,100]
    PlotResolution_vs_Eta_Ptvalue(df_hcal_uncalib, df_hcal_calib, odir, "HCAL", pt_values)


    print('\nDONE!!!\n')
