# 내 풀이
# 1. 미지의 변을 s로 상정 후 1~2000(최댓값)까지 반복문
# 2. 입력값인 sides 리스트에 s를 원소로 추가 => `sides+[s]` ex) [1, 2, s] 
# 3. 오름차순 정렬 => 인덱스2 < 인덱스0+인덱스1 인 경우의 수 누적합
def solution(sides):
    return sum([1 for s in range(1, 2000) if sorted(sides+[s])[2] < sorted(sides+[s])[0] + sorted(sides+[s])[1]])


# 다른 풀이 
# 삼각형이 되기 위한 조건: a > b > c일 때, a < b + c 를 만족해야 함.
# 주어진 두 변을 a, b(a > b), 나머지 한 변을 x라 상정
# 1. a가 가장 긴 변인 경우: a < b + x =>  x > a - b
# 2. x가 가장 긴 변인 경우: x < a + b
# 위의 1과 2를 모두 만족시키는 x의 범위는 (a - b) < x < (a + b) 
# 이때 x의 개수: (a + b) - (a - b) - 1 => 이를 정리하면 2 * b - 1
def solution(sides):
    return 2 * min(sides) - 1

print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))