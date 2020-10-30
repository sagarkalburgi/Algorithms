# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:45:39 2020

@author: LENOVO
"""

def isSafe(graph,color):
    for i in range(V):
        for j in range(i+1,V):
            if graph[i][j] and color[j] == color[i]:
                return False
    return True
    
def graphColoring(graph,m,i,color):
    
    if i == V:
        if isSafe(graph,color):
            printsolution(color)
            return True
        return False
    
    for j in range(0,m):
        color[i] = j
        if graphColoring(graph,m,i+1,color):
            return True
        
        color[i] = 0
    return False

def printsolution(color):
    print("Solution Exists: ")
    for i in range(V):
        print(" ",color[i]+1)

graph = [[0,1,1,1],
         [1,0,1,0],
         [1,1,0,1],
         [1,0,1,0]]
m = 3
V = 4
color = [[0 for x in range(V)]for x in range(V)]

graphColoring(graph,m,0,color)