from optparse import OptionParser
import json
import os


def splitInBlocks (l, n):
    """split the list l in n blocks of equal size"""
    k = len(l) / n
    r = len(l) % n

    i = 0
    blocks = []
    while i < len(l):
        if len(blocks)<r:
            blocks.append(l[i:i+k+1])
            i += k+1
        else:
            blocks.append(l[i:i+k])
            i += k

    return blocks

###########

if __name__ == "__main__" :

    parser = OptionParser()
    parser.add_option("--njobs", dest="njobs", type=int, default=200)
    parser.add_option("--applyHCALpfa1p", dest="applyHCALpfa1p", action='store_true', default=True)
    parser.add_option("--applyNoCalib", dest="applyNoCalib", action='store_true', default=False)
    parser.add_option("--applyOldCalib", dest="applyOldCalib", action='store_true', default=False)
    parser.add_option("--applyNewCalib", dest="applyNewCalib", action='store_true', default=False)
    parser.add_option("--applyNewCalibSaturAt", dest="applyNewCalibSaturAt", type=float, default=None)
    parser.add_option("--doEG0_200", dest="doEG0_200", action='store_true', default=False)
    parser.add_option("--doEG200_500", dest="doEG200_500", action='store_true', default=False)
    parser.add_option("--doQCDnoPU", dest="doQCDnoPU", action='store_true', default=False)
    parser.add_option("--doQCDpu", dest="doQCDpu", action='store_true', default=False)
    parser.add_option("--qcdPtBin", dest="qcdPtBin", default="")
    parser.add_option("--doPi0_200", dest="doPi0_200", action='store_true', default=False)
    parser.add_option("--doNu", dest="doNu", action='store_true', default=False)
    parser.add_option("--doMET", dest="doMET", action='store_true', default=False)
    parser.add_option("--testRun", dest="testRun", action='store_true', default=False)
    parser.add_option("--no_exec", dest="no_exec", action='store_true', default=False)
    (options, args) = parser.parse_args()
    

    if options.applyNoCalib == False and options.applyOldCalib == False and options.applyNewCalib == False and options.applyNewCalibSaturAt == None:
        print('** WARNING: no calibration to be used specified - EXITING!')
        exit()

    if options.doEG0_200 == False and options.doEG200_500 == False and options.doQCDnoPU == False and options.doQCDpu == False and options.doPi0_200 == False and options.doNu == False and options.doMET == False and options.testRun == False:
        print('** WARNING: no dataset to be used specified - EXITING!')
        exit()

    tagHCALpfa1p = ""
    tagCalib = ""
    config = "L1Ntuple"
    if   options.applyNoCalib:         config += "_uncalib"         ; tagCalib = "_uncalib"
    elif options.applyOldCalib:        config += "_oldCalib"        ; tagCalib = "_oldCalib"
    elif options.applyNewCalib:        config += "_newCalib"        ; tagCalib = "_newCalib" 
    elif options.applyNewCalibSaturAt: config += "_newCalibSatur"+str(options.applyNewCalibSaturAt).split('.')[0]+'p'+str(options.applyNewCalibSaturAt).split('.')[1] ; tagCalib = "_newCalibSatur"+str(options.applyNewCalibSaturAt).split('.')[0]+'p'+str(options.applyNewCalibSaturAt).split('.')[1]
    if options.doMET:                  config += "_forMET"
    if options.applyHCALpfa1p:         config += "_applyHCALpfa1p"  ; tagHCALpfa1p = "_applyHCALpfa1p"
    config += "_cfg.py"

    njobs = options.njobs
    filedir="/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleLauncher/inputFiles"

    if   options.doQCDpu:
        ## qcd flat0-80 pu
        filelist = open(filedir+"/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-FlatPU0to80FEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW.txt")
        folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-FlatPU0to80FEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p
        
        print('** WARNING: unbinned QCD samples not available at the moment, specify pt bin - EXITING!')
        exit()

    elif options.doQCDnoPU:
        ## qcd without pu - backup datasets
        if options.qcdPtBin=="20To30":
            filelist = open(filedir+"/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
            folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p
        
        elif options.qcdPtBin=="30To50":
            filelist = open(filedir+"/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
            folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p
        
        elif options.qcdPtBin=="50To80":
            filelist = open(filedir+"/QCD_Pt-50To80_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
            folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt-50To80_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p
        
        elif options.qcdPtBin=="80To120":
            filelist = open(filedir+"/QCD_Pt-80To120_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
            folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt-80To120_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p
        
        elif options.qcdPtBin=="120To170":
            filelist = open(filedir+"/QCD_Pt-120To170_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
            folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt-120To170_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p

        elif options.qcdPtBin=="PUForTRK":
            filelist = open(filedir+"/QCD_Pt-15to7000_TuneCP5_Flat_13p6TeV-pythia8__Run3Winter22DR-PUForTRK_DIGI_122X_mcRun3_2021_realistic_v9-v2__GEN-SIM-DIGI-RAW.txt")
            folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt-15to7000_TuneCP5_Flat_13p6TeV-pythia8__Run3Winter22DR-PUForTRK_DIGI_122X_mcRun3_2021_realistic_v9-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p

        else:
            filelist = open(filedir+"/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW.txt")
            folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p

    elif options.doEG0_200:
        ## signle photon 0-200 without pu
        filelist = open(filedir+"/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
        folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p
    
    elif options.doEG200_500:
        ## signle photon 200-500 without pu
        filelist = open(filedir+"/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
        folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p

    elif options.doPi0_200:
        ## signle pion 0-200 without pu
        filelist = open(filedir+"/SinglePion_Pt-0to200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW.txt")
        folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SinglePion_Pt-0to200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p

    elif options.doNu:
        ## single neutrino with pu
        filelist = open(filedir+"/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
        folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW"+tagCalib+tagHCALpfa1p

    elif options.doMET:
        ## H to invisible for MET
        filelist = open(filedir+"/VBFHToInvisible_M125_TuneCP5_14TeV-powheg-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__AODSIM.txt")
        folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/VBFHToInvisible_M125_TuneCP5_14TeV-powheg-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__AODSIM"+tagCalib+tagHCALpfa1p

    elif options.testRun:
        # TEST 10 files from signle photon 0-200 without pu
        filelist = open(filedir+"/test.txt")
        folder = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/test_"+tagCalib+tagHCALpfa1p


    ###########

    # calling this command only one at the beginning of submitOnTier3.sh
    # os.system ('source /opt/exp_soft/cms/t3/t3setup')

    os.system('mkdir -p ' + folder)
    os.system('cp '+config+' '+folder)
    os.system('cp listAll.sh /data_CMS/cms/motta/CaloL1calibraton/L1NTuples')
    files = [f.strip() for f in filelist]
    print "Input has" , len(files) , "files" 
    if njobs > len(files) : njobs = len(files)
    filelist.close()

    fileblocks = splitInBlocks (files, njobs)

    for idx, block in enumerate(fileblocks):
        #print idx, block

        outRootName = folder + '/Ntuple_' + str(idx) + '.root'
        outJobName  = folder + '/job_' + str(idx) + '.sh'
        outListName = folder + "/filelist_" + str(idx) + ".txt"
        if options.doMET: outSecondaryListName = folder + "/secondaryFilelist_" + str(idx) + ".txt"
        outLogName  = folder + "/log_" + str(idx) + ".txt"

        jobfilelist = open(outListName, 'w')
        for f in block: jobfilelist.write(f+"\n")
        jobfilelist.close()

        if options.doMET:
            jobsecondaryfilelist = open(outSecondaryListName, 'w')
            jobsecondaryfilelist.close()
            for f in block:
                os.system('dasgoclient --query="parent file='+f+'" >& '+outSecondaryListName)

        if options.doMET: cmsRun = "cmsRun "+config+" maxEvents=-1 inputFiles_load="+outListName + " secondaryInputFiles_load="+outSecondaryListName + " outputFile="+outRootName + " >& " + outLogName
        else:             cmsRun = "cmsRun "+config+" maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName

        skimjob = open (outJobName, 'w')
        skimjob.write ('#!/bin/bash\n')
        skimjob.write ('export X509_USER_PROXY=~/.t3/proxy.cert\n')
        skimjob.write ('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
        skimjob.write ('cd %s\n' % os.getcwd())
        skimjob.write ('export SCRAM_ARCH=slc6_amd64_gcc472\n')
        skimjob.write ('eval `scram r -sh`\n')
        skimjob.write ('cd %s\n'%os.getcwd())
        skimjob.write (cmsRun+'\n')
        skimjob.close ()

        os.system ('chmod u+rwx ' + outJobName)
        command = ('/home/llr/cms/motta/t3submit -long \'' + outJobName +"\'")
        # command = ('/home/llr/cms/motta/t3submit -short \'' + outJobName +"\'")
        print command
        if not options.no_exec: os.system (command)
        # break
