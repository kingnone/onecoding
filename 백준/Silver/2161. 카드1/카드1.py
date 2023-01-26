import sys

n = int(sys.stdin.readline())
card = [i for i in range(1, n + 1)]
res = []

while True:
    res.append(card.pop(0)) 
    if not card: 
        break
    card.append(card.pop(0)) 

print(*res)