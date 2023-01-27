N = int(input())
w_list = []

for i in range(1, N+1):
    word = input()
    w_list.append(word)

w_set = set(w_list)
ww = list(w_set)
ww.sort()
ww.sort(key = len)

for j in ww:
    print(j)
