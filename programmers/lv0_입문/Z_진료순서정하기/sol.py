# 내 풀이1
# 1. emergency 원소들을 num으로 설정해 for문 반복
# 2. emergency를 내림차순 정렬 시 해당 num의 index를 도출하고, 그에 1을 더한 값들을 리스트화
def solution(emergency):
    return [sorted(emergency, reverse=True).index(num) + 1 for num in emergency]

# 내 풀이2
# 1번 풀어쓴 ver.
def solution(emergency):
    answer = []
    for num in emergency:
        rank = sorted(emergency, reverse=True).index(num) + 1
        answer.append(rank)
    return answer


print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))