import re
first_multiple_input = input().strip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
print(matrix)

code=[]
for i in range(m):
    for j in range(n):
        code.append(matrix[j][i])

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", "".join(code)))