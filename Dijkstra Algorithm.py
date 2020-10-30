# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:35:11 2020

@author: LENOVO
"""

def dijkstra(graph, start, goal):
    shortest_distance = {}      # Creating dictionary for shortest distance
    predecessor = {}            # Creating dictionary for storing the predecessor vertices(nodes)
    unseenNodes = graph
    infinity = 999999           
    path = []                   # Path
    
    # Setting the start node to zero weight and rest all to infinity
    
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    
    # Going through all the nodes and finding the one with shortest distance. 
    
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        
        # Relaxation
        
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)        # For exiting the graph by removing the nodes
        
    # Tracing back to the original(start) node
        
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print("Path not reachable")
            break
        
    # Printing out the path and weight    
        
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print("Shortest Distance is: ", str(shortest_distance[goal]))
        print("The path is: ", str(path))
        

graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
dijkstra(graph, 'a', 'b')