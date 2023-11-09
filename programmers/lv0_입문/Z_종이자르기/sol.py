# 내 풀이

# M, N => 가위질 수
# 1, 1 => 0
# 1, 2 => 1
# 1, 3 => 2
# 1, 4 => 3

# 2, 1 => 1
# 2, 2 => 3
# 2, 3 => 5
# 2, 4 => 7

# 3, 1 => 2
# 3, 2 => 5
# 3, 3 => 8

# 규칙: M-1을 기본값으로 M씩 N-1번 증가 
# 예: (2, 4) => 1을 기본값으로 2씩 3번 증가

def solution(M, N):
    answer = M-1
    for _ in range(N-1):
        answer += M
    return answer
    
# 다른 풀이
def solution(M, N):
    return (M * N) - 1

print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))


