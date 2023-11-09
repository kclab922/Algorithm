# 내 코드
def solution(rsp):
    answer = ''
    for n in rsp:
        if n == '2':
            answer += '0'
        elif n == '0':
            answer += '5'
        else:
            answer += '2'

    return answer

# 참고 코드
# dictionary 이용
def solution(rsp):
    answer = ''
    rsp_dict = {
        '2': '0',
        '0': '5',
        '5': '2',
    }
    for char in rsp:
        answer += rsp_dict[char]

    return answer

print(solution("2"))
print(solution("205"))
