from array import array
import ROOT
ROOT.gROOT.SetBatch(True)
import sys
import os
import warnings
warnings.simplefilter(action='ignore')

import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.transforms import ScaledTranslation
import numpy as np
import mplhep
plt.style.use(mplhep.style.CMS)

def save_obj(obj,dest):
    with open(dest,'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--indir",       dest="indir",                            default=None)
parser.add_option("--tag",         dest="tag",                              default='')
parser.add_option("--ref",         dest="ref",                              default='')
parser.add_option("--label",       dest="label",                            default=None)
parser.add_option("--target",      dest="target",                           default=None)
parser.add_option("--reco",        dest="reco",        action='store_true', default=False)
parser.add_option("--gen",         dest="gen",         action='store_true', default=False)
parser.add_option("--thrsFixRate", dest="thrsFixRate", action='append',     default=None)
parser.add_option("--old",         dest="olddir_name",                      default='0000_00_00_NtuplesVold')
parser.add_option("--unc",         dest="uncdir_name",                      default='0000_00_00_NtuplesVunc')
parser.add_option("--doResponse",  dest="doResponse",                       default=True)
parser.add_option("--doResolution",dest="doResolution",                     default=True)
parser.add_option("--doTurnOn",    dest="doTurnOn",                         default=True)
parser.add_option("--doRate",      dest="doRate",                           default=True)
parser.add_option("--do_HoTot",    dest="do_HoTot",    action='store_true', default=False)
parser.add_option("--do_EoTot",    dest="do_EoTot",    action='store_true', default=False)
(options, args) = parser.parse_args()

# get/create folders
basedir = "/data_CMS/cms/motta/CaloL1calibraton/"
olddir = basedir+"/"+options.olddir_name+"/"
uncdir = basedir+"/"+options.uncdir_name+"/"
indir = basedir+options.indir
outdir = indir
print(" ### INFO: UnCalib dir  = {}".format(uncdir))
print(" ### INFO: OldCalib dir = {}".format(olddir))
print(" ### INFO: NewCalib dir = {}".format(indir))

label = options.label
target = options.target
os.system('mkdir -p '+outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref)
os.system('mkdir -p '+outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref)

#defining binning of histogram
if options.target == 'jet':
    ptBins  = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200, 500]
    etaBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.191]
if options.target == 'ele':
    ptBins  = [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110, 130, 160, 200]
    etaBins = [0., 0.5, 1.0, 1.305, 1.479, 2.0, 2.5, 3.0]
HoTotBins = [0, 0.2, 0.4, 0.6, 0.8, 0.95, 1.0]
EoTotBins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

x_lim_response = (0.5,1.5)

#############################
## RESOLUTIONS COMPARISONS ##

file_unCalib  = ROOT.TFile(uncdir+'/PerformancePlots/'+label+'/ROOTs/resolution_graphs_'+label+'_'+target+'.root', 'r')
file_oldCalib = ROOT.TFile(olddir+'/PerformancePlots/'+label+'/ROOTs/resolution_graphs_'+label+'_'+target+'.root', 'r')
file_newCalib = ROOT.TFile(indir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/resolution_graphs_'+label+'_'+target+'.root', 'r')

if options.reco:
    if options.target == 'jet':
        x_lim = (0.,3.)
        legend_label = r'$<|p_{T}^{jet, offline}|<$'
        x_label = r'$E_{T}^{jet, L1} / p_{T}^{jet, offline}$'
    if options.target == 'ele':
        x_lim = (0.2,1.5)
        legend_label = r'$<|p_{T}^{e, offline}|<$'
        x_label = r'$E_{T}^{e/\gamma, L1} / p_{T}^{e, offline}$'
if options.gen:
    if options.target == 'jet':
        x_lim = (0.,3.)
        legend_label = r'$<|p_{T}^{jet, gen}|<$'
        x_label = r'$E_{T}^{jet, L1} / p_{T}^{jet, gen}$'
    if options.target == 'ele':
        x_lim = (0.2,1.5)
        legend_label = r'$<|p_{T}^{e, gen}|<$'
        x_label = r'$E_{T}^{e/\gamma, L1} / p_{T}^{e, gen}$'

# #######
# inclusive responses

if options.doResponse == True:

    print("\n *** COMPARING RESPONSE")
    print(" ### INFO: UnCalib file  = {}".format(uncdir+'/PerformancePlots/'+label+'/ROOTs/resolution_graphs_'+label+'_'+target+'.root'))
    print(" ### INFO: OldCalib file = {}".format(olddir+'/PerformancePlots/'+label+'/ROOTs/resolution_graphs_'+label+'_'+target+'.root'))
    print(" ### INFO: NewCalib file = {}".format(indir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/resolution_graphs_'+label+'_'+target+'.root'))

    inclusive_resp_unCalib  = file_unCalib.Get("pt_response_ptInclusive")
    inclusive_resp_oldCalib = file_oldCalib.Get("pt_response_ptInclusive")
    inclusive_resp_newCalib = file_newCalib.Get("pt_response_ptInclusive")

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = inclusive_resp_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='black')
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = inclusive_resp_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='red')
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = inclusive_resp_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='green')
    Ymax = max(Ymax, max(Y))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('a.u.')
    plt.xlim(x_lim_response)
    plt.ylim(0., Ymax*1.3)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/response_inclusive_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_inclusive_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/response_inclusive_'+label+'_'+target)
    plt.close()

    #######
    # ptBins responses

    for i in range(len(ptBins)-1):
        ptBins_resp_unCalib = file_unCalib.Get("pt_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]))
        ptBins_resp_oldCalib = file_oldCalib.Get("pt_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]))
        ptBins_resp_newCalib = file_newCalib.Get("pt_resp_ptBin"+str(ptBins[i])+"to"+str(ptBins[i+1]))

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = ptBins_resp_unCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
        ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='black')
        Ymax = max(Y)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = ptBins_resp_oldCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
        ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='red')
        Ymax = max(Ymax, max(Y))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = ptBins_resp_newCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
        ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='green')
        Ymax = max(Ymax, max(Y))

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20, title=str(ptBins[i])+legend_label+str(ptBins[i+1]), title_fontsize=18)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('a.u.')
        plt.xlim(x_lim_response)
        plt.ylim(0., Ymax*1.3)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(ptBins[i])+"pt"+str(ptBins[i+1])+"_"+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(ptBins[i])+"pt"+str(ptBins[i+1])+"_"+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(ptBins[i])+"pt"+str(ptBins[i+1])+"_"+label+'_'+target)
        plt.close()

    #######
    # etaBins responses

    if options.reco:
        if options.target == 'jet': legend_label = r'$<|\eta^{jet, offline}|<$'
        if options.target == 'ele': legend_label = r'$<|\eta^{e, offline}|<$'
    if options.gen:
        if options.target == 'jet': legend_label = r'$<|\eta^{jet, gen}|<$'
        if options.target == 'ele': legend_label = r'$<|\eta^{e, gen}|<$'

    for i in range(len(etaBins)-1):
        etaBins_resp_unCalib = file_unCalib.Get("pt_resp_AbsEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]))
        etaBins_resp_oldCalib = file_oldCalib.Get("pt_resp_AbsEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]))
        etaBins_resp_newCalib = file_newCalib.Get("pt_resp_AbsEtaBin"+str(etaBins[i])+"to"+str(etaBins[i+1]))


        fig, ax = plt.subplots(figsize=(10,10))
        plt.grid(zorder=0)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = etaBins_resp_unCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
        ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='black')
        Ymax = max(Y)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = etaBins_resp_oldCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
        ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='red')
        Ymax = max(Ymax, max(Y))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = etaBins_resp_newCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
        ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='green')
        Ymax = max(Ymax, max(Y))

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20, title=str(etaBins[i])+legend_label+str(etaBins[i+1]), title_fontsize=18)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('a.u.')
        plt.xlim(x_lim_response)
        plt.ylim(0., Ymax*1.3)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(etaBins[i])+"eta"+str(etaBins[i+1])+"_"+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(etaBins[i])+"eta"+str(etaBins[i+1])+"_"+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(etaBins[i])+"eta"+str(etaBins[i+1])+"_"+label+'_'+target)
        plt.close()

    #######
    # HoTotBins responses

    if options.do_HoTot:
        legend_label = r'$<H/Tot<$'

        for i in range(len(HoTotBins)-1):
            HoTotBins_resp_unCalib = file_unCalib.Get("pt_resp_HoTotBin"+str(HoTotBins[i])+"to"+str(HoTotBins[i+1]))
            HoTotBins_resp_oldCalib = file_oldCalib.Get("pt_resp_HoTotBin"+str(HoTotBins[i])+"to"+str(HoTotBins[i+1]))
            HoTotBins_resp_newCalib = file_newCalib.Get("pt_resp_HoTotBin"+str(HoTotBins[i])+"to"+str(HoTotBins[i+1]))
            fig, ax = plt.subplots(figsize=(10,10))

            X = [] ; Y = [] ; X_err = [] ; Y_err = []
            histo = HoTotBins_resp_unCalib
            for ibin in range(0,histo.GetNbinsX()):
                X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
                Y.append(histo.GetBinContent(ibin+1))
                X_err.append(histo.GetBinWidth(ibin+1)/2.)
                Y_err.append(histo.GetBinError(ibin+1))
            ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
            ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='black')
            Ymax = max(Y)

            X = [] ; Y = [] ; X_err = [] ; Y_err = []
            histo = HoTotBins_resp_oldCalib
            for ibin in range(0,histo.GetNbinsX()):
                X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
                Y.append(histo.GetBinContent(ibin+1))
                X_err.append(histo.GetBinWidth(ibin+1)/2.)
                Y_err.append(histo.GetBinError(ibin+1))
            ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
            ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='red')
            Ymax = max(Ymax, max(Y))

            X = [] ; Y = [] ; X_err = [] ; Y_err = []
            histo = HoTotBins_resp_newCalib
            for ibin in range(0,histo.GetNbinsX()):
                X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
                Y.append(histo.GetBinContent(ibin+1))
                X_err.append(histo.GetBinWidth(ibin+1)/2.)
                Y_err.append(histo.GetBinError(ibin+1))
            ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
            ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='green')
            Ymax = max(Ymax, max(Y))

            for xtick in ax.xaxis.get_major_ticks():
                xtick.set_pad(10)
            leg = plt.legend(loc='upper right', fontsize=20, title=str(HoTotBins[i])+legend_label+str(HoTotBins[i+1]), title_fontsize=18)
            leg._legend_box.align = "left"
            plt.xlabel(x_label)
            plt.ylabel('a.u.')
            plt.xlim(x_lim_response)
            plt.ylim(0., Ymax*1.3)
            for xtick in ax.xaxis.get_major_ticks():
                xtick.set_pad(10)
            plt.grid()
            if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
            else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
            plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(HoTotBins[i])+"HoTot"+str(HoTotBins[i+1])+"_"+label+'_'+target+'.pdf')
            plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(HoTotBins[i])+"HoTot"+str(HoTotBins[i+1])+"_"+label+'_'+target+'.png')
            print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(HoTotBins[i])+"HoTot"+str(HoTotBins[i+1])+"_"+label+'_'+target)
            plt.close()

    #######
    # EoTotBins responses

    if options.do_EoTot:
        legend_label = r'$<E/Tot<$'

        for i in range(len(EoTotBins)-1):
            EoTotBins_resp_unCalib = file_unCalib.Get("pt_resp_EoTotBin"+str(EoTotBins[i])+"to"+str(EoTotBins[i+1]))
            EoTotBins_resp_oldCalib = file_oldCalib.Get("pt_resp_EoTotBin"+str(EoTotBins[i])+"to"+str(EoTotBins[i+1]))
            EoTotBins_resp_newCalib = file_newCalib.Get("pt_resp_EoTotBin"+str(EoTotBins[i])+"to"+str(EoTotBins[i+1]))
            fig, ax = plt.subplots(figsize=(10,10))

            X = [] ; Y = [] ; X_err = [] ; Y_err = []
            histo = EoTotBins_resp_unCalib
            for ibin in range(0,histo.GetNbinsX()):
                X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
                Y.append(histo.GetBinContent(ibin+1))
                X_err.append(histo.GetBinWidth(ibin+1)/2.)
                Y_err.append(histo.GetBinError(ibin+1))
            ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
            ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='black')
            Ymax = max(Y)

            X = [] ; Y = [] ; X_err = [] ; Y_err = []
            histo = EoTotBins_resp_oldCalib
            for ibin in range(0,histo.GetNbinsX()):
                X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
                Y.append(histo.GetBinContent(ibin+1))
                X_err.append(histo.GetBinWidth(ibin+1)/2.)
                Y_err.append(histo.GetBinError(ibin+1))
            ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
            ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='red')
            Ymax = max(Ymax, max(Y))

            X = [] ; Y = [] ; X_err = [] ; Y_err = []
            histo = EoTotBins_resp_newCalib
            for ibin in range(0,histo.GetNbinsX()):
                X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
                Y.append(histo.GetBinContent(ibin+1))
                X_err.append(histo.GetBinWidth(ibin+1)/2.)
                Y_err.append(histo.GetBinError(ibin+1))
            ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
            ax.step(np.array((np.array(X[:-1])+np.array(X[1:]))/2), np.array(Y[:-1]), color='green')
            Ymax = max(Ymax, max(Y))

            for xtick in ax.xaxis.get_major_ticks():
                xtick.set_pad(10)
            leg = plt.legend(loc='upper right', fontsize=20, title=str(EoTotBins[i])+legend_label+str(EoTotBins[i+1]), title_fontsize=18)
            leg._legend_box.align = "left"
            plt.xlabel(x_label)
            plt.ylabel('a.u.')
            plt.xlim(x_lim_response)
            plt.ylim(0., Ymax*1.3)
            for xtick in ax.xaxis.get_major_ticks():
                xtick.set_pad(10)
            plt.grid()
            if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
            else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
            plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(EoTotBins[i])+"EoTot"+str(EoTotBins[i+1])+"_"+label+'_'+target+'.pdf')
            plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(EoTotBins[i])+"EoTot"+str(EoTotBins[i+1])+"_"+label+'_'+target+'.png')
            print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/response_'+str(EoTotBins[i])+"EoTot"+str(EoTotBins[i+1])+"_"+label+'_'+target)
            plt.close()


if options.doResolution == True:

    print("** COMPARING RESOLUTIONS AND SCALES")
    #######
    # ptBins resolution

    if options.reco:
        if options.target == 'jet': x_label = r'$p_{T}^{jet, offline}$'
        if options.target == 'ele': x_label = r'$p_{T}^{e, offline}$'
    if options.gen:
        if options.target == 'jet': x_label = r'$p_{T}^{jet, gen}$'
        if options.target == 'ele': x_label = r'$p_{T}^{e, gen}$'

    ptBins_resol_unCalib  = file_unCalib.Get("pt_resol_fctPt")
    ptBins_resol_oldCalib = file_oldCalib.Get("pt_resol_fctPt")
    ptBins_resol_newCalib = file_newCalib.Get("pt_resol_fctPt")

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_resol_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    X_r_uncalib = X; Y_r_uncalib = Y
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_resol_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    X_r_oldcalib = X; Y_r_oldcalib = Y
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_resol_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    X_r_newcalib = X; Y_r_newcalib = Y
    Ymax = max(Ymax, max(Y))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy resolution')
    plt.xlim(0, 200)
    plt.ylim(0., Ymax*1.3)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/resolution_ptBins_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/resolution_ptBins_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/resolution_ptBins_'+label+'_'+target)
    plt.close()

    #######
    # ptBins scale

    ptBins_scale_unCalib  = file_unCalib.Get("pt_scale_fctPt")
    ptBins_scale_oldCalib = file_oldCalib.Get("pt_scale_fctPt")
    ptBins_scale_newCalib = file_newCalib.Get("pt_scale_fctPt")

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_scale_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    X_s_uncalib = X; Y_s_uncalib = Y
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_scale_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    X_s_oldcalib = X; Y_s_oldcalib = Y
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_scale_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    X_s_newcalib = X; Y_s_newcalib = Y
    Ymax = max(Ymax, max(Y))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(0, 200)
    plt.ylim(0.5, 1.5)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_ptBins_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_ptBins_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_ptBins_'+label+'_'+target)
    plt.close()

    fig, ax = plt.subplots(figsize=(14,10))
    trans_l = ax.transData + ScaledTranslation(-4/72, 0, fig.dpi_scale_trans)
    trans_r = ax.transData + ScaledTranslation(+4/72, 0, fig.dpi_scale_trans)
    ax.errorbar(X_s_uncalib, Y_s_uncalib, yerr=Y_r_uncalib, label='No Calibration', ls='None', lw=2, marker='v', capsize=3, color='black', zorder=0, transform=trans_l)
    ax.errorbar(X_s_oldcalib, Y_s_oldcalib, yerr=Y_r_oldcalib, label='Old Calibration', ls='None', lw=2, marker='^', capsize=3, color='red', zorder=1)
    ax.errorbar(X_s_newcalib, Y_s_newcalib, yerr=Y_r_newcalib, label='New Calibration', ls='None', lw=2, marker='o', capsize=3, color='green', zorder=2, transform=trans_r)

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(0, 200)
    plt.ylim(0.3, 1.8)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_res_ptBins_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_res_ptBins_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_res_ptBins_'+label+'_'+target)
    plt.close()

    #######
    # ptBins scale from maximum

    ptBins_scale_max_unCalib  = file_unCalib.Get("pt_scale_max_fctPt")
    ptBins_scale_max_oldCalib = file_oldCalib.Get("pt_scale_max_fctPt")
    ptBins_scale_max_newCalib = file_newCalib.Get("pt_scale_max_fctPt")

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_scale_max_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    X_s_uncalib = X; Y_s_uncalib = Y
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_scale_max_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    X_s_oldcalib = X; Y_s_oldcalib = Y
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = ptBins_scale_max_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    X_s_newcalib = X; Y_s_newcalib = Y
    Ymax = max(Ymax, max(Y))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(0, 200)
    plt.ylim(0.5, 1.5)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_max_ptBins_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_max_ptBins_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_max_ptBins_'+label+'_'+target)
    plt.close()

    #######
    # etaBins resolution

    if options.reco:
        if options.target == 'jet':
            x_lim = (-5.2,5.2)
            x_label = r'$\eta^{jet, offline}$'
        if options.target == 'ele':
            x_lim = (-3.1,3.1)
            x_label = r'$\eta^{e, offline}$'
    if options.gen:
        if options.target == 'jet':
            x_lim = (-5.2,5.2)
            x_label = r'$\eta^{jet, gen}$'
        if options.target == 'ele':
            x_lim = (-3.1,3.1)
            x_label = r'$\eta^{e, gen}$'

    etaBins_resol_unCalib  = file_unCalib.Get("pt_resol_fctEta")
    etaBins_resol_oldCalib = file_oldCalib.Get("pt_resol_fctEta")
    etaBins_resol_newCalib = file_newCalib.Get("pt_resol_fctEta")

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_resol_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    X_r_uncalib = X; Y_r_uncalib = Y
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_resol_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    X_r_oldcalib = X; Y_r_oldcalib = Y
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_resol_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    X_r_newcalib = X; Y_r_newcalib = Y
    Ymax = max(Ymax, max(Y))

    rect1 = patches.Rectangle((-1.479, 0), 0.174, Ymax*1.3, linewidth=1, edgecolor='gray', facecolor='gray', zorder=3)
    rect2 = patches.Rectangle((1.305, 0), 0.174, Ymax*1.3, linewidth=1, edgecolor='gray', facecolor='gray', zorder=3)
    ax.add_patch(rect1)
    ax.add_patch(rect2)

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper center', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy resolution')
    plt.xlim(x_lim)
    plt.ylim(0., Ymax*1.3)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/resolution_etaBins_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/resolution_etaBins_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/resolution_etaBins_'+label+'_'+target)
    plt.close()

    #######
    # etaBins scale

    etaBins_scale_unCalib  = file_unCalib.Get("pt_scale_fctEta")
    etaBins_scale_oldCalib = file_oldCalib.Get("pt_scale_fctEta")
    etaBins_scale_newCalib = file_newCalib.Get("pt_scale_fctEta")

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_scale_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    X_s_uncalib = X; Y_s_uncalib = Y
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_scale_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    X_s_oldcalib = X; Y_s_oldcalib = Y
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_scale_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    X_s_newcalib = X; Y_s_newcalib = Y
    Ymax = max(Ymax, max(Y))

    rect1 = patches.Rectangle((-1.479, 0.5), 0.174, 1.5, linewidth=1, edgecolor='gray', facecolor='gray', zorder=3)
    rect2 = patches.Rectangle((1.305, 0.5), 0.174, 1.5, linewidth=1, edgecolor='gray', facecolor='gray', zorder=3)
    ax.add_patch(rect1)
    ax.add_patch(rect2)

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper center', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(x_lim)
    plt.ylim(0.5, 1.5)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_etaBins_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_etaBins_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_etaBins_'+label+'_'+target)
    plt.close()

    fig, ax = plt.subplots(figsize=(14,10))
    trans_l = ax.transData + ScaledTranslation(-5/72, 0, fig.dpi_scale_trans)
    trans_r = ax.transData + ScaledTranslation(+5/72, 0, fig.dpi_scale_trans)
    ax.errorbar(X_s_uncalib, Y_s_uncalib, yerr=Y_r_uncalib, label='No Calibration', ls='None', lw=2, marker='v', capsize=3, color='black', zorder=0, transform=trans_l)
    ax.errorbar(X_s_oldcalib, Y_s_oldcalib, yerr=Y_r_oldcalib, label='Old Calibration', ls='None', lw=2, marker='^', capsize=3, color='red', zorder=1)
    ax.errorbar(X_s_newcalib, Y_s_newcalib, yerr=Y_r_newcalib, label='New Calibration', ls='None', lw=2, marker='o', capsize=3, color='green', zorder=2, transform=trans_r)

    # rect1 = patches.Rectangle((-1.479, 0.3), 0.174, 1.5, linewidth=1, edgecolor='gray', facecolor='gray', zorder=3)
    # rect2 = patches.Rectangle((1.305, 0.3), 0.174, 1.5, linewidth=1, edgecolor='gray', facecolor='gray', zorder=3)
    # ax.add_patch(rect1)
    # ax.add_patch(rect2)

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper center', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(x_lim)
    plt.ylim(0.3, 1.8)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_res_etaBins_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_res_etaBins_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_res_etaBins_'+label+'_'+target)
    plt.close()

    #######
    # etaBins scale from maximum

    etaBins_scale_max_unCalib  = file_unCalib.Get("pt_scale_max_fctEta")
    etaBins_scale_max_oldCalib = file_oldCalib.Get("pt_scale_max_fctEta")
    etaBins_scale_max_newCalib = file_newCalib.Get("pt_scale_max_fctEta")

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_scale_max_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    X_s_uncalib = X; Y_s_uncalib = Y
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_scale_max_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    X_s_oldcalib = X; Y_s_oldcalib = Y
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = etaBins_scale_max_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    X_s_newcalib = X; Y_s_newcalib = Y
    Ymax = max(Ymax, max(Y))

    rect1 = patches.Rectangle((-1.479, 0.5), 0.174, 1.5, linewidth=1, edgecolor='gray', facecolor='gray', zorder=3)
    rect2 = patches.Rectangle((1.305, 0.5), 0.174, 1.5, linewidth=1, edgecolor='gray', facecolor='gray', zorder=3)
    ax.add_patch(rect1)
    ax.add_patch(rect2)

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper center', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Energy scale')
    plt.xlim(x_lim)
    plt.ylim(0.5, 1.5)
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_max_etaBins_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_max_etaBins_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_max_etaBins_'+label+'_'+target)
    plt.close()

    # HoTotBins resolution

    if options.do_HoTot:
        x_lim = (0,1)
        x_label = r'H/Tot'

        HoTotBins_resol_unCalib  = file_unCalib.Get("pt_resol_fctHoTot")
        HoTotBins_resol_oldCalib = file_oldCalib.Get("pt_resol_fctHoTot")
        HoTotBins_resol_newCalib = file_newCalib.Get("pt_resol_fctHoTot")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_resol_unCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
        X_r_uncalib = X; Y_r_uncalib = Y
        Ymax = max(Y)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_resol_oldCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
        X_r_oldcalib = X; Y_r_oldcalib = Y
        Ymax = max(Ymax, max(Y))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_resol_newCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
        X_r_newcalib = X; Y_r_newcalib = Y
        Ymax = max(Ymax, max(Y))

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Energy resolution')
        plt.xlim(x_lim)
        plt.ylim(0., Ymax*1.3)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/resolution_HoTotBins_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/resolution_HoTotBins_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/resolution_HoTotBins_'+label+'_'+target)
        plt.close()

        #######
        # HoTotBins scale

        HoTotBins_scale_unCalib  = file_unCalib.Get("pt_scale_fctHoTot")
        HoTotBins_scale_oldCalib = file_oldCalib.Get("pt_scale_fctHoTot")
        HoTotBins_scale_newCalib = file_newCalib.Get("pt_scale_fctHoTot")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_scale_unCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
        X_s_uncalib = X; Y_s_uncalib = Y
        Ymax = max(Y)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_scale_oldCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
        X_s_oldcalib = X; Y_s_oldcalib = Y
        Ymax = max(Ymax, max(Y))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_scale_newCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
        X_s_newcalib = X; Y_s_newcalib = Y
        Ymax = max(Ymax, max(Y))

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Energy scale')
        plt.xlim(x_lim)
        plt.ylim(0.5, 1.5)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_HoTotBins_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_HoTotBins_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_HoTotBins_'+label+'_'+target)
        plt.close()

        fig, ax = plt.subplots(figsize=(14,10))
        trans_l = ax.transData + ScaledTranslation(-4/72, 0, fig.dpi_scale_trans)
        trans_r = ax.transData + ScaledTranslation(+4/72, 0, fig.dpi_scale_trans)
        ax.errorbar(X_s_uncalib, Y_s_uncalib, yerr=Y_r_uncalib, label='No Calibration', ls='None', lw=2, marker='v', capsize=3, color='black', zorder=0, transform=trans_l)
        ax.errorbar(X_s_oldcalib, Y_s_oldcalib, yerr=Y_r_oldcalib, label='Old Calibration', ls='None', lw=2, marker='^', capsize=3, color='red', zorder=1)
        ax.errorbar(X_s_newcalib, Y_s_newcalib, yerr=Y_r_newcalib, label='New Calibration', ls='None', lw=2, marker='o', capsize=3, color='green', zorder=2, transform=trans_r)

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Energy scale')
        plt.xlim(x_lim)
        plt.ylim(0.5, 1.5)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_res_HoTotBins_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_res_HoTotBins_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_res_HoTotBins_'+label+'_'+target)
        plt.close()

        #######
        # HoTotBins scale from maximum

        HoTotBins_scale_max_unCalib  = file_unCalib.Get("pt_scale_max_fctHoTot")
        HoTotBins_scale_max_oldCalib = file_oldCalib.Get("pt_scale_max_fctHoTot")
        HoTotBins_scale_max_newCalib = file_newCalib.Get("pt_scale_max_fctHoTot")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_scale_max_unCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
        X_s_uncalib = X; Y_s_uncalib = Y
        Ymax = max(Y)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_scale_max_oldCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
        X_s_oldcalib = X; Y_s_oldcalib = Y
        Ymax = max(Ymax, max(Y))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = HoTotBins_scale_max_newCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
        X_s_newcalib = X; Y_s_newcalib = Y
        Ymax = max(Ymax, max(Y))

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Energy scale')
        plt.xlim(x_lim)
        plt.ylim(0.5, 1.5)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_max_HoTotBins_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_max_HoTotBins_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_max_HoTotBins_'+label+'_'+target)
        plt.close()

############################################################################################################################################

    # EoTotBins resolution

    if options.do_EoTot:
        x_lim = (0,1)
        x_label = r'E/Tot'

        EoTotBins_resol_unCalib  = file_unCalib.Get("pt_resol_fctEoTot")
        EoTotBins_resol_oldCalib = file_oldCalib.Get("pt_resol_fctEoTot")
        EoTotBins_resol_newCalib = file_newCalib.Get("pt_resol_fctEoTot")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_resol_unCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
        X_r_uncalib = X; Y_r_uncalib = Y
        Ymax = max(Y)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_resol_oldCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
        X_r_oldcalib = X; Y_r_oldcalib = Y
        Ymax = max(Ymax, max(Y))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_resol_newCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
        X_r_newcalib = X; Y_r_newcalib = Y
        Ymax = max(Ymax, max(Y))

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Energy resolution')
        plt.xlim(x_lim)
        plt.ylim(0., Ymax*1.3)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/resolution_EoTotBins_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/resolution_EoTotBins_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/resolution_EoTotBins_'+label+'_'+target)
        plt.close()

        #######
        # EoTotBins scale

        EoTotBins_scale_unCalib  = file_unCalib.Get("pt_scale_fctEoTot")
        EoTotBins_scale_oldCalib = file_oldCalib.Get("pt_scale_fctEoTot")
        EoTotBins_scale_newCalib = file_newCalib.Get("pt_scale_fctEoTot")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_scale_unCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
        X_s_uncalib = X; Y_s_uncalib = Y
        Ymax = max(Y)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_scale_oldCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
        X_s_oldcalib = X; Y_s_oldcalib = Y
        Ymax = max(Ymax, max(Y))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_scale_newCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
        X_s_newcalib = X; Y_s_newcalib = Y
        Ymax = max(Ymax, max(Y))

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Energy scale')
        plt.xlim(x_lim)
        plt.ylim(0.5, 1.5)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_EoTotBins_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_EoTotBins_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_EoTotBins_'+label+'_'+target)
        plt.close()

        fig, ax = plt.subplots(figsize=(14,10))
        trans_l = ax.transData + ScaledTranslation(-4/72, 0, fig.dpi_scale_trans)
        trans_r = ax.transData + ScaledTranslation(+4/72, 0, fig.dpi_scale_trans)
        ax.errorbar(X_s_uncalib, Y_s_uncalib, yerr=Y_r_uncalib, label='No Calibration', ls='None', lw=2, marker='v', capsize=3, color='black', zorder=0, transform=trans_l)
        ax.errorbar(X_s_oldcalib, Y_s_oldcalib, yerr=Y_r_oldcalib, label='Old Calibration', ls='None', lw=2, marker='^', capsize=3, color='red', zorder=1)
        ax.errorbar(X_s_newcalib, Y_s_newcalib, yerr=Y_r_newcalib, label='New Calibration', ls='None', lw=2, marker='o', capsize=3, color='green', zorder=2, transform=trans_r)

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Energy scale')
        plt.xlim(x_lim)
        plt.ylim(0.5, 1.5)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_res_EoTotBins_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_res_EoTotBins_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_res_EoTotBins_'+label+'_'+target)
        plt.close()

        #######
        # EoTotBins scale from maximum

        EoTotBins_scale_max_unCalib  = file_unCalib.Get("pt_scale_max_fctEoTot")
        EoTotBins_scale_max_oldCalib = file_oldCalib.Get("pt_scale_max_fctEoTot")
        EoTotBins_scale_max_newCalib = file_newCalib.Get("pt_scale_max_fctEoTot")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_scale_max_unCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
        X_s_uncalib = X; Y_s_uncalib = Y
        Ymax = max(Y)

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_scale_max_oldCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
        X_s_oldcalib = X; Y_s_oldcalib = Y
        Ymax = max(Ymax, max(Y))

        X = [] ; Y = [] ; X_err = [] ; Y_err = []
        histo = EoTotBins_scale_max_newCalib
        for ibin in range(0,histo.GetNbinsX()):
            X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
            Y.append(histo.GetBinContent(ibin+1))
            X_err.append(histo.GetBinWidth(ibin+1)/2.)
            Y_err.append(histo.GetBinError(ibin+1))
        ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
        X_s_newcalib = X; Y_s_newcalib = Y
        Ymax = max(Ymax, max(Y))

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='upper right', fontsize=20)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Energy scale')
        plt.xlim(x_lim)
        plt.ylim(0.5, 1.5)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/scale_max_EoTotBins_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_max_EoTotBins_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/scale_max_EoTotBins_'+label+'_'+target)
        plt.close()


# #######
# # pt vs eta scale

# val_white = 0.
# Number = 3
# Red   = array("d", [0., 1., 1.])
# Green = array("d", [0., 1., 0.])
# Blue  = array("d", [1., 1., 0.])
# nb= 256


# PTvsETA_scale1 = file_oldCalib.Get("PTvsETA_events");
# PTvsETA_scale2 = file_newCalib.Get("PTvsETA_events");

# PTvsETA_relative_scale = ROOT.TH2F("PTvsETA_relative_scale","PTvsETA_relative_scale",len(ptBins)-1, array("f",ptBins),len(etaBins)-1, array("f",etaBins));

# for i in range(1,PTvsETA_scale1.GetNbinsX()+1):
#     for j in range(1,PTvsETA_scale1.GetNbinsY()+1):
#         scale1 = abs(PTvsETA_scale1.GetBinContent(i,j)-1);
#         scale2 = abs(PTvsETA_scale2.GetBinContent(i,j)-1);
        
#         if scale2 == 0.: continue

#         rel_scale = (scale1 - scale2)/scale1;
#         PTvsETA_relative_scale.SetBinContent(i,j,rel_scale);

# max_       = PTvsETA_relative_scale.GetMaximum();
# min_       = PTvsETA_relative_scale.GetMinimum();
# per_white = (val_white-min_)/(max_-min_);
# Stops1 = array("d", [ 0., per_white, 1. ]);
# PTvsETA_relative_scale.SetContour(nb);
# ROOT.TColor.CreateGradientColorTable(Number,Stops1,Red,Green,Blue,nb);

# #define canvas for plotting
# canvas = ROOT.TCanvas("c","c",800,800)
# canvas.SetRightMargin(0.2);
# canvas.SetGrid(10,10);

# PTvsETA_relative_scale.SetTitle("");
# PTvsETA_relative_scale.GetXaxis().SetRangeUser(15.,200.);
# PTvsETA_relative_scale.GetXaxis().SetTitle("p_{T}^{offline jet} [GeV]");
# PTvsETA_relative_scale.GetYaxis().SetTitle("#eta^{offline jet} [GeV]");
# PTvsETA_relative_scale.GetZaxis().SetTitle("Relative scale (oldCalib-newCalib)/oldCalib");
# PTvsETA_relative_scale.GetZaxis().SetTitleOffset(2);
# PTvsETA_relative_scale.Draw("colz");

# tex = ROOT.TLatex()
# tex.SetTextSize(0.03);
# tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
# tex.Draw("same")

# tex2 = ROOT.TLatex();
# tex2.SetTextSize(0.035);
# tex2.SetTextAlign(31);
# tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
# tex2.Draw("same");

# b5 = ROOT.TBox(15., 1.305,200.,1.479);
# b5.SetFillColor(16);
# b5.Draw("same");
# b6 = ROOT.TBox(15., 1.305,200.,1.479);
# b6.SetFillColor(1);
# b6.SetFillStyle(3004);
# b6.Draw("same");

# canvas.SaveAs(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+"/ptVSeta_relative_scale_"+label+'_'+target+".pdf")
# canvas.SaveAs(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+"/ptVSeta_relative_scale_"+label+'_'+target+".png")
# print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+"/ptVSeta_relative_scale_"+label+'_'+target)

# del canvas, tex2, tex, b5, b6

# #######
# # pt vs eta resolution

# PTvsETA_resolution1 = file_oldCalib.Get("PTvsETA_resolution");
# PTvsETA_resolution2 = file_newCalib.Get("PTvsETA_resolution");

# PTvsETA_relative_resolution = ROOT.TH2F("PTvsETA_relative_resolution","PTvsETA_relative_resolution",len(ptBins)-1, array("f",ptBins),len(etaBins)-1, array("f",etaBins));

# for i in range(1,PTvsETA_resolution1.GetNbinsX()+1):
#     for j in range(1,PTvsETA_resolution1.GetNbinsY()+1):
#         res1 = PTvsETA_resolution1.GetBinContent(i,j);
#         res2 = PTvsETA_resolution2.GetBinContent(i,j);

#         if res2 == 0.: continue

#         rel_res = (res1 - res2)/res2;
#         PTvsETA_relative_resolution.SetBinContent(i,j,rel_res);

# max_       = PTvsETA_relative_resolution.GetMaximum();
# min_       = PTvsETA_relative_resolution.GetMinimum();
# per_white = (val_white-min_)/(max_-min_);
# Stops2 = array("d", [ 0., per_white, 1. ])
# PTvsETA_relative_resolution.SetContour(nb);
# ROOT.TColor.CreateGradientColorTable(Number,Stops2,Red,Green,Blue,nb);

# #define canvas for plotting
# canvas = ROOT.TCanvas("c","c",800,800)
# canvas.SetRightMargin(0.2);
# canvas.SetGrid(10,10);

# PTvsETA_relative_resolution.SetTitle("");
# PTvsETA_relative_resolution.GetXaxis().SetRangeUser(15.,200.);
# PTvsETA_relative_resolution.GetXaxis().SetTitle("p_{T}^{offline jet} [GeV]");
# PTvsETA_relative_resolution.GetYaxis().SetTitle("#eta^{offline jet} [GeV]");
# PTvsETA_relative_resolution.GetZaxis().SetTitle("Relative resolution (oldCalib-newCalib)/oldCalib");
# PTvsETA_relative_resolution.GetZaxis().SetTitleOffset(2);
# PTvsETA_relative_resolution.Draw("colz");

# tex = ROOT.TLatex()
# tex.SetTextSize(0.03);
# tex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Simulation")
# tex.Draw("same")

# tex2 = ROOT.TLatex();
# tex2.SetTextSize(0.035);
# tex2.SetTextAlign(31);
# tex2.DrawLatexNDC(0.90,0.91,"(14 TeV)");
# tex2.Draw("same");

# b5 = ROOT.TBox(15., 1.305,200.,1.479);
# b5.SetFillColor(16);
# b5.Draw("same");
# b6 = ROOT.TBox(15., 1.305,200.,1.479);
# b6.SetFillColor(1);
# b6.SetFillStyle(3004);
# b6.Draw("same");

# canvas.SaveAs(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+"/ptVSeta_relative_resolution_"+label+'_'+target+".pdf")
# canvas.SaveAs(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+"/ptVSeta_relative_resolution_"+label+'_'+target+".png")
# print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+"/ptVSeta_relative_resolution_"+label+'_'+target)

# del canvas, tex2, tex, b5, b6

#######

file_unCalib.Close() 
file_oldCalib.Close() 
file_newCalib.Close() 

#############################
## RATE+TURNON COMPARISONS ##

if options.doRate == True or options.doTurnOn == True:
    file_rate_unCalib  = ROOT.TFile(uncdir+'/PerformancePlots/'+label+'/ROOTs/rate_graphs_'+label+'_'+target+'.root', 'r')
    file_rate_oldCalib = ROOT.TFile(olddir+'/PerformancePlots/'+label+'/ROOTs/rate_graphs_'+label+'_'+target+'.root', 'r')
    file_rate_newCalib = ROOT.TFile(indir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/rate_graphs_'+label+'_'+target+'.root', 'r')

    file_turnon_unCalib  = ROOT.TFile(uncdir+'/PerformancePlots/'+label+'/ROOTs/efficiency_graphs_'+label+'_'+target+'.root', 'r')
    file_turnon_oldCalib = ROOT.TFile(olddir+'/PerformancePlots/'+label+'/ROOTs/efficiency_graphs_'+label+'_'+target+'.root', 'r')
    file_turnon_newCalib = ROOT.TFile(indir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/efficiency_graphs_'+label+'_'+target+'.root', 'r')

    rateDi_unCalib  = file_rate_unCalib.Get("rateDiProgression0")
    rateDi_oldCalib = file_rate_oldCalib.Get("rateDiProgression0")
    rateDi_newCalib = file_rate_newCalib.Get("rateDiProgression0")

if options.doRate == True:
    print("\n *** COMPARING RATES")
    print(" ### INFO: UnCalib file  = {}".format(uncdir+'/PerformancePlots/'+label+'/ROOTs/rate_graphs_'+label+'_'+target+'.root'))
    print(" ### INFO: OldCalib file = {}".format(olddir+'/PerformancePlots/'+label+'/ROOTs/rate_graphs_'+label+'_'+target+'.root'))
    print(" ### INFO: NewCalib file = {}".format(indir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/rate_graphs_'+label+'_'+target+'.root'))

    # #######
    # DoubleObj rates

    if options.target == 'jet': x_label = r'$E_{T}^{jet, L1}$'
    if options.target == 'ele': x_label = r'$E_{T}^{e/\gamma, L1}$'

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateDi_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateDi_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateDi_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    Ymax = max(Ymax, max(Y))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Rate [kHz]')
    plt.xlim(0, 120)
    plt.ylim(0.1, 1E5)
    plt.yscale('log')
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObj_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObj_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObj_'+label+'_'+target)
    plt.close()

if options.doTurnOn == True:

    print("\n *** COMPARING TURN ONS")
    print(" ### INFO: UnCalib file  = {}".format(uncdir+'/PerformancePlots/'+label+'/ROOTs/efficiency_graphs_'+label+'_'+target+'.root'))
    print(" ### INFO: OldCalib file = {}".format(olddir+'/PerformancePlots/'+label+'/ROOTs/efficiency_graphs_'+label+'_'+target+'.root'))
    print(" ### INFO: NewCalib file = {}".format(indir+'/PerformancePlots'+options.tag+'/'+label+'/ROOTs/efficiency_graphs_'+label+'_'+target+'.root'))

    if options.reco:
        if options.target == 'jet': x_label = r'$p_{T}^{jet, offline}$'
        if options.target == 'ele': x_label = r'$p_{T}^{e, offline}$'
    if options.gen:
        if options.target == 'jet': x_label = r'$p_{T}^{jet, gen}$'
        if options.target == 'ele': x_label = r'$p_{T}^{e, gen}$'

    for thr in options.thrsFixRate:
        rateOldCalibAtThr = rateDi_oldCalib.GetBinContent(int(thr)+1)

        thrNewCalib_DiObjAtThr = 0
        for i in range(1,240):
            if rateDi_newCalib.GetBinContent(i) < rateOldCalibAtThr:
                thrNewCalib_DiObjAtThr = rateDi_newCalib.GetBinLowEdge(i-1)
                break

        thrUnCalib_DiObjAtThr = 0
        for i in range(1,240):
            if rateDi_unCalib.GetBinContent(i) < rateOldCalibAtThr:
                thrUnCalib_DiObjAtThr = rateDi_unCalib.GetBinLowEdge(i-1)
                break
        
        if thrUnCalib_DiObjAtThr == 0 or thrNewCalib_DiObjAtThr == 0: continue
        turnon_unCalib  = file_turnon_unCalib.Get("divide_passing"+str(int(thrUnCalib_DiObjAtThr))+"_by_total")
        turnon_oldCalib = file_turnon_oldCalib.Get("divide_passing"+str(int(thr))+"_by_total")
        turnon_newCalib = file_turnon_newCalib.Get("divide_passing"+str(int(thrNewCalib_DiObjAtThr))+"_by_total")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_unCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'No calibration: $p_{T}^{L1}>$'+str(int(thrUnCalib_DiObjAtThr))+' GeV', lw=2, marker='o', color='black', zorder=0)

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_oldCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'Old calibration: $p_{T}^{L1}>$'+str(int(thr))+' GeV', lw=2, marker='o', color='red', zorder=1)

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_newCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'New Calibration: $p_{T}^{L1}>$'+str(int(thrNewCalib_DiObjAtThr))+' GeV', lw=2, marker='o', color='green', zorder=2)

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='lower right', fontsize=20, title=r'Fixed rate: '+str(round(rateOldCalibAtThr,2))+' kHz', title_fontsize=18)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Efficiency')
        plt.xlim(0, 60) if int(thr) < 30 else plt.xlim(0, 250)
        plt.ylim(0., 1.05)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedDiObjRate_'+thr+'_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedDiObjRate_'+thr+'_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedDiObjRate_'+thr+'_'+label+'_'+target)
        plt.close()


# #######
# # DoubleObjEr rates
if options.doRate == True or options.doTurnOn == True:
    rateDiEr_unCalib  = file_rate_unCalib.Get("rateDiProgression0er2p5")
    rateDiEr_oldCalib = file_rate_oldCalib.Get("rateDiProgression0er2p5")
    rateDiEr_newCalib = file_rate_newCalib.Get("rateDiProgression0er2p5")

if options.doRate == True:

    if options.target == 'jet': x_label = r'$E_{T}^{jet, L1}$'
    if options.target == 'ele': x_label = r'$E_{T}^{e/\gamma, L1}$'

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateDiEr_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateDiEr_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateDiEr_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    Ymax = max(Ymax, max(Y))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Rate [kHz]')
    plt.xlim(0, 120)
    plt.ylim(0.1, 1E5)
    plt.yscale('log')
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObjEr2p5_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObjEr2p5_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObjEr2p5_'+label+'_'+target)
    plt.close()

if options.doTurnOn == True:
    for thr in options.thrsFixRate:
        rateOldCalibAtThr = rateDiEr_oldCalib.GetBinContent(int(thr)+1)

        thrNewCalib_FixedDiErRate = 0
        for i in range(1,240):
            if rateDiEr_newCalib.GetBinContent(i) < rateOldCalibAtThr:
                thrNewCalib_FixedDiErRate = rateDiEr_newCalib.GetBinLowEdge(i-1)
                break

        thrUnCalib_FixedDiErRate = 0
        for i in range(1,240):
            if rateDiEr_unCalib.GetBinContent(i) < rateOldCalibAtThr:
                thrUnCalib_FixedDiErRate = rateDiEr_unCalib.GetBinLowEdge(i-1)
                break

        if thrUnCalib_FixedDiErRate == 0 or thrNewCalib_FixedDiErRate == 0: continue
        turnon_unCalib  = file_turnon_unCalib.Get("divide_passing"+str(int(thrUnCalib_FixedDiErRate))+"_by_total")
        turnon_oldCalib = file_turnon_oldCalib.Get("divide_passing"+str(int(thr))+"_by_total")
        turnon_newCalib = file_turnon_newCalib.Get("divide_passing"+str(int(thrNewCalib_FixedDiErRate))+"_by_total")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_unCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'No calibration: $p_{T}^{L1}>$'+str(int(thrUnCalib_FixedDiErRate))+' GeV', lw=2, marker='o', color='black', zorder=0)

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_oldCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'Old calibration: $p_{T}^{L1}>$'+str(int(thr))+' GeV', lw=2, marker='o', color='red', zorder=1)

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_newCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'New Calibration: $p_{T}^{L1}>$'+str(int(thrNewCalib_FixedDiErRate))+' GeV', lw=2, marker='o', color='green', zorder=2)

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='lower right', fontsize=20, title=r'Fixed rate: '+str(round(rateOldCalibAtThr,2))+' kHz', title_fontsize=18)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Efficiency')
        plt.xlim(0, 60) if int(thr) < 30 else plt.xlim(0, 250)
        plt.ylim(0., 1.05)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedDiObjEr2p5Rate_'+thr+'_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedDiObjEr2p5Rate_'+thr+'_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedDiObjEr2p5Rate_'+thr+'_'+label+'_'+target)
        plt.close()

if options.doRate == True or options.doTurnOn == True:
    rate_unCalib  = file_rate_unCalib.Get("rateProgression0")
    rate_oldCalib = file_rate_oldCalib.Get("rateProgression0")
    rate_newCalib = file_rate_newCalib.Get("rateProgression0")

######
# SingleObj rates
if options.doRate == True:

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rate_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rate_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rate_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    Ymax = max(Ymax, max(Y))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Rate [kHz]')
    plt.xlim(0, 120)
    plt.ylim(0.1, 1E5)
    plt.yscale('log')
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObj_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObj_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/rate_DiObj_'+label+'_'+target)
    plt.close()

if options.doTurnOn == True:
    for thr in options.thrsFixRate:
        rateOldCalibAtThr = rate_oldCalib.GetBinContent(int(thr)+1)

        thrNewCalib_ObjAtThr = 0
        for i in range(1,240):
            if rate_newCalib.GetBinContent(i) < rateOldCalibAtThr:
                thrNewCalib_ObjAtThr = rate_newCalib.GetBinLowEdge(i-1)
                break

        thrUnCalib_ObjAtThr = 0
        for i in range(1,240):
            if rate_unCalib.GetBinContent(i) < rateOldCalibAtThr:
                thrUnCalib_ObjAtThr = rate_unCalib.GetBinLowEdge(i-1)
                break

        if thrNewCalib_ObjAtThr == 0 or thrUnCalib_ObjAtThr == 0: continue
        turnon_unCalib  = file_turnon_unCalib.Get("divide_passing"+str(int(thrUnCalib_ObjAtThr))+"_by_total")
        turnon_oldCalib = file_turnon_oldCalib.Get("divide_passing"+str(int(thr))+"_by_total")
        turnon_newCalib = file_turnon_newCalib.Get("divide_passing"+str(int(thrNewCalib_ObjAtThr))+"_by_total")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_unCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'No calibration: $p_{T}^{L1}>$'+str(int(thrUnCalib_ObjAtThr))+' GeV', lw=2, marker='o', color='black', zorder=0)

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_oldCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'Old calibration: $p_{T}^{L1}>$'+str(int(thr))+' GeV', lw=2, marker='o', color='red', zorder=1)

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_newCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'New Calibration: $p_{T}^{L1}>$'+str(int(thrNewCalib_ObjAtThr))+' GeV', lw=2, marker='o', color='green', zorder=2)

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='lower right', fontsize=20, title=r'Fixed rate: '+str(round(rateOldCalibAtThr,2))+' kHz', title_fontsize=18)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Efficiency')
        plt.xlim(0, 60) if int(thr) < 30 else plt.xlim(0, 250)
        plt.ylim(0., 1.05)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedObjRate_'+thr+'_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedObjRate_'+thr+'_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedObjRate_'+thr+'_'+label+'_'+target)
        plt.close()

if options.doRate == True or options.doTurnOn == True:
    rateEr_unCalib  = file_rate_unCalib.Get("rateProgression0er2p5")
    rateEr_oldCalib = file_rate_oldCalib.Get("rateProgression0er2p5")
    rateEr_newCalib = file_rate_newCalib.Get("rateProgression0er2p5")

# ######
# SingleObjEr rates
if options.doRate == True:

    fig, ax = plt.subplots(figsize=(10,10))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateEr_unCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='No calibration', ls='None', lw=2, marker='o', color='black', zorder=0)
    Ymax = max(Y)

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateEr_oldCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='Old calibration', ls='None', lw=2, marker='o', color='red', zorder=1)
    Ymax = max(Ymax, max(Y))

    X = [] ; Y = [] ; X_err = [] ; Y_err = []
    histo = rateEr_newCalib
    for ibin in range(0,histo.GetNbinsX()):
        X.append(histo.GetBinLowEdge(ibin+1) + histo.GetBinWidth(ibin+1)/2.)
        Y.append(histo.GetBinContent(ibin+1))
        X_err.append(histo.GetBinWidth(ibin+1)/2.)
        Y_err.append(histo.GetBinError(ibin+1))
    ax.errorbar(X, Y, xerr=X_err, yerr=Y_err, label='New Calibration', ls='None', lw=2, marker='o', color='green', zorder=2)
    Ymax = max(Ymax, max(Y))

    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    leg = plt.legend(loc='upper right', fontsize=20)
    leg._legend_box.align = "left"
    plt.xlabel(x_label)
    plt.ylabel('Rate [kHz]')
    plt.xlim(0, 120)
    plt.ylim(0.1, 1E5)
    plt.yscale('log')
    for xtick in ax.xaxis.get_major_ticks():
        xtick.set_pad(10)
    plt.grid()
    if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
    else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/rate_ObjEr2p5_'+label+'_'+target+'.pdf')
    plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/rate_ObjEr2p5_'+label+'_'+target+'.png')
    print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/rate_ObjEr2p5_'+label+'_'+target)
    plt.close()

if options.doTurnOn == True:
    for thr in options.thrsFixRate:
        rateOldCalibAtThr = rateEr_oldCalib.GetBinContent(int(thr)+1)

        thrNewCalib_FixedErRate = 0
        for i in range(1,240):
            if rateEr_newCalib.GetBinContent(i) < rateOldCalibAtThr:
                thrNewCalib_FixedErRate = rateEr_newCalib.GetBinLowEdge(i-1)
                break

        thrUnCalib_FixedErRate = 0
        for i in range(1,240):
            if rateEr_unCalib.GetBinContent(i) < rateOldCalibAtThr:
                thrUnCalib_FixedErRate = rateEr_unCalib.GetBinLowEdge(i-1)
                break

        if thrNewCalib_FixedErRate == 0 or thrUnCalib_FixedErRate == 0: continue
        turnon_unCalib  = file_turnon_unCalib.Get("divide_passing"+str(int(thrUnCalib_FixedErRate))+"_by_total")
        turnon_oldCalib = file_turnon_oldCalib.Get("divide_passing"+str(int(thr))+"_by_total")
        turnon_newCalib = file_turnon_newCalib.Get("divide_passing"+str(int(thrNewCalib_FixedErRate))+"_by_total")

        fig, ax = plt.subplots(figsize=(10,10))

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_unCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'No calibration: $p_{T}^{L1}>$'+str(int(thrUnCalib_FixedErRate))+' GeV', lw=2, marker='o', color='black', zorder=0)

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_oldCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'Old calibration: $p_{T}^{L1}>$'+str(int(thr))+' GeV', lw=2, marker='o', color='red', zorder=1)

        X = [] ; Y = [] ; Y_low = [] ; Y_high = []
        turnon = turnon_newCalib
        for ibin in range(0,turnon.GetN()):
            X.append(turnon.GetPointX(ibin))
            Y.append(turnon.GetPointY(ibin))
            Y_low.append(turnon.GetErrorYlow(ibin))
            Y_high.append(turnon.GetErrorYhigh(ibin))
        ax.errorbar(X, Y, xerr=1, yerr=[Y_low, Y_high], label=R'New Calibration: $p_{T}^{L1}>$'+str(int(thrNewCalib_FixedErRate))+' GeV', lw=2, marker='o', color='green', zorder=2)

        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        leg = plt.legend(loc='lower right', fontsize=20, title=r'Fixed rate: '+str(round(rateOldCalibAtThr,2))+' kHz', title_fontsize=18)
        leg._legend_box.align = "left"
        plt.xlabel(x_label)
        plt.ylabel('Efficiency')
        plt.xlim(0, 60) if int(thr) < 30 else plt.xlim(0, 250)
        plt.ylim(0., 1.05)
        for xtick in ax.xaxis.get_major_ticks():
            xtick.set_pad(10)
        plt.grid()
        if options.reco: mplhep.cms.label(data=False, rlabel='(13.6 TeV)')
        else:            mplhep.cms.label('Preliminary', data=True, rlabel=r'110 pb$^{-1}$ (13.6 TeV)') ## 110pb-1 is Run 362617
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PDFs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedObjEr2p5Rate_'+thr+'_'+label+'_'+target+'.pdf')
        plt.savefig(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedObjEr2p5Rate_'+thr+'_'+label+'_'+target+'.png')
        print(outdir+'/PerformancePlots'+options.tag+'/'+label+'/PNGs/comparisons_'+label+'_'+target+options.ref+'/turnon_fixedObjEr2p5Rate_'+thr+'_'+label+'_'+target)
        plt.close()

if options.doRate == True or options.doTurnOn == True:
    file_rate_unCalib.Close()
    file_rate_oldCalib.Close()
    file_rate_newCalib.Close()
    file_turnon_unCalib.Close()
    file_turnon_oldCalib.Close()
    file_turnon_newCalib.Close()

