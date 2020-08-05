# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy.special as spe
import numpy as np
import matplotlib.pyplot as plt

c=3*10**8
mC=12*931.49432
mO=15.994915*931.49432
mr=(mC*mO)/(mC+mO)
TCM=72.013
h=6.582*10**(-22)
r0=1.44*10**-15
k1=2.*mr*TCM
k2=c**2*h**2
k=np.sqrt(k1/k2)
R=r0*(16**(1/3)+12**(1/3))
kR=k*R
k2R4=k**2*R**4
k2R4mb=k2R4*10**31


y=np.array([400,180,70,28,20,10,18,27,45,70,80,90,80,70,50,25,11,6,1.1,4.2,7,12,16,20,15,11,9,7,5,3,2,1.8,2.2,3.1,3.8,4.1,3.7,3.1,2.7,2.5,1.1,1.5,1.3,1.0,0.9,0.8,0.9,1.0,1.05,1.2,1.2,0.8,0.6,0.4,0.3,0.2])
x=np.linspace(np.pi*15.0/180,np.pi*42.5/180,len(y))

theta=np.arange(np.pi*15.0/180,np.pi*42.5/180,0.005)
y1=k2R4mb*((spe.j1(kR*theta)/(kR*theta))**2)

plt.plot(x,y,'.')
plt.plot(theta,y1,'-')
plt.title('Difracción Teoría de Fraunhöfer vs. Pts. Experimentales',size='10')
plt.xlabel(r'$\theta$ (rad)')
plt.ylabel('Sección eficaz diferencial (mbarn/sr)')
plt.legend(('Pts. predichos por Fraunhöfer','Valores experimentales'),prop={'size':10},loc='upper right')




