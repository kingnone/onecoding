T = int(input())

for t in range(1, T+1):
    word = input()
    w = []
    for i in word[::-1]:
        if i == 'b':
            w.append('d')
        elif i == 'd':
            w.append('b')
        elif i == 'p':
            w.append('q')
        elif i == 'q':
            w.append('p')

    print(f'#{t}',''.join(w))