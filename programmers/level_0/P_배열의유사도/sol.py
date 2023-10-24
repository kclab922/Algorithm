def solution(s1, s2):
    count=0
    for i in s1:
        if i in s2:
            count += 1
    return count


print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]	))
print(solution(["n", "omg"], ["m", "dot"]))