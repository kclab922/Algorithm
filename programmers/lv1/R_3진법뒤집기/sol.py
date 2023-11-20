# 내 코드
def solution(n):
    three = ''
    if n < 3:
        return n
    while n//3 > 0 :
        three += str(n%3) 
        n = n//3
    return int(three+str(n), 3)



# 다른 코드
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    return int(tmp, 3)

print(solution(45))
print(solution(125))
print(solution(0))