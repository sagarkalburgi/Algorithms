# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:32:08 2020

@author: LENOVO
"""

# Prim's Algorithm in Python

INF = 999999
V = 5       # Number of Vertices
G = [[0, 9, 75, 0, 0],          # Graph with five vertices and weights of its edges connected. 0  ---> not connecetd to the vertice
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

selected = [0] * V      # Array to track selected vertices. If selected 1(True) else 0(False)

total_weight = 0

no_edge = 0     # number of edges initially zero

selected[0] = True      # Oth vertice selected

while (no_edge < V-1):      # Total number of edges V-1
    minimum = INF
    x, y = 0,0
    for i in range(V):
        for j in range(V):
            if ((not selected[j]) and G[i][j]):      # Not in selected and there is an edge
                if minimum > G[i][j]:      
                    minimum = G[i][j]
                    x = i
                    y = j
    print("Edge "+ str(x)+ "--"+str(y)+" Weight-"+str(G[x][y]))
    total_weight += G[x][y]
    selected[y] = True
    no_edge += 1
print("Total Weight - ",total_weight)