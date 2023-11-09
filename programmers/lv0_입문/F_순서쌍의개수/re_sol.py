# 틀린 풀이
def solution(n):
    solution(1) = 1
    soulution(2) = 2
    solution(4) = 3 
    count = 2
    if n % 2 == 0:
        count += 2
    if n % n == 0:
        count += 1
    
    return count

print(solution(20))
print(solution(100))