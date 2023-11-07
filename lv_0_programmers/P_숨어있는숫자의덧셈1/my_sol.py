# 내 코드 1 (list comprehension ver.)
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])

# 내 코드 2
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))
