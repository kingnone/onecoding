# scissors = 1
# rock = 2
# paper = 3

a, b = map(int, input().split())

if (a == 1 and b ==3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print('A')
elif (a == 1 and b ==1) or (a == 2 and b == 2) or (a == 3 and b == 3):
    print('A와 B가 비겼습니다')
else:
    print('B')
