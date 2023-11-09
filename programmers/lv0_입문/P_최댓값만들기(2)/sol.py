# 내 풀이 (max함수가 없다고 가정하고 풀어 쓴 ver.)
# 1. 구조: 리스트에서 중복되지 않는 숫자 2개 뽑고, 최댓값에 계속 재할당
# 2. my_max값 설정 이유: 가장 작은 두 수가 -10000, -10000일 수 있으므로

def solution(numbers):
    my_max = -100000000
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] * numbers[j] > my_max:
                my_max = numbers[i] * numbers[j]
    return my_max

# 다른 풀이
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 


print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))