def solution(sides):
    sides.sort()
    return 1 if sides[2] < sides[0] + sides[1] else 2
    
def solution(sides):
    sides.sort()
    return 1 if sides[2] < sum(sides) - sides[2] else 2

print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))