def solution(hp):
    answer = 0

    a, b = divmod(hp, 5)
    hp = b
    answer += answer
    
    a, b = divmod(hp, 3)
    hp = b
    answer += answer
    
    answer += hp

    return answer

print(solution(23))
print(solution(24))
print(solution(999))