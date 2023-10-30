# 내 풀이1
# 1. s의 각 문자를 c로 반복
# 2. 이때 s 안에 있는 c의 개수가 1개인 것들을 모아서 sorted로 알파벳순 정렬 후 join으로 문자열 묶기
def solution(s):
    return ''.join(sorted([c for c in s if s.count(c) == 1]))

# 내 풀이 2
# 1번 풀어씀
def solution(s):
    answer = ''
    for c in s:
        if s.count(c) == 1:
            answer += c
    return ''.join(sorted(answer))



print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))