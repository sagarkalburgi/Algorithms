# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:24:58 2020

@author: LENOVO
"""

def TwoListMergeSort(A,B,m,n):
    i = 0
    j = 0
    k = 0
    C = [None] * (n+m)
    while (i<m and j<n):
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1
    for i in range(i,m):
        C[k] = A[i]
        k += 1
    for j in range(j,n):
        C[k] = B[j]
        k += 1
    return print("Sorted List:", C)

A = list(map(int, input("Enter 'A' List: ").split()))
A.sort()
B = list(map(int, input("Enter 'B' List: ").split()))
B.sort()
m = len(A)
n = len(B)
TwoListMergeSort(A,B,m,n)