# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:42:52 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
in2 = input().split()

count = 0
for val in range(len(in2)):
    
    count += int(in2[val])
    
total = count/in1
print(total)