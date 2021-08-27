# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 11:46:11 2021

@author: Easin
"""

n = input()
n = int(n)
count = 0
for elm in range(n):
    #print(elm)
    B = input()
    if (B == "X--" or B == "--X"):
        count -= 1
    if (B == "X++" or B == "++X"):
        count += 1
print(count)