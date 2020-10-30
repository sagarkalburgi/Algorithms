# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:52:21 2020

@author: LENOVO
"""

def is_attack(i,j):
    # Checking rows and coloumns
    for k in range(0,N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
        
    # Checking Diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l == i+j) or (k-l == i-j):
                if board[k][l] == 1:
                    return True
    
    return False

def N_queen(n):
    # if n == 0 solution found
    if n==0:
        return True
    for i in range(0,N):
        # Checking if queen is not under attack or if we can place a queen
        for j in range(0,N):
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                # Recusion call for next queen
                if N_queen(n-1) == True:
                    return True
                board[i][j] = 0
    return False

N = int(input("Enter the Size of the board: "))
board = [[0]*N for _ in range(N)]
N_queen(N)
print("Solution:")
for i in board:
    print(i)