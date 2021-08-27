# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:35:15 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
in2 = input()
in2 = int(in2)
in3 = input()
in3 = int(in3)

x1 = (in1+in2)*in3
x2 = (in1*in2)*in3
x3 = (in1+in2)+in3
x4 = (in1*in2)+in3
x5 = in1*(in2+in3)
print(max(x1, x2, x3, x4,x5))
'''
if x1 > x2:
    print(x1)
if x1 < x2:
    print(x2)
'''    