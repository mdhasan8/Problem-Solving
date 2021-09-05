# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 11:19:30 2021

@author: Easin
"""

in1 = input().split()

list1 = []
for elem in range(len(in1)):
    list1.append(int(in1[elem]))
#print(list1)
maxm = max(list1)
list2=[]
for val in range(len(list1)):
    if list1[val] != maxm:
        out = maxm - list1[val]
        list2.append(out)
        print(out)