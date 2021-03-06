#!/usr/bin/env python3

import math
import argparse
import csv
import f90nml
import matplotlib
import numpy as np
from scipy import interpolate
from pylab import *
import matplotlib.pyplot as plt
from math import pi
# Original Blades
b=1.
croot=0.1
Nelem=40
alpha=10
rR=-np.cos(np.linspace(0,pi,Nelem))/2.
cR=np.sqrt(croot**2.*(1-(2*rR)**2.))/b
pitch=np.linspace(alpha,alpha,Nelem)
t2c=np.linspace(1,1,Nelem)
with open('EllipticWing_ae'+str(alpha)+'.al','w') as fout:
    fout.write('R  : '+str(b)+' \n')
    fout.write('Spanwise  : 0.0 0.0 1.0 \n')
    fout.write('NStations : '+str(Nelem)+'\n')
    for j in range(0,Nelem):
       fout.write(str(rR[j])+'\t'+str(cR[j])+'\t'+str(pitch[j])+'\t'+str(t2c[j])+'\n')

plt.plot(rR*b,cR*b)
plt.show()

AOA=np.linspace(-180,180,361)
CL=0.4+2*pi*AOA/180.*pi
CD=0.*AOA
CM25=0.*AOA
with open('ThinCambered.air','w') as fout:
	fout.write('Title: ThinCambered\n') 
	fout.write('Thickness to Chord Ratio: 1.0\n')
	fout.write('Zero Lift AOA (deg):  -3.64\n')
	fout.write('Reverse Camber Direction: 0\n')
	fout.write('\n')
	fout.write('Reynolds Number: 4e3\n')
	fout.write('AOA (deg) CL CD Cm25\n')
	for j in range(361):
       		fout.write(str(AOA[j])+'\t'+str(CL[j])+'\t'+str(CD[j])+'\t'+str(CM25[j])+'\n')
	fout.write('\n')
	fout.write('Reynolds Number: 4e8\n')
	fout.write('AOA (deg) CL CD Cm25\n')
	for j in range(361):
       		fout.write(str(AOA[j])+'\t'+str(CL[j])+'\t'+str(CD[j])+'\t'+str(CM25[j])+'\n')
	
