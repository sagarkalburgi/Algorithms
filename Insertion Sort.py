# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:43:43 2020

@author: LENOVO
"""

def InsertionSort(A,n):
    for i in range(1,n-1):
        value = A[i]
        dummy = i
        while (dummy>0 and A[dummy-1]>value):
            A[dummy] = A[dummy-1]
            dummy -= 1
        A[dummy] = value
    return print("Sorted List:", A)

A = list(map(int,input("Enter a list: ").split()))
n = len(A)
InsertionSort(A,n)