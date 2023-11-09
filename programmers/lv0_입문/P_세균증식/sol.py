# 내 코드
def solution(n, t):
    for i in range(t):
        n *= 2
    return n

# 참고 코드
# 굿
def solution(n, t):
    return 2**t * n

print(solution(2, 10))
print(solution(7, 15))