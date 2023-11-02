import os,sys

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

'''
python3 ProduceCaloParams.py --name caloParams_2023_v51A_newCalib_cfi \
    --ECAL /data_CMS/cms/motta/CaloL1calibraton/2023_06_21_NtuplesV51/JetMET_PuppiJet_BarrelEndcap_Pt30_HoTot95/HCALtrainingDataReco/data_A/ScaleFactors_HCAL_energystep2iEt.csv \
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

start_ECAL = [index for index, value in enumerate(Old_Lines) if 'layer1ECalScaleETBins = cms.' in value][0]
start_HCAL = [index for index, value in enumerate(Old_Lines) if 'layer1HCalScaleETBins = cms.' in value][0]
start_HF   = [index for index, value in enumerate(Old_Lines) if 'layer1HFScaleETBins = cms.' in value][0]
end_ECAL = [index for index, value in enumerate(Old_Lines) if '    ]),' in value][0]
end_HCAL = [index for index, value in enumerate(Old_Lines) if '    ]),' in value][1]
end_HF   = [index for index, value in enumerate(Old_Lines) if '    ]),' in value][2]

for line in Old_Lines[:start_ECAL]:
    New_Lines.append(line)

print('### INFO: Adding ECAL')
if options.ECAL:
    New_Lines.append("    layer1ECalScaleETBins = cms.vint32([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 256]),\n")
    New_Lines.append("    layer1ECalScaleFactors = cms.vdouble([\n")
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
    New_Lines.append("    layer1HCalScaleETBins = cms.vint32([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 256]),\n")
    New_Lines.append("    layer1HCalScaleFactors = cms.vdouble([\n")
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
    New_Lines.append("    layer1HFScaleETBins = cms.vint32([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 256]),\n")
    New_Lines.append("    layer1HFScaleFactors = cms.vdouble([\n")
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