T = 10

for t in range(1, T+1):
    length = int(input())
    string = input()

    s_list = []
    result = 1
    
    for i in range(length):
        if string[i] == '(' or string[i] == '{' or string[i] == '[' or string[i] == '<':
            s_list.append(string[i])

        if string[i] == ')':
            if len(s_list) > 0 and s_list.pop() != '(':
                result = 0
                break
        if string[i] == '}':
            if len(s_list) > 0 and s_list.pop() != '{':
                result = 0
                break
        if string[i] == ']':
            if len(s_list) > 0 and s_list.pop() != '[':
                result = 0
                break
        if string[i] == '>':
            if len(s_list) > 0 and s_list.pop() != '<':
                result = 0
                break

    print(f'#{t}', result)
