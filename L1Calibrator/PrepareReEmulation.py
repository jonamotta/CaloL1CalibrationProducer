import os,sys

#######################################################################
######################### SCRIPT BODY #################################
#######################################################################

# python3 PrepareReEmulation.py --indir 2023_04_13_NtuplesV40 --v HCAL --tag MCReco --addtag C3

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--indir",     dest="indir",                                                default=None)
parser.add_option("--v",         dest="v",                                                    default='')
parser.add_option("--tag",       dest="tag",                                                  default='')
parser.add_option("--addtag",    dest="addtag",                                               default='')
parser.add_option("--calo",      dest="calo",                                                 default='')
parser.add_option("--applyECAL", dest="applyECAL",    help="Apply ECAL calibration",          default='True')
parser.add_option("--applyHCAL", dest="applyHCAL",    help="Apply HCAL calibration",          default='True')
parser.add_option("--filesLim",  dest="filesLim",     help="Number of tensors for plotting",  default=None)
parser.add_option("--eventLim",  dest="eventLim",     help="Maximum number of events to use", default=None)
parser.add_option("--onlyRes",   dest="onlyRes",      help="Skip SFs if already existing",    default=False,   action='store_true')
parser.add_option("--modelRate", dest="modelRate",    help="Model structure with rate",       default=False,   action='store_true')

(options, args) = parser.parse_args()

if not options.onlyRes:
    # # produce SFs for plotting
    # cmd_1 = 'python3 CalibrationFactor.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag + ' --reg ' + options.v
    # if options.addtag: cmd_1 = cmd_1 + ' --addtag ' + options.addtag
    # print('\n-------- RUNNING:', cmd_1)
    # os.system(cmd_1)
    # if options.v == 'HCAL':
    #     cmd_1 = 'python3 CalibrationFactor.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag + ' --reg HF'
    #     if options.addtag: cmd_1 = cmd_1 + ' --addtag ' + options.addtag
    #     print('\n-------- RUNNING:', cmd_1)
    #     os.system(cmd_1)

    # produce SFs for caloParams
    cmd_2 = 'python3 CalibrationFactor.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag + ' --reg ' + options.v + ' --energystep 2'
    if options.addtag: cmd_2 = cmd_2 + ' --addtag ' + options.addtag 
    print('\n-------- RUNNING:', cmd_2)
    os.system(cmd_2)
    if options.v == 'HCAL':
        cmd_2 = 'python3 CalibrationFactor.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag + ' --reg HF --energystep 2'
        if options.addtag: cmd_2 = cmd_2 + ' --addtag ' + options.addtag
        print('\n-------- RUNNING:', cmd_2)
        os.system(cmd_2)

    # # plot SFs energy step 1
    # cmd_3 = 'python3 ModelPlots.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag
    # if options.addtag: cmd_3 = cmd_3 + ' --addtag ' + options.addtag
    # print('\n-------- RUNNING:', cmd_3)
    # os.system(cmd_3)

    # plot SFs energy step 2
    cmd_4 = 'python3 ModelPlots.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag + ' --energystep 2'
    if options.addtag: cmd_4 = cmd_4 + ' --addtag ' + options.addtag
    print('\n-------- RUNNING:', cmd_4)
    os.system(cmd_4)

# # plot Apllication of SFs to 9x9
# cmd_5 = 'python3 ApplicationPlots_TF.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag
# if options.v == 'ECAL':
#     # choose to apply or not HCAL SFs
#     cmd_5 = cmd_5 + ' --applyHCAL ' + options.applyHCAL
#     # use brand new SFs
#     SfFile_ECAL = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_ECAL_energystep1iEt.csv'
#     cmd_5 = cmd_5 + ' --ECALnewSF ' + SfFile_ECAL
# if options.v == 'HCAL':
#     # choose to apply or not ECAL SFs
#     cmd_5 = cmd_5 + ' --applyECAL ' + options.applyECAL
#     # use brand new SFs
#     SfFile_HCAL = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_HCAL_energystep1iEt.csv'
#     SfFile_HF = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_HF_energystep1iEt.csv'
#     cmd_5 = cmd_5 + ' --HCALnewSF ' + SfFile_HCAL + ' --HFnewSF ' + SfFile_HF
# if options.addtag:    cmd_5 = cmd_5 + ' --addtag ' + options.addtag
# if options.filesLim:  cmd_5 = cmd_5 + ' --filesLim ' + options.filesLim
# if options.eventLim:  cmd_5 = cmd_5 + ' --eventLim ' + options.eventLim
# if options.modelRate: cmd_5 = cmd_5 + ' --modelRate'
# print('\n-------- RUNNING:', cmd_5)
# os.system(cmd_5)

# plot Apllication of SFs to 9x9
cmd_6 = 'python3 ApplicationPlots_TF.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag
if options.v == 'ECAL':
    # choose to apply or not HCAL SFs
    # cmd_6 = cmd_6 + ' --applyHCAL ' + options.applyHCAL # there is a problem of the lost ieta information
    cmd_6 = cmd_6 + ' --applyHCAL False'
    # use brand new SFs
    SfFile_ECAL = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_ECAL_energystep2iEt.csv'
    cmd_6 = cmd_6 + ' --ECALnewSF ' + SfFile_ECAL
if options.v == 'HCAL':
    # choose to apply or not ECAL SFs
    # cmd_6 = cmd_6 + ' --applyECAL ' + options.applyECAL # there is a problem of the lost ieta information
    cmd_6 = cmd_6 + ' --applyECAL False'
    # use brand new SFs
    SfFile_HCAL = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_HCAL_energystep2iEt.csv'
    SfFile_HF = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_HF_energystep2iEt.csv'
    cmd_6 = cmd_6 + ' --HCALnewSF ' + SfFile_HCAL + ' --HFnewSF ' + SfFile_HF
if options.addtag:    cmd_6 = cmd_6 + ' --addtag ' + options.addtag
if options.filesLim:  cmd_6 = cmd_6 + ' --filesLim ' + options.filesLim
if options.eventLim:  cmd_6 = cmd_6 + ' --eventLim ' + options.eventLim
if options.modelRate: cmd_6 = cmd_6 + ' --modelRate'
print('\n-------- RUNNING:', cmd_6)
os.system(cmd_6)

# # plot Application of SFs to 9x9 in rate sample
# cmd_7 = 'python3 ApplicationPlotsRate_TF.py --indir ' + options.indir + ' --v ' + options.v + ' --tag ' + options.tag
# if options.v == 'ECAL':
#     # choose to apply or not HCAL SFs
#     # cmd_7 = cmd_7 + ' --applyHCAL ' + options.applyHCAL # there is a problem of the lost ieta information
#     cmd_7 = cmd_7 + ' --applyHCAL False'
#     # use brand new SFs
#     SfFile_ECAL = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_ECAL_energystep2iEt.csv'
#     cmd_7 = cmd_7 + ' --ECALnewSF ' + SfFile_ECAL
# if options.v == 'HCAL':
#     # choose to apply or not ECAL SFs
#     # cmd_7 = cmd_7 + ' --applyECAL ' + options.applyECAL # there is a problem of the lost ieta information
#     cmd_7 = cmd_7 + ' --applyECAL False'
#     # use brand new SFs
#     SfFile_HCAL = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_HCAL_energystep2iEt.csv'
#     SfFile_HF = '/data_CMS/cms/motta/CaloL1calibraton/' + options.indir + '/' + options.v + 'training' + options.tag + '/data' + options.addtag + '/ScaleFactors_HF_energystep2iEt.csv'
#     cmd_7 = cmd_7 + ' --HCALnewSF ' + SfFile_HCAL + ' --HFnewSF ' + SfFile_HF
# if options.addtag:    cmd_7 = cmd_7 + ' --addtag ' + options.addtag
# if options.filesLim:  cmd_7 = cmd_7 + ' --filesLim ' + options.filesLim
# if options.eventLim:  cmd_7 = cmd_7 + ' --eventLim ' + options.eventLim
# print('\n-------- RUNNING:', cmd_7)
# os.system(cmd_7)