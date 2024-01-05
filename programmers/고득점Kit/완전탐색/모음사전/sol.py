from itertools import product

def solution(word):
    myL = []
    for i in range(1, 6):
        for k in product('AEIOU', repeat=i): 
            myL.append(''.join(list(k))) 
            # A, E, I, O, U, AA, AE, AI, AO, AU ... UUUUU

    return sorted(myL).index(word) + 1

print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))




# 순열/조합 관련 내용 정리
num_list = [1,2,3,4]

# 순열(순서 상관 있을 경우)
from itertools import permutations
list(permutations(num_list,2))
list(permutations(num_list,3))
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
# [(1, 2, 3), (1, 2, 4), (1, 3, 2), (1, 3, 4), (1, 4, 2), (1, 4, 3), (2, 1, 3), (2, 1, 4), (2, 3, 1), (2, 3, 4), (2, 4, 1), (2, 4, 3), (3, 1, 2), (3, 1, 4), (3, 2, 1), (3, 2, 4), (3, 4, 1), (3, 4, 2), (4, 1, 2), (4, 1, 3), (4, 2, 1), (4, 2, 3), (4, 3, 1), (4, 3, 2)]

# 조합(순서 상관 없을 경우)
from itertools import combinations
list(combinations(num_list,2))
list(combinations(num_list,3))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

# 중복순열(여러 리스트, 문자열을 통해 곱집합 구하기)
from itertools import product
iterable1 = 'ABC'
iterable2 = ['cat','dog']
iterable3 = 'hi'
list(product(iterable1, iterable2, iterable3))
# [('A', 'cat', 'h'), ('A', 'cat', 'i'), ('A', 'dog', 'h'), ('A', 'dog', 'i'), ('B', 'cat', 'h'), ('B', 'cat', 'i'), ('B', 'dog', 'h'), ('B', 'dog', 'i'), ('C', 'cat', 'h'), ('C', 'cat', 'i'), ('C', 'dog', 'h'), ('C', 'dog', 'i')]

# 중복조합(조합을 만들되 중복 가능)
from itertools import combinations_with_replacement
list(combinations_with_replacement(num_list,2))
list(combinations_with_replacement(num_list,3))
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 3, 3), (1, 3, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 3), (2, 3, 4), (2, 4, 4), (3, 3, 3), (3, 3, 4), (3, 4, 4), (4, 4, 4)]