# 내 풀이
# 1. 반복문: 인덱스를 0, n, 2n, ...으로 잘라줌
# 2. 해당 인덱스~ +n번째까지 출력
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]

print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))