# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:33:45 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input()

countA = 0
countD =0

for elem in range(len(in2)):
    if in2[elem] == "A":
        countA += 1
    else:
        countD += 1
if countA > countD:
    print("Anton")
elif countA < countD:
    print("Danik")
else:
    print("Friendship")
        