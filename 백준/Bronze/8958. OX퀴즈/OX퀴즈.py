T = int(input())

for i in range(1, T+1):
    n = list(input())
    score = 0
    sscore = 0
    for j in n:
        if j =='O':
            score += 1
            sscore += score
        else:
            score = 0
    print(sscore)