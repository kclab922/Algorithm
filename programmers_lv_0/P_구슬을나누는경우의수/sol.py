# 내 풀이
# 팩토리얼 구하는 함수 만든 후, 경우의 수 구하는 공식에 적용

def ft(x):
    answer = 1
    for n in range(1, x+1):
        answer *= n
    return answer

def solution(balls, share):
    return int(ft(balls) / (ft(balls-share) * ft(share)))


# 다른 풀이
# math - combination 함수
import math

def solution(balls, share):
    return math.comb(balls, share)

print(solution(3, 2))
print(solution(5, 3))
