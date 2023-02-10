T = int(input())

for t in range(1, T+1):
    string = list(map(str, input()))
    error = 0

    for i in string:
        if string.count(i) == 2:
            pass
        else:
            error = 1
            break
            
    if error == 1:
        print(f'#{t} No')
    else:
        print(f'#{t} Yes')