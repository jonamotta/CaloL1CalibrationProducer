import os
import json
from subprocess import Popen, PIPE

#applyHCALpfa1p = False
applyHCALpfa1p = True

tagHCALpfa1p = ""
if applyHCALpfa1p: tagHCALpfa1p = "_appliedHCALpfa1p"

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

###########

njobs = 500
filedir="/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1NtupleLauncher/inputFiles"


### qcd flat0-80 pu
# filelist = open(filedir+"/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-FlatPU0to80FEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW.txt")
# folder = "/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-FlatPU0to80FEVT_castor_120X_mcRun3_2021_realistic_v6-v1__reEmulated"+tagHCALpfa1p

### qcd without pu
# filelist = open(filedir+"/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__GEN-SIM-DIGI-RAW.txt")
# folder = "/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/QCD_Pt15to7000_TuneCP5_14TeV-pythia8__Run3Summer21DR-NoPUFEVT_castor_120X_mcRun3_2021_realistic_v6-v1__reEmulated"+tagHCALpfa1p

### signle photon 0-200 without pu
# filelist = open(filedir+"/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
# folder = "/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-0To200-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated"+tagHCALpfa1p

### signle photon 200-500 without pu
filelist = open(filedir+"/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt")
folder = "/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/SinglePhoton_Pt-200to500-gun__Run3Summer21DR-NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2__reEmulated"+tagHCALpfa1p

# TEST 10 files from signle photon 0-200 without pu
# filelist = open(filedir+"/test.txt")
# folder = "/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/test__reEmulated"+tagHCALpfa1p


###########

os.system ('source /opt/exp_soft/cms/t3/t3setup')

os.system('mkdir -p ' + folder)
if applyHCALpfa1p: os.system('cp L1Ntuple_applyHCALpfa1p_cfg.py '+folder)
else:              os.system('cp L1Ntuple_cfg.py '+folder)
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
    outLogName  = folder + "/log_" + str(idx) + ".txt"

    jobfilelist = open(outListName, 'w')
    for f in block: jobfilelist.write(f+"\n")
    jobfilelist.close()

    if applyHCALpfa1p: cmsRun = "cmsRun L1Ntuple_applyHCALpfa1p_cfg.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName
    else:              cmsRun = "cmsRun L1Ntuple_cfg.py                maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName
    
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
    # command = ('/home/llr/cms/motta/t3submit -short -q cms \'' + outJobName +"\'")
    print command
    os.system (command)
