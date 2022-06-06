#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
nested_list=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name,score])

dic_students = dict(sorted(nested_list))
print(dic_students)
for key, val in dic_students.items():
    if val == sorted(list(set(dic_students.values())))[1]:
        print(key)



