n_list = []

for i in range(10):
    num = int(input())
    n_list.append(num)
   
average = int(sum(n_list) / 10)
m_num = max(n_list, key = n_list.count)

print(average)
print(m_num)