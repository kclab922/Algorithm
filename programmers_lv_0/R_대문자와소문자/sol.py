# str.isupper() / str.lower() / str.upper() / 대소변경: str.swapcase()

def solution(my_string):
    answer = ''
    for char in my_string:
        if char.isupper():
            answer += char.lower()
        else:
            answer += char.upper()
    return answer



print(solution("cccCCC"))
print(solution("abCdEfghIJ"))