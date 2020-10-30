# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:17:14 2020

@author: LENOVO
"""

def sum_of_subset(set, n, sum):
    subset = ([[False for i in range(sum+1)] for i in range(n+1)])
    
    # If sum is zero answer is true
    for i in range(n+1):
        subset[i][0] = True
    
    # If sum is not zero and set is empty answer is False
    for i in range(n+1):
        subset[0][i] = False
    
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i-1][j-set[i-1]])
            
    return subset[n][sum]
    
    
set = [1,2,3,4]
sum = 5
n = len(set)
if sum_of_subset(set,n,sum) == True:
    print("Found a sunset")
else:
    print("Subset not found")