#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:15:09 2020

@author: Maximilian Penz
license: GNU GPL-3.0
"""
from __future__ import division
#from scipy import symbols
import os
import glob
import natsort
import numpy as np
import sympy as sp

import matplotlib.pyplot as plt
import scatter_Rb
import scatter_Cs
import scatter_Na
import scatter_K
import scatter_Li
import scatter_VPSI
import scatter_PBSI

def auswerter(path):
    root_folder = natsort.natsorted(glob.glob(path + '*.txt'))
    for file_name in root_folder:
        config = np.loadtxt(file_name,dtype='string')
        path_measure = config[0]
        path_data = config[1]
        path_plot = config[2]
        name_string = config[3]
        module_string = config[4]
        cb = float(config[5])
        co = float(config[6])
        ci = float(config[7])
        t0 = int(config[8])
        tm = int(config[9])
        length = int(config[10])
        large_n = float(config[11])

        un = 11+1340                   #Indexierung beginnt bei 0
        ob = 11+1511
        q0 = 4.078			#=2pi/lamb

        file_list = natsort.natsorted(glob.glob(path_measure + '*.mca'))
        j=0
        output = np.zeros(shape=(len(file_list),4))

        for file_path in file_list:
            print(file_path)
            #remover = file_path.replace()
            angle_str = os.path.basename(file_path).replace(name_string,'').strip('.mca')
            if angle_str.startswith('_')==True:
                #angle = int(angle_str.replace('_','').strip('-5'))+0.5
                angle = int(angle_str.replace('_',''))                      #uncomment for normal angles
            #elif angle_str[2]=='-':
             #   angle=int(angle_str.replace('-5',''))+0.5
            #elif angle_str[1]=='-':
             #   angle=int(angle_str.strip('-5'))+0.5
            else:
                #angle = int(angle_str.strip('-5'))+0.5
                angle = int(angle_str)                     #uncomment for normal angles
            print(angle)
            q = 2*q0*np.sin(0.5*np.radians(angle))
            #print(q)
            f = eval(module_string).mean_f(q,cb,co,ci)           #RICHTIGE ATOMPROZENTE FÜR GLÄSER EINSETZEN! cb, co, ci
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
                ints_corr = thickness_correction(np.abs(np.radians(angle)),tm,ints,t0)
                ints_err_corr = thickness_correction(np.abs(np.radians(angle)),tm,ints_err,t0)
                #print(ints_corr)
            real_time = float(intensity_list[8].strip('REAL_TIME - '))
            #mit_ints = ints/real_time * 100
            mit_ints = (ints_corr/real_time) * 100
            mit_ints_err = (ints_err_corr/real_time) * 100
            output[j] = np.array([[mit_ints,q,f,mit_ints_err]])
            j=j+1

        err_I = output[:,[3]]
        err_S = np.zeros(len(output))
        sq = np.zeros(len(output))

        #for k in range(len(out)):
        	#sq[k] = out[k,0]/(30*out[k,2])
             #   err_S[k]=err_I[k]/(30*out[k,2])

        for k in range(len(output)):
            sq[k] = output[k,0]/(large_n*output[k,2])
            err_S[k] = err_I[k]/(large_n*output[k,2])


        uguu = np.reshape(output[:,[1]],(length,))
        data = np.array([sq,uguu,err_S])
        np.savetxt(path_data + name_string.replace('_DEG_','_data.txt'),np.transpose(data), delimiter='\t', header='S(q)'+'\t'+'q'+'\t''Err_S(q)')


    plt.figure(figsize=(15,13))
    plt.plot(output[:,1],sq,'bp')
    plt.title('Scattering function' + ' ' + name_string.replace('_DEG_',''),fontsize=18)
    plt.xlabel('q [$\AA^{-1}$]',fontsize=16)
    plt.ylabel('S(q) [arb. units]',fontsize=16)
    plt.grid()
    plt.savefig(path_plot + name_string.replace('_DEG_','_plot.png'), bbox_inches = 'tight')



    #print(path_measure)
    #print(module_string)
    #print(cb)
    #print(t0)



def correction(th,ud):
    ra = 0.4
    ri = 0.24
    rb = 0.353
    R = (ra-ri)/(rb-ri)
    corr = R * ((sp.exp(-1*ud/sp.cos(th))) - (sp.exp(-1*ud*((2/sp.cos(th))-(R)))))/((R) - (1/sp.cos(th)))
    return(corr)



def thickness_correction(th,I_m,I0,I_l):		#I_l: Transmission ohne Probe[c/s]; I_m Transmission bei Messpunkt; th:2theta; I0:unkorrigierte Int
    x = sp.symbols('x')
    sp.init_printing(use_unicode=True)
    #I_l = 212894
    ud = -1*sp.log(I_m/I_l)
    g = sp.limit(correction(x,ud),x,0)
    I_corr = g*(I0/correction(th,ud))
    return(I_corr)




path = '/home/anon/Dokumente/Studium/Masterarbeit/rb30_conf/'
auswerter(path)
