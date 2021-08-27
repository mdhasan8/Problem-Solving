# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:33:53 2021

@author: Easin
"""

in1 = input()
in2 = input()
str1 = ""
for elem in range(len(in1)):
    #for val in range(len(in2)):
    if in1[elem] == in2[elem]:
        str1 += "0"
    else:
        str1+= "1"
print(str1)
        