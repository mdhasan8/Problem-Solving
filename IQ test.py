# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:12:31 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()
list1 = []
list2 = []
for elem in range(len(in2)):
    #print(in2[elem])
    if int(in2[elem]) % 2 == 0:
        list1.append(in2[elem])
    else:
        list2.append(in2[elem])
#print(list1)
#print(list2)
od = ''
eve = ''
if len(list1) > len(list2):
    eve = list2[0]
else:
    od = list1[0]
#print(eve)

for val in range(len(in2)):
    if in2[val] == eve:
        print(val+1)
    elif in2[val] == od:
        print(val+1)
    
    

        