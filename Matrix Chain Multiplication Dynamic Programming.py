# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:38:53 2020

@author: LENOVO
"""

P = [5,4,6,2,7]
n = 5
m = [[0 for x in range(n)] for x in range(n)]
s = [[0 for x in range(n)] for x in range(n)]
d = 1
    
for d in range(2,n):
    for i in range(1,n-d+1):
        j = i+d-1
        m[i][j] = 9999999
        for k in range(i,j):
            q = m[i][k] + m[k+1][j] + P[i-1]*P[k]*P[j]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
                    
print("M - Matrix: ",m[0])
print("            ",m[1])
print("            ",m[2])
print("            ",m[3])
print("            ",m[4])
print("")
print("S - Matrix: ",s[0])
print("            ",s[1])
print("            ",s[2])
print("            ",s[3])
print("            ",s[4])