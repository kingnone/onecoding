T = int(input())

for t in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    
    average = sum(num)/n

    for i in num:
        if average >= i:
            cnt += 1

    print(f'#{t} {cnt}')