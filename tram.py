# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 12:10:10 2021

@author: Easin
"""
in1 = input()
in1 = int(in1)
list1 = [0]

for val in range(in1):
    n,k= input().split()
    n = int(n)
    k = int(k)
    list1.append(k-n+list1[-1]) 
print(max(list1))
    
'''
    1st = k-n + 0
    2nd = k-n+1st
    3rd = k-n+2nd
    4th = k-n+3rd
    last = 4th+k-n
    seat = k-n + sum(0,n)
'''