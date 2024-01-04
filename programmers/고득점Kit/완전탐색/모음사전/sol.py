from itertools import product

def solution(word):
    myL = []
    for i in range(1, 6):
        for k in product('AEIOU', repeat=i):
            myL.append(''.join(list(k)))
    
    return sorted(myL).index(word) + 1

print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))