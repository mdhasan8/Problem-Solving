# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:22:15 2021

@author: Easin
"""

a,b = input().split()

a = int(a)
b = int(b)

if a>b :
    print(b, end=" ")
    res = (a-b)//2
    print(res)
elif a <b:
    print(a, end = " ")
    res = (b-a)//2
    print(res)
elif a==b:
    print(a, end = " ")
    print(0)
    
    
