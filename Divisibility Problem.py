# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 11:19:36 2021

@author: Easin
"""
import math
in1 = input()
in1 = int(in1)

for elem in range(in1):
    in2 = input().split()
    a = int(in2[0])
    b = int(in2[1])
    
    if a%b != 0:
        x = a % b
    
        y = b-x
        #z = math.ceil(y*b)
        print(y)

    else:
        x = int(a/b)
        print(0)
    
