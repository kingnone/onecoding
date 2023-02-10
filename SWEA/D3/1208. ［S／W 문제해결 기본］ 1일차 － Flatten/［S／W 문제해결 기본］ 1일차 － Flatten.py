T = 10

for t in range(1, T+1):
    n = int(input())
    box = list(map(int, input().split()))

    for i in range(n):
        max_box = max(box)
        min_box = min(box)
        idx_max_box = box.index(max_box)
        idx_min_box = box.index(min_box)
        box[idx_max_box] -= 1
        box[idx_min_box] += 1
        
    print(f'#{t}', max(box) - min(box))