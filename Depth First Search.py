# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:07:09 2020

@author: LENOVO
"""

def dfs(graph, start, path=[]):
    path = path+[start]
    for node in graph[start]:
        if not node in path:
            path = dfs(graph, node, path)
    return path

graph = {1:set([2,4]),
         2:set([3,5,7,8]),
         3:set([2,4,10,9]),
         4:set([1,3]),
         5:set([2,6,7,8]),
         6:set([5]),
         7:set([2,5,8]),
         8:set([2,5,7]),
         9:set([3]),
         10:set([3])}
print("Depth First Search is: ",dfs(graph,1))