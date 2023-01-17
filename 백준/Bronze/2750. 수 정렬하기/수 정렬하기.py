N = int(input())
num_list = []

for i in range(N):
    n = int(input())
    num_list.append(n)

result = sorted(num_list)

for j in result:
    print(j)