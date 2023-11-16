import math

def solution(n, m):
    return [math.gcd(n,m), math.lcm(n,m)]


def solution(n, m):
    for i in range(min(n,m), 0, -1):
        if n%i == 0 and m%i == 0:
            i
            break
    
    for j in range(max(n,m), (n*m)+1, max(n,m)):
        if j%min(n,m) == 0:
            j
            break

    return [i,j]


# 다른 코드
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]

print(solution(3, 12))
print(solution(2, 5))