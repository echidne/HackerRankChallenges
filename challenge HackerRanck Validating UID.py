import re
def valid_uid(string):
    if 2<len(re.findall(r"[A-Z]", string)) and len(re.findall(r"\d", string))>3 and re.match(r"[a-zA-Z0-9]{10}", string) and len(set(string)) ==10 :
        return "Valid"
    else:
        return "Invalid"

for _ in range(int(input())):
    print(valid_uid(input()))