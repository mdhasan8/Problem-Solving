# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:45:26 2021

@author: Easin
"""
import math
n,m,a,b = input().split()
n = int(n)
m = int(m)
a = int(a)
b = int(b)

x = b/m
#print(x)

if x ==a:
    print(n*a)
elif x <a:
    p = n%m
    #print(p)
    q = n-p
    #print(q*x)
    c1 = (q*x) + (p*a)
    c2 = (q+m)*x #math.ceil(n*x)
    #print(c1)
    #print(c2)
    if c1 < c2:
        print(int(c1))
    else:
        print(int(c2))
elif x > a:
    print(n*a)
    
    