n = int(input())
size = []
c_list = []

for i in range(n):
    weight, height = map(int, input().split())
    size.append((weight, height))

for i in size:
    cnt = 0
    for j in size:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    c_list.append(cnt + 1)

print(*c_list)