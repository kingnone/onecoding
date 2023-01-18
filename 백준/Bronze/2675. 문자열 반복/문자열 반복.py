T = int(input())

for i in range(1, T+1):
    n, s = input().split()
    text = ''
    for j in s:
        text += int(n)*j
    print(text)