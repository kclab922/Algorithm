def solution(my_string):
    for c in my_string:
        if my_string.count(c) >= 2:
            my_string.replace(c, '')
    return my_string

print(solution("people"))
print(solution("We are the world"))