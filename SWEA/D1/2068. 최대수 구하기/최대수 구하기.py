T = int(input())

for t in range(1, T+1):
    num_list=list(map(int, input().split()))
    max_num = max(num_list)
    print(f"#{t} {max_num}")