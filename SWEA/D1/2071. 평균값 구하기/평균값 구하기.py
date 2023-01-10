T = int(input())

for t in range(1, T+1):
    number=list(map(int, input().split()))
    average = sum(number)/len(number)
    average = round(average)
    
    print(f"#{t} {average}")