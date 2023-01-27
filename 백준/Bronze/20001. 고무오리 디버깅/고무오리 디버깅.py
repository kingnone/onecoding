string = input()
question = 0

while string != '고무오리 디버깅 끝':
    string = input()
    if string == '문제':
        question += 1
    elif string == '고무오리':
        if question == 0:
            question += 2
        else:
            question -= 1

if question == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')