T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    
    hits = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            fly = 0 
            for k in range(m):
                for l in range(m):
                    fly += array[i+k][j+l]
            hits.append(fly)

    print(f'#{t}', max(hits))
