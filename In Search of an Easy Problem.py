# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:39:18 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
in2 = input().split()
list1 = []

for val in range(in1):
    input2 = int(in2[val])
    list1.append(input2)
for val2 in range(len(list1)):
    if list1[val2] == 1:
        flag = False
        break
        
    else:
        flag = True
if flag == True:
    print("EASY")
else:
    print("HARD")