# 내 풀이 
# 1. 문자열을 공백 기준으로 split
# 2. answer의 기본값은 첫번째 원소
# 3. 연산자만 반복 검토 => +면 연산자 뒤 숫자 더하기, -면 연산자 뒤 숫자 빼기
def solution(my_string):
    ms = my_string.split()
    answer = int(ms[0])
    for i in range(1, len(ms), 2):
        if ms[i] == '+':
            answer += int(ms[i+1])
        elif ms[i] == '-':
            answer -= int(ms[i+1])
            
    return answer


# 다른 풀이 1
# 천재인듯
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))


# 다른 풀이 2
solution=eval


print(solution('3 + 4'))
print(solution('3 + 4 - 9 - 2 + 0 - 199 + 392'))