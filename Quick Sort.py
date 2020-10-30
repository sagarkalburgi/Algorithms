# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:47:11 2020

@author: LENOVO
"""

def QuickSort(A,low,high):
    if (low<high):
        j = Partition(A,low,high)
        QuickSort(A,low,j-1)
        QuickSort(A,j+1,high)
    #return A
        
def Partition(A,low,high):
    pivot = A[high]
    p_index = low
#    i = low
#    while (low<p_index):
#        while (A[i] <= pivot):
#            i += 1
#        while (A[p_index] > pivot):
#            p_index -= 1
#        if i<p_index:
#            A[i],A[p_index] = A[p_index],A[i]
#    A[high],A[p_index] = A[p_index],A[high]
#    return p_index
    for i in range(low,high):
        if A[i] < pivot:
            A[i],A[p_index] = A[p_index],A[i]
            p_index += 1
    A[p_index],A[high] = A[high],A[p_index]
    return p_index

A = list(map(int,input("Enter a list: ").split()))
low, high = 0,len(A)
QuickSort(A,low,high-1)
print("Sort list: ",A)