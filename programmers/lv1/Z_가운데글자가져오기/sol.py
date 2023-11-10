# 내 코드
def solution(s):
    return s[(len(s)//2)] if len(s)%2 else s[len(s)//2-1:len(s)//2+1]

# 다른 코드
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]

print(solution('abcde'))
print(solution('qwer'))