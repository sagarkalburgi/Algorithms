# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:10:30 2020

@author: LENOVO
"""
cost = 0

def tsp_bb(c):
    cost = 0
    nearest_city = 9999
    minimum = 9999
    for count in range(limit):
        if matrix[c][count] != 0 and visited_cities[count] == 0:
            if matrix[c][count] < minimum:
                minimum = matrix[count][0] + matrix[c][count]
            temp = matrix[c][count]
            nearest_city = count
            
    if minimum != 9999:
        cost = cost + temp
    return nearest_city

def minimum_cost(city):
    cost = 0
    visited_cities[city] = 1
    print(city+1)
    nearest_city = tsp_bb(city)
    if nearest_city == 9999:
        nearest_city = 0
        print(nearest_city+1)
        cost = cost + matrix[city][nearest_city]
        return
    minimum_cost(nearest_city)
    
limit = 4
INF = 9999999
matrix = [[1,2,3,4],
          [5,6,7,8],
          [3,4,5,6],
          [9,8,4,3]]

visited_cities = [None for i in range(5*5)]
minimum_cost(0)
print(cost)