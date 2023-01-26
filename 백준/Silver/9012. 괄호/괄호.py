T = int(input())

for i in range(1, T+1):
    cnt = 0 
    string = list(map(str, input()))
    for i in string:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break

    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')