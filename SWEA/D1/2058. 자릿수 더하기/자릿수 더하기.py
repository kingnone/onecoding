number = int(input())
num = str(number)
sum = 0

for i in range(len(num)):
    sum += int(num[i])
print(sum) 