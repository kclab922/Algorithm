def solution(array, height):
    array.append(height)
    array.sort(reverse = True)
    return array.index(height)


print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))