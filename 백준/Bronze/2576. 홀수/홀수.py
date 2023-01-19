n_list = []
cnt = 0 

for i in range(7):
    num = int(input())
    if num % 2 == 1:
        n_list.append(num)
        cnt += num

if cnt == 0:
    print(-1)
else :   
    print(cnt)
    print(min(n_list))