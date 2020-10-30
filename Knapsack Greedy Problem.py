# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:21:45 2020

@author: LENOVO
"""

def Knapsack(P,W,m):
    PbW = [None]*len(P)
    #IS = []
    TP = 0
    n = len(P)
    for i in range(0,n):
        PbW[i] = P[i]/W[i]
    PbW.sort(reverse = True)
    for i in range(0,n):
        if (m>0 and W[i]<=m):
            m = m-W[i]
            TP += P[i]
            print(" Item",i+1,"selected")
        elif (m>0 and W[i]>m):
            TP += P[i]*(m/W[i])
            print("",m/W[i]," of Item", i+1,"selected")
        else:
            break
    return print("Maximum Profit Obtainable: ", TP)

n = int(input("Enter the number of objects: "))
P = list(map(int,input("Enter the Profit/Value of the items: ").split()))
W = list(map(int,input("Enter the Weights of the items: ").split()))
m = int(input("Enter the max weight: "))
Knapsack(P,W,m)