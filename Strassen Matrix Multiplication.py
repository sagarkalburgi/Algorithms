# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:05:00 2020

@author: LENOVO
"""
import numpy as np

def split(matrix):
    row,col = matrix.shape
    row2,col2 = row//2, col//2
    return matrix[:row2,:col2], matrix[:row2,col2:], matrix[row2:,:col2], matrix[row2:,col2:]

def StrassenMultiplication(x,y):
    if len(x) == 1:
        return x*y
    
    a,b,c,d = split(x)
    e,f,g,h = split(y)
    
    p1 = StrassenMultiplication(a,f-h)
    p2 = StrassenMultiplication(a+b,h)
    p3 = StrassenMultiplication(c+d,e)
    p4 = StrassenMultiplication(d,g-e)
    p5 = StrassenMultiplication(a+b,e+h)
    p6 = StrassenMultiplication(b-d,g+h)
    p7 = StrassenMultiplication(a-c,e+f)
    
    c11 = p5+p4-p2+p6
    c12 = p1+p2
    c21 = p3+p4
    c22 = p1+p5-p3-p7
    
    C = np.vstack((np.hstack((c11,c12)),np.hstack((c21,c22))))
    return print("Matrix Multiplication: ",C)

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
B = np.array([[16,15,14,13],[12,11,10,9],[8,7,6,5],[4,3,2,1]])
StrassenMultiplication(A,B)