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


# 다른 코드
def solution(s):
    answer = True
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)           
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                answer = True
            else:
                return False
    if stack:
        return False
    return answer