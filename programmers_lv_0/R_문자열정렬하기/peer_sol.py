# 풀이1
# tip: list comprehension 에서 sorted 쓸 때는 리스트도 함수도 전체를 감싼다...?

def solution(my_string):
    return sorted([int(char) for char in my_string if char.isdigit()])

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))