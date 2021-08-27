# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:19:20 2021

@author: Easin
"""

n,m = input().split()
n = int(n)
m = int(m)
list1 = []
in2 = input().split()
for elem in range(len(in2)):
    list1.append(int(in2[elem]))
#print(list1)

count = 0
pos = 1
for val in range(len(list1)):
    if list1[val] > pos:
        count += list1[val] - pos
        pos = list1[val]
        
    elif list1[val] < pos:
        count += n - pos
        count += list1[val] - 1 +1
        pos = list1[val]
    
        
print(count)
        