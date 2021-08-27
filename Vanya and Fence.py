# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 11:22:00 2021

@author: Easin
"""

n,h = input().split()
n = int(n)
h = int(h)
in2 = input().split()
list1 = []
for elem in range(n):
    input2 = int(in2[elem])
    list1.append(input2)
#print(list1)
count1 = 0
count2 = 0
for val in range(len(list1)):
    if list1[val] > h:
        count1 += 1
    else:
        count2 += 1

value =(count1*2)+(count2*1)
print(value)
    