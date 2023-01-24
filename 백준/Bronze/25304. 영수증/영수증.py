X = int(input())
N = int(input())
cnt = 0 

for i in range(N):
    p, price =  map(int, input().split())
    cnt += p * price

if X == cnt:
    print('Yes')
else:
    print('No')