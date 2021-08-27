# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 11:37:44 2021

@author: Easin
"""
import math
M,N = input().split()
M = int(M)
N = int(N)
MN = M *N
D = 2
print(math.floor(MN/D))