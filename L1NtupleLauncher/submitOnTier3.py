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
    parser.add_option("--inFileList", dest="inFileList", type=str,            default=None,   help="Input list of files to process (should include the subfolder inside .../EgTauTagAndProbe/EgTauTagAndProbe/inputFiles)")
    parser.add_option("--outTag",     dest="outTag",     type=str,            default=None,   help="Tag for the output folder name")
    parser.add_option("--nJobs",      dest="nJobs",      type=int,            default=None,   help="Number of jobs to run per filelist")
    parser.add_option("--queue",      dest="queue",      type=str,            default='long', help="long or short queue")
    parser.add_option("--no_exec",    dest="no_exec",    action='store_true', default=False)
    parser.add_option("--resubmit",   dest="resubmit",   action='store_true', default=False)

    parser.add_option("--maxEvts",      dest="maxEvts",      type=str,            default='-1',   help="Number of events to process")
    parser.add_option("--inJson",       dest="inJson",       type=str,            default=None,   help="Input list of data certification Json files")
    parser.add_option("--caloParams",   dest="caloParams",   type=str,            default=None,   help="Which caloParams to use")
    parser.add_option("--noL1calib",    dest="noL1calib",    action='store_true', default=False,  help="Turn off Layer1 calibration")
    parser.add_option("--globalTag",    dest="globalTag",    type=str,            default=None,   help="Which globalTag to use")
    parser.add_option("--data",         dest="data",         action='store_true', default=False,  help="Running on data?")
    parser.add_option("--recoFromSKIM", dest="recoFromSKIM", action='store_true', default=False,  help="Run reco from pre-skimmed dataset?")
    parser.add_option("--recoFromAOD",  dest="recoFromAOD",  action='store_true', default=False,  help="Run reco from primary AOD file?")

    (options, args) = parser.parse_args()
    
    if not options.outTag:
        print('** WARNING: outTag not specified, will default to date and time. Please consider specifying a meaningfull tag, e.g. GT130XdataRun3Promptv10_CPv28newCalib_data_reco_json')

    currentdir = os.getcwd()
    filelist = open(currentdir + '/inputFiles/'+options.inFileList+'.txt', 'r')
    folder = '/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/'+options.inFileList+'__'+options.outTag
    if options.inJson: JSONfile = currentdir+'/DataCertificationJsons/'+options.inJson+'.json'

    ###########

    os.system('export SITECONFIG_PATH=/cvmfs/cms.cern.ch/SITECONF/T2_FR_GRIF_LLR/GRIF-LLR')
    os.system('source /opt/exp_soft/cms/t3/t3setup')

    os.system('mkdir -p ' + folder)
    os.system('cp listAll.sh /data_CMS/cms/motta/CaloL1calibraton/L1NTuples')
    files = [f.strip() for f in filelist]
    print "Input has" , len(files) , "files" 
    if options.nJobs > len(files) : options.nJobs = len(files)
    filelist.close()

    fileblocks = splitInBlocks (files, options.nJobs)

    resubmit = 0

    for idx, block in enumerate(fileblocks):
        #print idx, block

        outRootName = folder + '/Ntuple_' + str(idx) + '.root'
        outJobName  = folder + '/job_' + str(idx) + '.sh'
        outListName = folder + "/filelist_" + str(idx) + ".txt"
        outLogName  = folder + "/log_" + str(idx) + ".txt"

        if options.resubmit:
            if (len(os.popen('grep "Failed to open the file" '+outLogName).read()) == 0) or (len(os.popen('grep "Begin processing the 2nd record." '+outLogName).read()) > 0) :
                continue
            resubmit = resubmit + 1

        jobfilelist = open(outListName, 'w')
        for f in block: jobfilelist.write(f+"\n")
        jobfilelist.close()

        if options.recoFromAOD:
            outSecondaryListName = folder + "/secondaryFilelist_" + str(idx) + ".txt"
            jobsecondaryfilelist = open(outSecondaryListName, 'w')
            jobsecondaryfilelist.close()
            for f in block:
                os.system('dasgoclient --query="parent file='+f+'" >> '+outSecondaryListName)

        cmsRun = "cmsRun L1Ntuple_cfg.py maxEvents="+options.maxEvts+" inputFiles_load="+outListName+" outputFile="+outRootName+" caloParams="+options.caloParams+" globalTag="+options.globalTag
        if options.recoFromAOD:  cmsRun += " reco=1 secondaryInputFiles_load="+outSecondaryListName
        if options.recoFromSKIM: cmsRun += " reco=1"
        if options.data:         cmsRun += " data=1"
        if options.inJson:       cmsRun += " JSONfile="+JSONfile
        if options.noL1calib:    cmsRun += " noL1calib=1"
        cmsRun += " >& " + outLogName

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
        command = ('/data_CMS/cms/motta/CaloL1calibraton/t3submit -'+options.queue+' \'' + outJobName +"\'")
        print command
        if not options.no_exec: os.system (command)
        # break
        # if idx == 2: break

    print("resubmit = ", resubmit)
