import re
import string
vowels = 'aeiouAEIOU'
consonnants = "".join([letter for letter in string.ascii_letters if letter not in vowels])
regex = r"(?=[%s]([%s]{2,})[%s])" %(consonnants, vowels, consonnants)
s = input()

if re.findall(regex, s):
    for match in re.findall(regex, s):
        print(match)
else:
    print(-1)
