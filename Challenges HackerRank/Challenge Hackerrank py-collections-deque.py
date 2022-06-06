"""
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Constraints
0<N<=100

Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
"""
from collections import deque
d= deque()
N = int(input())
for _ in range(N):
    entry= input().rsplit(' ',1)
    if len(entry) == 1:
        method='.' + entry[0] + '()'
    else :
        method='.' + entry[0]+'('+entry[1]+')'
    exec('d' + method)
for el in d:
    print(el, end= " ")