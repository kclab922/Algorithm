# 내 코드
def solution(s):
    return True if s.isdigit() and (len(s) == 4 or len(s) == 6) else False

# 다른 코드
# 1. if 안 써도 True/False 반환 가능
# 2. 길이 점검시 리스트 활용 
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]
print(solution("a234"))
print(solution("1234"))