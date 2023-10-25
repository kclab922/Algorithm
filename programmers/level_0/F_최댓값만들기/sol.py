def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i]*numbers[j] > answer and i != j:
                answer = numbers[i]*numbers[j]
            else: 
                continue
    return answer

print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))