import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sys, glob, os
import pandas as pd
import math
sys.path.insert(0,'../L1Calibrator/')

import mplhep
plt.style.use(mplhep.style.CMS)

# from caloParamsOnTheFly import *
from NNModelTraining_FullyCustom_GPUdistributed_batchedRate_oldDatasets import * 

c_uncalib = 'black'
c_oldcalib = 'red'
c_newcalib = 'green'

leg_uncalib = 'No calib'
leg_oldcalib = 'Old calib'
leg_newcalib = 'New calib'

feature_description = {
    'chuncky_donut': tf.io.FixedLenFeature([], tf.string, default_value=''), # byteslist to be read as string 
    'trainingPt'   : tf.io.FixedLenFeature([], tf.float32, default_value=0)  # single float values
}

# parse proto input based on description
def parse_function(example_proto):
    example = tf.io.parse_single_example(example_proto, feature_description)
    chuncky_donut = tf.io.parse_tensor(example['chuncky_donut'], out_type=tf.float32) # decode byteslist to original 81x43 tensor
    return chuncky_donut, example['trainingPt']

TowersEta = {
    1:  [0,     0.087],    2: [0.087,  0.174],    3: [0.174,  0.261],    4: [0.261,  0.348],    5: [0.348,  0.435],    6: [0.435,  0.522],    7: [0.522,  0.609],    8: [0.609,  0.696],    9: [0.696,  0.783],    10: [0.783,  0.870],
    11: [0.870, 0.957],    12: [0.957, 1.044],    13: [1.044, 1.131],    14: [1.131, 1.218],    15: [1.218, 1.305],    16: [1.305, 1.392],    17: [1.392, 1.479],    18: [1.479, 1.566],    19: [1.566, 1.653],    20: [1.653, 1.740],
    21: [1.740, 1.830],    22: [1.830, 1.930],    23: [1.930, 2.043],    24: [2.043, 2.172],    25: [2.172, 2.322],    26: [2.322, 2.5],      27: [2.5,   2.650],    28: [2.650, 3.],       29: [3., 3.139],       30: [3.139, 3.314],
    31: [3.314, 3.489],    32: [3.489, 3.664],    33: [3.664, 3.839],    34: [3.839, 4.013],    35: [4.013, 4.191],    36: [4.191, 4.363],    37: [4.363, 4.538],    38: [4.538, 4.716],    39: [4.716, 4.889],    40: [4.889, 5.191],}

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def PlotResolutionInclusive(df_jets, odir, v_sample):

    bins_res = np.linspace(0,3,240)
    cmap = matplotlib.cm.get_cmap('Set1')

    plt.figure(figsize=(10,10))
    sel_barrel = np.abs(df_jets['jetEta']) < 1.305
    text_1 = leg_uncalib+r' barrel : $\mu={:.3f}, res={:.3f}$'.format(df_jets[sel_barrel]['unc_res'].mean(), df_jets[sel_barrel]['unc_res'].std()/df_jets[sel_barrel]['unc_res'].mean())
    plt.hist(df_jets[sel_barrel]['unc_res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(0))
    sel_endcap = np.abs(df_jets['jetEta']) >= 1.305
    text_1 = leg_uncalib+r' endcap : $\mu={:.3f}, res={:.3f}$'.format(df_jets[sel_endcap]['unc_res'].mean(), df_jets[sel_endcap]['unc_res'].std()/df_jets[sel_endcap]['unc_res'].mean())
    plt.hist(df_jets[sel_endcap]['unc_res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(1))
    text_1 = leg_uncalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['unc_res'].mean(), df_jets['unc_res'].std()/df_jets['unc_res'].mean())
    counts, bins, _ = plt.hist(df_jets['unc_res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(2))
    plt.xlabel('Response')
    plt.ylabel('a.u.')
    plt.ylim(0, 1.3*np.max(counts))
    plt.xlim(0,3)
    plt.grid(linestyle='dotted')
    plt.legend(fontsize=15, loc='upper left')
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
    # plt.title('Jets Resolution {}'.format(v_sample))
    savefile = odir + '/Res_{}.png'.format(v_sample)
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    if v_sample == "ECAL":
        plt.figure(figsize=(10,10))
        sel_barrel = np.abs(df_jets['jetEta']) < 1.305
        text_1 = leg_uncalib+r' barrel : $\mu={:.3f}, res={:.3f}$'.format(df_jets[sel_barrel]['unc_res_iem'].mean(), df_jets[sel_barrel]['unc_res_iem'].std()/df_jets[sel_barrel]['unc_res_iem'].mean())
        plt.hist(df_jets[sel_barrel]['unc_res_iem'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(0))
        sel_endcap = np.abs(df_jets['jetEta']) >= 1.305
        text_1 = leg_uncalib+r' endcap : $\mu={:.3f}, res={:.3f}$'.format(df_jets[sel_endcap]['unc_res_iem'].mean(), df_jets[sel_endcap]['unc_res_iem'].std()/df_jets[sel_endcap]['unc_res_iem'].mean())
        plt.hist(df_jets[sel_endcap]['unc_res_iem'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(1))
        text_1 = leg_uncalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['unc_res_iem'].mean(), df_jets['unc_res_iem'].std()/df_jets['unc_res_iem'].mean())
        counts, bins, _ = plt.hist(df_jets['unc_res_iem'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(2))
        plt.xlabel('Response Only Iem')
        plt.ylabel('a.u.')
        plt.ylim(0, 1.3*np.max(counts))
        plt.xlim(0,3)
        plt.grid(linestyle='dotted')
        plt.legend(fontsize=15, loc='upper left')
        mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
        # plt.title('Jets Resolution {}'.format(v_sample))
        savefile = odir + '/Res_{}_Iem.png'.format(v_sample)
        plt.savefig(savefile)
        print(savefile)
        plt.close()

    if v_sample == "HCAL":
        plt.figure(figsize=(10,10))
        sel_barrel = np.abs(df_jets['jetEta']) < 1.305
        text_1 = leg_uncalib+r' barrel : $\mu={:.3f}, res={:.3f}$'.format(df_jets[sel_barrel]['unc_res_ihad'].mean(), df_jets[sel_barrel]['unc_res_ihad'].std()/df_jets[sel_barrel]['unc_res_ihad'].mean())
        plt.hist(df_jets[sel_barrel]['unc_res_ihad'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(0))
        sel_endcap = np.abs(df_jets['jetEta']) >= 1.305
        text_1 = leg_uncalib+r' endcap : $\mu={:.3f}, res={:.3f}$'.format(df_jets[sel_endcap]['unc_res_ihad'].mean(), df_jets[sel_endcap]['unc_res_ihad'].std()/df_jets[sel_endcap]['unc_res_ihad'].mean())
        plt.hist(df_jets[sel_endcap]['unc_res_ihad'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(1))
        text_1 = leg_uncalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['unc_res_ihad'].mean(), df_jets['unc_res_ihad'].std()/df_jets['unc_res_ihad'].mean())
        counts, bins, _ = plt.hist(df_jets['unc_res_ihad'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=cmap(2))
        plt.xlabel('Response')
        plt.ylabel('a.u.')
        plt.ylim(0, 1.3*np.max(counts))
        plt.xlim(0,3)
        plt.grid(linestyle='dotted')
        plt.legend(fontsize=15, loc='upper left')
        mplhep.cms.label(data=False, rlabel='(13.6 TeV)', fontsize=20)
        # plt.title('Jets Resolution {}'.format(v_sample))
        savefile = odir + '/Res_{}_Ihad.png'.format(v_sample)
        plt.savefig(savefile)
        print(savefile)
        plt.close()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def PlotResolutionPtBins(df_jets, odir, v_sample, bin_type):
    
    bins_res = np.linspace(0,3,240)

    if v_sample == 'HCAL':
        if bin_type == 'pt':
            keyBins  = [30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200, 500]
            key = 'jetPt'
            legend_label = r'$<p_{T}^{jet, offline}<$'
            x_label = r'$p_{T}^{jet, offline}$'
        elif bin_type == 'eta':
            keyBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.191]
            key = 'jetEta'
            legend_label = r'$<|\eta^{jet, offline}|<$'
            x_label = r'$\eta^{jet, offline}$'
        elif bin_type == 'ieta':
            keyBins = np.arange(1,40)
            key = 'jetIEta'
            legend_label = r'$<|i_{\eta}^{jet, offline}|<$'
            x_label = r'$\eta^{jet, offline}$'
        x_lim = (0.,3.)
        x_label_res = r'$E_{T}^{jet, L1} / p_{T}^{jet, offline}$'
    if v_sample == 'ECAL':
        if bin_type == 'pt':
            keyBins  = [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200]
            key = 'jetPt'
            legend_label = r'$<p_{T}^{e, offline}<$'
            x_label = r'$p_{T}^{e, offline}$'
        elif bin_type == 'eta':
            keyBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0]
            key = 'jetEta'
            legend_label = r'$<|\eta^{e, offline}|<$'
            x_label = r'$\eta^{e, offline}$'
        x_lim = (0.2,1.5)
        x_label_res = r'$E_{T}^{e/\gamma, L1} / p_{T}^{e, offline}$'

    mean_vs_pt_unc = []
    res_vs_pt_unc = []
    maximum_vs_pt_unc = []

    for i in range(len(keyBins)-1):
        
        fig, ax = plt.subplots(figsize=(10,10))
        if bin_type == 'pt': sel_pt = (df_jets[key] > keyBins[i]*2) & (df_jets[key] < keyBins[i+1]*2)
        elif bin_type == 'eta': sel_pt = (df_jets[key] > keyBins[i]) & (df_jets[key] < keyBins[i+1])
        h = plt.hist(df_jets[sel_pt]['unc_res'], bins=bins_res, label=leg_uncalib, histtype='step', density=True, stacked=True, linewidth=2, color=c_uncalib)
        mean_vs_pt_unc.append(df_jets[sel_pt]['unc_res'].mean())
        res_vs_pt_unc.append(df_jets[sel_pt]['unc_res'].std()/df_jets[sel_pt]['unc_res'].mean())
        if h[0][0] >= 0: maximum_vs_pt_unc.append(h[1][np.where(h[0] == h[0].max())][0])
        else: maximum_vs_pt_unc.append(0)
        if h[0][0] >= 0: Ymax = h[0].max()
        
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20, title=str(keyBins[i])+legend_label+str(keyBins[i+1]), title_fontsize=18)
        leg._legend_box.align = "left"
        plt.xlabel(x_label_res)
        plt.ylabel('a.u.')
        plt.xlim(x_lim)
        plt.ylim(0., Ymax*1.3)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        savefile = odir+'/response_'+str(keyBins[i])+bin_type+str(keyBins[i+1])+'_'+v_sample+'.png'
        plt.savefig(savefile)
        print(savefile)
        plt.close()

    # plot resolution vs keyBins

    fig = plt.figure(figsize = [10,10])
    X = [(keyBins[i] + keyBins[i+1])/2 for i in range(len(keyBins)-1)]
    X_err = [(keyBins[i+1] - keyBins[i])/2 for i in range(len(keyBins)-1)]
    plt.errorbar(X, res_vs_pt_unc, xerr=X_err, label=leg_uncalib, ls='None', lw=2, marker='o', color=c_uncalib, zorder=0)
    Ymax = max(res_vs_pt_unc)

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy resolution')
    plt.xlim(keyBins[0], keyBins[-1])
    plt.ylim(0., Ymax*1.3)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    savefile = odir+'/resolution_'+bin_type+'Bins_'+v_sample+'.png'
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    # plot scale vs keyBins
    fig = plt.figure(figsize = [10,10])
    plt.errorbar(X, mean_vs_pt_unc, xerr=X_err, label=leg_uncalib, ls='None', lw=2, marker='o', color=c_uncalib, zorder=0)
    Ymax = max(mean_vs_pt_unc)

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(keyBins[0], keyBins[-1])
    plt.ylim(0., Ymax*1.3)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    savefile = odir+'/scale_'+bin_type+'Bins_'+v_sample+'.png'
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    # plot scale from maximum vs keybins
    fig = plt.figure(figsize = [10,10])
    plt.errorbar(X, maximum_vs_pt_unc, xerr=X_err, label=leg_uncalib, ls='None', lw=2, marker='o', color=c_uncalib, zorder=0)
    Ymax = max(maximum_vs_pt_unc)

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(keyBins[0], keyBins[-1])
    plt.ylim(0., Ymax*1.3)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    savefile = odir+'/scale_max_'+bin_type+'Bins_'+v_sample+'.png'
    plt.savefig(savefile)
    print(savefile)
    plt.close()

### To run:
### python3 PlotResponseTF.py --indir 2023_05_01_NtuplesV44 --v HCAL --tag DataReco --filesLim 2 --addtag _A
### python3 PlotResponseTF.py --indir 2023_05_19_NtuplesV46 --v ECAL --tag DataReco --filesLim 2

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",        dest="indir",       help="Input folder with trained model",     default=None)
    parser.add_option("--tag",          dest="tag",         help="tag of the training folder",          default="")
    parser.add_option("--v",            dest="v",           help="Ntuple type ('ECAL' or 'HCAL')",      default='ECAL')
    parser.add_option("--filesLim",     dest="filesLim",    help="Maximum number of npz files to use",  default=1000000, type=int)
    parser.add_option("--addtag",       dest="addtag",      help="Add tag for different trainings",     default="")
    parser.add_option("--ietacut",      dest="ietacut",     help="Apply ieta cut",                      default=None)
    parser.add_option("--ljetPtcut",    dest="ljetPtcut",   help="Apply lowerjetPt cut [GeV]",          default=None)
    parser.add_option("--ujetPtcut",    dest="ujetPtcut",   help="Apply upperjetPt cut [GeV]",          default=None)
    parser.add_option("--HoEcut",       dest="HoEcut",      help="Apply HoE cut at 0.95",               default=None)
    (options, args) = parser.parse_args()
    print(options)

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/plots' + options.addtag + '/PerformancePlots_Uncalib'
    os.system('mkdir -p '+ odir)
    print('\n ### Reading TF records from: ' + indir + '/testTFRecords/record_*.tfrecord')
    InTestRecords = glob.glob(indir+'/t*TFRecords/record_*.tfrecord')[:options.filesLim]
    dataset = tf.data.TFRecordDataset(InTestRecords)
    batch_size = len(list(dataset))
    parsed_dataset = dataset.map(parse_function)
    data = parsed_dataset.batch(batch_size).as_numpy_iterator().next()
    print('\n ### N events: ' + str(len(list(dataset))))

    Towers = data[0]
    Jets = data[1]

    print('\n ### Load Dataframes')

    # Extract the iem and hcalET columns from Towers
    if options.v == 'ECAL':
        iem = Towers[:, :, 1].reshape(-1)
        hcalET = Towers[:, :, 0].reshape(-1)
    elif options.v == 'HCAL':
        iem = Towers[:, :, 0].reshape(-1)
        hcalET = Towers[:, :, 1].reshape(-1)
    # Extract the ieta column from Towers using argmax
    ieta = np.argmax(Towers[:, :, 2:], axis=2).reshape(-1) + 1
    # Create arrays for the id and jetPt columns
    id_arr = np.repeat(np.arange(len(Towers)), Towers.shape[1])
    jetPt_arr = np.repeat(Jets, Towers.shape[1])

    # Combine the arrays into a dictionary and create the dataframe
    df_Towers = pd.DataFrame({'id': id_arr, 'jetPt': jetPt_arr, 'iem': iem, 'hcalET': hcalET, 'ieta': ieta})

    if options.ljetPtcut:
        df_Towers = df_Towers[df_Towers['jetPt'] > float(options.ljetPtcut)*2]
    if options.ujetPtcut:
        df_Towers = df_Towers[df_Towers['jetPt'] < float(options.ujetPtcut)*2]

    # compute sum of the raw energy 
    df_jets = pd.DataFrame()
    df_jets['SumIem']     = df_Towers.groupby('id').iem.sum()
    df_jets['SumIhad']    = df_Towers.groupby('id').hcalET.sum()
    df_jets['unCalib']    = df_Towers.groupby('id').iem.sum() + df_Towers.groupby('id').hcalET.sum()
    df_jets['jetPt']      = df_Towers.groupby('id').jetPt.median()
    df_jets['jetIEta']    = df_Towers.groupby('id').ieta.first()
    df_jets['jetEta']     = df_jets.apply(lambda row: (TowersEta[row['jetIEta']][0] + TowersEta[row['jetIEta']][1])/2, axis=1)

    if options.ietacut:
        df_jets = df_jets[(df_jets['jetIEta'] < float(options.ietacut)) & (df_jets['jetIEta'] > -1*float(options.ietacut))]

    if options.HoEcut:
        df_jets['HoE'] = df_Towers.groupby('id').hcalET.sum() / (df_Towers.groupby('id').iem.sum() + df_Towers.groupby('id').hcalET.sum())
        df_jets = df_jets[df_jets['HoE'] >= 0.95]

    # compute resolution
    df_jets['unc_res'] = df_jets.apply(lambda row: row['unCalib']/row['jetPt'], axis=1)
    df_jets['unc_res_iem'] = df_jets.apply(lambda row: row['SumIem']/row['jetPt'], axis=1)
    df_jets['unc_res_ihad'] = df_jets.apply(lambda row: row['SumIhad']/row['jetPt'], axis=1)

    print('\n ### Saving plots in: ' + odir)

    # plot the resposnse
    PlotResolutionInclusive(df_jets, odir, options.v)
    PlotResolutionPtBins(df_jets, odir, options.v, 'pt')
    PlotResolutionPtBins(df_jets, odir, options.v, 'eta')
