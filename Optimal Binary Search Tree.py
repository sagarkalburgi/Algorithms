# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:22:29 2020

@author: LENOVO
"""

def optimal_binary_search_tree(key, freq, n):
    cost = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(n):          # Single key cost is equal to frequency of the key
        cost[i][i] = freq[i]
        
    for L in range(2,n+1):      # Lenght 2,3,... L chain lenght
        for i in range(n-L+2):  # Row number in cost
            j = L          # Get column number j from i and l
            if i>=n or j>=n:
                break
            cost[i][j] = 99999999
            
            for r in range(i,j+1):  # try making all in interval keys[i,,,j] as roots
                c = 0               # c is the cost when keys[r] becomes root of a sub tree
                if r>i:
                    c += cost[i][r-1]
                if r<j:
                    c += cost[r+1][j]
                c += sum(freq,i,j)
                if c<cost[i][j]:
                    cost[i][j] = c
    return cost[0][n-1]

def sum(freq,i,j):                  # sum of array functions freq[i] to freq[j]
    s = 0
    for k in range(i,j+1):
        s += freq[k]
    return s

keys = [10,20,30,40]
freq = [14,25,16,31]
n = len(keys)
print("Cost of Optimal BST is:", optimal_binary_search_tree(keys,freq,n))