import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('RAW2DIGI',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


options = VarParsing.VarParsing ('analysis')
options.outputFile = 'L1Ntuple.root'
options.inputFiles = []
options.maxEvents  = -999
options.parseArguments()


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    #output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

if options.maxEvents >= 1:
    process.maxEvents.input = cms.untracked.int32(options.maxEvents)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # dummy for creation
        '/store/mc/Run3Summer21DR/SinglePhoton_Pt-0To200-gun/GEN-SIM-DIGI-RAW/NoPUFEVT_120X_mcRun3_2021_realistic_v6-v2/30000/24ceed17-25ac-4fba-a275-0821ad765052.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

if options.inputFiles:
    process.source.fileNames = cms.untracked.vstring(options.inputFiles)


process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1Ntuple nevts:300'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '123X_mcRun3_2021_realistic_v11', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAWSimHcalTP 

#call to customisation function L1TReEmulMCFromRAWSimHcalTP imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulMCFromRAWSimHcalTP(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMUGEN_MC 

#call to customisation function L1NtupleRAWEMUGEN_MC imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMUGEN_MC(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2022_noL1calib 

#call to customisation function L1TSettingsToCaloParams_2022_noL1calib imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParams_2022_noL1calib(process)

# End of customisation functions

# Settings of the HCAL PFA1p
process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")

process.simHcalTriggerPrimitiveDigis.overrideDBweightsAndFilterHB = cms.bool(True)
process.simHcalTriggerPrimitiveDigis.overrideDBweightsAndFilterHE = cms.bool(True)

process.HcalTPGCoderULUT.overrideDBweightsAndFilterHB = cms.bool(True)
process.HcalTPGCoderULUT.overrideDBweightsAndFilterHE = cms.bool(True)

process.simHcalTriggerPrimitiveDigis.numberOfFilterPresamplesHBQIE11 = 1
process.simHcalTriggerPrimitiveDigis.numberOfFilterPresamplesHEQIE11 = 1
process.simHcalTriggerPrimitiveDigis.weightsQIE11 = {
    "ieta1" :  [-0.47, 1.0],
    "ieta2" :  [-0.47, 1.0],
    "ieta3" :  [-0.47, 1.0],
    "ieta4" :  [-0.47, 1.0],
    "ieta5" :  [-0.47, 1.0],
    "ieta6" :  [-0.47, 1.0],
    "ieta7" :  [-0.47, 1.0],
    "ieta8" :  [-0.47, 1.0],
    "ieta9" :  [-0.47, 1.0],
    "ieta10" : [-0.47, 1.0],
    "ieta11" : [-0.47, 1.0],
    "ieta12" : [-0.47, 1.0],
    "ieta13" : [-0.47, 1.0],
    "ieta14" : [-0.47, 1.0],
    "ieta15" : [-0.47, 1.0],
    "ieta16" : [-0.47, 1.0],
    "ieta17" : [-0.47, 1.0],
    "ieta18" : [-0.47, 1.0],
    "ieta19" : [-0.47, 1.0],
    "ieta20" : [-0.47, 1.0],
    "ieta21" : [-0.43, 1.0],
    "ieta22" : [-0.43, 1.0],
    "ieta23" : [-0.43, 1.0],
    "ieta24" : [-0.43, 1.0],
    "ieta25" : [-0.43, 1.0],
    "ieta26" : [-0.43, 1.0],
    "ieta27" : [-0.43, 1.0],
    "ieta28" : [-0.43, 1.0]
}

process.HcalTPGCoderULUT.contain1TSHB = True
process.HcalTPGCoderULUT.contain1TSHE = True
# End of HCAL PFA1p settings


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Adding ntuplizer
process.TFileService=cms.Service('TFileService',fileName=cms.string(options.outputFile))
