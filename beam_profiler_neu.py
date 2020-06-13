#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:20:04 2020

@author: Maximilian Penz
license: GNU GPL-3.0
"""

from __future__ import division
import numpy as np
#import scipy as sc
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def sigmoid(x,b,c):
    return 218906 * (1.0 / (1.0 + np.exp(-c * (x - b))))

do_x = True

xx = np.arange(32.9,33.7,0.01)
ix = [217659,208022,215887,216028,214235,217405,207359,217351,207176,215930,214360,
210878,211113,208021,205242,204392,200044,197582,194785,190971,187277,179996,
180546,171759,172538,166314,164045,158760,154931,148357,147283,141950,137456,
132942,128019,123048,116952,113586,109450,104233,98882,94519,89819,85614,79724,
76016,71583,67274,62401,57963,53495,50063,45517,42175,37766,34958,31111,27490,
24114,21157,17751,14672,12973,10181,8144,6285,4329,2768,1700,981,520,263,132,77,
61,32,23,19,12,17,17]

yy = np.arange(57.5,59.01,0.01)
iy = [12,13,16,16,14,11,12,16,11,12,8,8,26,16,19,16,8,10,25,9,15,5,19,17,19,18,17,10,
12,14,8,16,15,13,18,15,11,21,9,26,16,19,12,22,49,42,72,109,222,396,793,1374,
2557,4208,6311,8665,10984,13882,16648,18793,22272,26168,29896,33555,37799,41127,
45467,49752,53696,58358,61761,67349,72344,76225,81377,85782,85622,94754,100058,
104789,110035,114309,112460,124403,128941,132399,137548,140625,146916,150257,
155019,158981,163141,168917,173128,176997,178771,182852,188137,189920,194923,
195994,201019,202913,205100,206966,210491,207471,214131,213929,215942,215959,
215759,216432,215374,217180,217052,214108,217251,215766,216436,216344,206143,
216673,217344,216658,216464,217481,213711,216658,215502,215698,212309,213346,
215657,214879,213951,217238,217481,217221,216900,216579,217159,214164,215846,
216127,215192,218125,217023,214602,218906]


if do_x == True:

    fitx_coord = np.loadtxt('profileX.txt',usecols=0)
    fitx_fit = np.loadtxt('profileX.txt',usecols=1)

    #fit = np.poly1d(np.polyfit(xx,ix,7))

    popt, pcov = curve_fit(sigmoid,-1*xx,ix,method='trf', bounds = ([-33.4,9.0],[-33.15,15.0]))
    #p, res = np.polyfit(xx,ix,7,full=True)
    gg = sigmoid(-1*xx,popt[0],popt[1])

    di = np.gradient(gg,xx)
    di_real = -1*di
    di_real_0 = di_real - min(di_real)
    #height, x, y, width_x, width_y = gauss.fitgaussian(di)

    #print(p)
    #print(res)
    #print(np.sqrt(np.diag(cov)))

    plt.figure(figsize=(15,13))
    plt.grid(True)
    plt.subplot(2,1,1)
    plt.title('Intensity distribution x-axis', fontsize=25)
    plt.xlabel('Position [mm]', fontsize=25)
    plt.ylabel('Intensity [counts]', fontsize=25)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(-xx,ix,'bp')
    plt.plot(-xx,gg,'r',label='Sigmoid Fit')
    plt.legend(fontsize='xx-large')
    #plt.subplot(2,1,2)
    #plt.plot(ch, en-yfit,'bp')
    plt.subplot(2,1,2)
    plt.title('Beam Profile x-axis', fontsize=25)
    plt.xlabel('Position [mm]', fontsize=25)
    plt.ylabel('d/dx(Intensity) [arb. units]', fontsize=25)
    plt.plot(xx,di_real_0,'bp')
    plt.plot(fitx_coord,fitx_fit,'r',label='Gaussian Fit')
    plt.legend(fontsize='xx-large')
    plt.tight_layout()
    plt.show()

else:

    fity_coord = np.loadtxt('profile_Y_voigt_neu.txt',usecols=0)
    fity_fit = np.loadtxt('profile_Y_voigt_neu.txt',usecols=1)

    #fit = np.poly1d(np.polyfit(xx,ix,7))

    popt, pcov = curve_fit(sigmoid,yy,iy,method='trf', bounds = ([57.5,10.0],[59.1,15.0]))
    #p, res = np.polyfit(xx,ix,7,full=True)
    gg = sigmoid(yy,popt[0],popt[1])

    di = np.gradient(gg,yy)
    #di_real = -1*di
    di_real_y = di - min(di)
    #height, x, y, width_x, width_y = gauss.fitgaussian(di)

    #print(p)
    #print(res)
    #print(np.sqrt(np.diag(cov)))

    plt.figure(figsize=(15,13))
    plt.grid(True)
    plt.subplot(2,1,1)
    plt.title('Intensity distribution y-axis', fontsize=25)
    plt.xlabel('Position [mm]', fontsize=25)
    plt.ylabel('Intensity [counts]', fontsize=25)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.plot(yy,iy,'bp')
    plt.plot(yy,gg,'r',label='Sigmoid Fit')
    plt.legend(fontsize='xx-large')
    #plt.subplot(2,1,2)
    #plt.plot(ch, en-yfit,'bp')
    plt.subplot(2,1,2)
    plt.title('Beam Profile y-axis', fontsize=25)
    plt.xlabel('Position [mm]', fontsize=25)
    plt.ylabel('d/dx(Intensity) [arb. units]', fontsize=25)
    plt.plot(yy,di_real_y,'bp')
    plt.plot(fity_coord,fity_fit,'r',label='Voigt Fit')
    plt.legend(fontsize='xx-large')
    plt.tight_layout()
    plt.show()
