# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:07:24 2017

@author: 3670463
"""
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import animation 
from pylab import*
fig= plt.figure() 
fig.set_dpi(100) 
fig.set_size_inches(50, 50) 
ax=plt.axes(xlim=(-7, 7), ylim=(-7, 7))
plt.ylabel('distance en UA')
plt.xlabel('masse exprimée en masse de Jupiter')
patch = plt.Circle((5,-5), 0.15, fc='b', label="Exoplanete") 
patch2 = plt.Circle((0, 3), 0.25, fc='y', label="étoile") 
a= plt.Circle((0, 3), 0.1, fc='r', label="centre de masse")
m=1
M=3
R=6
def init(): 
     patch.center = (0, 0) 
     patch2.center = (0, 0) 
     a.center = (0, 0)
     ax.add_patch(patch) 
     ax.add_patch(patch2) 
     ax.add_patch(a) 
     return patch, patch2,a, 

 
def animate(t): 
     x,y = patch.center 
     x = R* np.cos(np.radians(t)) 
     y =-R* np.sin(np.radians(t)) 
     patch.center = (x,y) 
     x,y = patch2.center 
     x =-np.cos(np.radians(t))*(m*R/(m+M)) 
     y =+np.sin(np.radians(t))*(m*R/(m+M)) 
     patch2.center= (x,y) 
      
     return patch, patch2,a, 
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=360,interval=20,blit=True)

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1, ncol=2, mode="expand", borderaxespad=0, handles=[a, patch, patch2]) 


