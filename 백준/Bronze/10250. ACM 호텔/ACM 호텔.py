T = int(input())

for i in range(1, T+1):
    h, w, n = map(int, input().split())

    floor = n % h
    room = (n//h) + 1
    if floor == 0:
        floor = h
        room -= 1
    print(floor * 100 + room)