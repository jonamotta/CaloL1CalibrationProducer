import numpy as np

TowersEta = {
    1: [0,      0.087],
    2: [0.087,  0.174],
    3: [0.174,  0.261],
    4: [0.261,  0.348],
    5: [0.348,  0.435],
    6: [0.435,  0.522],
    7: [0.522,  0.609],
    8: [0.609,  0.696],
    9: [0.696,  0.783],
    10: [0.783,  0.870],
    11: [0.870, 0.957],
    12: [0.957, 1.044],
    13: [1.044, 1.131],
    14: [1.131, 1.218],
    15: [1.218, 1.305],
    16: [1.305, 1.392],
    17: [1.392, 1.479],
    18: [1.479, 1.566],
    19: [1.566, 1.653],
    20: [1.653, 1.740],
    21: [1.740, 1.830],
    22: [1.830, 1.930],
    23: [1.930, 2.043],
    24: [2.043, 2.172],
    25: [2.172, 2.322],
    26: [2.322, 2.5],
    27: [2.5,   2.650],
    28: [2.650, 3.],
    # 29: [2.83,  3.], Should not be considered. Summed with TT28, such that TT28 goes to |eta| = 3 and summed with TT30, such that TT30 starts at |eta| = 3
    30: [3., 3.139],
    31: [3.139, 3.314],
    32: [3.314, 3.489],
    33: [3.489, 3.664],
    34: [3.664, 3.839],
    35: [3.839, 4.013],
    36: [4.013, 4.191],
    37: [4.191, 4.363],
    38: [4.363, 4.538],
    39: [4.538, 4.716],
    40: [4.716, 4.889],
    41: [4.889, 5.191],
}

def FindIeta(jetEta):
    if jetEta == 0:
        return 1
    elif jetEta == 5.191:
        return 41
    else:
        jetEta_sign = np.sign(jetEta)
        jetEta_abs = np.abs(jetEta)
        IetaFound = False
        for key in TowersEta.keys():
            if IetaFound == False:
                if jetEta_abs > TowersEta[key][0] and jetEta_abs <= TowersEta[key][1]:
                    Ieta = key
                    IetaFound = True
        return int(jetEta_sign*Ieta)

######################################
############# Phi Towers #############
######################################

TowersPhi = {i+1 : [] for i in range(72)}
x = np.linspace(0, 2*np.pi, 73)
for i in range(72):
    TowersPhi[i+1].append(x[i])
    TowersPhi[i+1].append(x[i+1])

def ConvertPhi(jetPhi):
    if jetPhi > 0:
        return jetPhi
    else:
        return jetPhi + 2*np.pi

def FindIphi(jetPhi_off):
    jetPhi = ConvertPhi(jetPhi_off)
    if jetPhi == 0:
        return 1
    elif jetPhi == 2*np.pi:
        return 72
    else:
        IphiFound = False
        for key in TowersPhi.keys():
            if IphiFound == False:
                if jetPhi > TowersPhi[key][0] and jetPhi <= TowersPhi[key][1]:
                    Iphi = key
                    IphiFound = True
        return Iphi

############################################## Previous and next towers definition ##############################################

def NextPhiTower(iphi):
    if iphi in list(TowersPhi.keys()):
        IkeyFound = False
        Ikey = 0
        if iphi == 72:
            next_iphi = 1
        else:
            for i, key in enumerate(list(TowersPhi.keys())):
                if IkeyFound == False:
                    if iphi == key:
                        next_iphi = list(TowersPhi.keys())[i+1]
        return next_iphi
    else:
        print('{} not in range [1,72]'.format(iphi))

def NextEtaTower(ieta):
    if ieta == 41:
        return 41
    elif np.abs(ieta) in list(TowersEta.keys()):
        IkeyFound = False
        Ikey = 0
        next_ieta = 0
        if ieta == -1:
            next_ieta = 1
        elif ieta == 41:
            print('{} not in range [-41,41]'.format(ieta))
            return 0
        else:
            if ieta > 0:
                for i, key in enumerate(list(TowersEta.keys())):
                    if IkeyFound == False:
                        if np.abs(ieta) == key:
                            next_ieta = list(TowersEta.keys())[i+1]
            else:
                for i, key in enumerate(list(TowersEta.keys())):
                    if IkeyFound == False:
                        if np.abs(ieta) == key:
                            next_ieta = -1*list(TowersEta.keys())[i-1]
        return next_ieta
    else:
        print('{} not in range [-41,41]'.format(ieta))
        return 0
        
def PrevPhiTower(iphi):
    if iphi in list(TowersPhi.keys()):
        IkeyFound = False
        Ikey = 0
        if iphi == 1:
            next_iphi = 72
        else:
            for i, key in enumerate(list(TowersPhi.keys())):
                if IkeyFound == False:
                    if iphi == key:
                        next_iphi = list(TowersPhi.keys())[i-1]
        return next_iphi
    else:
        print('{} not in range [1,72]'.format(iphi))
        
def PrevEtaTower(ieta):
    if ieta == -41:
        return -41
    if np.abs(ieta) in list(TowersEta.keys()):
        IkeyFound = False
        Ikey = 0
        next_ieta = 0
        if ieta == 1:
            next_ieta = -1
        elif ieta == -41:
            print('{} not in range [-40,41]'.format(ieta))
        else:
            if ieta > 0:
                for i, key in enumerate(list(TowersEta.keys())):
                    if IkeyFound == False:
                        if np.abs(ieta) == key:
                            next_ieta = list(TowersEta.keys())[i-1]
            else:
                for i, key in enumerate(list(TowersEta.keys())):
                    if IkeyFound == False:
                        if np.abs(ieta) == key:
                            next_ieta = -1*list(TowersEta.keys())[i+1]
        return next_ieta
    else:
        print('{} not in range [-40,41]'.format(ieta))