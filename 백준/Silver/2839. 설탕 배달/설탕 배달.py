N = int(input())

carry = 0

while 0 <= N:
    if N % 5 == 0:
        carry += (N // 5)
        print(carry)
        break
    N -= 3
    carry += 1
else:
    print(-1)