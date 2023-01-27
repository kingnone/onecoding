n1, n2 = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

a1 = len(a - b)
b1 = len(b - a)
print(a1 + b1)