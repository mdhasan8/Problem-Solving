# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:33:12 2021

@author: Easin
"""

in1 = input().split()

in2 = input().split()

for eleme in range(len(in1)):
    in1[eleme] = int(in1[eleme])
    
for elem in range(len(in2)):
    in2[elem] = int(in2[elem])
#print(in1)

in2.sort()
#print(in2)
n = in1[0]

list2 = []
for val in range(len(in2)-n+1):
    res = in2[val + n-1] - in2[val +0]
    list2.append(res)
xx = min(list2) 
print(xx)
    