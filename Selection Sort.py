# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:47:51 2020

@author: LENOVO
"""

def SelectionSort(A,n):
    for i in range(0,n):
        i_min = i
        for j in range(i+1,n):
            if A[j] < A[i_min]:
                i_min = j
        A[i], A[i_min] = A[i_min], A[i]
    return print("Sorted List:",A)

A = list(map(int,input("Enter a list: ").split()))
n = len(A)
SelectionSort(A,n)