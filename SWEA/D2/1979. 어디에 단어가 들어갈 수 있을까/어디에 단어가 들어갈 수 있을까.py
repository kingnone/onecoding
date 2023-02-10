T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    total = 0

    for x in range(n):
        cnt = 0
        for y in range(n):
            if puzzle[x][y] == 1:
                cnt += 1
                if  y == n-1:
                    if cnt == k:
                        total += 1
            elif puzzle[x][y] == 0:
                if cnt == k:
                    total += 1
                cnt = 0

    for x in range(n):
        cnt = 0
        for y in range(n):
            if puzzle[y][x] == 1:
                cnt += 1
                if y == n-1:
                    if cnt == k:
                        total += 1
            elif puzzle[y][x] == 0:
                if cnt == k:
                    total += 1
                cnt =0 

    print(f'#{t}', total)    