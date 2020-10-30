# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:12:44 2020

@author: LENOVO
"""
INF = 9999999
A = [[0,3,INF,7],
     [8,0,2,INF],
     [5,INF,0,1],
     [2,INF,INF,0]]

for k in range(4):
    for i in range(4):
        for j in range(4):
            A[i][j] = min(A[i][j],(A[i][k]+A[k][j]))
    print("Matrix:",k+1,A[0])
    print("         ",A[1])
    print("         ",A[2])
    print("         ",A[3])
            
print("Final Matrix: ",A[0])
print("              ",A[1])
print("              ",A[2])
print("              ",A[3])