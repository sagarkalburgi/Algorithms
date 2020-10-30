# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:30:44 2020

@author: LENOVO
"""

def KMPsearch(pattern, text):
    M = len(pattern)
    N = len(text)
    lps = [0] * M
    j = 0
    computeLPS(pattern, M, lps)
    i = 0
    x = 0
    while i<N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            print("Found the pattern at index:", i-j)
            j = lps[j-1]
            return           
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        x += 1
    if i>=N and x != 0:
        print("Pattern Not Found")

def computeLPS(pattern, M, lps):
    length = 0
    lps[0] = 0
    i = 1
    
    while i<M:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
pattern = "ab"
KMPsearch(pattern, text)