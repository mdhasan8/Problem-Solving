# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:20:06 2021

@author: Easin
"""

in1 = input()

list1 = []

for elem in range(len(in1)):
    if in1[elem] != "+":
        list1.append(in1[elem])
#print(list1)
list1.sort()
str1 = ""
for elem in range(len(list1)):
    str1 += list1[elem]+ "+" 
print(str1[:-1])