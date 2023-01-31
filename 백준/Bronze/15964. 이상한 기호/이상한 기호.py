def strange_words(a,b):
    return (a + b) * (a - b)
    
a, b = map(int, input().split())
print(strange_words(a, b))