def solution(n):
    total = 0
    count = 0
    three = 0
    while count <= 3:
        for i in n:
            total += i
            count += 1
            if total == 0:
                three += 1
            
    return three


print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))