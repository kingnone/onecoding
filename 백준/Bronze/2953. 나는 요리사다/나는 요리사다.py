score = []

for i in range(5):
    s = list(map(int, input().split()))
    score.append(sum(s))

    
print(score.index(max(score))+1, max(score))