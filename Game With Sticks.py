# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:52:12 2021

@author: Easin
"""

n,m = input().split()
n = int(n)
m = int(m)

if n % 2 == 0 and m%2 == 0 and n ==m:
    print("Malvika")
if n % 2 != 0 and m%2 != 0 and n ==m:
    print("Akshat")
    
if n < m and n % 2 == 0:
    print("Malvika")
    
if n > m and m % 2 == 0:
    print("Malvika")
    
if n < m and n % 2 != 0:
    print("Akshat")
    
if n > m and m % 2 != 0:
    print("Akshat")
    
    
    