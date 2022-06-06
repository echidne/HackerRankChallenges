"""
    In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. 
    There are m words belonging to word group B.
    For each m words, check whether the word has appeared in group A or not. 
    Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions 1 and 3 in group A.
The second word, 'c', does not appear in group A, so print -1 .

Expected output:

1 3
-1
Input Format

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Constraints

1<=n<=10000
1<=m<=100
1<= length of word <=100

Output Format

Output m lines.
The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.

Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  3 times in positions 1, 2 and 4.
'b' appeared  2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group , you would print -1.
"""

from collections import defaultdict

n,m = (int(x) for x in input().split())
#print(n)
A= defaultdict(list)
B= []
for i in range(n):
    A[input()].append(str(i+1))
    #print(A)
#print(m)
for i in range(m):
    B.append(input())
for word in B:
    val = A.get(word, -1)
    if val != -1:
        print(" ".join(val))
    else :
        print(val)

