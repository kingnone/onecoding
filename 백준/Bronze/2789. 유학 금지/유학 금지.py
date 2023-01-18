a = "CAMBRIDGE"
word = list(input())

for i in a:
    for j in range(len(word)):
        if i == word[j]:
            word[j] =''

print(''.join(word))