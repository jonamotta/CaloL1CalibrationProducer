import os
import json
from subprocess import Popen, PIPE

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

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--v", dest="v", default='gamma1')
(options, args) = parser.parse_args()

if options.v == 'gamma1':
    taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_gamma0-200.txt')
    filedir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_gamma0-200_batches/'
    folder = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_gamma0-200_batches/paddedAndReadyToMerge'

elif options.v == 'gamma2':
    taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_gamma200-500.txt')
    filedir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_gamma200-500_batches/'
    folder = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_gamma200-500_batches/paddedAndReadyToMerge'

elif options.v == 'qcd':
    taglist = open('/home/llr/cms/motta/Run3preparation/CaloL1calibraton/CMSSW_12_3_0_pre6/src/L1CalibrationProducer/L1NtupleReader/inputBatches/taglist_qcdNoPU.txt')
    filedir = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_qcdNoPU_batches/'
    folder = '/data_CMS/cms/motta/CaloL1calibraton/2022_04_02_NtuplesV0/hdf5dataframes_qcdNoPU_batches/paddedAndReadyToMerge'

else:
    print(' ** WARNING: wrong request --> EXITING!')
    exit()

###########

os.system ('source /opt/exp_soft/cms/t3/t3setup')

os.system('mkdir -p ' + folder + '/dataframes ; mkdir -p ' + folder + '/tensors')
tags = [tag.strip() for tag in taglist]
njobs = len(tags)
print("Input has" , len(tags) , "files", "-->", len(tags), "jobs")
taglist.close()

for idx, tag in enumerate(tags):
    #print(idx, tag)

    outJobName  = folder + '/job_' + str(idx) + '.sh'
    outLogName  = folder + "/log_" + str(idx) + ".txt"

    cmsRun = "python batchReader.py --fin "+filedir+" --tag "+tag+" --fout "+folder+" >& "+outLogName
    
    skimjob = open (outJobName, 'w')
    skimjob.write ('#!/bin/bash\n')
    skimjob.write ('export X509_USER_PROXY=~/.t3/proxy.cert\n')
    skimjob.write ('module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7\n')
    skimjob.write ('module load python/3.7.0\n')
    skimjob.write ('cd %s\n'%os.getcwd())
    skimjob.write (cmsRun+'\n')
    skimjob.close ()

    os.system ('chmod u+rwx ' + outJobName)
    # command = ('/home/llr/cms/motta/t3submit -long \'' + outJobName +"\'")
    command = ('/home/llr/cms/motta/t3submit -short \'' + outJobName +"\'")
    print(command)
    os.system (command)
