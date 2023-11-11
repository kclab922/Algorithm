def solution(n):
    answer = ''
    count = 0
    while count != n:
        for i in '수박':
            answer += i
            count += 1
    return answer



print(solution(3))
print(solution(4))