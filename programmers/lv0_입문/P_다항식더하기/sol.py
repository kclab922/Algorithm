# 내 코드
def solution(pol):
    sum_n = 0 
    sum_x = 0

    for i in pol.split(' + '):
        if 'x' in i:
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


# 다른 코드
# f스트링 사용!
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'

        
print(solution("3x + 7 + x"))
print(solution("x + x + x"))
