# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:45:46 2021

@author: Easin
"""

def findPoint(px, py, qx, qy):
    # Write your code here
    r1 = qx-px
    r2 = qy-py
    rx = qx + r1
    ry = qy + r2
    
    return rx,ry
print(findPoint(0, 0, 1, 1))

'''
Consider two points,  and . We consider the inversion or point reflection, , of point  across point  to be a  rotation of point  around .

Given  sets of points  and , find  for each pair of points and print two space-separated integers denoting the respective values of  and  on a new line.

Function Description

Complete the findPoint function in the editor below.

findPoint has the following parameters:

int px, py, qx, qy: x and y coordinates for points  and 
Returns

int[2]: x and y coordinates of the reflected point 
Input Format

The first line contains an integer, , denoting the number of sets of points.
Each of the  subsequent lines contains four space-separated integers that describe the respective values of , , , and  defining points  and .

Constraints

Sample Input

2
0 0 1 1
1 1 2 2
Sample Output

2 2
'''