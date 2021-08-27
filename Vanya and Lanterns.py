# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 11:43:43 2021

@author: Easin
"""

n,l = input().split()
n = int(n)
l = int(l)

#for elem in range(n):
in2 = input().split()
    #in2 = int(in2)
#print(in2)
list1 = []
for elem in range(len(in2)):
    list1.append(int(in2[elem]))
list1.sort()

list2 = []
for val in range(len(list1)-1):
    diff = list1[val+1] - list1[val]
    list2.append(diff)
maxim = max(list2)
fin = maxim /2
if list1[0] >= fin:
    fin = list1[0]-0
if list1[-1] >= fin:
    fin = l -list1[-1]
print(fin)