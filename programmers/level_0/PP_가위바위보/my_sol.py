def solution(rsp):
    answer = ''
    for n in rsp:
        if n == '2':
            answer += '0'
        if n == '0':
            answer += '5'
        if n == '5':
            answer += '2'
    return answer

print(solution("2"))
print(solution("205"))
