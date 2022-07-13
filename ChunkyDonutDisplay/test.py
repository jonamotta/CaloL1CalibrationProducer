import matplotlib.pyplot as plt
from TowerGeometry import *
import numpy as np
from pylab import cm
import mplhep
plt.style.use(mplhep.style.CMS)

# returns an array with 81 entries, for each entry we have [eta,phi] number of the tower belonging to the chunky donut
def ChunkyDonutTowers(jetIeta, jetIphi):

    CD = []
    iphi_start = jetIphi
    # define the top position of the chunky donut
    for i in range(0,4):
        iphi_start = PrevPhiTower(iphi_start)
    
    if jetIeta < 0:
        ieta_start = jetIeta
        # define the top right position of the chunky donut
        for i in range(0,4):
            ieta_start = NextEtaTower(ieta_start)
        
        ieta = ieta_start
        iphi = iphi_start 

        for i in range(0,9): # scan eta direction towards left
            if i > 0:
                ieta = PrevEtaTower(ieta)
            iphi = iphi_start # for every row in eta we restart from the first iphi
            for j in range(0,9): # scan phi direction
                if j > 0:
                    iphi = NextPhiTower(iphi)
                CD.append([ieta,iphi])
    
    elif jetIeta > 0:
        ieta_start = jetIeta
        # define the top left position of the chunky donut
        for i in range(0,4):
            ieta_start = PrevEtaTower(ieta_start)

        ieta = ieta_start
        iphi = iphi_start

        for i in range(0,9): # scan eta direction towards right
            if i > 0:
                ieta = NextEtaTower(ieta)
            iphi = iphi_start # for every row in eta we restart from the first iphi
            for j in range(0,9): # scan phi direction
                if j > 0:
                    iphi = NextPhiTower(iphi)
                CD.append([ieta,iphi,0])
    return CD



import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

def colorbar_index(ncolors, cmap, label):
    cmap = cmap_discretize(cmap, ncolors)
    mappable = cm.ScalarMappable(cmap=cmap)
    mappable.set_array([])
    mappable.set_clim(-0.5, ncolors+0.5)
    colorbar = plt.colorbar(mappable, label=label)
    colorbar.set_ticks(np.linspace(0, ncolors, ncolors))
    colorbar.set_ticklabels(range(ncolors))

def cmap_discretize(cmap, N):
    """Return a discrete colormap from the continuous colormap cmap.

        cmap: colormap instance, eg. cm.jet. 
        N: number of colors.

    Example
        x = resize(arange(100), (5,100))
        djet = cmap_discretize(cm.jet, 5)
        imshow(x, cmap=djet)
    """

    if type(cmap) == str:
        cmap = plt.get_cmap(cmap)
    colors_i = np.concatenate((np.linspace(0, 1., N), (0.,0.,0.,0.)))
    colors_rgba = cmap(colors_i)
    indices = np.linspace(0, 1., N+1)
    cdict = {}
    for ki,key in enumerate(('red','green','blue')):
        cdict[key] = [ (indices[i], colors_rgba[i-1,ki], colors_rgba[i,ki])
                       for i in range(N+1) ]
    # Return colormap object.
    return mcolors.LinearSegmentedColormap(cmap.name + "_%d"%N, cdict, 1024)



skeleton = np.asarray(ChunkyDonutTowers(13,30))
skeleton[39,2] = 1 ; skeleton[40,2] = 3 ; skeleton[41,2] = 1
skeletonE = skeleton[:,2].reshape(9,9)


pt = 6
eta = 1.35
phi = 2.9


HADcmap = cm.get_cmap('Reds')

plt.figure(figsize=(10,8))
fig, ax = plt.subplots()
im = ax.pcolormesh(skeletonE, cmap=HADcmap, edgecolor='black', vmin=0)

# ax.figure.colorbar(im, ax=ax, label='ihad')
colorbar_index(ncolors=4, cmap=HADcmap, label='ihad')  

plt.xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5], np.unique(skeleton[:,0]))
plt.yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5], np.unique(skeleton[:,1]))
plt.xlabel(f'$i\eta$')
plt.ylabel(f'$i\phi$')
props = dict(boxstyle='square', facecolor='white')
textstr = '\n'.join((
    r'$p_T^{9\times9}=%.0f$' % (pt*2, ),
    r'$p_T^{Gen}=%.2f$ GeV' % (pt, ),
    r'$\eta^{Gen}=%.2f$' % (eta, ),
    r'$\phi^{Gen}=%.2f$' % (phi, )))
ax.text(0.05, 0.96, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top',  bbox=props)
mplhep.cms.label('', data=False, rlabel='(14 TeV)')
plt.savefig('test.pdf')
plt.close()
