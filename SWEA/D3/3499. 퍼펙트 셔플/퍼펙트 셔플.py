T = int(input())

for t in range(1, T+1):
    n = int(input())
    card = list(input(). split())
    result = ['']*len(card)

    if n%2 == 0:
        for i in range(n//2): 
            result[2*i] = card[i]
            result[2*i+1] = card[n//2+i]
    else:
        for i in range(n//2+1):
            result[2*i] = card[i]
        for i in range(n//2):
            result[2*i+1] = card[n//2+1+i]

    print(f'#{t}', *result)