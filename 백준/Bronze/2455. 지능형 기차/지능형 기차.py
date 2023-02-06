passengers = 0
p_list = []

for i in range(4):
    out_p, in_p = map(int, input().split())
    passengers += in_p
    passengers -= out_p
    p_list.append(passengers)

print(max(p_list))