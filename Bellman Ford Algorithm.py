# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:53:00 2020

@author: LENOVO
"""

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices           # Total number of vertices in the graph
        self.graph = []             # Array of edges
        
    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
        
    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
        
        
    def bellman_ford(self, src):
        
        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        
        # Mark the source vertex
        dist[src] = 0
        
        # Step 2: Relax edges |V| - 1 times
        for _ in range(self.V-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        # Step 3: Detect negative cycle
        # If value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return
            
        # If no negative cycle found print the results
        self.print_solution(dist)
        
g = Graph(5)
g.add_edge(0, 1, -1)  
g.add_edge(0, 2, 4)  
g.add_edge(1, 2, 3)  
g.add_edge(1, 3, 2)  
g.add_edge(1, 4, 2)  
g.add_edge(3, 2, 5)  
g.add_edge(3, 1, 1)  
g.add_edge(4, 3, -3)  

g.bellman_ford(0)