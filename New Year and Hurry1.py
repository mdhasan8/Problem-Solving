# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 11:58:10 2021

@author: Easin
"""

n,k = input().split()
n = int(n)
k = int(k)

total = 240

left = 240 -k
time = 0
for elem in range(n+1):
    
    time += 5*(elem+1)
     
    if left - time < 0:
        break
print(elem)


