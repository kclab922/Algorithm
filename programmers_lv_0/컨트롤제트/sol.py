def solution(s):
    # answer = 0
    # s = s.split(' ')
    # for n in s:
    #     if n.isalpha():
    #         answer += int(n)
    #     elif n == 'Z':
    #         answer -= int(s[s.index('Z')-1])
    return sum(int(s))


print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))