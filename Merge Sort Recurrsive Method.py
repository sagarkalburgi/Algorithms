# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:20:02 2020

@author: LENOVO
"""

#def TwoListMergeSort(L,R,C):
#    i,j,k = 0,0,0
#    nl = len(L)
#    nr = len(R)
#    C = [None] * (nl+nr)
#    while (i<nl and j<nr):
#        if L[i] < R[j]:
#            C[k] = L[i]
#            i += 1
#        else:
#            C[k] = R[j]
#            j += 1
#        k += 1
#    for i in range(i,nl):
#        C[k] = L[i]
#        k += 1
#    for j in range(j,nr):
#        C[k] = R[j]
#        k += 1
#    return print("Sorted List:", C)

def MergeSortRec(A):
    n = len(A)
#    if n < 2:
#        return print(A)
    if n > 1:
        
        mid = n//2
        left = A[:mid]
        #print(left)
        right = A[mid:n]
        #print(right)
        MergeSortRec(left)
        MergeSortRec(right)
        
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
            
        for i in range(i,len(left)):
            A[k] = left[i]
            k += 1
        for j in range(j,len(right)):
            A[k] = right[j]
            k += 1
        return print("Sorted List: ", A)
#            
        #TwoListMergeSort(left,right,A)
    
A = list(map(int, input("Enter 'A' List: ").split()))
MergeSortRec(A)
#TwoListMergeSort(A,B,m,n)