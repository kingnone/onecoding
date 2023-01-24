C = int(input())

for i in range(1, C+1):
    n = list(map(int, input().split()))
    average = sum(n[1:])/n[0] # 평균 구하기 n[0] : 학생수 n[1:] : 점수
    cnt = 0
    for j in n[1:]:
        if j > average:
            cnt += 1
    result = cnt / n[0] * 100
    print(f'{result:.3f}%')