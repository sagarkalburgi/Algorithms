# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:09:35 2020

@author: LENOVO
"""

def OptimalMergePattern(L):
    T = 0
    while True:
        if len(L) > 1:
            L.sort()
            left,right = L[0],L[1]
            weight = left+right
            L = L[1:]
            L[0] = weight
            T += L[0]
            if len(L) == 1:
                break
    return print("Total minimal Cost/Weight is: ", T)
        
L = list(map(int,input("Enter the list: ").split()))
OptimalMergePattern(L)