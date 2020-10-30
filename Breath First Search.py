# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:58:35 2020

@author: LENOVO
"""

def bfs(graph, start, path=[]):
    q = [start]
    while q:
        v = q.pop(0)
        if not v in path:
            path = path+[v]
            q = q+graph[v]
    return path
    
                
graph = {1:[2,4],
         2:[3,5,7,8],
         3:[2,4,10,9],
         4:[1,3],
         5:[2,6,7,8],
         6:[5],
         7:[2,5,8],
         8:[2,5,7],
         9:[3],
         10:[3]}
print("Breath First Path is: ",bfs(graph,1))