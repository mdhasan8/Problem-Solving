# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:51:20 2021

@author: Easin
"""
input1 = int(input())
in1 = input()
count = 0
for elem in range(len(in1)-1):
    if in1[elem] == in1[elem+1]:
        count += 1
print(count)
        