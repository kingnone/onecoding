w_list =[]
k_list = []
wscore = 0
kscore = 0

for i in range(10):
    w = int(input())
    w_list.append(w)

for i in range(10):
    k = int(input())
    k_list.append(k)

w_3 = sorted(w_list, reverse=True)
k_3 = sorted(k_list, reverse=True)

for i in range(3):
    wscore += w_3[i]
    kscore += k_3[i]

print(wscore, kscore)