def solution(pol):
    pol = pol.split(' ') # ['3x', '+', '7', '+', 'x']
    cal_x = 0
    cal_n = 0
    for p in pol:
        if 'x' in p:
            if len(p) == 1:
                cal_x += 1
            else:
                cal_x += int(p[:-1])
        elif p =='+':
            continue
        else:
            cal_n += int(p)
    
    answer_a = str(cal_x) + 'x' 
    if cal_x == 0:
        answer_a = ''
    elif cal_x == 1:
        answer_a = 'x'

    answer_b = ' ' + '+' + ' ' + str(cal_n)
    if cal_n == 0:
        answer_b = ''
    elif cal_n < 0:
        answer_b = ' ' + '-' + str(cal_n)[1:-2]
                
    return answer_a + answer_b

print(solution("3x + 7 + x"))
print(solution("x + x + x"))

