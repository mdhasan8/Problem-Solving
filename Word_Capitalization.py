# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:34:40 2021

@author: Easin
"""

in1 = input()
x = in1[0].upper()
str1 = x
for elem in range(len(in1)-1):
    str1 += in1[elem+1]
print(str1)