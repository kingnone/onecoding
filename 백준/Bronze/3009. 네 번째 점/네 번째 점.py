x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for j in range(3):
    if x_list.count(x_list[j]) == 1:
        xx = x_list[j]
    elif y_list.count(y_list[j]) == 1:
        yy = y_list[j]

print(xx, yy)