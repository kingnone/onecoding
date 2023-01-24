N = int(input())
score = list(map(int, input().split()))
result = []
m = max(score)

for i in score:
    s = i / m * 100
    result.append(s)

print(sum(result) / N)