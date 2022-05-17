import os
import json
# from subprocess import Popen, PIPE

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

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

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

### To run:
### source batchSubmitOnTier3.sh (check which commends are inside it first)

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--indir",     dest="indir",    default=None)
parser.add_option("--odir",     dest="odir",    default="")
parser.add_option("--uJetPtCut", dest="uJetPtCut", default=False)
parser.add_option("--lJetPtCut", dest="lJetPtCut", default=False)
parser.add_option("--etacut",   dest="etacut",  default=False)
parser.add_option("--ecalcut",  dest="ecalcut", default=False)
parser.add_option("--hcalcut",  dest="hcalcut", default=False)
parser.add_option("--calibECALOnTheFly",  dest="calibECALOnTheFly", default=False, help="oldCalib or newCalib; not specified == noCalib")
parser.add_option("--trainPtVers",  dest="trainPtVers", default=False)
parser.add_option("--applyHCALpfa1p", dest="applyHCALpfa1p", action='store_true', default=True)
parser.add_option("--applyNoCalib", dest="applyNoCalib", action='store_true', default=False)
parser.add_option("--applyOldCalib", dest="applyOldCalib", action='store_true', default=False)
parser.add_option("--applyNewECALcalib", dest="applyNewECALcalib", action='store_true', default=False)
parser.add_option("--applyNewECALpHCALcalib", dest="applyNewECALpHCALcalib", action='store_true', default=False)
parser.add_option("--doEG0_200", dest="doEG0_200", action='store_true', default=False)
parser.add_option("--doEG200_500", dest="doEG200_500", action='store_true', default=False)
parser.add_option("--doQCDnoPU", dest="doQCDnoPU", action='store_true', default=False)
parser.add_option("--doQCDpu", dest="doQCDpu", action='store_true', default=False)
parser.add_option("--qcdPtBin", dest="qcdPtBin", default="")
parser.add_option("--FilesLim", dest="FilesLim", type=int, default=0)
(options, args) = parser.parse_args()

if options.indir == None:
    print('** WARNING: no input directory specified - EXITING!')
    exit()

if options.applyNoCalib == False and options.applyOldCalib == False and options.applyNewECALcalib == False and options.applyNewECALpHCALcalib == False:
    print('** WARNING: no calibration to be used specified - EXITING!')
    exit()

if options.doEG0_200 == False and options.doEG200_500 == False and options.doQCDnoPU == False and options.doQCDpu == False and options.testRun == False:
    print('** WARNING: no dataset to be used specified - EXITING!')
    exit()

tagHCALpfa1p = ""
tagCalib = ""
if   options.applyNoCalib:           tagCalib = "_uncalib"
elif options.applyOldCalib:          tagCalib = "_oldCalib"
elif options.applyNewECALcalib:      tagCalib = "_newECALcalib" 
elif options.applyNewECALpHCALcalib: tagCalib = "_newECALpHCALcalib"
if   options.applyHCALpfa1p:         tagHCALpfa1p = "_applyHCALpfa1p"

basedir = '/data_CMS/cms/motta/CaloL1calibraton'
filedir = basedir + '/' + options.indir

if   options.doQCDpu:
    ## qcd flat0-80 pu
    #folder_names.append("QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-FlatPU0to80FEVT_castor_120X_mcRun3_2021_realistic_v6-v1__reEmulated"+tagCalib+tagHCALpfa1p)
    print('** WARNING: unbinned QCD samples not available at the moment, specify pt bin - EXITING!')
    exit()

elif options.doQCDnoPU:
    ## qcd without pu - backup datasets
    if options.qcdPtBin=="20To30":
        taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt20To30.txt')
        filedir = filedir +'/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'
        folder = filedir+'/paddedAndReadyToMerge'

    elif options.qcdPtBin=="30To50":
        taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt30To50.txt')
        filedir = filedir +'/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'
        folder = filedir+'/paddedAndReadyToMerge'

    elif options.qcdPtBin=="50To80":
        taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt50To80.txt')
        filedir = filedir +'/QCD_Pt-50To80_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'
        folder = filedir+'/paddedAndReadyToMerge'

    elif options.qcdPtBin=="80To120":
        taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt80To120.txt')
        filedir = filedir +'/QCD_Pt-80To120_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'
        folder = filedir+'/paddedAndReadyToMerge'

    elif options.qcdPtBin=="120To170":
        taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_Pt120To170.txt')
        filedir = filedir +'/QCD_Pt-120To170_TuneCP5_14TeV-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'
        folder = filedir+'/paddedAndReadyToMerge'

    else:
        ## qcd without pu
        taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU_tmp.txt')
        filedir = filedir +'/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW'+tagCalib+tagHCALpfa1p+'_batches'
        folder = filedir+'/paddedAndReadyToMerge'

elif options.doEG0_200:
    ## signle photon 0-200 without pu
    taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_eg_Pt0To200.txt')
    filedir = filedir +'/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated'+tagCalib+tagHCALpfa1p+'_batches'
    folder = filedir+'/paddedAndReadyToMerge'

elif options.doEG200_500:
    ## signle photon 200-500 without pu
    taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_eg_Pt0To200.txt')
    filedir = filedir +'/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated'+tagCalib+tagHCALpfa1p+'_batches'
    folder = filedir+'/paddedAndReadyToMerge'

else:
    print(' ** WARNING: wrong request --> EXITING!')
    exit()

# appemnd the outdir tag
folder += options.odir
os.system('mkdir -p ' + folder)


###########

#os.system ('source /opt/exp_soft/cms/t3/t3setup')

os.system('mkdir -p ' + folder + '/dataframes ; mkdir -p ' + folder + '/tensors')
tags = [tag.strip() for tag in taglist]
njobs = len(tags)
print("Input has" , len(tags) , "files", "-->", len(tags), "jobs")
taglist.close()

for idx, tag in enumerate(tags):
    #print(idx, tag)

    outJobName  = folder + '/job_' + str(idx) + '.sh'
    outLogName  = folder + "/log_" + str(idx) + ".txt"

    cmsRun = "python batchReader.py --fin "+filedir+" --tag "+tag+" --fout "+folder
    if options.uJetPtCut != False:
        cmsRun = cmsRun + " --uJetPtCut "+options.uJetPtCut
    if options.lJetPtCut != False:
        cmsRun = cmsRun + " --lJetPtCut "+options.lJetPtCut
    if options.etacut != False:
        cmsRun = cmsRun + " --etacut "+options.etacut
    if options.ecalcut != False:
        cmsRun = cmsRun + " --ecalcut "+options.ecalcut
    if options.hcalcut != False:
        cmsRun = cmsRun + " --hcalcut "+options.hcalcut
    if options.trainPtVers != False:
        cmsRun = cmsRun + " --trainPtVers "+options.trainPtVers
    if options.calibECALOnTheFly != False:
        cmsRun = cmsRun + " --calibrateECAL "+options.calibECALOnTheFly

    cmsRun = cmsRun + " >& "+outLogName

    skimjob = open (outJobName, 'w')
    skimjob.write ('#!/bin/bash\n')
    skimjob.write ('export X509_USER_PROXY=~/.t3/proxy.cert\n')
    skimjob.write ('module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7\n')
    skimjob.write ('module load python/3.7.0\n')
    skimjob.write ('cd %s\n'%os.getcwd())
    skimjob.write (cmsRun+'\n')
    skimjob.close ()

    os.system ('chmod u+rwx ' + outJobName)
    command = ('/home/llr/cms/motta/t3submit -long \'' + outJobName +"\'")
    #command = ('/home/llr/cms/evernazza/t3submit -short \'' + outJobName +"\'")
    print(command)
    os.system (command)
    #break
