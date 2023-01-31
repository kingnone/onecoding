
def mul(num):
    n = 0
    for i in num:
        n += i ** 2
        result = n % 10 
    return result

num = map(int, input().split())
print(mul(num))