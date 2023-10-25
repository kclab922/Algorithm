# 풀이1
def solution(n):
    answer = []
    for num in range(1, n+1):
        if n % num == 0:
            answer.append(num)
    return answer

# 풀이2
def solution(n):
    return [num for num in range(1, n+1) if n % num == 0]

print(solution(24))
print(solution(29))