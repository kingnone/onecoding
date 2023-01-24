N = int(input())
num = map(int, input().split())
v = int(input())
cnt = 0 

for i in range(N+1):
    if v in num:
        cnt +=1

print(cnt)