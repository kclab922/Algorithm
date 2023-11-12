# 내 코드
# 1. enumerate() for문 돌리기 => a,b = (0, 'zero') ...
#    (list로 감싼 이유는 해당 함수가 lazy하므로. map 쓸 때와 같은 원리.)
# 2. s에서 b를 a로 바꿔주기
#    (str으로 감싼 이유는 replace 함수 쓰기 위해선 두 argument가 다 str이어야 하므로.)
# 3. int화 해서 답 도출
def solution(s):
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for a, b in list(enumerate(word)):
        s = s.replace(b, str(a))
    return int(s)


# 다른 코드
# 인덱스 활용
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)



print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))