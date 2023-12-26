def solution(brown, yellow):

    for i in range(1, int(yellow**0.5+1)):
        if yellow % i == 0:
            a, b = yellow//i, i
            if (a+2) * (b+2) - yellow == brown:
                return [a+2, b+2]
    
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

