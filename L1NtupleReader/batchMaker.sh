# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG0_200 --applyNewECALcalib
# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG0_200 --applyOldCalib
# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG0_200 --applyNoCalib


# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG200_500 --applyNewECALcalib
# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG200_500 --applyOldCalib
# python batchMaker.py --v ECAL --applyHCALpfa1p --chunk_size 5000 --doEG200_500 --applyNoCalib


python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "50To80" --applyNewECALcalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "50To80" --applyOldCalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "50To80" --applyNoCalib


python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "80To120" --applyNewECALcalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "80To120" --applyOldCalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "80To120" --applyNoCalib


python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "120To170" --applyNewECALcalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "120To170" --applyOldCalib
python batchMaker.py --v HCAL --applyHCALpfa1p --chunk_size 250 --doQCDnoPU --qcdPtBin "120To170" --applyNoCalib





