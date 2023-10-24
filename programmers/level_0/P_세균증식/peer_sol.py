# 풀이1
# tip: for문에서 range 설정시 0~t-1 이나 1~t 나 반복횟수는 같음.
def solution(n, t):
    for i in range(t) :
        n *= 2
    return n

# 풀이2
# 수학적 접근인듯...?
def solution(n, t):
    return 2**t * n