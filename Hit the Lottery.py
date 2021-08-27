# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:09:50 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

count = 0
rem = 0
if in1 >= 100:
    x = in1 // 100
    #print(x)
    count += x
    in1 = in1%100
    #print(in1)
if in1 >= 20:
    #y = rem // 20 
    y = in1 // 20
    count += y
    in1 = in1%20
    #print(in1)

if in1 >= 10:
    #y = rem // 10 
    y = in1 // 10
    count += y
    in1 = in1%10
    
if in1 >= 5:
    #y = rem // 5 
    y = in1 // 5
    count += y
    in1 = in1%5
    #print(in1)
    
if in1 >= 1:
    #y = rem // 1
    y = in1 // 1
    count += y
    in1 = in1%1
    
print(count)
