T = int(input())
dollar = [25, 10, 5, 1]

for i in range(1, T+1):
    change = []
    C = int(input())
    for j in dollar:
        change.append(C//j)
        C = C % j
    print(*change)