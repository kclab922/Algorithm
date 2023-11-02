def solution(polynomial):
    # v = ''
    # n = 0
    p = (polynomial.replace('x', '*1')).split()
    
    # for i in range(0, len(p), 2):
    #     if p[i].isdigit():
    #         n += p[i]
    #     else:

    
    # return v + ' + ' + str(n)

    return p

print(solution("3x + 7 + x"))
print(solution("x + x + x"))

