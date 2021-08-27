# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 09:25:41 2021

@author: Easin
"""

n,k = input().split()
k = int(k)
count = 0
a = input().split()
for elm in range(len(a)):
    
    a[elm] = int(a[elm])
    
    if int(a[k-1]) <= a[elm] and a[elm]:
        count += 1
        
print(count)
