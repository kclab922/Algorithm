# 문제 설명
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 0 < n ≤ 1000


# 첫 번째 방식 (먼저 이해해야 함)
def solution(n):

    answer = 0

    numbers = range(1, n+1)

    for number in numbers:
        if number % 2 == 0:
            answer = answer + number
    return answer


# # 두 번째 방식 (차차 활용)
# def solution(n):
#     numbers = range(2, n+1, 2)
#     return sum(numbers)


# # 세 번째 방식 (내 풀이 확장적용하기)
# def solution(n):

#     result = []

#     numbers = range(1, n+1)

#     for number in numbers:
#         if number % 2 == 0:
#             result.append(number)
#     return sum(result)



print(solution(10)) # -> 30
print(solution(4)) # -> 6
