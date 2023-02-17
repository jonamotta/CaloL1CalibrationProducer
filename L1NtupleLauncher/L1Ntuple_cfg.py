import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.PythonUtilities.LumiList as LumiList

from Configuration.Eras.Era_Run3_cff import Run3

options = VarParsing.VarParsing ('analysis')
options.outputFile = 'L1Ntuple.root'
options.inputFiles = []
options.secondaryInputFiles = []
options.maxEvents  = -999
options.register ('JSONfile',
                  "", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,         # string, int, or float
                  "JSON file (empty for no JSON)")
options.register ('caloParams',
                  "", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,         # string, int, or float
                  "which caloParams to use?")
options.register ('globalTag',
                  "", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,         # string, int, or float
                  "which globalTag to use?")
options.register ('data',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,            # string, int, or float
                  "running on data?")
options.register ('reco',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,            # string, int, or float
                  "running also reco?")
options.parseArguments()


process = cms.Process('RAW2DIGI',Run3)
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
if options.data: process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
else:            process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    #output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

if options.maxEvents >= 1:
    process.maxEvents.input = cms.untracked.int32(options.maxEvents)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
    secondaryFileNames = cms.untracked.vstring()
    # eventsToProcess = cms.untracked.VEventRange("1:224001-1:224020"),
    # eventsToSkip = cms.untracked.VEventRange('1:224002-1:224019', '1:224021-1:max')
)

if options.inputFiles:
    process.source.fileNames = cms.untracked.vstring(options.inputFiles)

if options.secondaryInputFiles:
    process.source.secondaryFileNames = cms.untracked.vstring(options.secondaryInputFiles)

if options.JSONfile:
    process.source.lumisToProcess = LumiList.LumiList(filename = options.JSONfile).getVLuminosityBlockRange()

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
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
    wantSummary = cms.untracked.bool(False),
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
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

if options.data:
    # Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
    from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAWsimHcalTP 
    process = L1TReEmulFromRAWsimHcalTP(process)

    if options.reco:
        # Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
        from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleAODRAWEMU 
        process = L1NtupleAODRAWEMU(process)
    else:
        # Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
        from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 
        process = L1NtupleRAWEMU(process)

else:
    # Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
    from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAWSimHcalTP 
    process = L1TReEmulMCFromRAWSimHcalTP(process)

    if options.reco:
        # Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
        from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleAODRAWEMUGEN_MC 
        process = L1NtupleAODRAWEMUGEN_MC(process)
    else:
        # Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
        from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMUGEN_MC
        process = L1NtupleRAWEMUGEN_MC(process)

process.load("L1Trigger.L1TCalorimeter."+options.caloParams)

# End of customisation functions

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
