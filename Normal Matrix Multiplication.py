# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:16:40 2020

@author: LENOVO
"""

A = [[5,7,6],[4,7,8],[2,4,8]]
B = [[2,4,6],[4,8,2],[3,4,9]]
C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        #C[[i],[j]] = 0
        for k in range(0,3):
            C[i][j] += (A[i][k] * B[k][j])
print(C)