import matplotlib.pyplot as plt
import numpy as np
import sys, glob, os
import pandas as pd
import math
import warnings
import mplhep
plt.style.use(mplhep.style.CMS)
warnings.simplefilter(action='ignore')

sys.path.insert(0,'../L1NtupleReader/')
from caloParamsOnTheFly import *
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

def GetECALSFs (file_ECAl):

    SFs = []
    f_ECAL = open(file_ECAl)
    f_ECAL_lines = f_ECAL.readlines()
    for i, line in enumerate(f_ECAL_lines):
        if '#' in line: continue
        sf_line_ECAL = line.split(',\n')[0]
        sf_vec_ECAL = [float(j) for j in sf_line_ECAL.split(',')]
        SFs = SFs + sf_vec_ECAL
    print('First line:', SFs[:28])
    return SFs

def GetHCALSFs (file_HCAL, file_HF):

    SFs = []
    f_HCAL = open(file_HCAL)
    f_HF = open(file_HF)
    f_HCAL_lines = f_HCAL.readlines()
    f_HF_lines = f_HF.readlines()
    for i, line in enumerate(f_HCAL_lines):
        if '#' in line: continue
        sf_line_HCAL = line.split(',\n')[0]
        sf_vec_HCAL = [float(j) for j in sf_line_HCAL.split(',')]
        sf_line_HF = f_HF_lines[i].split(',\n')[0]
        sf_vec_HF = [float(j) for j in sf_line_HF.split(',')]
        SFs = SFs + sf_vec_HCAL + sf_vec_HF
    print('First line:', SFs[:40])
    return SFs

def PlotResolutionInclusive(df_jets, odir, v_sample):

    bins_res = np.linspace(0,3,240)

    plt.figure(figsize=(10,10))
    text_1 = leg_uncalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['unc_res'].mean(), df_jets['unc_res'].std()/df_jets['unc_res'].mean())
    plt.hist(df_jets['unc_res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_uncalib)
    text_2 = leg_oldcalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['old_res'].mean(), df_jets['old_res'].std()/df_jets['old_res'].mean())
    plt.hist(df_jets['old_res'], bins=bins_res, label=text_2, histtype='step', stacked=True, linewidth=2, color=c_oldcalib)
    text_3 = leg_newcalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['new_res'].mean(), df_jets['new_res'].std()/df_jets['new_res'].mean())
    plt.hist(df_jets['new_res'], bins=bins_res, label=text_3, histtype='step', stacked=True, linewidth=2, color=c_newcalib)
    plt.xlabel('Response')
    plt.ylabel('a.u.')
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
        text_1 = leg_uncalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['unc_res'].mean(), df_jets['unc_res'].std()/df_jets['unc_res'].mean())
        plt.hist(df_jets['unc_res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_uncalib)
        text_2 = leg_oldcalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['old_res'].mean(), df_jets['old_res'].std()/df_jets['old_res'].mean())
        plt.hist(df_jets['old_res'], bins=bins_res, label=text_2, histtype='step', stacked=True, linewidth=2, color=c_oldcalib)
        text_3 = leg_newcalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['new_res_iem'].mean(), df_jets['new_res_iem'].std()/df_jets['new_res_iem'].mean())
        plt.hist(df_jets['new_res_iem'], bins=bins_res, label=text_3, histtype='step', stacked=True, linewidth=2, color=c_newcalib)
        plt.xlabel('Response EM')
        plt.ylabel('a.u.')
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
        text_1 = leg_uncalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['unc_res'].mean(), df_jets['unc_res'].std()/df_jets['unc_res'].mean())
        plt.hist(df_jets['unc_res'], bins=bins_res, label=text_1, histtype='step', stacked=True, linewidth=2, color=c_uncalib)
        text_2 = leg_oldcalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['old_res'].mean(), df_jets['old_res'].std()/df_jets['old_res'].mean())
        plt.hist(df_jets['old_res'], bins=bins_res, label=text_2, histtype='step', stacked=True, linewidth=2, color=c_oldcalib)
        text_3 = leg_newcalib+r': $\mu={:.3f}, res={:.3f}$'.format(df_jets['new_res_ihad'].mean(), df_jets['new_res_ihad'].std()/df_jets['new_res_ihad'].mean())
        plt.hist(df_jets['new_res_ihad'], bins=bins_res, label=text_3, histtype='step', stacked=True, linewidth=2, color=c_newcalib)
        plt.xlabel('Response HAD')
        plt.ylabel('a.u.')
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
        elif bin_type == 'HoTot':
            keyBins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
            key = 'HoTot'
            legend_label = r'$<|H/Tot|<$'
            x_label = r'$H/Tot$'
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
        elif bin_type == 'ieta':
            keyBins = np.arange(1,40)
            key = 'jetIEta'
            legend_label = r'$<|i_{\eta}^{e, offline}|<$'
            x_label = r'$\eta^{e, offline}$'
        elif bin_type == 'EoTot':
            keyBins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
            key = 'EoTot'
            legend_label = r'$<|E/Tot|<$'
            x_label = r'$E/Tot$'
        x_lim = (0.2,1.5)
        x_label_res = r'$E_{T}^{e/\gamma, L1} / p_{T}^{e, offline}$'

    mean_vs_pt_unc = []
    res_vs_pt_unc = []
    maximum_vs_pt_unc = []
    mean_vs_pt_old = []
    res_vs_pt_old = []
    maximum_vs_pt_old = []
    mean_vs_pt_new = []
    res_vs_pt_new = []
    maximum_vs_pt_new = []

    Ymax = 0
    for i in range(len(keyBins)-1):
        
        fig, ax = plt.subplots(figsize=(10,10))
        if bin_type == 'pt': sel_pt = (df_jets[key] > keyBins[i]*2) & (df_jets[key] < keyBins[i+1]*2)
        else: sel_pt = (df_jets[key] > keyBins[i]) & (df_jets[key] < keyBins[i+1])
        h = plt.hist(df_jets[sel_pt]['unc_res'], bins=bins_res, label=leg_uncalib, histtype='step', stacked=True, linewidth=2, color=c_uncalib)
        mean_vs_pt_unc.append(df_jets[sel_pt]['unc_res'].mean())
        res_vs_pt_unc.append(df_jets[sel_pt]['unc_res'].std()/df_jets[sel_pt]['unc_res'].mean())
        if h[0][0] >= 0: maximum_vs_pt_unc.append(h[1][np.where(h[0] == h[0].max())][0])
        else: maximum_vs_pt_unc.append(0)
        if h[0][0] >= 0: Ymax = h[0].max()

        h = plt.hist(df_jets[sel_pt]['old_res'], bins=bins_res, label=leg_oldcalib, histtype='step', stacked=True, linewidth=2, color=c_oldcalib)
        mean_vs_pt_old.append(df_jets[sel_pt]['old_res'].mean())
        res_vs_pt_old.append(df_jets[sel_pt]['old_res'].std()/df_jets[sel_pt]['old_res'].mean())
        if h[0][0] >= 0: maximum_vs_pt_old.append(h[1][np.where(h[0] == h[0].max())][0])
        else: maximum_vs_pt_old.append(0)
        if h[0][0] >= 0: Ymax = max(Ymax, h[0].max())

        h = plt.hist(df_jets[sel_pt]['new_res'], bins=bins_res, label=leg_newcalib, histtype='step', stacked=True, linewidth=2, color=c_newcalib)
        mean_vs_pt_new.append(df_jets[sel_pt]['new_res'].mean())
        res_vs_pt_new.append(df_jets[sel_pt]['new_res'].std()/df_jets[sel_pt]['new_res'].mean())
        if h[0][0] >= 0: maximum_vs_pt_new.append(h[1][np.where(h[0] == h[0].max())][0])
        else: maximum_vs_pt_new.append(0)
        if h[0][0] >= 0: Ymax = max(Ymax, h[0].max())
        
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

    Ymax = 0
    fig = plt.figure(figsize = [10,10])
    X = [(keyBins[i] + keyBins[i+1])/2 for i in range(len(keyBins)-1)]
    X_err = [(keyBins[i+1] - keyBins[i])/2 for i in range(len(keyBins)-1)]
    plt.errorbar(X, res_vs_pt_unc, xerr=X_err, label=leg_uncalib, ls='None', lw=2, marker='o', color=c_uncalib, zorder=0)
    Ymax = max(res_vs_pt_unc)
    plt.errorbar(X, res_vs_pt_old, xerr=X_err, label=leg_oldcalib, ls='None', lw=2, marker='o', color=c_oldcalib, zorder=0)
    Ymax = max(Ymax, max(res_vs_pt_old))
    plt.errorbar(X, res_vs_pt_new, xerr=X_err, label=leg_newcalib, ls='None', lw=2, marker='o', color=c_newcalib, zorder=0)
    Ymax = max(Ymax, max(res_vs_pt_new))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy resolution')
    plt.xlim(keyBins[0], keyBins[-1])
    plt.ylim(0., 0.7)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    savefile = odir+'/resolution_'+bin_type+'Bins_'+v_sample+'.png'
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    # plot scale vs keyBins
    Ymax = 0
    fig = plt.figure(figsize = [10,10])
    plt.errorbar(X, mean_vs_pt_unc, xerr=X_err, label=leg_uncalib, ls='None', lw=2, marker='o', color=c_uncalib, zorder=0)
    Ymax = max(mean_vs_pt_unc)
    plt.errorbar(X, mean_vs_pt_old, xerr=X_err, label=leg_oldcalib, ls='None', lw=2, marker='o', color=c_oldcalib, zorder=0)
    Ymax = max(Ymax, max(mean_vs_pt_old))
    plt.errorbar(X, mean_vs_pt_new, xerr=X_err, label=leg_newcalib, ls='None', lw=2, marker='o', color=c_newcalib, zorder=0)
    Ymax = max(Ymax, max(mean_vs_pt_new))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(keyBins[0], keyBins[-1])
    plt.ylim(0.5, 1.5)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    savefile = odir+'/scale_'+bin_type+'Bins_'+v_sample+'.png'
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    # plot scale from maximum vs keybins
    Ymax = 0
    fig = plt.figure(figsize = [10,10])
    plt.errorbar(X, maximum_vs_pt_unc, xerr=X_err, label=leg_uncalib, ls='None', lw=2, marker='o', color=c_uncalib, zorder=0)
    Ymax = max(maximum_vs_pt_unc)
    plt.errorbar(X, maximum_vs_pt_old, xerr=X_err, label=leg_oldcalib, ls='None', lw=2, marker='o', color=c_oldcalib, zorder=0)
    Ymax = max(Ymax, max(maximum_vs_pt_old))
    plt.errorbar(X, maximum_vs_pt_new, xerr=X_err, label=leg_newcalib, ls='None', lw=2, marker='o', color=c_newcalib, zorder=0)
    Ymax = max(Ymax, max(maximum_vs_pt_new))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(keyBins[0], keyBins[-1])
    plt.ylim(0.5, 1.5)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    savefile = odir+'/scale_max_'+bin_type+'Bins_'+v_sample+'.png'
    plt.savefig(savefile)
    print(savefile)
    plt.close()

### To run:
### python3 ApplicationPlots_TF.py --indir 2023_05_01_NtuplesV44 --v HCAL --tag DataReco --filesLim 2 --addtag _A

if __name__ == "__main__" :

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--indir",        dest="indir",       help="Input folder with trained model",     default=None)
    parser.add_option("--tag",          dest="tag",         help="tag of the training folder",          default="")
    parser.add_option("--out",          dest="odir",        help="Output folder",                       default=None)
    parser.add_option("--v",            dest="v",           help="Ntuple type ('ECAL' or 'HCAL')",      default='ECAL')
    parser.add_option("--applyECAL",    dest="applyECAL",   help="Apply ECAL calibration",              default=True)
    parser.add_option("--applyHCAL",    dest="applyHCAL",   help="Apply HCAL calibration",              default=True)
    parser.add_option("--ECALnewSF",    dest="ECALnewSF",   help="New ECAL calibration",                default='/data_CMS/cms/motta/CaloL1calibraton/2023_03_06_NtuplesV33/ECALtrainingDataReco_normalOrder/data/ScaleFactors_ECAL_energystep2iEt.csv')
    parser.add_option("--HCALnewSF",    dest="HCALnewSF",   help="New HCAL calibration",                default='/data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV43/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv')
    parser.add_option("--HFnewSF",      dest="HFnewSF",     help="New HCAL calibration",                default='/data_CMS/cms/motta/CaloL1calibraton/2023_04_29_NtuplesV43/HCALtrainingDataReco/data_A/ScaleFactors_HF_energystep2iEt.csv')
    parser.add_option("--filesLim",     dest="filesLim",    help="Maximum number of npz files to use",  default=1000000, type=int)
    parser.add_option("--addtag",       dest="addtag",      help="Add tag for different trainings",     default="")
    parser.add_option("--ietacut",      dest="ietacut",     help="Apply ieta cut",                      default=None)
    parser.add_option("--ljetPtcut",    dest="ljetPtcut",   help="Apply lowerjetPt cut [GeV]",          default=None)
    parser.add_option("--ujetPtcut",    dest="ujetPtcut",   help="Apply upperjetPt cut [GeV]",          default=None)
    parser.add_option("--HoEcut",       dest="HoEcut",      help="Apply HoE cut at 0.95",               default=None)
    parser.add_option("--MinusIem",     dest="MinusIem",    help="Add Iem to the jetPt target",         default=False,   action='store_true')
    # parser.add_option("--EstepECAL",    dest="EstepECAL",   help="Energy step ECAL SFs",                default=2, type=int)
    # parser.add_option("--EstepHCAL",    dest="EstepHCAL",   help="Energy step HCAL SFs",                default=2, type=int)
    (options, args) = parser.parse_args()
    print(options)

    EnergyBins2iEt = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 256]
    EnergyBins1iEt = [-1 ,0.5 ,1.0 ,1.5 ,2.0 ,2.5 ,3.0 ,3.5 ,4.0 ,4.5 ,5.0 ,5.5 ,6.0 ,6.5 ,7.0 ,7.5 ,8.0 ,8.5 ,9.0 ,9.5 ,10.0 ,10.5 ,11.0 ,11.5 ,12.0 ,12.5 ,13.0 ,13.5 ,14.0 ,14.5 ,15.0 ,15.5 ,16.0 ,16.5 ,17.0 ,17.5 ,18.0 ,18.5 ,19.0 ,19.5 ,20.0 ,20.5 ,21.0 ,21.5 ,22.0 ,22.5 ,23.0 ,23.5 ,24.0 ,24.5 ,25.0 ,25.5 ,26.0 ,26.5 ,27.0 ,27.5 ,28.0 ,28.5 ,29.0 ,29.5 ,30.0 ,30.5 ,31.0 ,31.5 ,32.0 ,32.5 ,33.0 ,33.5 ,34.0 ,34.5 ,35.0 ,35.5 ,36.0 ,36.5 ,37.0 ,37.5 ,38.0 ,38.5 ,39.0 ,39.5 ,40.0 ,40.5 ,41.0 ,41.5 ,42.0 ,42.5 ,43.0 ,43.5 ,44.0 ,44.5 ,45.0 ,45.5 ,46.0 ,46.5 ,47.0 ,47.5 ,48.0 ,48.5 ,49.0 ,49.5 ,50.0 ,50.5 ,51.0 ,51.5 ,52.0 ,52.5 ,53.0 ,53.5 ,54.0 ,54.5 ,55.0 ,55.5 ,56.0 ,56.5 ,57.0 ,57.5 ,58.0 ,58.5 ,59.0 ,59.5 ,60.0 ,60.5 ,61.0 ,61.5 ,62.0 ,62.5 ,63.0 ,63.5 ,64.0 ,64.5 ,65.0 ,65.5 ,66.0 ,66.5 ,67.0 ,67.5 ,68.0 ,68.5 ,69.0 ,69.5 ,70.0 ,70.5 ,71.0 ,71.5 ,72.0 ,72.5 ,73.0 ,73.5 ,74.0 ,74.5 ,75.0 ,75.5 ,76.0 ,76.5 ,77.0 ,77.5 ,78.0 ,78.5 ,79.0 ,79.5 ,80.0 ,80.5 ,81.0 ,81.5 ,82.0 ,82.5 ,83.0 ,83.5 ,84.0 ,84.5 ,85.0 ,85.5 ,86.0 ,86.5 ,87.0 ,87.5 ,88.0 ,88.5 ,89.0 ,89.5 ,90.0 ,90.5 ,91.0 ,91.5 ,92.0 ,92.5 ,93.0 ,93.5 ,94.0 ,94.5 ,95.0 ,95.5 ,96.0 ,96.5 ,97.0 ,97.5 ,98.0 ,98.5 ,99.0 ,99.5 , 256]

    if 'energystep1iEt' in options.ECALnewSF:
        newECALEnergyBins = EnergyBins1iEt
        if options.v == 'ECAL' : energystep = 1
    elif 'energystep2iEt' in options.ECALnewSF:
        newECALEnergyBins = EnergyBins2iEt
        if options.v == 'ECAL' : energystep = 2

    if 'energystep1iEt' in options.HCALnewSF:
        newHCALEnergyBins = EnergyBins1iEt
        if options.v == 'HCAL' : energystep = 1
    elif 'energystep2iEt' in options.HCALnewSF:
        newHCALEnergyBins = EnergyBins2iEt
        if options.v == 'HCAL' : energystep = 2

    indir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag
    odir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/plots' + options.addtag + '/Performance_' + str(energystep) + 'iEt'
    os.system('mkdir -p '+ odir)
    print('\n ### Reading TF records from: ' + indir + '/testTFRecords/record_*.tfrecord')
    InTestRecords = glob.glob(indir+'/testTFRecords/record_*.tfrecord')[:options.filesLim]
    dataset = tf.data.TFRecordDataset(InTestRecords)
    batch_size = len(list(dataset))
    parsed_dataset = dataset.map(parse_function)
    data = parsed_dataset.batch(batch_size).as_numpy_iterator().next()
    print('\n ### N events: ' + str(len(list(dataset))))

    Towers = data[0]
    Jets = data[1]

    print('\n ### Load Dataframes')

# ''' df_Towers_list = []
#     for i, CD in enumerate(Towers):
#         if options.v == 'ECAL':
#             df_CD = pd.DataFrame(data={'id': i, 'jetPt': Jets[i], 'iem': CD[:,1:2].ravel(), 'hcalET': CD[:,0:1].ravel(), 'ieta': np.argmax(CD[:,2:], axis=1).ravel() + 1})
#         elif options.v == 'HCAL':
#             df_CD = pd.DataFrame(data={'id': i, 'jetPt': Jets[i], 'iem': CD[:,0:1].ravel(), 'hcalET': CD[:,1:2].ravel(), 'ieta': np.argmax(CD[:,2:], axis=1).ravel() + 1})
#         df_Towers_list.append(df_CD)
#     df_Towers = pd.concat(df_Towers_list)
# '''

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

    if options.v == 'ECAL':
        # dummy_rateProxy_input = np.repeat([np.zeros(42)], len(list(dataset)), axis=0) # old version 33
        dummy_rateProxy_input = np.repeat([np.repeat([np.zeros(42)], 81, axis=0)], len(list(dataset)), axis=0)
    if options.v == 'HCAL':
        dummy_rateProxy_input = np.repeat([np.repeat([np.zeros(42)], 81, axis=0)], len(list(dataset)), axis=0)
    modeldir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/model_' + options.v + options.addtag
    print('\n ### Reading model from: ' + modeldir)
    model = keras.models.load_model(modeldir + '/model', compile=False, custom_objects={'Fgrad': Fgrad})
    modelPt = model.predict([Towers, dummy_rateProxy_input])[0]
    modelPt_arr = np.repeat(modelPt, Towers.shape[1])

    # Combine the arrays into a dictionary and create the dataframe
    df_Towers = pd.DataFrame({'id': id_arr, 'jetPt': jetPt_arr, 'modelPt': modelPt_arr, 'iem': iem, 'hcalET': hcalET, 'ieta': ieta})

    if options.ljetPtcut:
        df_Towers = df_Towers[df_Towers['jetPt'] > float(options.ljetPtcut)*2]
    if options.ujetPtcut:
        df_Towers = df_Towers[df_Towers['jetPt'] < float(options.ujetPtcut)*2]

    # apply oldCalib
    # taken from the caloParams file (always the same)
    if options.applyECAL == True:
        print('\n ### Apply current calibration to ECAL')
        energy_bins = np.array(layer1ECalScaleETBins_currCalib)*2+0.1 # to convert to iEt and shift to center of bin
        SFs = layer1ECalScaleFactors_currCalib
        nEtaBins = 28

        df_Towers['old_iemBin'] = np.digitize(df_Towers['iem'], energy_bins)
        df_Towers['oldESF'] = df_Towers.apply(lambda row: SFs[int( abs(row['ieta']) + nEtaBins*(row['old_iemBin']-1) ) -1], axis=1)
        df_Towers['oldCalib_iem'] = df_Towers.apply(lambda row: math.floor(row['iem'] * row['oldESF']), axis=1)

    else:
        df_Towers['oldCalib_iem'] = df_Towers['iem']

    if options.applyHCAL == True:
        print('\n ### Apply current calibration to HCAL')
        energy_bins = np.array(layer1HCalScaleETBins_currCalib)*2+0.1 # to convert to iEt and shift to center of bin
        SFs = layer1HCalScaleFactors_currCalib
        nEtaBins = 40

        df_Towers['old_ihadBin'] = np.digitize(df_Towers['hcalET'], energy_bins)
        df_Towers['oldHSF'] = df_Towers.apply(lambda row: SFs[int( abs(row['ieta']) + nEtaBins*(row['old_ihadBin']-1) ) -1], axis=1)
        df_Towers['oldCalib_ihad'] = df_Towers.apply(lambda row: math.floor(row['hcalET'] * row['oldHSF']), axis=1)
    
    else:
        df_Towers['oldCalib_ihad'] = df_Towers['hcalET']

    # apply newCalib
    # taken directly from the SFs extracted from the NN in the "data" folder
    if options.applyECAL == True:
        print('\n ### Apply new calibration to ECAL')
        print(' ### ECAL SFs from: ' + options.ECALnewSF)
        print(' ### Energy bins:', newECALEnergyBins)
        # define new SFs
        file_ECAL = options.ECALnewSF
        energy_bins = np.array(newECALEnergyBins)*2+0.1 # to convert to iEt and shift to center of bin
        SFs = GetECALSFs(file_ECAL)
        nEtaBins = 28 # [FIXME]

        df_Towers['new_iemBin'] = np.digitize(df_Towers['iem'], energy_bins)
        df_Towers['newESF'] = df_Towers.apply(lambda row: SFs[int( abs(row['ieta']) + 28*(row['new_iemBin']-1) ) -1], axis=1)
        df_Towers['newCalib_iem'] = df_Towers.apply(lambda row: math.floor(row['iem'] * row['newESF']), axis=1)

    else:
        df_Towers['newCalib_iem'] = df_Towers['iem']

    if options.applyHCAL == True:
        print('\n ### Apply new calibration to HCAL')
        print(' ### HCAL SFs from: ' + options.HCALnewSF)
        print(' ### HF SFs from: ' + options.HFnewSF)
        print(' ### Energy bins:', newHCALEnergyBins)

        # define new SFs
        file_HCAL = options.HCALnewSF
        file_HF = options.HFnewSF
        energy_bins = np.array(newHCALEnergyBins)*2+0.1 # to convert to iEt and shift to center of bin
        SFs = GetHCALSFs(file_HCAL, file_HF)
        nEtaBins = 40 # [FIXME]

        df_Towers['new_ihadBin'] = np.digitize(df_Towers['hcalET'], energy_bins)
        df_Towers['newHSF'] = df_Towers.apply(lambda row: SFs[int( abs(row['ieta']) + nEtaBins*(row['new_ihadBin']-1) ) -1], axis=1)
        df_Towers['newCalib_ihad'] = df_Towers.apply(lambda row: math.floor(row['hcalET'] * row['newHSF']), axis=1)
        
    else:
        df_Towers['newCalib_ihad'] = df_Towers['hcalET']

    # compute sum of the raw energy 
    df_jets = pd.DataFrame()
    df_jets['oldCalib']   = df_Towers.groupby('id').oldCalib_iem.sum() + df_Towers.groupby('id').oldCalib_ihad.sum()
    df_jets['newCalib']   = df_Towers.groupby('id').newCalib_iem.sum() + df_Towers.groupby('id').newCalib_ihad.sum()
    df_jets['unCalib']    = df_Towers.groupby('id').iem.sum() + df_Towers.groupby('id').hcalET.sum()
    df_jets['modelCalib'] = df_Towers.groupby('id').modelPt.median()
    if options.MinusIem:
        df_jets['jetPt']  = df_Towers.groupby('id').jetPt.median() + df_Towers.groupby('id').iem.sum()
    else:
        df_jets['jetPt']  = df_Towers.groupby('id').jetPt.median()
    df_jets['jetIEta']    = df_Towers.groupby('id').ieta.first()
    df_jets['jetEta']     = df_jets.apply(lambda row: (TowersEta[row['jetIEta']][0] + TowersEta[row['jetIEta']][1])/2, axis=1)
    df_jets['EoTot']      = df_Towers.groupby('id').iem.sum() / df_jets['unCalib']
    df_jets['HoTot']      = df_Towers.groupby('id').hcalET.sum() / df_jets['unCalib']
    if options.v == "ECAL":
        df_jets['newCalib_iem']   = df_Towers.groupby('id').newCalib_iem.sum()
    if options.v == "HCAL":
        df_jets['newCalib_ihad']  = df_Towers.groupby('id').newCalib_ihad.sum()

    if options.v == 'ECAL':
        df_jets['SFCalib'] = df_Towers.groupby('id').newCalib_iem.sum()
    if options.v == 'HCAL':
        df_jets['SFCalib'] = df_Towers.groupby('id').newCalib_ihad.sum()

    if options.ietacut:
        df_jets = df_jets[(df_jets['jetIEta'] < float(options.ietacut)) & (df_jets['jetIEta'] > -1*float(options.ietacut))]

    if options.HoEcut:
        df_jets['HoE'] = df_Towers.groupby('id').hcalET.sum() / (df_Towers.groupby('id').iem.sum() + df_Towers.groupby('id').hcalET.sum())
        df_jets = df_jets[df_jets['HoE'] >= 0.95]

    # compute resolution
    df_jets['old_res'] = df_jets.apply(lambda row: row['oldCalib']/row['jetPt'], axis=1)
    df_jets['new_res'] = df_jets.apply(lambda row: row['newCalib']/row['jetPt'], axis=1)
    df_jets['unc_res'] = df_jets.apply(lambda row: row['unCalib']/row['jetPt'], axis=1)
    df_jets['mod_res'] = df_jets.apply(lambda row: row['modelCalib']/row['jetPt'], axis=1)
    df_jets['SFs_res'] = df_jets.apply(lambda row: row['SFCalib']/row['jetPt'], axis=1)
    if options.v == "ECAL":
        df_jets['new_res_iem'] = df_jets.apply(lambda row: row['newCalib_iem']/row['jetPt'], axis=1)
    if options.v == "HCAL":
        if options.MinusIem:
            df_jets['new_res_ihad'] = df_jets.apply(lambda row: row['newCalib_ihad']/(df_Towers.groupby('id').jetPt.median()), axis=1)
        else:
            df_jets['new_res_ihad'] = df_jets.apply(lambda row: row['newCalib_ihad']/row['jetPt'], axis=1)
    
    # compute MAPE value
    df_jets['old_mape'] = df_jets.apply(lambda row: np.abs(row['oldCalib']-row['jetPt'])/row['jetPt'], axis=1)
    df_jets['new_mape'] = df_jets.apply(lambda row: np.abs(row['newCalib']-row['jetPt'])/row['jetPt'], axis=1)
    df_jets['unc_mape'] = df_jets.apply(lambda row: np.abs(row['unCalib']-row['jetPt'])/row['jetPt'], axis=1)
    df_jets['mod_mape'] = df_jets.apply(lambda row: np.abs(row['modelCalib']-row['jetPt'])/row['jetPt'], axis=1)
    df_jets['SFs_mape'] = df_jets.apply(lambda row: np.abs(row['SFCalib']-row['jetPt'])/row['jetPt'], axis=1)

    print('\n ### Saving plots in: ' + odir)

    # plots for debug
    plt.figure(figsize=(12,8))
    plt.hist(df_jets['SFs_res'], bins=np.linspace(0,3,50), histtype='step', stacked=True, linewidth=2, label='Calib from SFs')
    plt.hist(df_jets['mod_res'], bins=np.linspace(0,3,50), histtype='step', stacked=True, linewidth=2, label='Calib from model')
    plt.xlabel('L1 Et / jet Pt')
    plt.legend()
    plt.grid()
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    savefile = odir+'/Response_Model_vs_SFs.png'
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    plt.figure(figsize=(12,8))
    plt.hist(df_jets['SFs_mape'], bins=np.linspace(0,3,50), histtype='step', stacked=True, linewidth=2, label='Calib from SFs')
    plt.hist(df_jets['mod_mape'], bins=np.linspace(0,3,50), histtype='step', stacked=True, linewidth=2, label='Calib from model')
    plt.xlabel('MAPE')
    plt.legend()
    plt.grid()
    mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    savefile = odir+'/MAPE_Model_vs_SFs.png'
    plt.savefig(savefile)
    print(savefile)
    plt.close()

    # plot the resposnse
    PlotResolutionInclusive(df_jets, odir, options.v)
    PlotResolutionPtBins(df_jets, odir, options.v, 'pt')
    PlotResolutionPtBins(df_jets, odir, options.v, 'eta')
    if options.v == 'ECAL':
        PlotResolutionPtBins(df_jets, odir, options.v, 'EoTot')
    if options.v == 'HCAL':
        PlotResolutionPtBins(df_jets, odir, options.v, 'HoTot')