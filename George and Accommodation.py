# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:08:02 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
count = 0
for elem in range(in1):
    p,q = input().split()
    p = int(p)
    q = int(q)
    if q-p >= 2:
        count += 1
print(count)