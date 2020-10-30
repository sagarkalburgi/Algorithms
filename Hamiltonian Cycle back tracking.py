# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:46:50 2020

@author: LENOVO
"""

class Graph():
    
    def __init__(self, vertices):
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]
        self.V = vertices
        
    def isSafe(self,v,pos,path):
        # Check if the vertex is adjacent
        if self.graph[path[pos-1]][v] == 0:
            return False
        # Check if it is not already in path
        for vertex in path:
            if vertex == v:
                return False
            
        return True
    
    def hamiltoniancycle(self,path,pos):
        # all the vertices must be included in the path
        if pos == self.V:
            #last and first vertex must have a path
            if self.graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False
            
        # Try different vertices n!
        for v in range(1,self.V):
            if self.isSafe(v,pos,path) == True:
                path[pos] = v
                if self.hamiltoniancycle(path,pos+1) == True:
                    return True
                path[pos] = -1
        return False
    
    def hamcycle(self):
        path = [-1] * self.V
        # Vertex first as starting point
        path[0] = 0
    
        if self.hamiltoniancycle(path,1) == False:
            print("Solution does not exist")
            return False
        self.printsolution(path)
        return True
    
    def printsolution(self,path):
        print("Solution Exists as follows: ")
        for vertex in path:
            print(vertex)
        print(path[0])
        
g = Graph(5)
g.graph = [[0,1,1,0,1],
           [1,0,1,1,1],
           [1,1,0,1,0],
           [0,1,1,0,1],
           [1,1,0,1,0]]
g.hamcycle()