# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:26:12 2021

@author: Easin
"""

import math
n,m,a = input().split()
#m = int(input())
#a = int(input())

x = math.ceil(int(n)/int(a))
#print(x)
y = math.ceil(int(m)/int(a))
#print(y)
print(x*y)
