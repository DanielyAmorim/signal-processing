# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:44:06 2021

@author: Daniely Amorim
"""

def shn_entropy(y,nclass):
    '''
    Estimates Shannon Entropy
   
    Sintax: sh,p,bin_edges = shn_entropy(y,nclass)
   
    Input:
        y - Signal
        nclass - Signal will be divided into 'nclass' number of classes
       
    Output:
        sh - Shannon Entropy
        p - Probabilities for each bin
        bin_edges - Edges of each bin        
    '''
    import numpy as np
    
    hist,bin_edges = np.histogram(y,bins=nclass)
    p = hist/hist.sum()
    sh = p*np.log2(p)
    sh = -np.sum(sh[~np.isnan(sh)])
    
    return sh,p,bin_edges