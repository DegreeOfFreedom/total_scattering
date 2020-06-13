#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:08:01 2020

@author: Maximilian Penz
license: GNU GPL-3.0
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


ch = np.array([803.1,877.99,962.455,1043.77,1057.77,
               1137.31,1252.25,1425.38])
en = np.array([4.509,4.932,5.412,5.895,5.947,
               6.4,7.058,8.041])
ch_err = np.array([0.078, 0.433, 0.0885, 3.005, 1.795, 0.105, 0.562, 0.0371])
detektor_fwhm = np.array([23.4,24.7,24.4,24.9,22.6,26.9,27.7,30.5])
#sigma_kev = np.array([0.0057,0.0089,0.0083,0.0163,0.0140,0.0163,0.0231])
sigma_ch = np.array([10.1199,10.6347,10.1137,9.2377,9.2377,10.8922,11.495,12.7118])
#fwhm_err = np.array([0.048, 0.133, 0.063, 2.8, 1.4, 0.079, 0.183, 0.039])*2
sigma_ch_err = np.array([0.0814,0.4538,0.0931,1.112,1.112,0.111,0.5948,0.03881])

fwhm = 2*np.sqrt(2*np.log(2))*sigma_ch
fwhm_err = 2*np.sqrt(2*np.log(2))*sigma_ch_err

weights = 1/(ch_err**2)

reg = LinearRegression().fit(en.reshape(-1,1),ch.reshape(-1,1),sample_weight=weights)
predicted_ch = reg.predict(en.reshape(-1,1))
mse = mean_squared_error(ch.reshape(-1,1),predicted_ch)
#reg = LinearRegression().fit(zip(en,ch),sample_weight=weights)

#standard error calculation
en_rs = en.reshape(1,-1)
predictor_ch = predicted_ch.reshape(1,-1)
ones = np.ones(predictor_ch.shape)

predictor_matrix = np.matrix(np.vstack((predictor_ch, ones)))

covariance = mse * np.linalg.inv(predictor_matrix * predictor_matrix.T)

one = np.zeros(8)

resp = ch.reshape(-1,1) - predicted_ch

fwhm_kev = 13.372*sigma_ch
fwhm_kev_err = 13.372*sigma_ch_err


fwhm_weights = 1/(fwhm_kev_err.flatten()**2)

reg2 = LinearRegression().fit(en.reshape(-1,1),fwhm_kev.reshape(-1,1),sample_weight=fwhm_weights)

predicted_fwhm = reg2.predict(en.reshape(-1,1))

plt.figure(figsize=(13,12))
plt.grid()
#plt.subplot(2,1,1)
plt.title('Detector FWHM vs. energy', fontsize=25)
plt.xlabel('Energy [keV]', fontsize=25)
plt.ylabel('Detector FWHM [ev]', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.ylim((-0.005,0.013))
#seaborn.residplot(en,fit_fn(ch),color='r')

#plt.errorbar(en, ch, yerr=ch_err, xerr=None, fmt='bp', capsize=10)
#plt.plot(en,ch,'bp')
#plt.plot(en_rs.flatten(), predictor_ch.flatten(), 'r', label='Linear fit')
#plt.legend(fontsize='xx-large')
#plt.subplot(2,1,2)

#plt.errorbar(en, resp.flatten(), yerr=ch_err, xerr=None, fmt='bp', capsize=10)
#plt.plot(en, resp.flatten(), 'bp')
#plt.plot(en,one,'r--')

plt.errorbar(en, fwhm_kev.flatten(), yerr=fwhm_kev_err.flatten(), xerr=None, fmt='bp', capsize=10)
plt.plot(en, predicted_fwhm.flatten(), 'r', label='Linear fit | FWHM = 10.9(9) $\cdot$ E + 82(7)')
plt.legend(fontsize='xx-large')
print(reg2.coef_)
print(reg2.intercept_)
print(mse)
