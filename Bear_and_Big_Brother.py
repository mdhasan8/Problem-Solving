# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:43:06 2021

@author: Easin
"""

a,b= input().split()
a = int(a)
b = int(b)

iteration = 0
while a <= b:
    a = 3*a
    b = 2*b
    iteration += 1
print(iteration)
    