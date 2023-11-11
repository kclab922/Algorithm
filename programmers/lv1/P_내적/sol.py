# 내 코드
def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

# 다른 코드 1
# zip() 숙지해보자 
# https://docs.python.org/ko/3/library/functions.html?highlight=zip#zip
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

# 다른 코드 2
# 람다...
solution = lambda x, y: sum(a*b for a, b in zip(x, y))

print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))