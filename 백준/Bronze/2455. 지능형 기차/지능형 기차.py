passengers = 0
p_list = []

for i in range(4):
    in_p, out_p = map(int, input().split())
    passengers += out_p
    passengers -= in_p
    p_list.append(passengers)

print(max(p_list))