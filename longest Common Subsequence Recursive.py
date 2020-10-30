# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:46:56 2020

@author: LENOVO
"""

def longest_common_subsequence(A,B,i,j):
    if i == 0 or j == 0:
        return 0
    elif A[i-1] == B[j-1]:
        return 1 + longest_common_subsequence(A,B,i-1,j-1)
    else:
        return max(longest_common_subsequence(A,B,i-1,j), longest_common_subsequence(A,B,i,j-1))
        
string1 = list(input("Enter string 1: "))
string2 = list(input("Enter string 2: "))
print("The Longest Common Subsequence is:", longest_common_subsequence(string1,string2,len(string1),len(string2)))