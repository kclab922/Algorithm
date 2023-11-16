# import math

# def solution(n, m):
#     return [math.gcd(n,m), math.lcm(n,m)]


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


print(solution(3, 12))
print(solution(2, 5))