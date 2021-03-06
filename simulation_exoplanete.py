# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:43:22 2017

@author: 3670463
"""

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import animation 
from pylab import*
fig= plt.figure() 
fig.set_dpi(100) 
fig.set_size_inches(100, 100) 
ax=plt.axes(xlim=(-0.08, 0.08), ylim=(-0.08, 0.08))
plt.xlabel('distance en UA')
plt.ylabel('distance en UA')

patch = plt.Circle((5,-5), 0.005, fc='b', label="HD 209458 b") 
patch2 = plt.Circle((0, -2), 0.001, fc='y', label="HD 209458") 
a=plt.Circle((0, -2),0.001, color="red",label=' centre de masse ')
plt.annotate('masse en masse de Jupiter', xy=(0, 0), xytext=(0.003, -0.07))

m=0.69
M=102
R=0.04747

def init(): 
     patch.center = (0, 0) 
     patch2.center = (0, 0) 
     a.center = (0, 0)
     ax.add_patch(patch) 
     ax.add_patch(patch2) 
     ax.add_patch(a) 
     return a,patch, patch2, 

 
def animate(t): 
     x,y = patch.center 
     x = R* np.cos(np.radians(t)) 
     y =-R* np.sin(np.radians(t)) 
     patch.center = (x,y) 
     x,y = patch2.center 
     x =-np.cos(np.radians(t))*(m*R/(m+M)) 
     y =+np.sin(np.radians(t))*(m*R/(m+M)) 
     patch2.center= (x,y) 
      
     return a,patch, patch2, 
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=360,interval=20,blit=True)

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1, ncol=2, mode="expand", borderaxespad=0, handles=[a, patch, patch2]) 
