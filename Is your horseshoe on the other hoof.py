# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:50:36 2021

@author: Easin
"""

in1 = input().split()
#print(in1)
count = 0
in1.sort()
for elem in range(len(in1)-1):
    
    if in1[elem] == in1[elem+1]:
            count += 1
print(count)
    

