# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:41:21 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
count = 0
list1 = []
for elem in range(in1):
    list1.append(input().split())
#print(list1)

for val in range(len(list1)):
    for val2 in range(0,in1):
        #print(list1[val][0])
        #print(list1[val2][1])
        if list1[val][0] == list1[val2][1]:
            count += 1
print(count)
    
    
    
#list1[0][1], list1[1][1], list1[2][1]