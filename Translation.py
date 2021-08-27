# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 11:11:34 2021

@author: Easin
"""

s = input()
t = input()

str1 = ""

for elem in range(len(s)):
        #print(elem)
    str1 += "".join(s[-elem-1])
if str1 == t:
    print("YES")
else:
    print("NO")
        
    