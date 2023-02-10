T = int(input())
d = ''

for t in range(1, T+1):
    a, b, c = map(int, input().split())
    if a == b:
        d = c
    else :
        d = a + b - c

    print(f'#{t} {d}')