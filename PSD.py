# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:48:31 2021

@author: Daniely Amorim
"""
def PSD(variable,time,segc):
    '''
    Estimates power spectral density
   
    Sintax: freq, Sxx = PSD (Data, time, segc)
   
    Input:
        data - Signal
        time - time vector
        segc - number of segments
       
    Output:
        freq -  frequency
        Sxx  -  power spectral density
    '''
    import numpy as np
    from scipy import signal
    
    dt = time[1]-time[0]
    fs = 1/dt

    Nc_dP1 = len(variable)
    nfft = 2**(np.ceil(np.log2(abs(2*Nc_dP1-1)))) #Corrigindo 
    nsegc = int(np.floor(Nc_dP1/segc)) #Number of Segments
    foverlapc = 0.5 #Percentage of the segment that shall have overlap
    nov1 = np.floor(nsegc*foverlapc);
    freq, Sxx1 = signal.welch(variable, fs=fs, window='hann', nfft=nfft , nperseg=nsegc, noverlap=nov1, return_onesided=True)
    
    return freq,Sxx1 