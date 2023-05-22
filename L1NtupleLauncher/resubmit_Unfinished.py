import os, sys, glob
from tqdm import tqdm

indir = sys.argv[1]
# indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/JetMET__Run2022G_Early-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json"
# indir = "/data_CMS/cms/motta/CaloL1calibraton/L1NTuples/Muon__Run2022G-PromptReco-v1__AOD__GT130XdataRun3Promptv3_CaloParams2023v02_noL1Calib_data_reco_json"

print("\n ### INFO : Reading from {}".format(indir))

LogFiles = glob.glob(indir+'/log*.txt')

print( "\n ### INFO : Looping on log files to find the good ones")
good_log = []
empty_log = []
resubmit_log = []
bad_log = []
for LogFile in tqdm(LogFiles):
    ans1 = os.popen("tail -n 1 {}".format(LogFile)).read()
    # print(ans1)
    if "Closed file root:" in ans1:
        if len(os.popen("grep -l 'Begin processing the 2nd record.' {}".format(LogFile)).read()):
            number = LogFile.split("/log_")[1].split(".txt")[0]
            good_log.append(number)
        else:
            number = LogFile.split("/log_")[1].split(".txt")[0]
            empty_log.append(number)
    else:
        if len(os.popen("grep -l 'Begin processing the 2nd record.' {}".format(LogFile)).read()):
            number = LogFile.split("/log_")[1].split(".txt")[0]
            resubmit_log.append(number)
        else:
            number = LogFile.split("/log_")[1].split(".txt")[0]
            bad_log.append(number)

print("\n ### INFO : Number of total files = {}".format(len(LogFiles)))
print(" ### INFO : Number of bad files = {}".format(len(bad_log)))
print(" ### INFO : Number of empty files = {}".format(len(empty_log)))
print(" ### INFO : Number of files to resubmit = {}".format(len(resubmit_log)))
print(" ### INFO : Number of good files = {}".format(len(good_log)))
print(good_log)


print("\n ### INFO : Looping on log files to find the bad ones")
do_resubmit = input(" ### Do you want to resubmit the unfinished files? [y/n]\n")

if do_resubmit == "y":
    #     os.system("voms")
    for LogFile in LogFiles:
        ans1 = os.popen("tail -n 1 {}".format(LogFile)).read()
        if "Closed file root:" in ans1:
            continue
        else:
            if len(os.popen("grep -l 'Begin processing the 2nd record.' {}".format(LogFile)).read()):
                number = LogFile.split("/log_")[1].split(".txt")[0]
                job = LogFile.split("/log_")[0] + "/job_" + number + ".sh"
                if do_resubmit == "y":
                    command = ('/data_CMS/cms/motta/CaloL1calibraton/t3submit -long \'' + job +"\'")
                    print(command)
                    os.system(command)
                else:
                    print(job)
