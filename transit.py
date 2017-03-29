# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:20:47 2017

@author: 3670463
"""

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import animation 
from pylab import*
fig, ax = plt.subplots() 
fig.set_dpi(100) 
fig.set_size_inches(10, 10) 
ax=plt.axes(xlim=(-5, 5), ylim=(-4, 4))
plt.xlabel('distance en UA')
plt.ylabel('distance en UA')
title(u"observation d'une etoile evant laquelle passe une exoplanete", fontsize=10) 
patch = plt.Circle((0,3), 0.15, fc='b', label="Exoplanete") 

a= plt.Circle((0, 0), 2, fc='y', label="etoile")

R=4
#coordonnées du centre de l'orbite de l'exoplanete
xcoord=-3
ycoord=3
def init(): 
     patch.center = (-3, 3) 
     
     a.center = (0, 0)
     
    
     ax.add_patch(a) 
     ax.add_patch(patch)
     return a,patch, 

 
def animate(t): 
     x,y = patch.center 
     x = R* np.cos(np.radians(t))+xcoord
     y =-R* np.sin(np.radians(t)) +ycoord
     patch.center = (x,y) 
     
      
     return a,patch,
     
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=360,interval=20,blit=True)

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1, ncol=2, mode="expand", borderaxespad=0, handles=[a, patch]) 
plt.show()
