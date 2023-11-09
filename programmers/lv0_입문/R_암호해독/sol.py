# 풀이1
# tip: ''.join(list): join 함수는 '리스트' 속 문자열을 합칠 때 서야 함. 
def solution(cipher, code):
    answer = ''
    for num in range(1, len(cipher)//code + 1):
        i = num * code
        answer += cipher[i-1]
    return answer 

print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))