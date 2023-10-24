# 풀이1
# tip: range 설정 시 3번째 변수로 '간격'도 지정 가능함을 잊지 말자!

def solution(n):
    return [num for num in range(1, n+1, 2)]

print(solution(10))
print(solution(15))