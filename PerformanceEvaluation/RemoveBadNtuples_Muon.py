import glob, os, sys

# indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_noL1Calib_data_reco_json" # 13
# indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06_data_reco_json" #12
# indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT124XdataRun3Promptv10_CaloParams2022v06oldHcalL1Calib_data_reco_json" #14
# indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW__GT124XdataRun3Promptv10_CaloParams2022v06_data"
indir = sys.argv[1]
gooddir = indir + "/GoodNtuples"
os.system('mkdir -p ' + gooddir)
doMove = True

logs = glob.glob(indir+'/log*.txt')
good = 0
tot = 0
for log in logs:
    tot = tot + 1
    begin = len(os.popen('grep "Begin processing the 2nd record." '+log).read()) > 0
    end = len(os.popen('grep "Closed file" '+log).read()) > 0
    gooddata = begin and end
    if gooddata:
        # print(log,'is good')
        idx = log.split('/log_')[1].split('.txt')[0]
        ntuple = log.split('/log_')[0] + '/Ntuple_' + idx + '.root'
        filelist = log.split('/log_')[0] + '/filelist_' + idx + '.txt'
        # print(ntuple)
        # os.system('cat '+filelist)
        if doMove:
            cmd = 'mv ' + log.split('/log_')[0] + '/*' + idx + '* ' + gooddir
            print(cmd)
            os.system(cmd)
        good = good + 1

print('Number good = ',good)
print('Number tot = ', tot)
