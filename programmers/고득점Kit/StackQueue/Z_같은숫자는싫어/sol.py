# 내 코드
# 1. 1번~끝번 인덱스까지 반복
# 2. i번 인덱스가 그 앞 인덱스와 다르면 => answer에 추가
# 3. 0번인덱스 + answer 리턴

def solution(arr):
    answer = []
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return [arr[0]] + answer




print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))