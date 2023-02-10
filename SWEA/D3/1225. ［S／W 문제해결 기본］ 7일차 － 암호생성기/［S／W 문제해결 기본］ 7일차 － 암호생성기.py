T = 10

for i in range(1, T+1):
    t = int(input())
    code = list(map(int, input().split()))
    
    error = 0

    while code:
        for i in range(1, 6):
            f = code.pop(0)
            if f - i <= 0:
                code.append(0)
                error = 1
                break
            code.append(f - i)
        if error == 1:
            break

    print(f'#{t}', *code)