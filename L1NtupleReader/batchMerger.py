from optparse import OptionParser
from TowerGeometry import *
import pandas as pd
import numpy as np
import os

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### python3 batchMerger.py --indir 2022_04_21_NtuplesV2 --sample train --v (ECAL or HCAL) 

if __name__ == "__main__" :

    # read the batched input tensors to the NN and merge them
    parser = OptionParser()
    parser.add_option("--v",        dest="v",       help="Ntuple type ('ECAL' or 'HCAL')",      default='ECAL')
    parser.add_option("--odir",     dest="odir",    default="")
    parser.add_option("--jetcut",   dest="jetcut",  help="JetPt cut in GeV",                    default=None)
    parser.add_option("--indir",      dest="indir",     help="Folder with npz files to be merged",  default='')
    parser.add_option("--sample",   dest="sample",  help="Type of sample (train or test)",       default='')
    parser.add_option("--applyHCALpfa1p", dest="applyHCALpfa1p", action='store_true', default=True)
    parser.add_option("--applyNoCalib", dest="applyNoCalib", action='store_true', default=False)
    parser.add_option("--applyOldCalib", dest="applyOldCalib", action='store_true', default=False)
    parser.add_option("--applyNewECALcalib", dest="applyNewECALcalib", action='store_true', default=False)
    parser.add_option("--applyNewECALpHCALcalib", dest="applyNewECALpHCALcalib", action='store_true', default=False)
    parser.add_option("--doEG0_200", dest="doEG0_200", action='store_true', default=False)
    parser.add_option("--doEG", dest="doEG", action='store_true', default=False)
    parser.add_option("--doQCDnoPU", dest="doQCDnoPU", action='store_true', default=False)
    parser.add_option("--doQCDpu", dest="doQCDpu", action='store_true', default=False)
    parser.add_option("--applyOnTheFly", dest="applyOnTheFly", action='store_true', default=False)
    parser.add_option("--filesLim", dest="filesLim", type=int, default=150)
    (options, args) = parser.parse_args()
    print(options)


    if options.applyNoCalib == False and options.applyOldCalib == False and options.applyNewECALcalib == False and options.applyNewECALpHCALcalib == False:
        print('** WARNING: no calibration to be used specified - EXITING!')
        exit()

    if options.doEG0_200 == False and options.doEG == False and options.doQCDnoPU == False and options.doQCDpu == False:
        print('** WARNING: no dataset to be used specified - EXITING!')
        exit()

    tagHCALpfa1p = ""
    tagCalib = ""
    if   options.applyNoCalib:           tagCalib = "_uncalib"
    elif options.applyOldCalib:          tagCalib = "_oldCalib"
    elif options.applyNewECALcalib:      tagCalib = "_newECALcalib" 
    elif options.applyNewECALpHCALcalib: tagCalib = "_newECALpHCALcalib"
    if   options.applyHCALpfa1p:         tagHCALpfa1p = "_applyHCALpfa1p"


    taglists = []
    tensordirs = []
    dataframedirs = []

    filedir = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir

    outputFolderName = 'paddedAndReadyToMerge'
    if options.applyOnTheFly: outputFolderName = 'appliedOnTheFly'

    if   options.doQCDpu:
        ## qcd flat0-80 pu
        #folder_names.append("QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-FlatPU0to80FEVT_castor_120X_mcRun3_2021_realistic_v6-v1__reEmulated"+tagCalib+tagHCALpfa1p)
        print('** WARNING: unbinned QCD samples not available at the moment, specify pt bin - EXITING!')
        exit()

    elif options.doQCDnoPU:
        ## qcd without pu - backup datasets
            # taglist20To30 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt20To30_{0}.txt'.format(options.sample))
            # taglists.append(taglist20To30)
            # tensordirs.append(filedir +'/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/tensors'.format(outputFolderName))
            # dataframedirs.append(filedir +'/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/dataframes'.format(outputFolderName))

            # taglist30To50 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt30To50_{0}.txt'.format(options.sample))
            # taglists.append(taglist30To50)
            # tensordirs.append(filedir +'/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/tensors'.format(outputFolderName))
            # dataframedirs.append(filedir +'/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/dataframes'.format(outputFolderName))

            # taglist50To80 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt50To80_{0}.txt'.format(options.sample))
            # taglists.append(taglist50To80)
            # tensordirs.append(filedir +'/QCD_Pt-50To80_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/tensors'.format(outputFolderName))
            # dataframedirs.append(filedir +'/QCD_Pt-50To80_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/dataframes'.format(outputFolderName))

            # taglist80To120 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt80To120_{0}.txt'.format(options.sample))
            # taglists.append(taglist80To120)
            # tensordirs.append(filedir +'/QCD_Pt-80To120_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/tensors'.format(outputFolderName))
            # dataframedirs.append(filedir +'/QCD_Pt-80To120_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/dataframes'.format(outputFolderName))

            # taglist120To170 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt120To170_{0}.txt'.format(options.sample))
            # taglists.append(taglist120To170)
            # tensordirs.append(filedir +'/QCD_Pt-120To170_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/tensors'.format(outputFolderName))
            # dataframedirs.append(filedir +'/QCD_Pt-120To170_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}/dataframes'.format(outputFolderName))

            ## qcd without pu
            taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_{0}.txt'.format(options.sample))
            taglists.append(taglist)
            tensordirs.append(filedir +'/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}{1}/tensors'.format(outputFolderName,options.odir))
            dataframedirs.append(filedir +'/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}{1}/dataframes'.format(outputFolderName,options.odir))


    elif options.doEG0_200:
        ## signle photon 0-200 without pu
        taglist0_200 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_eg_Pt0To200_{0}.txt'.format(options.sample))
        taglists.append(taglist0_200)
        tensordirs.append(filedir +'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}{1}/tensors'.format(outputFolderName,options.odir))
        dataframedirs.append(filedir +'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}{1}/dataframes'.format(outputFolderName,options.odir))

    elif options.doEG:
        ## signle photon 0-200 without pu
        taglist0_200 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_eg_Pt0To200_{0}.txt'.format(options.sample))
        taglists.append(taglist0_200)
        tensordirs.append(filedir +'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}_0pt200/tensors'.format(outputFolderName,options.odir))
        dataframedirs.append(filedir +'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}_0pt200/dataframes'.format(outputFolderName,options.odir))

        taglist200_500 = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_eg_Pt200To500_{0}.txt'.format(options.sample))
        taglists.append(taglist200_500)
        tensordirs.append(filedir +'/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}_200pt500/tensors'.format(outputFolderName,options.odir))
        dataframedirs.append(filedir +'/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches/{0}_200pt500/dataframes'.format(outputFolderName,options.odir))


    else:
        print(' ** WARNING: wrong request --> EXITING!')
        exit()

    XsToConcatenate = []
    YsToConcatenate = []

    training_folder = filedir + '/{0}training{1}'.format(options.v, options.odir)
    os.system('mkdir -p ' + training_folder)

    for i_fold, taglist in enumerate(taglists):
        for idx,tag in enumerate(taglist):
            tag = tag.strip()
            if not idx%10: print('reading batch', idx)
            try:
                # DEBUG
                # print(tag)
                # print(np.load(tensordirs[i_fold]+'/towers'+tag+'.npz', allow_pickle=True)['arr_0'])
                # exit()

                XsToConcatenate.append(np.load(tensordirs[i_fold]+'/towers'+tag+'.npz', allow_pickle=True)['arr_0'])
                YsToConcatenate.append(np.load(tensordirs[i_fold]+'/jets'+tag+'.npz', allow_pickle=True)['arr_0'])

            except FileNotFoundError:
                # DEBUG
                print('** INFO: towers'+tag+' not found --> skipping')
                continue

            if idx == options.filesLim: break # break at the n-th file to speed up the process

    X = np.concatenate(XsToConcatenate)
    Y = np.concatenate(YsToConcatenate)

    ## DEBUG
    print(len(X))
    print(len(Y))

    # We will produce one sample fot training and one for testing from different ntuples
    np.savez_compressed(training_folder+'/X_'+options.sample+'.npz', X)
    np.savez_compressed(training_folder+'/Y_'+options.sample+'.npz', Y)

    print("Saved data samples in folder: {}".format(training_folder))    
