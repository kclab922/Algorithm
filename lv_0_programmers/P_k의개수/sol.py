# 내 풀이 
# 1. i~j까지 반복
# 2. n과 k 모두 글자로 바꿔서 count 메소드

def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        answer += str(n).count(str(k))
    return answer

# 다른 풀이
def solution(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i,j+1)])
    return answer

print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10, 2))
