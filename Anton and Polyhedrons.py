# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:01:22 2021

@author: Easin
"""

in1 = input()

in1 = int(in1)
count = 0
for elem in range(in1):
    in2 = input()
    if in2 == "Cube":
        
        count = count + 6
    if in2 == "Icosahedron":
        count += 20
    if in2 == "Octahedron":
        count += 8
    if in2 == "Dodecahedron":
        count += 12
    if in2 == "Tetrahedron":
        count += 4
print(count)  
'''
Tetrahedron = 4
Cube = 6
Octahedron = 8
Dodecahedron = 12
Icosahedron = 20
'''
