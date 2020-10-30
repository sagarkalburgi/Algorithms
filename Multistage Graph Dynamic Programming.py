# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 11:11:45 2020

@author: LENOVO
"""
n = 8
INF = 9999999

graph = [[INF,INF,2,1,3,INF,INF,INF],
         [INF,INF,INF,INF,2,3,INF,INF],
         [INF,INF,INF,INF,6,7,INF,INF],
         [INF,INF,INF,INF,6,8,9,INF],
         [INF,INF,INF,INF,INF,INF,INF,6],
         [INF,INF,INF,INF,INF,INF,INF,4],
         [INF,INF,INF,INF,INF,INF,INF,5]]

dist = [0] * n
#dist[n-1] = 0
P = []
for i in range(n-2,-1,-1):
    
    dist[i] = INF
    
    for k in range(n):
        
        if graph[i][k] == INF:
            continue
        
        dist[i] = min(dist[i],graph[i][k]+dist[k])

#P = [1,0,0,n]
#for i in range(2,3):
#    P[i] = dist[P[i-1]]
print("Minimum total weight:",dist[0])
