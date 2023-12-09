def solution(numbers):
    numbers.sort(key=lambda x: (str(x)[0], str(x)[1]), reverse=True)
    return numbers

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))