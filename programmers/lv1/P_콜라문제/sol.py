# 내 코드
# 호진님 헌정문제
def solution(a, b, n):
    answer = 0
    while n >= a:
        i, j = divmod(n, a)
        answer += i*b
        n = i*b + j
    
    return answer 


# 다른 코드
# 이해노노
# a개만 팔고 b개를 받는 과정은 결국 a-b 개씩 병을 소비하는 것으로 생각
# 첫번째 진행할 때는 a개만 소비되기 때문에, b만큼 못받음(-b)
# 그 조건을 먼저 계산 n-b 
# 반복횟수는 n-b // (a-b) 여기에 받는 병수 b 곱한 것
solution = lambda a, b, n: (n - b) // (a - b) * b


print(solution(2, 1, 20))
print(solution(3, 1, 20))