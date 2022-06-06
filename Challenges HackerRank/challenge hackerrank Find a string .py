"""
find the number of substring in a string
exemple:
string ='ABCDCDC'
substing = 'CDC'
answer = 2
"""

import re

def count_substring(string, sub_string):
    return len(re.findall(r"(?=%s)"%sub_string, string))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)