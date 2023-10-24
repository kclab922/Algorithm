# 첫 번째 방식

def solution(numbers):
    answer = 0
    total = 0
    for number in numbers:
        total += number
    
    answer = total / len(numbers)

    return answer



# # 두 번째 방식
# def solution(numbers):
#     answer = sum(numbers) / len(numbers)
#     return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # -> 5.5
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]	)) # -> 94.0