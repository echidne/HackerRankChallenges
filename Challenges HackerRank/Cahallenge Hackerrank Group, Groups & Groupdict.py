# solution 1
import string
import re
def firstreapeatedasciiordigitchar(str):
    res = -1
    for char in string.ascii_letters:
        m=re.search(fr"([{char}]{{2,}})",str)
        if m:
            res = m[0][0]
            return res
    for char in string.digits:
        m=re.search(fr"([{char}]{{2,}})",str)
        if m:
            res= m[0][0]
            return res
    return res

print(firstreapeatedasciiordigitchar(input()))

# solution 2
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)