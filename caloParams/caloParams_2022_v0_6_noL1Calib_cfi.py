import FWCore.ParameterSet.Config as cms

from L1Trigger.L1TCalorimeter.caloParams_cfi import caloParamsSource
import L1Trigger.L1TCalorimeter.caloParams_cfi
caloStage2Params = L1Trigger.L1TCalorimeter.caloParams_cfi.caloParams.clone(

    # towers
    #towerLsbH        = 0.5
    #towerLsbE        = 0.5
    #towerLsbSum      = 0.5
    #towerNBitsH      = 8
    #towerNBitsE      = 8
    #towerNBitsSum    = 9
    #towerNBitsRatio  = 3
    #towerEncoding    = True

    # regions
    #regionLsb        = 0.5
    #regionPUSType    = "None"
    #regionPUSParams  = []

    # EG
    #egEtaCut                   = 28
    #egLsb                      = 0.5
    #egSeedThreshold            = 2.
    #egNeighbourThreshold       = 1.
    egHcalThreshold            = 0.,
    egTrimmingLUTFile          = "L1Trigger/L1TCalorimeter/data/egTrimmingLUT_10_v16.01.19.txt",
    #egMaxHcalEt                = 0.
    #egMaxPtHOverE              = 128.
    egHOverEcutBarrel          = 3,
    egHOverEcutEndcap          = 4,
    egBypassExtHOverE          = 0,
    egMaxHOverELUTFile         = "L1Trigger/L1TCalorimeter/data/HoverEIdentification_0.995_v15.12.23.txt",
    egCompressShapesLUTFile    = "L1Trigger/L1TCalorimeter/data/egCompressLUT_v4.txt",
    egShapeIdType              = "compressed",
    #egShapeIdVersion           = 0
    egShapeIdLUTFile           = "L1Trigger/L1TCalorimeter/data/shapeIdentification_adapt0.99_compressedieta_compressedE_compressedshape_v15.12.08.txt", #Not used any more in the current emulator version, merged with calibration LUT

    #egPUSType                  = "None"
    egIsolationType            = "compressed",
    # LUT = tight
    egIsoLUTFile               = "L1Trigger/L1TCalorimeter/data/eg_IsoLUT_tight_Opt_L281_7p5_0p9_30p0_12_Jul_2022.txt",
    # LUT 2 = loose
    egIsoLUTFile2              = "L1Trigger/L1TCalorimeter/data/eg_IsoLUT_loose_Opt_L137_5p0_0p9_30p0_12_Jul_2022.txt",

    #egIsoAreaNrTowersEta       = 2
    #egIsoAreaNrTowersPhi       = 4
    egIsoVetoNrTowersPhi       = 2,
    #egIsoPUEstTowerGranularity = cms.uint32(1)
    #egIsoMaxEtaAbsForTowerSum  = cms.uint32(4)
    #egIsoMaxEtaAbsForIsoSum    = cms.uint32(27)
    egPUSParams                = cms.vdouble(1,4,32), #Isolation window in firmware goes up to abs(ieta)=32 for now
    egCalibrationType          = "compressed",
    egCalibrationVersion       = 0,
    egCalibrationLUTFile       = "L1Trigger/L1TCalorimeter/data/egRecalibratedLUTv1_2022_v0_2.txt",

    # Tau
    #tauLsb                     = 0.5
    isoTauEtaMax               = 25,
    tauSeedThreshold           = 0.,
    #tauNeighbourThreshold      = 0.
    #tauIsoAreaNrTowersEta      = 2
    #tauIsoAreaNrTowersPhi      = 4
    #tauIsoVetoNrTowersPhi      = 2
    #tauPUSType                 = "None"
    tauIsoLUTFile              = "L1Trigger/L1TCalorimeter/data/Tau_Iso_LUT_2022_calibThr1p7_rate14kHz_V11gs_effMin0p9_G3.txt",
    tauIsoLUTFile2             = "L1Trigger/L1TCalorimeter/data/Tau_Iso_LUT_2022_calibThr1p7_rate14kHz_V11gs_effMin0p9_G3.txt",
    tauCalibrationLUTFile      = "L1Trigger/L1TCalorimeter/data/Tau_Cal_LUT_2022_calibThr1p7_V11.txt",
    tauCompressLUTFile         = "L1Trigger/L1TCalorimeter/data/tauCompressAllLUT_12bit_v3.txt",
    tauPUSParams               = [1,4,32],

    # jets
    #jetLsb                    = 0.5
    jetSeedThreshold           = 4.0,
    #jetNeighbourThreshold = 0.
    jetPUSType                 = "ChunkyDonut",
    #jetBypassPUS          = 0

    # Calibration options
    jetCalibrationType         = "LUT",
    jetCompressPtLUTFile       = "L1Trigger/L1TCalorimeter/data/lut_pt_compress_2017v1.txt",
    jetCompressEtaLUTFile      = "L1Trigger/L1TCalorimeter/data/lut_eta_compress_2017v1.txt",
    jetCalibrationLUTFile      = "L1Trigger/L1TCalorimeter/data/lut_calib_2022v5_ECALZS_noHFJEC.txt",


    # sums: 0=ET, 1=HT, 2=MET, 3=MHT
    #etSumLsb                = 0.5
    etSumEtaMin             = [1, 1, 1, 1, 1],
    etSumEtaMax             = [28,  26, 28,  26, 28],
    etSumEtThreshold        = [0.,  30.,  0.,  30., 0.], # only 2nd (HT) and 4th (MHT) values applied
    etSumMetPUSType         = "LUT", # et threshold from this LUT supercedes et threshold in line above
    #etSumEttPUSType         = "None"
    #etSumEcalSumPUSType     = "None"
    #etSumBypassMetPUS       = 0
    etSumBypassEttPUS       = 1,
    etSumBypassEcalSumPUS   = 1,
    #etSumXCalibrationType   = "None"
    #etSumYCalibrationType   = "None"
    #etSumEttCalibrationType = "None"
    #etSumEcalSumCalibrationType = "None"

    etSumMetPUSLUTFile               = "L1Trigger/L1TCalorimeter/data/metPumLUT_2022_HCALOff_p5.txt",
    #etSumEttPUSLUTFile               = "L1Trigger/L1TCalorimeter/data/lut_towEtThresh_dummy.txt"
    #etSumEcalSumPUSLUTFile           = "L1Trigger/L1TCalorimeter/data/lut_towEtThresh_dummy.txt"
    #etSumXCalibrationLUTFile         = "L1Trigger/L1TCalorimeter/data/lut_etSumPUS_dummy.txt"
    #etSumYCalibrationLUTFile         = "L1Trigger/L1TCalorimeter/data/lut_etSumPUS_dummy.txt"
    #etSumEttCalibrationLUTFile       = "L1Trigger/L1TCalorimeter/data/lut_etSumPUS_dummy.txt"
    #etSumEcalSumCalibrationLUTFile   = "L1Trigger/L1TCalorimeter/data/lut_etSumPUS_dummy.txt"


    # Layer 1 SF
    # layer1ECalScaleETBins = cms.vint32([3, 6, 9, 12, 15, 20, 25, 30, 35, 40, 45, 55, 70, 256]),
    layer1ECalScaleETBins = cms.vint32([6, 12, 18, 24, 30, 40, 50, 60, 70, 80, 90, 110, 140, 256]), # DOUBLE BIN EDGES VALUE TO KEEP THE SAME BEHAVIOUR AS NOW
    layer1ECalScaleFactors = cms.vdouble([
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.
    ]),

    # layer1HCalScaleETBins = cms.vint32([6, 9, 12, 15, 20, 25, 30, 35, 40, 45, 55, 70, 256]),
    layer1HCalScaleETBins = cms.vint32([2, 12, 18, 24, 30, 40, 50, 60, 70, 80, 90, 110, 140, 256]), # THE FIRST BIN WILL BE ZERO-SUPPRESSING <1.0GeV, THE REST IS KEPT AS NOW
    layer1HCalScaleFactors = cms.vdouble([
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.
    ]),

    # layer1HFScaleETBins = cms.vint32([6, 9, 12, 15, 20, 25, 30, 35, 40, 45, 55, 70, 256]),
    layer1HFScaleETBins = cms.vint32([12, 18, 24, 30, 40, 50, 60, 70, 80, 90, 110, 140, 256]), # DOUBLE BIN EDGES VALUE TO KEEP THE SAME BEHAVIOUR AS NOW
    layer1HFScaleFactors = cms.vdouble([
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.
    ])
)

