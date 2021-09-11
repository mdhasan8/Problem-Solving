# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:20:27 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()
list1 = []

for elem in range(len(in2)):
    x = in2[elem]
    list1.append(int(x))
count_1 = 0
count_2 = 0
count_3 = 0

for val in range(len(list1)):
    if list1[val] == 1:
        count_1 +=1
    elif list1[val] == 2:
        count_2 += 1
    elif list1[val] == 3:
        count_3 +=1
m = min(count_1,count_2,count_3)
print(m)
list2 = []
for val1 in range(len(list1)):
    if list1[val1] == 1:
        list2.append(val1+1)
        #print(list2)
list3 = []
for val1 in range(len(list1)):       
    if list1[val1] == 2:
        list3.append(val1+1)
        #print(list3)
list4 = []
for val1 in range(len(list1)):        
    if list1[val1] == 3:
        list4.append(val1+1)
        #print(list4)
for vals in range(m):
    print(list2[vals],list3[vals],list4[vals])
    
        


