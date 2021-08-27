# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:03:07 2021

@author: Easin
"""

input1 = input()
input1 = input1.lower()
Vowels = ["a", "o", "y", "e", "u", "i"]
str1 = ""
for elm in range(len(input1)):
    if input1[elm]  not in Vowels:
        str1 = str1 + "." + (input1[elm])
        
print(str1)