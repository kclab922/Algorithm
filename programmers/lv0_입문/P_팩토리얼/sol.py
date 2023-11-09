# 내 풀이 (팩토리얼 기능 없다고 가정)
# 1. for문 돌려 i!만들기
# 2. i!이 n을 넘는 순간 if문에 break
# 3. break 걸린 i는 팩토리얼 시 n을 넘으므로, i-1이 답

def solution(n):
    f = 1
    for i in range(1, 12):
        f *= i
        if f>n:
            break 
    return i-1


# 다른 풀이
# 팩토리얼 기능 사용

from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k


print(solution(3628800))
print(solution(7))