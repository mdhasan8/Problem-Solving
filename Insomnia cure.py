# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:03:43 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)


in2 = input()
in2 = int(in2)

in3 = input()
in3 = int(in3)

in4 = input()
in4 = int(in4)

in5 = input()
in5 = int(in5)

list1 = []

for elem in range(in5+1):
    list1.append(0)
#print(list1)

tot = 1
while tot*in1 <= in5:
    
    list1[tot*in1] = 1
    tot +=1
    
tot = 1
while tot*in2 <= in5:
    
    list1[tot*in2] = 1
    tot +=1
    
tot = 1
while tot*in3 <= in5:
    
    list1[tot*in3] = 1
    tot +=1
    
tot = 1
while tot*in4 <= in5:
    
    list1[tot*in4] = 1
    tot +=1

count = 0
#print(len(list1))
for val in range(1,len(list1)):
    if list1[val] == 1:
        count += 1
print(count)
    