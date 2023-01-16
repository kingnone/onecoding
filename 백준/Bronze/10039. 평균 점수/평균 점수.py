cnt = 0

for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    cnt += score

print(cnt // 5)