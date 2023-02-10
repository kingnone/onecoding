T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))
    
    no_submit = []

    for i in range(1, n+1):
        if i not in submit:
            no_submit.append(i)
    print(f'#{t}', *no_submit)