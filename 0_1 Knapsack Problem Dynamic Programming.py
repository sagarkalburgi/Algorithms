# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 21:00:09 2020

@author: LENOVO
"""

def knapsack(profit, weight, k, n):
    
    for i in range(n):
        for w in range(kweight+1):
            if (i == 0 or w == 0):
                continue
            elif weight[i] <= w:
                k[i][w] = max(profit[i] + k[i-1][w-weight[i]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
    
    i,j = n-1,kweight
    while i>=0 and j>=0:
        if k[i][j] == k[i-1][j]:
            print(profit[i],"= Not Selected")
            i -= 1
        else:
            print(profit[i],"= Selected")
            j = j-weight[i]
            i -= 1


profit = [0,1,2,5,6]
weight = [0,2,3,4,5]
kweight = 8
n = len(profit)
k = [[0 for x in range(kweight+1)] for x in range(len(profit))]
knapsack(profit, weight, k, n)