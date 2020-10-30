# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:22:36 2020

@author: LENOVO
"""
d = 10
def rabin_karp(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p=t=i=j=0
    h =1
    
    for i in range(m-1):
        h = (h*d) % q
        
    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
        
    # find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("Pattern found in index:", i+1)
            
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
            
            if t < 0:
                t = t+q
    
text = "abcddaefg"
pattern = "cdd"
q = 13
rabin_karp(pattern,text,q)