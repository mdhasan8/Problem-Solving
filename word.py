# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:11:06 2021

@author: Easin
"""

in1 = input()
upper = 0
lower = 0
for elem in range(len(in1)):
    if in1[elem] == in1[elem].upper():
        upper += 1
    elif in1[elem] == in1[elem].lower():
        lower += 1


if upper > lower:
    x = in1.upper()
else:
    x = in1.lower()
    
print(x)