# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 12:01:02 2021

@author: Easin
"""

in1 = input()

#print(in1)
count = 0
list1 = []
list2 = []
for values in range(len(in1)):
    if in1[values] >= 'a' and in1[values] <= 'z':
        list1.append(in1[values])
flag = True        
for elem in range(len(list1)):
    for val in range(elem,len(list1)-1):
        
        if list1[elem] == list1[val+1]:
            flag = False
            break
        
    if flag == True:
        count += 1
    flag = True
print(count)
            
    