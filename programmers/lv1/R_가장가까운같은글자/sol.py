def solution(s):
    result = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            result += [s[:i][::-1].index(s[i]) + 1]
        else:
            result += [-1]
        
    return result


print(solution("banana"))
print(solution("foobar"))