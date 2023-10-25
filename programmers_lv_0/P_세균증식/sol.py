def solution(n, t):
    for i in range(1, t+1):
        n *= 2
    return n

print(solution(2, 10))
print(solution(7, 15))