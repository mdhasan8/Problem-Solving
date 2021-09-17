# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:31:38 2021

@author: Easin
"""
in1 = input()
t = int(in1)
for elem in range(t):
    
    x,y,n = input().split()
    x = int(x)
    y = int(y)
    n = int(n)
    
    
    if (n-y) >= (n//x)*x:
        p = (n//x)
        q = x*p+y
    else:
        p = (n//x)-1
        q = x*p+y
    
    if x > n:
        q = y
    elif p>0:
        q = q
    print(q)
    



    