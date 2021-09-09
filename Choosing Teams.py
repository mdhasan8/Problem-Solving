# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:10:19 2021

@author: Easin
"""

n,k = input().split()
n = int(n)
k = int(k)
in2 = input().split()

list1 = []
for elem in range(len(in2)):
    x = in2[elem]
    list1.append(int(x))
count = 0
for val in range(len(list1)):
    m = 5 - list1[val]
    if m >= k:
        count+=1
print(count //3)
        
 
    
