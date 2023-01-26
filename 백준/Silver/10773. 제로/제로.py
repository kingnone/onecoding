K = int(input())
n_list = []

for i in range(1, K+1):
    num = int(input())
    
    if num == 0 :
        n_list.pop()
    else:
        n_list.append(num)
print(sum(n_list))