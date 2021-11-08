# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:52:43 2021

@author: Easin
"""

# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def solve(n, m):
    if n ==1 or m==1:
        return abs(n-m)
    elif n > m:
        return (m-1)+m*(n-1)
    elif m > n:
        return (n-1)+n*(m-1)
    elif n == m:
        return (m-1)+(m)*(n-1)
print(solve(3,1))


'''
Mary has an  piece of paper that she wants to cut into  pieces according to the following rules:

She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer already-cut pieces on top of one another.
Each cut is a straight line from one side of the paper to the other side of the paper. For example, the diagram below depicts the three possible ways to cut a  piece of paper:
example-cutting-squares.png
Given  and , find and print the minimum number of cuts Mary must make to cut the paper into  squares that are  unit in size.

Input Format

A single line of two space-separated integers denoting the respective values of  and .

Constraints

Output Format

Print a long integer denoting the minimum number of cuts needed to cut the entire paper into  squares.

Sample Input

3 1
Sample Output

2
Explanation

Mary first cuts the  piece of paper into a  piece and a  piece. She then cuts the  piece into two  pieces:

cutting-paper-squares.png

Because it took her two cuts to get  pieces of size , we print  as our answer.
'''