# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:17:25 2020
@author: John
"""

import numpy as np
import matplotlib.pyplot as plt
g=9.8
Rt=10
ht=8
ho=4
Ro=0.1
h=ho
t = 0 #Empezamos en 0 segundos
dt=5  
plt.plot([0,0,2*Rt,2*Rt,2*Rt+0.5,2*Rt+0.5,0],[0,ht,ht,2*Ro,2*Ro,0,0])
linea,=plt.plot([0,20],[ho,ho])

while h>0:
    t = t + dt #Tiempo de simulación
    h = (-np.sqrt(2*g)/2*(Ro/Rt)**2*t+np.sqrt(ho))**2 #Altura del agua
    linea.set_ydata([h,h])
    plt.pause(0.033)
    plt.title("Tiempo= "+str(t))
    if h<2*Ro:
        linea.set_xdata([0,20.5])
        

# At=np.arange(0,3600,0.1)  #Tiempo
# plt.plot(At,Ah)
# plt.xlabel("Tiempo")
# plt.ylabel("Altura del agua")