def solution(n):
    odd = []
    for num in range(1, n+1):
        if num % 2 == 1:
            odd.append(num)
    return odd


print(solution(10))
print(solution(15))