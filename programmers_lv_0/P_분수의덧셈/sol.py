# 내 풀이 (허세 버전)
# 풀이구조: 분모/분자의 곱으로 통분 => 분모/분자의 최대공약수로 나누기
# tc1: [(1*4)+(3*2), (2*4)] => [10, 8] => 8~1 순서로 for문 돎 => 이중 최대공약수인 2로 나누기 => [5, 4] 
# [0] 붙인 이유: for문이 계속 돌면서 공약수로 나눈 모든 리스트를 출력. 이 중 0번 인덱스가 최대공약수로 나눈 것.
# Q. list comprehension에서 if문에 break 거는 방법?
def solution(n1, d1, n2, d2):
    [a, b] = [(n1*d2)+(n2*d1), (d1*d2)]
    return [[int(a/n), int(b/n)] for n in range(min([a,b]), 0, -1) if a%n == 0 and b%n == 0 ][0]


# 내 풀이 (풀어쓴 버전)
def solution(n1, d1, n2, d2):
    [a, b] = [(n1*d2)+(n2*d1), (d1*d2)]
    for n in range(min([a,b]), 0, -1):
        if a%n == 0 and b%n == 0:
            return [int(a/n), int(b/n)]


# 다른 풀이 1.
# 나와 동일한 구조로 풀이. (다만 최대공약수 함수 사용)
# math.gcd(n,m): n과 m의 최대공약수
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]



# 다른 풀이 2.
# 함수 적극 활용
# Fraction(분자,분모): 기약분수화
# Fraction(분자,분모).numerator => 분자 도출
# Fraction(분자,분모).denominator => 분모 도출
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]


print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))