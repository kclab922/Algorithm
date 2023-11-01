# 내 풀이
# 1. 람다식 통해 튜플 생성
# 2. 첫째 인자 기준 오름차순 => n과의 거리가 작은 수부터
# 3. 둘째 인자 기준 내림차순 => n과의 거리가 같을 땐 더 큰 수 먼저

def solution(numlist, n):
    return sorted(numlist, key = lambda x: (abs(n-x), -x))

print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))