def solution(n):
    if n % 7 == 0:
        pizza = n // 7
    else:
        pizza = n // 7 + 1
    return pizza


print(solution(7))
print(solution(1))
print(solution(15))