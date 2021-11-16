# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:11:35 2021

@author: Easin
"""

def isFibo(n):
    list1 = [0,1]
    for val in range(50):
        x = list1[-1] + list1[-2]
        list1.append(x)
    #print(list1)
    if n in list1:
        return "IsFibo"
    else:
        return "IsNotFibo"
print(isFibo(5))

'''
You are given an integer, . Write a program to determine if  is an element of the Fibonacci sequence.

The first few elements of the Fibonacci sequence are . A Fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. The first two elements are  and .

Formally:
Function Description

Complete the isFibo function in the editor below.

isFibo has the following parameters:
- int n: the number to check

Returns
- string: either IsFibo or IsNotFibo

Input Format
The first line contains , number of test cases.
 lines follow. Each line contains an integer .

Constraints


Sample Input

STDIN   Function
-----   --------
3       t = 3
5       n = 5
7       n = 7
8       n = 8
Sample Output

IsFibo
IsNotFibo
IsFibo

'''