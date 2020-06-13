#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:32:59 2019

@author: Maximilian Penz
license: GNU GPL-3.0
"""

import numpy as np
import matplotlib.pyplot as plt
#import seaborn

#ch = np.array([38.5,803.1,878.3,1136.8,1252,1425.5])
#en = np.array([0.756,4.509,4.932,6.4,7.058,8.041])

ch = np.array([803.1,878.3,962.6,1054.1,
               1136.8,1252,1425.5])
en = np.array([4.509,4.932,5.412,5.947,
               6.4,7.058,8.041])
ch_err = np.array([0.058, 0.144, 0.072, 0.161, 0.093, 0.207, 0.045])
detektor_fwhm = np.array([23.4,24.7,24.4,27.9,26.9,27.7,30.5])
sigma_kev = np.array([0.0057,0.0089,0.0083,0.0163,0.0140,0.0163,0.0231])
fwhm_err = np.array([0.048, 0.133, 0.063, 0.149, 0.079, 0.183, 0.039])*2

fit = np.polyfit(en,ch,1)
p, res, _, _, _ = np.polyfit(en,ch,1,full=True)
fit_fn = np.poly1d(fit)
uguu,cov = np.polyfit(en,ch,1,cov=True)


#fit_fwhm = np.polyfit(en,detektor_fwhm,1)
#p_fwhm, res_fwhm , _, _, _ = np.polyfit(en,detektor_fwhm,1,full=True)
#fit_fn_fwhm = np.poly1d(fit_fwhm)
#uguu_fwhm,cov_fwhm = np.polyfit(en,detektor_fwhm,1,cov=True)



one = np.zeros(7)

#y_err = ((en - fit_fn(ch))/(0.017))**2

#rmse = np.sqrt(np.sum((en - fit_fn(ch))**2)/6) #root mean squared error

print(p)
print(res)
print(np.sqrt(np.diag(cov))) #Fehler +/-
#coefs = np.polyfit(lengths, breadths, 1)

#yfit = np.polyval(fit,en)
#resp = ch - yfit


error_fwhmp = en*0.386 + 2.378 + 1.893*sigma_kev


plt.figure(figsize=(13,12))
plt.grid()
#plt.subplot(2,1,1)
plt.title('Detector FWHM vs. energy', fontsize=25)
plt.xlabel('Energy [keV]', fontsize=25)
plt.ylabel('Detector FWHM [channels]', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.ylim((-0.005,0.013))
#seaborn.residplot(en,fit_fn(ch),color='r')

plt.errorbar(en, ch, yerr=ch_err, xerr=None, fmt='bp', capsize=10)
plt.plot(en,fit_fn(en),'r', label='Linear fit: FWHM = 1.9(4)$\cdot$E+15(2)')
plt.legend(fontsize='xx-large')
#plt.subplot(2,1,2)

#plt.errorbar(en, resp, yerr=ch_err, xerr=None, fmt='bp', capsize=10)
#plt.plot(en, resp, 'bp')
#plt.plot(en,one,'r--')
plt.show()

#ch = np.array([38.5,803.1,878.3,962.6,1054.1,
 #              1136.8,1252,1425.5])
#en = np.array([0.756,4.509,4.932,5.412,5.947,
 #              6.4,7.058,8.041])
