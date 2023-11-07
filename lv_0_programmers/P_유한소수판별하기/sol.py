# 내 코드 (math함수 없이 / 시간단축 ver: 모두 0ms대)
# 풀이과정
# 1. 기약분수일 때의 분모 b 도출
# 2. b의 소인수 중 2나 5가 아닌 것만 soinsu에 누적 
# 3. soinsu의 길이가 0이면 1 도출

def solution(a, b):
    # 1.
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i == 0:
            b = b/i
            break
    # 2.
    d = 2
    soinsu = []
    while d <= b:
        if b%d == 0:
            b = b/d
            if d != 2 and d != 5:  
                soinsu.append(d)
        else:
            d += 1
    # 3.
    return 1 if len(soinsu) == 0 else 2




# 다른 코드
# gcd(a, b): a,b의 최대공약수
# 굿굿

from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2


print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))