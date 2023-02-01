T = int(input())

for i in range(1, T+1):
    score = list(map(int, input().split()))
    score.remove(max(score))
    score.remove(min(score))
    if max(score) - min(score) >= 4:
        print('KIN')
    else:
        print(sum(score))