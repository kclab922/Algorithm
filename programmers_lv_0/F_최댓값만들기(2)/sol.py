# 내 풀이1 (tc 하나가 계속 실패 뜸)
def solution(numbers):
    my_max = 0
    # 일단 인덱스 2개 뽑기 
    # 왜 인덱스? 원소2개를 안 겹치게 고를 때 단순히 '첫째 숫자와 둘째 숫자가 다르다'고 하면 모든 원소를 이용할 수 없으므로. tc3 20, 5 참고
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            # 인덱스가 서로 다른 두 원소이고 + 둘의 곱이 앞선 최댓값보다 크면 => 최댓값을 대체
            if i != j and numbers[i] * numbers[j] > my_max:
                my_max = numbers[i] * numbers[j]
    return my_max




print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))