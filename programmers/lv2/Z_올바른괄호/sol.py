def solution(s):
    temp = []
    s = list(s)

    while len(s):
        temp.append(s.pop())
        if temp[-2:] == [')', '(']:
            temp.pop()
            temp.pop()

    return temp == []

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))