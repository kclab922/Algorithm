def solution(numbers, num1, num2):
    answer = []
    if len(numbers) > num2 + 1:
        answer = list(range(numbers[num1], numbers[num2 + 1]))
    else:
        answer = list(range(numbers[num1], numbers[len(numbers) - 1]))
    return answer
    
print(solution([1, 2, 3, 4, 5], 1, 3))
print(solution([1, 3, 5], 1, 2))