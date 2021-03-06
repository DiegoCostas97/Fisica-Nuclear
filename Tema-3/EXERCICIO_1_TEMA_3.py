#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:47:38 2020

@author: diego
"""
import pylab as py
import matplotlib.pyplot as plt


c2=9*10**16
ma=8.03393439*931.494/c2
mb=13.00573861*931.494/c2
mB=6569.082/c2
Q0=-22.87284303
Q1=-23.87284303
Q2=-25.87284303
print('Q0=', Q0)
print('Q1=', Q1)
print('Q2=', Q2)
print('')

Ta=120.
Tb=60.
A=ma*mb*Ta
B=mB+mb
C=(mB+mb)/mb
D=C*2.*mb*Tb
E=2.*ma*Ta
F0=2.*mB*(Q0+Ta)
F1=2.*mB*(Q1+Ta)
F2=2.*mB*(Q2+Ta)
G=2.*py.sqrt(2.*ma*Ta)*py.sqrt(2.*mb*Tb)

primer=(py.sqrt(A))/(B)
segundo0=(B)*(mB*Q0+(mB-ma)*Ta)
segundo1=(B)*(mB*Q1+(mB-ma)*Ta)
segundo2=(B)*(mB*Q2+(mB-ma)*Ta)

thetamin0=py.arccos(py.sqrt(-segundo0/A))
thetamin1=py.arccos(py.sqrt(-segundo1/A))
thetamin2=py.arccos(py.sqrt(-segundo2/A))
print('thetamin0=', thetamin0)
print('thetamin1=', thetamin1)
print('thetamin2=', thetamin2)
print('')

x=py.arange(0,thetamin0,0.000005)
y1=(py.cos(x)*primer+(py.sqrt(A*(py.cos(x)**2)+segundo0)/B))**2
y2=(py.cos(x)*primer-(py.sqrt(A*(py.cos(x)**2)+segundo0)/B))**2
y3=(py.cos(x)*primer+(py.sqrt(A*(py.cos(x)**2)+segundo1)/B))**2
y4=(py.cos(x)*primer-(py.sqrt(A*(py.cos(x)**2)+segundo1)/B))**2
y5=(py.cos(x)*primer+(py.sqrt(A*(py.cos(x)**2)+segundo2)/B))**2
y6=(py.cos(x)*primer-(py.sqrt(A*(py.cos(x)**2)+segundo2)/B))**2

plt.figure(1)
plt.plot(x, y1, x, y2, x, y3, x, y4, x, y5, x, y6, 'b')

plt.title('CINEMATICA')
plt.xlabel('Theta(Rad)')
plt.ylabel('Tb(Mev)')
plt.legend(('Raiz0 +', 'Raiz0 -', 'Raiz1 +', 'Raiz1 -', 'Raiz2 +', 'Raiz2 -'),prop={'size':8},loc='upper right')

x=py.arange(0.4,0.6,0.05)
y1=(py.cos(x)*primer+(py.sqrt(A*(py.cos(x)**2)+segundo0)/B))**2
y3=(py.cos(x)*primer+(py.sqrt(A*(py.cos(x)**2)+segundo1)/B))**2
y5=(py.cos(x)*primer+(py.sqrt(A*(py.cos(x)**2)+segundo2)/B))**2

plt.figure(2)
plt.plot(x, y1, x, y3, x, y5, 'b')

plt.title('CINEMATICA')
plt.xlabel('Theta(Rad)')
plt.ylabel('Tb(Mev)')
plt.legend(('Raiz0 +', 'Raiz1 +', 'Raiz2 +'),prop={'size':8},loc='upper right')

theta=py.arccos((((mB+mb)/mb)*2.*mb*Tb+2.*ma*Ta-2.*mb*(Q0+Ta))/(2.*py.sqrt(2*ma*Ta)*py.sqrt(2.*mb*Tb)))

thetafijo0=py.arccos((D+E-F0)/G)
thetafijo1=py.arccos((D+E-F1)/G)
thetafijo2=py.arccos((D+E-F2)/G)
print('thetafijo0=', thetafijo0)
print('thetafijo1=', thetafijo1)
print('thetafijo2=', thetafijo2)
print('')

Efijo0=(py.cos(0.5)*primer+(py.sqrt(A*(py.cos(0.5)**2)+segundo0)/B))**2
Efijo1=(py.cos(0.5)*primer+(py.sqrt(A*(py.cos(0.5)**2)+segundo1)/B))**2
Efijo2=(py.cos(0.5)*primer+(py.sqrt(A*(py.cos(0.5)**2)+segundo2)/B))**2
print('Tbfijo0=', Efijo0)
print('Tbfijo1=', Efijo1)
print('Tbfijo2=', Efijo2)
print('')

REmin=(Efijo0-Efijo1)
RAmin=(thetafijo0-thetafijo1)

print('A resolución mínima en enerxía ten que ser:', REmin)
print('A resolución mínima angular ten que ser:', RAmin)