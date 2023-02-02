n = int(input())
nums = list(map(int, input().split()))
high = 0
h_list = []

for i in range(1, n):
    if nums[i] > nums[i-1]:
        high += nums[i] - nums[i-1]
        if i == n-1:
            h_list.append(high)    
    else:
        h_list.append(high)
        high = 0

print(max(h_list))