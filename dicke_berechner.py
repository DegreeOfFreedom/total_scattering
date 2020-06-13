#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:50:19 2020

@author: Maximilian Penz
license: GNU GPL-3.0
"""
from __future__ import division
import numpy as np

def dicke(mu,i,il):


    d = - np.log(i/il)*mu
    return d


def dicke_fehler(mu,i,il):
    d_err = (1/mu)*np.sqrt((i+il)/(i*il))
    return d_err


il_1 = 182400   #leer 1
il_2 = 212894   #leer 2
i = 145702      #Intensität Probe
mu = 661.9      #Streulänge Probe
thicc = dicke(mu,i,il_2)
thicc_err = dicke_fehler(mu,i,il_2)
print(thicc)
print(thicc_err)
