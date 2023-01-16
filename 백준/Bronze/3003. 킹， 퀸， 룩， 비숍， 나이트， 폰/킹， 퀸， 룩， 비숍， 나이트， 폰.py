num = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]

for i in range(6):
    result = chess[i] - num[i]
    print(result, end=' ')
