students = []

for i in range(28):
    n = int(input())
    students.append(n)

for s in range(1, 31):
    if s not in students:
        print(s)