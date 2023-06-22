import json
import glob
import os

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
parser.add_option("--indir",              dest="indir",              default=None)
parser.add_option("--outdir",             dest="outdir",             default="")
parser.add_option("--addtag",             dest="addtag",             default="")
parser.add_option("--target",             dest="target",             default='')
parser.add_option("--type",               dest="type",               default='')
parser.add_option("--queue",              dest="queue",              default='long')
parser.add_option("--chunk_size",         dest="chunk_size",         default=5000,  type=int)
parser.add_option("--uJetPtCut",          dest="uJetPtCut",          default=False)
parser.add_option("--lJetPtCut",          dest="lJetPtCut",          default=False)
parser.add_option("--etacut",             dest="etacut",             default=False)
parser.add_option("--etacutmin",          dest="etacutmin",          default=False)
parser.add_option("--applyCut_3_6_9",     dest="applyCut_3_6_9",     default=False)
parser.add_option("--ecalcut",            dest="ecalcut",            default=False)
parser.add_option("--hcalcut",            dest="hcalcut",            default=False)
parser.add_option("--HoTotcut",           dest="HoTotcut",           default=False)
parser.add_option("--TTNumberCut",        dest="TTNumberCut",        default=False)
parser.add_option("--TTNumberCutInverse", dest="TTNumberCutInverse", default=False)
parser.add_option("--flatPtDist",         dest="flatPtDist",         default=False)
parser.add_option("--flatEtaDist",        dest="flatEtaDist",        default=False)
parser.add_option("--calibECALOnTheFly",  dest="calibECALOnTheFly",  default=False, help="oldCalib or currCalib; not specified == noCalib")
parser.add_option("--calibHCALOnTheFly",  dest="calibHCALOnTheFly",  default=False, help="oldCalib or currCalib; not specified == noCalib")
parser.add_option("--trainPtVers",        dest="trainPtVers",        default=False)
parser.add_option("--applyOnTheFly",      dest="applyOnTheFly",      default=False)
parser.add_option("--ClusterFilter",      dest="ClusterFilter",      default=False)
parser.add_option("--applyZS",            dest="applyZS",            default=False)
parser.add_option("--LooseEle",           dest="LooseEle",           default=False, action='store_true')
parser.add_option("--PuppiJet",           dest="PuppiJet",           default=False, action='store_true')
parser.add_option("--resubmit_failed",    dest="resubmit_failed",    default=False, action='store_true')
parser.add_option("--no_exec",            dest="no_exec",            default=False, action='store_true')
(options, args) = parser.parse_args()

if not options.indir or not options.outdir or not options.target or not options.type:
    print('** WARNING: need to specify all the following: indir, outdir, target, type')
    print('** EXITING')
    exit()

folder = options.outdir+'/'+options.indir.split('/')[-1]+options.addtag
os.system('mkdir -p '+folder+'/dataframes ; mkdir -p '+folder+'/tensors')

###########

#os.system ('source /opt/exp_soft/cms/t3/t3setup')

InFiles = glob.glob(options.indir+'/Ntuple*.root')
InFiles.sort()
print("Input has" , len(InFiles) , "files", "-->", len(InFiles), "jobs")

n_failed = 0
n_empty = 0

for file in InFiles:

    idx = file.split(".root")[0].split("/Ntuple")[1].split("_")[1]

    # skip the ntuple if it is empty
    ret = os.popen('du -sh '+options.indir+'/Ntuple_'+idx+'.root').read()
    if '4.0K' in ret:
        print("Empty")
        n_empty = n_empty + 1
        continue

    outJobName  = folder + '/job_' + str(idx) + '.sh'
    outLogName  = folder + "/log_" + str(idx) + ".txt"
    # print(outLogName)

    # [Elena] if the job has already finished we skip it
    if os.path.exists(outLogName):
        if len('grep "DONE" '+outLogName) > 0:
            continue
        else:
            print(outLogName)
    else:
        pass
        # print(outLogName)

    # only resubmit failed jobs
    # grep "ModuleNotFoundError: No module named 'uproot3'" log* -R | wc -l
    if options.resubmit_failed:
        if os.path.isfile(outLogName):
            if len(os.popen('grep "ModuleNotFoundError: No module named" '+outLogName).read()) > 0:
                print('Resubmit failed job due to uproot problem')
                n_failed = n_failed + 1
            else:
                continue

    # print(idx, file)

    cmsRun = "python3 batchReader.py --fin "+file+" --fout "+folder+" --target "+options.target+" --type "+options.type
    cmsRun = cmsRun + " --chunk_size "+str(options.chunk_size)
    if options.uJetPtCut != False:
        cmsRun = cmsRun + " --uJetPtCut "+options.uJetPtCut
    if options.lJetPtCut != False:
        cmsRun = cmsRun + " --lJetPtCut "+options.lJetPtCut
    if options.etacut != False:
        cmsRun = cmsRun + " --etacut "+options.etacut
    if options.etacutmin != False:
        cmsRun = cmsRun + " --etacutmin "+options.etacutmin
    if options.applyCut_3_6_9 != False:
        cmsRun = cmsRun + " --applyCut_3_6_9 "+options.applyCut_3_6_9
    if options.ecalcut != False:
        cmsRun = cmsRun + " --ecalcut "+options.ecalcut
    if options.hcalcut != False:
        cmsRun = cmsRun + " --hcalcut "+options.hcalcut
    if options.HoTotcut != False:
        cmsRun = cmsRun + " --HoTotcut "+options.HoTotcut
    if options.TTNumberCut != False:
        cmsRun = cmsRun + " --TTNumberCut "+options.TTNumberCut
    if options.TTNumberCutInverse != False:
        cmsRun = cmsRun + " --TTNumberCutInverse "+options.TTNumberCutInverse
    if options.trainPtVers != False:
        cmsRun = cmsRun + " --trainPtVers "+options.trainPtVers
    if options.calibECALOnTheFly != False:
        cmsRun = cmsRun + " --calibrateECAL "+options.calibECALOnTheFly
    if options.calibHCALOnTheFly != False:
        cmsRun = cmsRun + " --calibrateHCAL "+options.calibHCALOnTheFly
    if options.flatPtDist != False:
        cmsRun = cmsRun + " --flattenPtDistribution "+options.flatPtDist
    if options.flatEtaDist != False:
        cmsRun = cmsRun + " --flattenEtaDistribution "+options.flatEtaDist
    if options.applyOnTheFly != False:
        cmsRun = cmsRun + " --applyOnTheFly "+options.applyOnTheFly
    if options.ClusterFilter != False:
        cmsRun = cmsRun + " --ClusterFilter "+options.ClusterFilter
    if options.applyZS != False:
        cmsRun = cmsRun + " --applyZS "+options.applyZS
    if options.LooseEle != False:
        cmsRun = cmsRun + " --LooseEle"
    if options.PuppiJet != False:
        cmsRun = cmsRun + " --PuppiJet"

    cmsRun = cmsRun + " >& "+outLogName

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
    print(command)
    if options.no_exec == False:
        os.system (command)
    # break

print("n_empty = ", n_empty)
print("n_failed = ", n_failed)