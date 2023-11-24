# 내 코드
# 전체구조: 가운데 물(0)을 기준으로, 왼쪽 오른쪽 파트를 나눔 => 왼쪽을 먼저 구한 뒤 뒤집어서 오른쪽 만들기
# 1. 왼쪽 파트 구하기
#   - food의 0번 인덱스는 항상 물이므로, 1번 인덱스부터 for문 돌리기
#   - '해당 인덱스에 해당하는 food의 원소값'을 2로 나눈 몫만큼 '인덱스번호'를 반복하면 왼쪽 파트 완성
#   - 이때 '인덱스번호'를 int 그대로 쓰면 반복이 아닌 연산이 되므로, 인덱스번호를 str화해서 숫자열 만들기
# 2. 왼쪽파트 + '0' + 뒤집은 왼쪽파트

def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    return answer + '0' + answer[::-1]



print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))