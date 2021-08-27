# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 12:03:34 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
in2 = input().split()
count = 1
variable = 1
for elem in range(len(in2)-1): 
    #6print(count)
    
    if int(in2[elem]) <= int(in2[elem+1]):
        count += 1
    else:
        count = 1
    if count > variable:
        variable = count
        
print(variable)
        
    