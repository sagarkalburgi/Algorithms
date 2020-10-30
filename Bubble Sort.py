# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:33:01 2020

@author: LENOVO
"""

def BubbleSort(A,n):
    for k in range(1,n):
        for i in range(0,n-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
    return print("Sorted List: ",A)

A = list(map(int,input("Enter the list: ").split()))
n = len(A)
BubbleSort(A,n)