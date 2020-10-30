# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:03:58 2020

@author: LENOVO
"""

def RecBinSearch(low,high,key):
    if low == high:
        if A[low] == key:
            return print("Key found in", low, "index")
        else:
            return print("Key",key,"not found")
    else:
        mid = (low + high)//2
        if key == A[mid]:
            return print("Key found in", mid,"index")
        elif key < A[mid]:
            return RecBinSearch(low,mid-1,key)
        else:
            return RecBinSearch(mid+1,high,key)
        
A = list(map(int, input("Enter the Array: ").split()))
A.sort()
low = 0
high = len(A)
key = int(input("Enter the key element to be found: "))
RecBinSearch(low,high,key)