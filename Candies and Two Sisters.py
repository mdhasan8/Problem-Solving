# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:02:07 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

for elem in range(in1):
    in2 = input()
    in2 = int(in2)
    #print("in2",in2)
    if in2 % 2 == 0 and in2 != 1 and in2 != 2 and in2 != 3:
        res = (in2 //2)-1
        print(res)
    elif in2 == 1:
        print("0")
    elif in2 == 3:
        print("1")
    elif in2 == 2:
        print("0")
    
    else:
        res = in2//2
        print(res)
        