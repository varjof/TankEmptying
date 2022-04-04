# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:05:31 2020

@author: John
"""

import matplotlib.pyplot as plt
import numpy as np

Ro=0.15
Rt=10
ht=8
ho=4
g=9.8

dt=50

h=ho
t=0

plt.plot([0,0,2*Rt,2*Rt,2*Rt+0.5,2*Rt+0.5,0],[0,ht,ht,2*Ro,2*Ro,0,0])

linea,=plt.plot([0,20],[ho,ho])

for i in range(90):
    h=-((Ro/Rt)**2*np.sqrt(2*g*h))*dt+h
    t=t+dt
    linea.set_ydata(h)
    plt.pause(0.1)    
    
