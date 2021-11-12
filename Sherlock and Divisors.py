# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 00:37:36 2021

@author: Easin
"""

def divisors(n):
    list1 = []
    for val in range(1,n+1):
        if n % val ==0:
            list1.append(val)
    count = 0
    for val1 in range(len(list1)):
        if list1[val1] % 2 ==0:
            count += 1
    return count
print(divisors(9))

'''
Watson gives an integer  to Sherlock and asks him: What is the number of divisors of  that are divisible by 2?.

Input Format
First line contains , the number of testcases. This is followed by  lines each containing an integer .

Output Format
For each testcase, print the required answer in one line.

Constraints


Sample Input

2
9
8
Sample Output

0
3
Explanation
9 has three divisors 1, 3 and 9 none of which is divisible by 2.
8 has four divisors 1,2,4 and 8, out of which three are divisible by 2.
'''