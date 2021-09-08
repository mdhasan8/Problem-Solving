# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:36:57 2021

@author: Easin
"""

x,y,z = input().split()
x = int(x)
y = int(y)
z = int(z)

list1 = []

m = abs(x-y)
n = abs(x-z)
list1.append(m+n)

m = abs(y-x)
n = abs(y-z)
list1.append(m+n)

m = abs(z-x)
n = abs(z-y)
list1.append(m+n)
    
print(min(list1))