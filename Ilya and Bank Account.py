# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:23:31 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
list1 = []
if in1 >= 0:
    print(in1)
else:
    x = abs(in1)//10
    list1.append(-x)
    y = abs(in1) % 10
    #print(y)
    z = abs(in1)//100
    #print(z)
    m = str(z)+str(y)
    list1.append(-int(m))
    print(max(list1))