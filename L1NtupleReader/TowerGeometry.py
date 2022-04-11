import os
import sys
import glob
import numpy as np
import uproot3
import pandas as pd
import argparse

# FIXME - THIS NEEDS TO BE CHECKED!!!
# len(TowersEta) = 41, from 1 to 41 BUT TO BE CHECKED BECAUSE OF TOWER 29
TowersEta = np.array([0, 0.087, 0.174, 0.261, 0.348, 0.435, 0.522, 0.609, 0.696, 0.783, 0.870, 
                      0.957, 1.044, 1.131, 1.218, 1.305, 1.392, 1.479, 1.566, 1.653, 1.740, 1.830,
                      1.930, 2.043, 2.172, 2.322, 2.5, 2.650, 2.853, 3.139, 3.314, 3.489, 3.664,
                      3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889, 5.191])

# FIXME - THIS NEEDS TO BE CHECKED!!!
# len(TowersPhi) = 72, from 1 to 72
TowersPhi = np.linspace(0, 2*np.pi, 73)
# TowersPhi = np.array([0. , 0.04424778, 0.08849557, 0.13274335, 0.17699114, 0.22123892, 0.2654867 , 0.30973449, 0.35398227, 0.39823005,
#                       0.44247784, 0.48672562, 0.53097341, 0.57522119, 0.61946897, 0.66371676, 0.70796454, 0.75221233, 0.79646011, 0.84070789,
#                       0.88495568, 0.92920346, 0.97345124, 1.01769903, 1.06194681, 1.1061946 , 1.15044238, 1.19469016, 1.23893795, 1.28318573,
#                       1.32743352, 1.3716813 , 1.41592908, 1.46017687, 1.50442465, 1.54867243, 1.59292022, 1.637168  , 1.68141579, 1.72566357,
#                       1.76991135, 1.81415914, 1.85840692, 1.90265471, 1.94690249, 1.99115027, 2.03539806, 2.07964584, 2.12389362, 2.16814141,
#                       2.21238919, 2.25663698, 2.30088476, 2.34513254, 2.38938033, 2.43362811, 2.4778759 , 2.52212368, 2.56637146, 2.61061925,
#                       2.65486703, 2.69911482, 2.7433626 , 2.78761038, 2.83185817, 2.87610595, 2.92035373, 2.96460152, 3.0088493 , 3.05309709,
#                       3.09734487, 3.14159265])

def FindIeta(jetEta):
    jetEta_sign = np.sign(jetEta)
    jetEta_abs = np.abs(jetEta)
    IetaFound = False
    
    i = 1
    while IetaFound == False and i != len(TowersEta):
        if jetEta_abs >= TowersEta[i-1] and jetEta_abs < TowersEta[i]:
            Ieta = i
            IetaFound = True
        else:
            i = i+1
            Ieta = 41

    # FIXME - THIS NEEDS TO BE CHECKED!!!
    # splitting if tower 29 in half -> to be uncommented whe we are sure about the eta values of the towers
    if Ieta == 29:
        if jetEta_abs >= (TowersEta[28]-TowersEta[29])/2: Ieta = 28
        else:                                             Ieta = 30

    return jetEta_sign*Ieta


def FindIphi(jetPhi):
    IphiFound = False
    i = 1
    while IphiFound == False and i != len(TowersPhi):
        if jetPhi >= TowersPhi[i-1] and jetPhi < TowersPhi[i]:
            Iphi = i
            IphiFound = True
        else:
            i = i+1
            Iphi = 72
    return abs(Iphi)
