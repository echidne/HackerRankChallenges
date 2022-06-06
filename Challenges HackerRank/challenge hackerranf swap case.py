"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
"""
#import string

def swap_case(s):
    new_string=""
    for letter in s:
        if letter.islower():
            new_string +=letter.upper()
        elif letter.isupper():
            new_string +=letter.lower()
        else:
            new_string += letter
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)