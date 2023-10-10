# 1. 나눗셈 이용

# def solution(n):
#     answer = 0
#     while n > 0:
#         a = n // 10 # 몫
#         b = n % 10 # 나머지
#         n = a
#         answer += b

#     return answer


# 2.

def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)
    
    return answer


print(solution(1234))
print(solution(930211))