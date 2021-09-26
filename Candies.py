# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:27:12 2021

@author: Easin
"""
t = input()
t = int(t)
for val in range(t):
    
    n = input()
    n = int(n)
    
    k = 2
    x = 1
    f = 1
    while f != n:
        f = f+(2**(k-1))
        if n % f == 0:
            print(int(n/f))
            break
        else:
            k = k+1
        
        
    
    