#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:26:48 2019

@author: Maximilian Penz
license: GNU GPL-3.0
"""


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
#import os
import glob
import scatter_Li
import sympy as sp
import natsort

def auswerter(path):
    
    un = 11+1340                   #Indexierung beginnt bei 0
    ob = 11+1511
    q0 = 4.078			#=2pi/lamb
    
    file_list = natsort.natsorted(glob.glob(path + '*.mca'))
    j=0
    output = np.zeros(shape=(len(file_list),4))
    #f = np.zeros((len(file_list),1))
    for file_path in file_list:
        print(file_path)
        #remover = file_path.replace()
        angle_str = file_path.replace('/home/anon/Dokumente/Studium/Masterarbeit/Amptek_05_2019/5Li2O95B2O3/5Li2O95B2O3_DEG_','')[:-6]
        if angle_str.startswith('_')==True:
            #angle = int(angle_str.replace('_','').strip('-5'))+0.5
            angle = int(angle_str.replace('_',''))                      #uncomment for normal angles
        #elif angle_str[2]=='-':
         #   angle=int(angle_str.replace('-5',''))+0.5
        #elif angle_str[1]=='-':
         #   angle=int(angle_str.strip('-5'))+0.5
        else:
            #angle = int(angle_str.strip('-5'))+0.5
            angle = int(angle_str)+0.5                     #uncomment for normal angles
        print(angle)
        q = 2*q0*np.sin(0.5*np.radians(angle))
        #print(q)
        f = scatter_Li.mean_f(q,0.388,0.592,0.02)
        #f = scatter.mean_f(q,0.375,0.583,0.04167)
        #ff.append(f)
        intensity_list=[]
        file = open(file_path)
        for line in file:
            intensity_list.append(line.strip('\r\n'))
            
        ints=0
        for i in range(un,ob):
            ints = ints + np.int(intensity_list[i])
            ints_err = np.sqrt(ints)
            ints_corr = thickness_correction(np.abs(np.radians(angle)),39000,ints)
            ints_err_corr = thickness_correction(np.abs(np.radians(angle)),39000,ints_err)
            #print(ints_corr)
        real_time = float(intensity_list[8].strip('REAL_TIME - '))
        #mit_ints = ints/real_time * 100
        mit_ints = (ints_corr/real_time) * 100
        mit_ints_err = (ints_err_corr/real_time) * 100
        output[j] = np.array([[mit_ints,q,f,mit_ints_err]])
        j=j+1
    #print(ff)
    return(output)


def correction(th,ud):
	corr = ((sp.exp(-1*ud/sp.cos(th))) - (sp.exp(-1*ud)))/(1 - (1/sp.cos(th)))
	return(corr)



def thickness_correction(th,I_m,I0):		#I_l: Transmission ohne Probe[c/s]; I_m Transmission bei Messpunkt; th:2theta; I0:unkorrigierte Int
    x = sp.symbols('x')
    sp.init_printing(use_unicode=True)
    I_l = 182400
    ud = -1*sp.log(I_m/I_l)
    g = sp.limit(correction(x,ud),x,0)
    I_corr = g*(I0/correction(th,ud))
    return(I_corr)
	








PATH = '/home/anon/Dokumente/Studium/Masterarbeit/Amptek_05_2019/5Li2O95B2O3/'

#ara=[]
#uguu = open(PATH+'10Rb2O90B2O3_DEG_10.mca')
#for line in uguu:
#    ara.append(line.strip('\r\n'))


#rt = float(ara[8].strip('REAL_TIME - '))

#un = 11+1340                   #Indexierung beginnt bei 0
#ob = 11+1511

#ints=0
#for i in range(un,ob):
    #ints = ints + np.int(ara[i])
    #print(ints)


#mit_ints = ints/rt * 100
#print(mit_ints)
#list = glob.glob(PATH+'*.mca')

out = auswerter(PATH)

err_I = out[:,[3]]

#for m in range(len(out)):
    #err_I[m] = np.std(np.random.poisson(lam=out[m,0],size=150), axis=0)

#print(out)

err_S = np.zeros(len(out))
sq = np.zeros(len(out))

#for k in range(len(out)):
	#sq[k] = out[k,0]/(30*out[k,2])
     #   err_S[k]=err_I[k]/(30*out[k,2])

for k in range(len(out)):
    sq[k] = out[k,0]/(80*out[k,2])
    err_S[k] = err_I[k]/(80*out[k,2])


uguu = np.reshape(out[:,[1]],(31,))
data = np.array([sq,uguu,err_S])
np.savetxt('/run/media/anon/Fedora-KDE-Live-28-1-1/Masterarbeit/Data/Punkte/5Li2O95B2O3_data.txt',np.transpose(data), delimiter='\t', header='S(q)'+'\t'+'q'+'\t''Err_S(q)')
#uguu=q
plt.figure(figsize=(15,13))
#plt.subplot(2,1,1)
#plt.plot(out[:,1],out[:,0],'bp')
#plt.title(PATH[-14:])
#plt.xlabel('q [Angstrom**-1]')
#plt.ylabel('Intensity [counts]')
#plt.subplot(2,1,2)
plt.plot(out[:,1],sq,'bp')
plt.title('Streufunktion' + ' ' + PATH[-21:],fontsize=18)
plt.xlabel('q [Angstrom**-1]',fontsize=16)
plt.ylabel('S(q)',fontsize=16)
plt.grid()
plt.show()




