# 내 코드 1
def solution(p, m, c):
    total = sum([p*i for i in range(1, c+1)])
    return total-m if total>m else 0

# 내 코드 2
# zip() 사용 연습!
def solution(p, m, c):
    total = sum([i*j for i, j in zip([p]*c, range(1, c+1))])
    return total-m if total>m else 0

# 다른 코드 1
# https://docs.python.org/3/library/functions.html#max
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

# 다른 코드 2
def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))


print(solution(3, 20, 4))