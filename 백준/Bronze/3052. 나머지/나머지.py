n_list = []

for i in range(10):
    num = int(input())
    n = num % 42
    n_list.append(n)

result = set(n_list)

print(len(result))