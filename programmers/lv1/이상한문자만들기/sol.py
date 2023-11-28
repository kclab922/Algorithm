def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            if i%2:
                answer += s[i].lower()
            else:
                answer += s[i].upper()
    
    return answer


print(solution("try hello world"))
