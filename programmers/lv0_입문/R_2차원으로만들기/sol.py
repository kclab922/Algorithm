# 내 풀이
# 1. 빈 이차원 배열을 만든다.
# 2. 빈 이차원 배열을 'num_list의 맨 앞 원소부터 하나씩 빼서' 채운다.
def solution(num_list, n):
    answer = [[0 for _ in range(n)] for _ in range(len(num_list)//n)]
    for i in range(len(num_list)//n):
        for j in range(n):        
             answer[i][j] = num_list.pop(0)
    return answer

# 다른 풀이
# list[0:3] => [list[0], list[1], list[2]]
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))