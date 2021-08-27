# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:40:32 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
if in1%2 == 0:
    in1 = in1//2 
else:
    in1 = -(in1//2) -1
print(in1)
'''
def func(in1):
    val = 0
    for elem in range(in1):
        val1 = pow(-1,elem+1)*(elem+1)
        val += val1
    return val

print(func(in1))
'''  
# -1,1,-2,2,-3,3,-4,4,-5,5  ......
#1,2,3,4,5,6,7,8