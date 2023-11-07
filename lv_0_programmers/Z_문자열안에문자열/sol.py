# 내 코드 1 (list comprehension ver.)
def solution(str1, str2):
    return 1 if str2 in str1 else 2

# 내 코드 2
def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))