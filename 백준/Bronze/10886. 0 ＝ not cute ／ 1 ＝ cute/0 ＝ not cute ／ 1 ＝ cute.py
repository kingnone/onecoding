N = int(input())
cnt = 0
notcnt = 0

for i in range(N):
    num = int(input())
    if num == 1:
        cnt += 1
    else :
        notcnt += 1
if cnt > notcnt:
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
