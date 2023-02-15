N = int(input())
nums = map(int, input().split())
cnt = 0 
result = 0

for i in nums: 
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        result += 1
    cnt = 0

print(result)
