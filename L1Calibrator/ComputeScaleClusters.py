import numpy as np
import random
import glob
import sys
import os
import ROOT

import matplotlib.pyplot as plt

# for ECAL
# python3 ComputeScaleClusters.py 
# --LogDir /data_CMS/cms/motta/CaloL1calibraton/2023_04_06_NtuplesV39/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data/ 
# --L1Dir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data/

# for HCAL
# python3 ComputeScaleClusters.py 
# --LogDir /data_CMS/cms/motta/CaloL1calibraton/2023_04_13_NtuplesV40/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data/ 
# --L1Dir /data_CMS/cms/motta/CaloL1calibraton/L1NTuples/EphemeralZeroBias__Run2022G-v1__Run362616__RAW__GT124XdataRun3v11_CaloParams2022v06_data/


##############################################################################
################################## MAIN BODY #################################
##############################################################################

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--LogDir",          dest="LogDir",          help="Input folder with log from the reader", default=None             )
parser.add_option("--L1Dir",           dest="L1Dir",           help="Input folder with L1Ntuples", default=None                       )
(options, args) = parser.parse_args()

indir = options.LogDir
n_clusters = 0
for log in glob.glob(indir + '/log*.txt'):
    line = os.popen('grep "Number of clusters =  " '+log).read()
    if len(line) > 0:
        n_clusters += int(line.split('\n')[0].split('Number of clusters =  ')[1])
print("Number of Total Clusters =", n_clusters)

l1folder = options.L1Dir
level1Tree = ROOT.TChain("l1UpgradeTree/L1UpgradeTree")
level1Tree.Add(l1folder+"/Ntuple*.root")
n_events = level1Tree.GetEntries()
print("Number of Total Events =", n_events)

print("scale_clusters15GeV = ", n_clusters/n_events)
