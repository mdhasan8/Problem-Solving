# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:02:55 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()
list1 = []

for elem in range(len(in2)):
    x = in2[elem]
    list1.append(int(x))
#print(list1)
list1.sort(reverse=True)
#print(list1)
m = list1[0]
p =0
for val in range(len(list1)):
    
    q = abs(list1[val] - m)
    p = p + q
    
print(p)