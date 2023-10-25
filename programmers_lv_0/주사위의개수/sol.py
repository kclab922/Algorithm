def solution(box, n):
    max_dice = 1
    for num in box:
        max_dice *= num // n 
    return max_dice

print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))