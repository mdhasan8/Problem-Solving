# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 12:28:09 2021

@author: Easin
"""

input1 = int(input())

str1 = ""

for elm in range(input1):
    str1 = ""
    #print(elm)
    input2 = input()
    if len(input2) > 10:
        str1 += input2[0]
        str1 += str(len(input2)-2)
        str1 += input2[-1]
    print(str1)
    
    if len(input2) <= 10:
        print(input2)

