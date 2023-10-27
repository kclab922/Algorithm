def solution(numbers, direction):
    if direction == 'right':
        numbers[0] = numbers[len(numbers)-1] 
    elif direction == 'left':
        numbers[len(numbers)-1] = numbers[0]
    return numbers

print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))