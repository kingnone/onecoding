n = int(input())

for i in range(n):
    num = n - i
    error = 0

    for j in str(num):
        if j == "7" or j == "4":
            pass
        else:
            error = 1
            break
    
    if error == 0:
        break

print(num)