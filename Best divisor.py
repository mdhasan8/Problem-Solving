# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:12:15 2021

@author: Easin
"""

n = int(input().strip())
list1 = []
for val in range(n):
    if n % (val+1)==0:
        list1.append(val+1)
list2 = []
for elem in range(len(list1)):
    n = list1[elem]
    count = 0
    
    while n > 9:
        x = n % 10
        count = count + x
        n = n//10
        
    count = count + n
    list2.append(count)
max1 = 0
for ind in range(len(list2)):
    if list2[ind] > max1:
        max1 = list2[ind]
        index = ind
print(list1[index])

'''
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.
'''
