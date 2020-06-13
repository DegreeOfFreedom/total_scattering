#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:32:59 2019

@author: Maximilian Penz
license: GNU GPL-3.0
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn

#ch = np.array([38.5,803.1,878.3,1136.8,1252,1425.5])
#en = np.array([0.756,4.509,4.932,6.4,7.058,8.041])

ch = np.array([803.1,878.3,962.6,1054.1,
               1136.8,1252,1425.5])
en = np.array([4.509,4.932,5.412,5.947,
               6.4,7.058,8.041])

fit = np.polyfit(ch,en,1)
p, res, _, _, _ = np.polyfit(ch,en,1,full=True)
fit_fn = np.poly1d(fit)
uguu,cov = np.polyfit(ch,en,1,cov=True)

one = np.zeros(7)

y_err = ((en - fit_fn(ch))/(0.017))**2

rmse = np.sqrt(np.sum((en - fit_fn(ch))**2)/6) #root mean squared error

print(p)
print(res)
print(np.sqrt(np.diag(cov))) #Fehler +/-
#coefs = np.polyfit(lengths, breadths, 1)
yfit = np.polyval(fit,ch)


plt.figure(figsize=(13,12))
plt.grid()
#plt.subplot(2,1,1)
plt.title('Peak energy vs. channel - Residuals', fontsize=25)
plt.xlabel('Energy [keV]', fontsize=25)
plt.ylabel('Difference [keV]', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.ylim((-0.005,0.013))
#seaborn.residplot(en,fit_fn(ch),color='r')

#plt.plot(ch,en,'bp')
#plt.plot(ch,fit_fn(ch),'r')

#plt.subplot(2,1,2)
plt.errorbar(ch, abs(en-yfit), yerr=rmse, xerr=None, fmt='bp', capsize=10)
plt.plot(ch,one,'r--')
plt.show()

#ch = np.array([38.5,803.1,878.3,962.6,1054.1,
 #              1136.8,1252,1425.5])
#en = np.array([0.756,4.509,4.932,5.412,5.947,
 #              6.4,7.058,8.041])
