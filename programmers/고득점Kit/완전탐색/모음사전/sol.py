from itertools import permutations

def solution(word):
    loc = 1
    for i in range(1, 6, 1):
        for j in list(permutations(['A', 'E', 'I', 'O', 'U'], i)):
            if ''.join(j) == word:
                return j
            else:
                loc += 1
    return j
                    

print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
# print(solution("EIO"))