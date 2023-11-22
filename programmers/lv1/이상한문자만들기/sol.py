def solution(s):
    answer = ''
    for w in s.split(' '):
        if w == ' ':
            answer += ' '
        else: 
            for i in range(len(w)):  
                if i % 2:
                    answer += w[i].lower() 
                else:
                    answer += w[i].upper() 
        answer += ' '
    return answer

print(solution("try hello world"))
print(solution("try     hello    world"))
