# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:51:48 2020

@author: LENOVO
"""

def JobSequenceDeadline(P,D,fd):
    for j in range(0,len(P)):
        for i in range(0,len(P)-1-j):
            if P[i] < P[i+1]:
                P[i],P[i+1] = P[i+1],P[i]
                D[i],D[i+1] = D[i+1],D[i]
            
    result = [0] * fd
    slot = [-1]*fd
    total = 0
    for i in range(len(P)):
        for j in range(min(fd-1,D[i]-1),-1,-1):
            if result[j] == 0:
                result[j] = 1
                print("Job with profit",P[i],"selected")
                slot[j] = P[i]
                total += P[i]
                break
    print("Jobs selected: ",slot)
    print("Maximum total profit: ",total)
    return

P = list(map(int,input("Enter the Profit of the Jobs: ").split()))
D = list(map(int,input("Enter the Deadlines of the Jobs: ").split()))
fd = int(input("Enter the final deadline: "))
JobSequenceDeadline(P,D,fd)