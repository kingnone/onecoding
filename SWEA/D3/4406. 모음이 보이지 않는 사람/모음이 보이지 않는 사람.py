T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']


for t in range(1, T+1):
    result = []
    string = list(map(str, input()))

    for i in string:
        if i not in vowel:
            result.append(i)

    print(f'#{t}', end=" ")
    for j in result:
        print(j, end = "")
    print()