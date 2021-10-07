# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:17:23 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
in2 = input().split()
list1 = []

for elem in range(len(in2)):
    x = in2[elem]
    list1.append(int(x))
    
in3 = input()
in3 = int(in3)
list1.sort()
for elem in range(in3):
    in4 = input()
    in4 = int(in4)
    
    first = 0
    end = len(list1)-1
    mid = (first + end)//2
    
    while mid < len(list1) and mid >= 0 :
        if (list1[mid] <= in4 and (len(list1) > mid+1 and list1[mid+1] > in4) or len(list1) <= mid):
            #for vals in range(mid+1,len(list1)):
            #    if list1[vals] != in4:
                
            break
        #else:
        #    mid = mid +1
        #   break
        if list1[mid] <= in4:
            first = mid +1
            mid = (first + end)//2
            
        elif list1[mid] >= in4:
            end = mid -1
            mid = (first + end)//2
        if first > end:
            break
    print(mid+1)
            