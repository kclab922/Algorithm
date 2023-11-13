# 내 코드
# 1. 가운데 물을 기준으로 왼쪽 파트 구하기
#   - 0번인덱스는 항상 물이므로, 1번 인덱스부터 for문 돌리기
#   - 곱하기 연산자를 쓰기 위해 인덱스번호를 str화
#   - '해당 인덱스의 값'을 2로 나눈 몫만큼 '인덱스번호'를 반복하면 왼쪽 파트 완성
# 2. 왼쪽파트 + '0' + 뒤집은 왼쪽파트
  
def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    return answer + '0' + answer[::-1]



print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))