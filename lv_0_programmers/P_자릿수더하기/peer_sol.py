# 풀이1
# sum(iterable): 인자 -> 리스트, 튜플, 딕셔너리 등 인덱스 순환 접근이 가능 + 숫자로만 구성

def solution(n):
    return sum(int(num) for num in str(n))

print(solution(1234))
print(solution(930211))

