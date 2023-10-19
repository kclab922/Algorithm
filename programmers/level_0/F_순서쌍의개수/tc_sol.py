# 해제1
def solution(n):
    answer = 0

    for num in range(1, n+1):
        if n % num == 0:
            answer += 1

    return answer



# 해제2 (연산시간단축 버전, 효율성 향상)
def solution(n):
    answer = 0

    for num in range(1, int(n ** 0.5) + 1): # n ** 0.5 = 루트n , int 씌워서 소수도 정수로.
        if n % num == 0:
            answer += 2
        if num * num == n:
            answer -= 1

    return answer


print(solution(20))
print(solution(100))