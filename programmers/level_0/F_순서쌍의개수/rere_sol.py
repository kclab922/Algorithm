def solution(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

print(solution(20))
print(solution(100))

def solution(n):
    count = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            count += 2
            if n ** 0.5 == i:
                count -= 1
    return count

print(solution(20))
print(solution(100))

