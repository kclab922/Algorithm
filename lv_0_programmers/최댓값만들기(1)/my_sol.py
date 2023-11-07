def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[len(numbers) - 1] * numbers[len(numbers) - 2]
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))