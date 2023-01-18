T = int(input())

for i in range(T):
    word = list(input().split())
    wword = []

    for w in word:
        wword.append(w[::-1])

    print(*wword)