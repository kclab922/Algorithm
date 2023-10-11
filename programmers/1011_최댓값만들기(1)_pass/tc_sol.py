# # 방법1: 모든 경우의 수 구하기
# def solution(numbers):
#     answer = 0
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             multi = numbers[i] * numbers[j]

#             if answer < multi:
#                 answer = multi
    
#     return answer

# 방법2: 정렬하기
def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer



print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))