"""
Task
You are given a complex . Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines:
The first line should contain the value of .
The second line should contain the value of .

Sample Input

  1+2j
Sample Output

 2.23606797749979 
 1.1071487177940904
Note: The output should be correct up to 3 decimal places
"""

from cmath import phase
complex_number = input()
print(abs(eval(complex_number)))
print(phase(eval(complex_number)))
