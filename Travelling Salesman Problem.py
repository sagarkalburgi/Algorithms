# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:18:13 2020

@author: LENOVO
"""

def travelling_salesman_problem(graph, v, currPos, n, count, cost):
    # If last node is reached and it has  
    # a link to the starting node i.e  
    # the source then keep the minimum  
    # value out of the total cost of  
    # traversal and "ans" 
    # Finally return to check for  
    # more possible values
    if count == n and graph[currPos][0]:
        answer.append(cost + graph[currPos][0])
        return
    
    # Backtracking step
    for i in range(n):
        if v[i] == False and graph[currPos][i]:
            # Marked as visited
            v[i] = True
            travelling_salesman_problem(graph, v, i, n, count+1, cost+graph[currPos][i])
            # Mark ith node as unvisited
            v[i] = False
            
n = 4
graph = [[0,10,15,20],
         [5,0,9,10],
         [6,13,0,12],
         [8,8,9,0]]

v = [False for i in range(n)]

v[0] = True

answer = []

travelling_salesman_problem(graph, v, 0, n, 1, 0)

print(min(answer))