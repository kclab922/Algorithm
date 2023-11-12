# 내 코드
# 1. 알파벳 문자열 a 설정 / 빈 문자열 answer 설정
# 2. 문자열s의 각 원소 i를 for문 반복
#    (1) 소문자면? => a에서 i의 인덱스 -26 + n 를 뽑아 answer에 더해주기 (-26: index out of range 방지용) 
#    (2) 대문자면? => 소문자로 바꿔서 (1) 진행 후 다시 대문자로 바꿔서 answer에 더해주기
#    (3) ' '이면? => ' ' 그대로 answer에 더해주기
def solution(s, n):
    a = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in s:
        if i.islower():
            answer += a[a.index(i) + n - 26 ]
        elif i.isupper():
            answer += a[a.index(i.lower()) + n - 26].upper()
        else:
            answer += ' '
            
    return answer


# 다른 코드 1
# ord(str): 문자열 => int (유니코드)
# chr(int): int => 문자열 (유니코드)
# 아스키코드: a의 시작값은 97, A의 시작값은 65...리뷰 요망.
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)



# 다른 코드 2
# -26 대신, %26 써도 됨!


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))