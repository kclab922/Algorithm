# 내 코드
def solution(n):
    answer = []
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
               answer.append(n[i] + n[j])
    return sorted(set(answer))


# 다른 코드
# 4째줄 굿
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))