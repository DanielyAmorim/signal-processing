# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:46:07 2021

@author: Daniely Amorim
"""

def HurstCoeficient(data):
    '''
    Estimates Hurst Coeficient
   
    Sintax: H = HurstCoeficient(data)
   
    Input:
        data - Signal
       
    Output:
        h - Hurst Coeficient      
    '''
    
    import numpy as np
    serie = data
    n = np.log2(len(serie)/8) + 1 
    logN = np.array([i for i in range(int(np.floor(n)))])
    N  = 2**(logN)              # number of sequences
    logRS = np.zeros(len(N))
    logRegiao = np.zeros(len(N))
    
    for i in range(0, len(N)):
        intsize = int(np.floor(len(serie)/N[i]))      # numero de partições
        logRegiao[i] = np.log2(intsize)               # Armazenar log do tamanho da região
        A = serie[0:N[i]*intsize]                     # cut values at the end of data to make the array divisible by n
        Particao = np.reshape(A,(N[i],intsize))       # Matriz com uma linha para cada partição
        Mean = np.transpose(np.mean(Particao,axis=1)) # Média de cada partição (mean(x,2)por linha)
        B = np.ones(intsize)                          # vetor de 1
        C = np.outer(Mean, B)                         # matriz com as medias de cada partição
        Particao = Particao - C                       # Subtrair a média de cada partição da partição
        CumDeviation = np.cumsum(Particao, axis=1)
        Max = np.max(CumDeviation, axis=1) 
        Min = np.min(CumDeviation, axis=1)
        Range = Max - Min # find ranges
        DP = np.std(Particao , axis=1)  # find standard deviation
        Rescalonamento = Range/DP
        ExpectedRS = np.mean(Rescalonamento)
        logRS[i] = np.log2(ExpectedRS)
    
    xvals = logRegiao
    yvals = logRS
    poly = np.polyfit(xvals, yvals, 1)
    h = poly[0]
    
    # plt.figure()
    # plt.plot(xvals, yvals, "bo")
    # plt.plot(xvals, np.polyval(poly, xvals), "r-")
    # plt.legend(loc="best")
    return h