# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:59:00 2020

@author: LENOVO
"""

def BinSearch(A,n,key):
    low, high = 0, n
    while (low <= high):
        mid = (low+high)//2
        if key == A[mid]:
            return print("Key found in", mid,"index")
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return print("Key", key, "not found in the list.")

A = list(map(int, input("Enter the Array: ").split()))
A.sort()
n = len(A)
key = int(input("Enter the key element to be found: "))
BinSearch(A,n,key)