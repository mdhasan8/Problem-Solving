# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 13:09:07 2021

@author: Easin
"""

def matchingStrings(strings, queries):
    list1 = []
    for elem in range(len(queries)):
        count = 0
        #list1 = []
        for val in range(len(strings)): 
            if queries[elem] == strings[val]:
                count +=1
        list1.append(count)
    return list1 

print(matchingStrings([1,2,3,4],[1,2,2,3]))
'''
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

Example

There are  instances of ',  of '' and  of ''. For each query, add an element to the return array, .

Function Description

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search
string queries[q] - an array of query strings
Returns

int[q]: an array of results for each query
Input Format

The first line contains and integer , the size of .
Each of the next  lines contains a string .
The next line contains , the size of .
Each of the next  lines contains a string .

'''