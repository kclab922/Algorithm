# # 방법1 (.isdigit() 이용)
# def solution(my_string):
#     answer = 0
#     for char in my_string:
#         if char.isdigit():
#             answer += int(char)
#     return answer


# # 방법2 (예외처리 이용)
# def solution(my_string):
#     answer = 0
#     for char in my_string:
#         try:
#             answer += int(char)
#         except:
#             continue 

#     return answer

# 방법3 (아스키코드 이용. 비추)
def solution(my_string):
    answer = 0
    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('z')):
            answer += int(char)

    return answer
    
print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))