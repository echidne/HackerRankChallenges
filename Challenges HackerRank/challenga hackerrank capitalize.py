"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.
"""
def solve(s):
    capitalized_list =list(s.capitalize())
    for i, el in enumerate(capitalized_list):
        if el == " " and 0 < i < len(s)-1:
            capitalized_list[i+1] = capitalized_list[i+1].upper()          
    return "".join(capitalized_list)

if __name__ == '__main__':
    s = input()
    print(solve(s))