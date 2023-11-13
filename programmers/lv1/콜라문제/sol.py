# 내 코드
# 호진님 헌정문제
def solution(a, b, n):
    answer = 0
    while n >= a:
        i, j = divmod(n, a)
        answer += i*b
        n = i*b + j
    
    return answer 


# 다른 코드

solution = lambda a, b, n: (n - b) // (a - b) * b


print(solution(2, 1, 20))
print(solution(3, 1, 20))