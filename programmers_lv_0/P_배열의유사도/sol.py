# 내 코드 1 (list comprehension ver.)
def solution(s1, s2):
    return sum([1 for i in s1 if i in s2])

# 내 코드 2
def solution(s1, s2):
    count=0
    for i in s1:
        if i in s2:
            count += 1
    return count

# 참고 코드
# set()을 이용한 교집합/합집합/차집합
def solution(s1, s2):
    return len(set(s1) & set(s2))

# input
A = ['a', 'b']
B = ['b', 'c']
print(list(set(A) & set(B))) # 교집합
print(list(set(A) | set(B))) # 합집합
print(A + B) # list concatenation
print(list(set(A) - set(B))) # 차집합

# output
['b']
['c', 'a', 'b']
['a', 'b', 'b', 'c']
['a']

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]	))
print(solution(["n", "omg"], ["m", "dot"]))