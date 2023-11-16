# 내 코드
def solution(n):
    if n%2 == 0:
        return '수박'*(n//2)
    else:
        return '수박'*(n//2) + '수'


# 다른 코드
# 왜 이 생각을!
def water_melon(n):
    return ("수박"*n)[0:n]

print(solution(3))
print(solution(4))
