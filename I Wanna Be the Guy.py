# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:10:50 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()
in3 = input().split()

list1 = []

for elem in range(len(in2)-1):
    list1.append(in2[elem+1])
for val in range(len(in3)-1):
    list1.append(in3[val+1])    
print(list1)
list2 = []
for vals in range(in1):
    list2.append(0)
flag = True
print(list2)
for val1 in range(len(list1)):
    print(int(list1[val1])-1)
    list2[int(list1[val1])-1] = 1
    
print("new list2",list2)
for val2 in range(len(list2)):
    if list2[val2] == 0:
       flag = False 
#flag = False
#for val1 in range(len(list1)):
#    for val2 in range(len(list2)):
#        if list1[val] != list2[val2]:
#            flag = True
#            break



if flag == True:
    print("I become the guy.")
else:
    print( "Oh, my keyboard!" )
            
#for elements in range(len(list1)):
    