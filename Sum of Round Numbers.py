# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:19:08 2021

@author: Easin
"""

t = input()
t = int(t)
for elem in range(t):
    in1 = input()
    in1 = int(in1)
    list1 = []
    qu = in1
    rem1 = 1
    count = 0
    while qu !=0:
        rem = qu % 10
        qu = qu // 10
        
        #print(qu)
        if rem*rem1 != 0:
            list1.append(rem*rem1)
            count +=1    
        rem1 = rem1*10
    print(count)
    for val in range(len(list1)):
    
        print(list1[val])