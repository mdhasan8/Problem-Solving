# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 12:10:17 2021

@author: Easin
"""

t = input()
t = int(t)
for val in range(t):
    in2 = input()
    
    str1 = in2[0]
    for elem in range(len(in2)):
        if elem %2 ==0:
            str1 +=in2[elem+1]
    print(str1)
    
    