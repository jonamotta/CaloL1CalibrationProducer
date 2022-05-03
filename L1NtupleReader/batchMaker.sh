# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG0_200 --applyNewECALcalib
# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG0_200 --applyOldCalib
# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG0_200 --applyNoCalib


# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG200_500 --applyNewECALcalib
# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG200_500 --applyOldCalib
# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG200_500 --applyNoCalib


python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "50To80" --outdir 2022_05_02_NtuplesV8 --applyNewECALcalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "50To80" --outdir 2022_05_02_NtuplesV8 --applyOldCalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "50To80" --outdir 2022_05_02_NtuplesV8 --applyNoCalib


python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "80To120" --outdir 2022_05_02_NtuplesV8 --applyNewECALcalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "80To120" --outdir 2022_05_02_NtuplesV8 --applyOldCalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "80To120" --outdir 2022_05_02_NtuplesV8 --applyNoCalib


python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "120To170" --outdir 2022_05_02_NtuplesV8 --applyNewECALcalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "120To170" --outdir 2022_05_02_NtuplesV8 --applyOldCalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 2500 --doQCDnoPU --qcdPtBin "120To170" --outdir 2022_05_02_NtuplesV8 --applyNoCalib





