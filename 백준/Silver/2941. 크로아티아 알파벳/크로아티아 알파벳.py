word = input()
w = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in w:
    word = word.replace(i, '0')

print(len(word))