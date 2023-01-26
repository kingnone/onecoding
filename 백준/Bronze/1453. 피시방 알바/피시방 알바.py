N = int(input())
guest = list(map(int, input().split()))
cnt = 0 
seat = []

for i in range(N):
    if guest[i] in seat:
        cnt += 1 
    else:
        seat.append(guest[i])
print(cnt)