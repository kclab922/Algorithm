def solution(numbers):
    my_max = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i]*numbers[j] > my_max and i != j:
                my_max = numbers[i]*numbers[j]
    return my_max

print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))