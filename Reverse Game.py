# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:40:07 2021

@author: Easin
"""

t = int(input().strip())
for elements in range(t):
    first_multiple_input = input().rstrip().split()
    
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    list1 = []
    for val in range(n):
        list1.append(val)
    list2 = []
    for val1 in range(len(list1)):
        list2.append(list1[-val1-1])
        list2.append(list1[val1])

        
    for val2 in range(len(list2)):
        if list2[val2] == k:
            print(val2)
            break
        
'''
Akash and Akhil are playing a game. They have  balls numbered from  to . Akhil asks Akash to reverse the position of the balls, i.e., to change the order from say, 0,1,2,3 to 3,2,1,0. He further asks Akash to reverse the position of the balls  times, each time starting from one position further to the right, till he reaches the last ball. So, Akash has to reverse the positions of the ball starting from  position, then from  position, then from  position and so on. At the end of the game, Akhil will ask Akash the final position of any ball numbered . Akash will win the game, if he can answer. Help Akash.

Input Format
The first line contains an integer , i.e., the number of the test cases.
The next  lines will contain two integers  and .

Output Format
Print the final index of ball  in the array.

Constraints



Sample Input

2
3 1
5 2
Sample Output

2
4
Explanation
For first test case, The rotation will be like this:
0 1 2 -> 2 1 0 -> 2 0 1 -> 2 0 1
So, Index of 1 will be 2.

Language
Python 3

More
8910111213141516171819202122232425262728293031323334
if __name__ == '__main__':
    t = int(input().strip())
    for elements in range(t):
        first_multiple_input = input().rstrip().split()
        
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        list1 = []
        for val in range(n):
            list1.append(val)
…        
    
    

Line: 12 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input
'''