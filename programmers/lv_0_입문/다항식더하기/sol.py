# 내 코드
def solution(pol):
    sum_n = 0 
    sum_x = 0

    pol = pol.split(' ') # ['3x', '+', '7', '+', 'x']

    for i in pol:
        if i == '+':
            continue
        elif 'x' in i:
            i = i.strip('x')
            if i == '':
                sum_x += 1
            else:
                sum_x += int(i)
        else:
            sum_n += int(i)
    
    if sum_n > 0:
        if sum_x == 0:
            return str(sum_n)
        elif sum_x == 1:
            return 'x' + ' ' + '+' + ' ' + str(sum_n)
        else:
            return str(sum_x) + 'x' +' ' + '+' + ' ' + str(sum_n)
    elif sum_n == 0:
        if sum_x == 0:
            return '0'
        elif sum_x == 1:
            return 'x'
        else:
            return str(sum_x) + 'x'
    elif sum_n < 0:
        if sum_x == 0:
            return str(sum_n)
        elif sum_x == 1:
            return 'x' + ' ' + '-' + ' ' + str(int(sum_n))
        else:
            return str(sum_x) + 'x' + ' ' + '-' + ' ' + str(sum_n)        


print(solution("3x + 7 + x"))
print(solution("x + x + x"))
