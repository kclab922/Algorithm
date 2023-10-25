# #방법1 
# def solution(my_string, letter):
#     anwer = ''
#     answer = answer.replace(letter, '')

#     return answer

#방법2 응용
def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string

    return answer

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))
