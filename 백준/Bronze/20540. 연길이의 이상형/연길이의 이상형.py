string = input()
mbti = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
for i in string:
    mbti.remove(i)
result = ''.join(mbti)
print(result)