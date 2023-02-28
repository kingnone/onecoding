import sys
input = sys.stdin.readline

max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]
hacker = False

score = list(map(int, input().split()))

for i in range(9):
    if score[i] > max_score[i]:
        hacker = True
        break

if hacker:
    print('hacker')
elif sum(score) < 100:
    print('none')
else:
    print('draw')