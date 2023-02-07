import sys
input = sys.stdin.readline

n = int(input())
n_list = [int(input()) for _ in range(n)]

cnt = 0
max_num = 0

for i in reversed(n_list):
    if i > max_num:
        max_num = i
        cnt += 1

print(cnt)