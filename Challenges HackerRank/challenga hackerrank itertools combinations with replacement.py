""" 
Task

You are given a string .
Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the combinations with their replacements of string  on separate lines.

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""
from itertools import combinations_with_replacement
string, number = input().split()
number=int(number)
liste= sorted(list(string))
for el in combinations_with_replacement(liste, number):
    print("".join(el))

