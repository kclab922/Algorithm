def solution(numbers, direction):
    for i in range(len(numbers)-1):
        if direction == 'right':
            numbers[len(numbers)-1] = numbers[0]
            numbers[i] = numbers[i+1]
    return numbers

print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))