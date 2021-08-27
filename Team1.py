# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:45:35 2021

@author: Easin
"""
input1 = int(input())
count = 0
for elm in range(input1):
    P,V,T = input().split()
    if (P =="1" and V =="1" and T =="0"):
        count += 1
    if (P =="1" and V =="1" and T =="1"):
        count += 1
    if (P == "1" and V =="0" and T =="1"):
        count += 1
    if (P == "0" and V =="1" and T =="1"):
        count += 1
    #print("count",count)
print(count)
