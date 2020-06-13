#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:30:34 2020

@author: Maximilian Penz
license: GNU GPL-3.0
"""

from __future__ import division
import glob
#import os
import natsort
import numpy as np
import matplotlib.pyplot as plt

path = '/home/anon/Dokumente/Studium/Masterarbeit/Amptek_05_2019/Absorber/'

file_list = natsort.natsorted(glob.glob(path + '*.mca'))

un = 11+1340                   #Indexierung beginnt bei 0
ob = 11+1511
q0 = 4.078
ints_list = []
ints_err_list = []
for file_path in file_list:
    intensity_list = []

    ints = 0
    file = open(file_path)

    for line in file:
        intensity_list.append(line.strip('\r\n'))
    real_time = float(intensity_list[8].strip('REAL_TIME - '))
    for i in range(un,ob):
            ints = ints + np.int(intensity_list[i])
    mit_ints = (ints/real_time)*100
    ints_list.append(mit_ints)
    print(mit_ints)
    print(file_path)
    file.close()
    mit_ints_err = np.sqrt(mit_ints)
    ints_err_list.append(mit_ints_err)

thicc = 17.52     #micrometer
thicc_list = [0,]
th=0
for j in range(6):
    th = th + thicc
    thicc_list.append(th)

tr_list = []
tr_err_list = []
for k in range(len(thicc_list)):
	transmission = np.exp(-(thicc_list[k]*78.77)) #bogdan formel falsch ??
	transmission_error = 0.02 * (1/78.77) * np.exp(-(thicc_list[k]/78.77))
	tr_list.append(transmission)
	tr_err_list.append(transmission_error)

fit = np.polyfit(tr_list,ints_list,1)
p, res, _, _, _ = np.polyfit(tr_list,ints_list,1,full=True)
fit_fn = np.poly1d(fit)
uguu,cov = np.polyfit(tr_list,ints_list,1,cov=True)

one = np.ones(7)

print(p)
print(res)
print(np.sqrt(np.diag(cov)))


plt.figure(figsize=(13,11))
#plt.plot(tr_list,ints_list,'bp')
plt.errorbar(tr_list, ints_list, yerr=ints_err_list, xerr=None, fmt='bp', capsize=7)
plt.plot(tr_list,fit_fn(tr_list),'r',label='Linear fit')
#plt.plot(out[:,1],sq,'bp')

#plt.errorbar(tr_list, abs(ints_list-fit_fn(tr_list)), yerr=None, xerr=tr_err_list, fmt='bp', capsize=10)
#plt.plot(tr_list,one,'r--')

plt.title('Absorption linearity' ,fontsize=18)
plt.xlabel('Transmission (dimensionless)',fontsize=16)
plt.ylabel('Intensity per 100s [counts]',fontsize=16)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize='xx-large')
plt.grid()
