def solution(n, k):
    total = (12000 * n) + (2000 * k) 
    discount = 2000 * (n // 10)
    answer = total - discount
    return answer

print(solution(10, 3))
print(solution(64, 6))