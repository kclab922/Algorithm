def solution(array, height):
    count = 0
    for psn in array:
        if psn > height:
            count += 1
    return count

print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))