# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:07:33 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()

val = 0
element = 0
for elem in range(len(in2)):
    if int(in2[elem]) > val:
        val = int(in2[elem])
        element = elem
        
val1 = 100
element1 = 100
for elem1 in range(len(in2)):
    if int(in2[elem1]) <= val1:
        val1 = int(in2[elem1])
        element1 = elem1

count = in1 - element1 -1


if element < element1:
    total = element + count
else:
    total = element + count -1
    
#print(count)
#4print(element)
print(total)

        
        