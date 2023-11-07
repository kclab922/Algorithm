# 내 코드
# 1. count(a, b) 함수 규정: 숫자 a부터 b까지 중, '3의 배수나 3을 포함한 수'가 총 몇 개인지 세는 함수
# 2. solution(n)
# (tc) n=10일 때
# a~b : count(a,b) => answer
# 1~10 : 3 => 13
# 11~13: 2 => 15
# 14~15: 1 => 16
# 16~16: 0 => 16

def count(a, b):
    return sum([1 for i in range(a, b+1) if i%3 == 0 or '3' in str(i)])

def solution(n):
    a = 1
    b = n 
    answer = n
    while count(a, b) > 0:
        answer += count(a,b) 
        a = n+1 
        b = answer 
        n = b
    return answer



# 다른 코드
# 아놔
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

print(solution(15))
print(solution(40))