num_list = []
r_list = []

for i in range(10):
    num = int(input())
    num_list.append(num)

for j in num_list:
    result = j % 42
    r_list.append(result)
    
r = set(r_list)
print(len(r))