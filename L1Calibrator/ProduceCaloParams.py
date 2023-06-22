import os,sys

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

'''
python3 ProduceCaloParams.py --name caloParams_2023_v51B_newCalib_cfi \
    --HCAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
    --HF /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HF_energystep2iEt.csv \
    --HCAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco_A/ScaleFactors_HCAL_energystep2iEt.csv \
'''

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--name",      dest="name",       default='caloParams_2023_vX_newCalib_cfi')
parser.add_option("--base",      dest="base",       default='caloParams_2023_v0_2_noL1Calib_cfi.py')
parser.add_option("--ECAL",      dest="ECAL",       default=None)
parser.add_option("--HCAL",      dest="HCAL",       default=None)
parser.add_option("--HF",        dest="HF",         default=None)
(options, args) = parser.parse_args()

# prepare caloParams file
base_dir = os.getcwd().split('/L1Calibrator')[0] + '/caloParams/'

base_file = base_dir + options.base
new_file = base_dir + options.name + '.py'

print('\n### INFO: Producing new calo params file : {}'.format(new_file))
print('### INFO: Reference calo params file : {}\n'.format(base_file))

if os.path.exists(new_file):
    print("This file already exists: {}".format(new_file))
    write = input("Do you want to over-write it? (y/n)\n")
    if write != 'y':
        sys.exit()

print('### INFO: Adding first part')
f_base = open(base_file)
Old_Lines = f_base.readlines()
New_Lines = []

start_ECAL = [index for index, value in enumerate(Old_Lines) if 'layer1ECalScaleFactors = cms.vdouble([' in value][0]+1
start_HCAL = [index for index, value in enumerate(Old_Lines) if 'layer1HCalScaleFactors = cms.vdouble([' in value][0]+1
start_HF   = [index for index, value in enumerate(Old_Lines) if 'layer1HFScaleFactors = cms.vdouble([' in value][0]+1
end_ECAL = [index for index, value in enumerate(Old_Lines) if '    ]),' in value][0]
end_HCAL = [index for index, value in enumerate(Old_Lines) if '    ]),' in value][1]
end_HF   = [index for index, value in enumerate(Old_Lines) if '    ]),' in value][2]

for line in Old_Lines[:start_ECAL]:
    New_Lines.append(line)

print('### INFO: Adding ECAL')
if options.ECAL:
    f_ECAL = options.ECAL
    with open(f_ECAL) as f:
        for line in f.readlines():
            if '#' in line: continue
            New_Lines.append('        ' + line)
else:
    for line in Old_Lines[start_ECAL:end_ECAL]:
        New_Lines.append(line)

for line in Old_Lines[end_ECAL:start_HCAL]:
    New_Lines.append(line)

print('### INFO: Adding ECAL')
if options.HCAL:
    f_HCAL = options.HCAL
    with open(f_HCAL) as f:
        for line in f.readlines():
            if '#' in line: continue
            New_Lines.append('        ' + line)
else:
    for line in Old_Lines[start_HCAL:end_HCAL]:
        New_Lines.append(line)

for line in Old_Lines[end_HCAL:start_HF]:
    New_Lines.append(line)

print('### INFO: Adding HF')
if options.HF:
    f_HF = options.HF
    with open(f_HF) as f:
        for line in f.readlines():
            if '#' in line: continue
            New_Lines.append('        ' + line)
else:
    for line in Old_Lines[start_HF:end_HF]:
        New_Lines.append(line)

for line in Old_Lines[end_HF:]:
    New_Lines.append(line)

print('### INFO: Writing')
with open(new_file, 'w') as file:
    for line in New_Lines:
        file.write(line)

cmd = 'cp '+new_file+' ../../L1Trigger/L1TCalorimeter/python/'
print('cp '+new_file+' ../../L1Trigger/L1TCalorimeter/python/')
os.system(cmd)
print('### INFO: DONE!')