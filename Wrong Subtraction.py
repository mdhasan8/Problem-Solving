# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:54:00 2021

@author: Easin
"""

n,k= input().split()
n = int(n)
k = int(k)

while k>0:
    k = k-1
    if n % 10 == 0:
        n = n//10
    else:
        n = n-1
print(n)