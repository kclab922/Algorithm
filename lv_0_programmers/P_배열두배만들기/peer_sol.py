# 풀이1
# list comprehension


def solution(numbers):
    return [num*2 for num in numbers]

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))