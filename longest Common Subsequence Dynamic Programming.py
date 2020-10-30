# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 18:29:19 2020

@author: LENOVO
"""

def longest_common_subsequence(A,B):
    m = len(A)
    n = len(B)
    lcs = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif A[i-1] == B[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
    
    i,j = m,n
    count = lcs[m][n]
    sequence_list = []
    while i>=0 and j>=0 and count != 0:
        if lcs[i][j] == lcs[i-1][j]:
            i -= 1
        else: 
            sequence_list.append(A[i-1])
            j-=1
            i-=1
            count -= 1
    sequence_list = sequence_list[::-1]
    return lcs[m][n], sequence_list
        
string1 = list(input("Enter string 1: "))
string2 = list(input("Enter string 2: "))
print("The Longest Common Subsequence is:", longest_common_subsequence(string1,string2))