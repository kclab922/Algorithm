def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
        else:
            continue
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))
