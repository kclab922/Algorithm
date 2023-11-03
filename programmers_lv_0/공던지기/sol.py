# 내 풀이
# 풀이구조: (numbers 리스트의 무한추가를 가정하면) 답은 (k-1)*2 번 인덱스 => numbers 리스트를 필요한만큼 붙여주기
# tc2: (5-1)*2 = 8번째 인덱스가 답 => 8//6 + 1 = 2번의 numbers 반복 필요하므로 곱해주기

def solution(numbers, k):
    return (numbers*((k-1)*2//len(numbers)+1))[(k-1)*2]


# 다른 풀이
# 명쾌하다.
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]


print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))