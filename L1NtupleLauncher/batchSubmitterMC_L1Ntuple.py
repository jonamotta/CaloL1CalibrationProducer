import os, glob
from datetime import datetime
from optparse import OptionParser

# Script to submit MC production
# --------- L1Ntuples ---------
'''
python3 batchSubmitterMC_L1Ntuple.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X/AOD \
--secondarydir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X/RAW \
--out /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X/L1Ntuples \
--maxEvents -1 --queue short --globalTag 126X_mcRun3_2023_forPU65_v1 --caloParams caloParams_2022_v0_6_cfi --reco #(DONE) 1381
python3 batchSubmitterMC_L1Ntuple.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_7000_10000/AOD \
--secondarydir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_7000_10000/RAW \
--out /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_7000_10000/L1Ntuples \
--maxEvents -1 --queue short --globalTag 124X_mcRun3_2022_realistic_postEE_v1 --caloParams caloParams_2022_v0_6_cfi --reco #(DONE) 2998/3000
python3 batchSubmitterMC_L1Ntuple.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_10000_15000/AOD \
--secondarydir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_10000_15000/RAW \
--out /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_10000_15000/L1Ntuples \
--maxEvents -1 --queue short --globalTag 124X_mcRun3_2022_realistic_postEE_v1 --caloParams caloParams_2022_v0_6_cfi --reco
python3 batchSubmitterMC_L1Ntuple.py --indir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_15000_20000/AOD \
--secondarydir /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_15000_20000/RAW \
--out /data_CMS/cms/motta/CaloL1calibraton/PrivateMC/QCD_Pt30_500_TuneCP5_13p6TeV_124X_15000_20000/L1Ntuples \
--maxEvents -1 --queue short --globalTag 124X_mcRun3_2022_realistic_postEE_v1 --caloParams caloParams_2022_v0_6_cfi --reco
'''

if __name__ == "__main__" :

    parser = OptionParser()    
    parser.add_option("--indir",        dest="indir",     type=str,            default=None,                            help="Input folder name (AOD)")
    parser.add_option("--secondarydir", dest="secondarydir",   type=str,            default=None,                            help="Secondary dir folder name (RAW)")
    parser.add_option("--out",          dest="out",       type=str,            default=None,                            help="Output folder name")
    parser.add_option("--maxEvents",    dest="maxEvents", type=int,            default=-1,                              help="Number of events per job")
    parser.add_option("--queue",        dest="queue",     type=str,            default='long',                          help="long or short queue")
    parser.add_option("--globalTag",    dest="globalTag", type=str,            default='126X_mcRun3_2023_forPU65_v1',   help="Which globalTag to use")
    parser.add_option("--caloParams",   dest="caloParams",type=str,            default='caloParams_2022_v0_6_cfi',      help="Which caloParams to use")
    parser.add_option("--reco",         dest="reco",      action='store_true', default=False)
    parser.add_option("--no_exec",      dest="no_exec",   action='store_true', default=False)
    (options, args) = parser.parse_args()

    os.system('mkdir -p '+options.out)

    inRootNameList = glob.glob(options.indir+"/Ntuple_*.root")
    inRootNameList.sort()

    skipped = 0
    resubmitting = 0

    for inRootName in inRootNameList:

        idx = inRootName.split(".root")[0].split("Ntuple")[1].split("_")[1]
        SecondaryRootName = options.secondarydir + '/Ntuple_' + str(idx) + '.root'
        outJobName  = options.out + '/job_' + str(idx) + '.sh'
        outLogName  = options.out + '/log_' + str(idx) + '.txt'
        outRootName = options.out + '/Ntuple_' + str(idx) + '.root'

        # if the outRootName already exists there is no need of resubmitting
        # but files not correctly closed have to be resubmitted
        if os.path.isfile(outRootName):
            if len(os.popen('grep "Run 1, Event 2000," '+outLogName).read()) > 0:
                # print("Skipping "+outRootName)
                skipped = skipped + 1
                continue

        resubmitting = resubmitting + 1

        cmsRun = "cmsRun L1Ntuple_cfg.py inputFiles=file:"+inRootName+" outputFile=file:"+outRootName+" secondaryInputFiles=file:"+SecondaryRootName
        cmsRun = cmsRun+" maxEvents="+str(options.maxEvents)+" globalTag="+options.globalTag+" caloParams="+options.caloParams
        if options.reco:
            cmsRun = cmsRun + " reco=1"
        cmsRun = cmsRun+" >& "+outLogName

        skimjob = open (outJobName, 'w')
        skimjob.write ('#!/bin/bash\n')
        skimjob.write ('export X509_USER_PROXY=~/.t3/proxy.cert\n')
        skimjob.write ('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
        skimjob.write ('cd %s\n' %os.getcwd())
        skimjob.write ('export SCRAM_ARCH=slc6_amd64_gcc472\n')
        skimjob.write ('eval `scram r -sh`\n')
        skimjob.write ('cd %s\n' %os.getcwd())
        skimjob.write (cmsRun+'\n')
        skimjob.close ()

        os.system ('chmod u+rwx ' + outJobName)
        command = ('/home/llr/cms/evernazza/t3submit -'+options.queue+' \'' + outJobName +"\'")
        print(command)
        if not options.no_exec: os.system (command)

    print("skipped = ", skipped)
    print("resubmitting = ", resubmitting)
