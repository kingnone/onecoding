n = int(input())
dic = {}

for i in range(n):
    name, log = input().split()
    dic[name] = log
    if log == 'leave':
        del dic[name]

result = sorted(dic.keys(), reverse=True)

for j in result:
    print(j)