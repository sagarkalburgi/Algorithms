# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:07:41 2020

@author: LENOVO
"""

def sum_of_subsets(set,n,sum):
    # Best case
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    # Ignore if last element is greater than sum
    if set[n-1] > sum:
        return sum_of_subsets(set,n-1,sum)
    # Else check for sum including the last element and excluding last element
    return sum_of_subsets(set,n-1,sum) or sum_of_subsets(set,n-1,sum-set[n-1])

set = [5,10,12,13,15,18]
sum = 30
n = len(set)
if sum_of_subsets(set, n, sum) == True:
    print("Found a subset with given sum: ")
else:
    print("No subset with given sum")