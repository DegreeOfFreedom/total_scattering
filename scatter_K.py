#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#author: Bogdan Sepiol (original Fortran script), Maximilian Penz
#license: GNU GPL-3.0
#Parameters from D. Waasmaier, A. Kirfel, "New Analytical Scattering-Factor Functions for Free Atoms and Ions", Acta Cryst, 416-431, 1994

import numpy as np
#import os

def mean_f(q,c_b,c_o,c_i):
	
	file = open('./plot.txt','w')
	file.write('q(A**-1)	<f**2>\n')
	f2=[]
	
	if(isinstance(q, (int, float))):
		fa = f_b(q,np.pi*4)
		fb = f_o(q,np.pi*4)
		fc = f_k(q,np.pi*4)
		f2 = (c_b*fa*fa + c_o*fb*fb + c_i*fc*fc)/(c_b+c_o+c_i)
	else:
		for i in q:
			fa = f_b(i,np.pi*4)
			fb = f_o(i,np.pi*4)
			fc = f_k(i,np.pi*4)
			res = (c_b*fa*fa + c_o*fb*fb + c_i*fc*fc)/(c_b+c_o+c_i)
			f2.append(res)
			file.write('%s' % i + '\t')
			file.write('%s' % res + '\n')
	file.close()
	return(f2)

def f_b(x,pi4):
	
	
	
	f_B= 1.533712*np.exp(-42.662078*(x/pi4)**2)+0.638283*np.exp(-0.595420*(x/pi4)**2)+ \
		0.601052*np.exp(-99.106501*(x/pi4)**2)+0.106139*np.exp(-0.151340*(x/pi4)**2) + \
		1.118414*np.exp(-1.843093*(x/pi4)**2) + 0.002511
	return(f_B)

def f_o(x,pi4):

	f_O= 3.106934*np.exp(-19.868080*(x/pi4)**2) + 3.235142*np.exp(-6.960252*(x/pi4)**2) + \
			1.148886*np.exp(-0.170043*(x/pi4)**2) + 0.783981*np.exp(-65.693509*(x/pi4)**2) + \
			0.676953*np.exp(-0.630757*(x/pi4)**2) + 0.046136
	return(f_O)

def f_cs(x,pi4):

	f_Cs= 19.939057*np.exp(-3.770511*(x/pi4)**2)+24.967620*np.exp(-0.004040*(x/pi4)**2)+ \
				10.375884*np.exp(-25.311276*(x/pi4)**2)+ 0.454243*np.exp(-76.537763*(x/pi4)**2) + \
				17.660247*np.exp(-0.384730*(x/pi4)**2) - 19.394307


	return(f_Cs)
	
def f_rb(x,pi4):
	
	f_Rb= 17.684321*np.exp(-1.710209*(x/pi4)**2)+7.761588*np.exp(-14.919863*(x/pi4)**2)+ \
		6.680874*np.exp(-0.128542*(x/pi4)**2)+ 2.668883*np.exp(-31.654478*(x/pi4)**2) + \
		0.070974*np.exp(-0.128543*(x/pi4)**2) + 1.133263

	return(f_Rb)
	

def f_na(x,pi4):
	
	f_Na= 3.14869*np.exp(-2.594987*(x/pi4)**2)+4.073989*np.exp(-6.046925*(x/pi4)**2)+ \
		0.767888*np.exp(-0.070139*(x/pi4)**2)+ 0.995612*np.exp(-14.122657*(x/pi4)**2) + \
		0.968249*np.exp(-0.217037*(x/pi4)**2) + 0.04530
	
	return(f_Na)
	

def f_k(x,pi4):

	f_K= -17.609339*np.exp(-18.840979*(x/pi4)**2)+1.494873*np.exp(-0.053453*(x/pi4)**2)+ \
		7.150305*np.exp(-0.812940*(x/pi4)**2)+ 10.899569*np.exp(-22.264104*(x/pi4)**2) + \
		15.808228*np.exp(-14.351593*(x/pi4)**2) + 0.257164

	return(f_K)
	

def f_li(x,pi4):

	f_Li= 0.432724*np.exp(-0.260367*(x/pi4)**2)+0.549257*np.exp(-1.042836*(x/pi4)**2)+ \
		0.376575*np.exp(-7.885294*(x/pi4)**2)- 0.336481*np.exp(-0.260368*(x/pi4)**2) + \
		0.976060*np.exp(-3.042539*(x/pi4)**2) + 0.001764



#q = np.array([3.0552913759,0.852534146411,3.18680308396,1.97311498051,4.078,
#	1.55623816629,4.67808941488,2.24809827404,2.78951628896,2.38458362372,
#	0.993966364812,2.52034260612,1.27587949687,3.82901006608,1.41627453705,
#	0.284640295106,4.32202151909,0.426852059117,2.65533386775,1.13509581143,
#	3.70274651588,2.92284899649,2.11092813186,3.31734406093,1.69572775031,
#	3.57535507321,0.142341826902,4.50159805221,3.44687454276,0.568933799857,
#	1.83470079923,0.71084223785])






#mean_f(q,0.375,0.583,0.04167)



