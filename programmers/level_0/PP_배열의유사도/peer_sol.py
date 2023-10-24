# 풀이1
def solution(s1, s2):
    return len(set(s1) & set(s2))

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]	))
print(solution(["n", "omg"], ["m", "dot"]))


# 이해값: 두 리스트의 교집합-`set(s1) & set(s2)` / 합집합 - `set(s1) | set(s2)` / 차집합 - `set(s1) - set(s2)`

# input
A = ['a', 'b']
B = ['b', 'c']
print(list(set(A) & set(B))) # 교집합
print(list(set(A) | set(B))) # 합집합
print(A + B) # list concatenation
print(list(set(A) - set(B))) # 차집합

# # output
# ['b']
# ['c', 'a', 'b']
# ['a', 'b', 'b', 'c']
# ['a']




