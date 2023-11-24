# 풀이과정
# 1. 앞에 나왔던 글자라면? = 'i번째 value값'이 '0~i-1번째 밸류값' 속에 있다면?
#    '0~i번째 밸류값'을 뒤집은 문자열에서 / i의 인덱스값을 도출한 후 / +1 
#    (활용: [::-1]=> 뒤집기 / .index(i) => i가 처음 등장했을 때의 인덱스를 도출)
# 2. 처음 나오는 글자라면?
#    result 리스트에 [-1]을 추가 

def solution(s):
    result = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            result += [s[:i][::-1].index(s[i]) + 1]
        else:
            result += [-1]
        
    return result


# 인덱싱 사용법
# str[::-1]: 문자열 뒤집기
# str[3:0:-1]: 3번~1번까지 역순으로 출력 (0번제외)
# str[3::-1]: 3번~0번까지 역순으로 출력

print(solution("banana"))
print(solution("foobar"))