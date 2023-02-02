word = list(input())
result = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        w1 = word[:i]
        w2 = word[i:j]
        w3 = word[j:]

        w1.reverse()
        w2.reverse()
        w3.reverse()
        result.append(''.join(w1 + w2 + w3))

r = sorted(result)
print(r[0])