# 내 코드
# 1. 빈 2차원 배열 answer을 만들고
# 2. a,b 더한 값을 answer에 할당
def solution(a, b):
    answer = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            answer[i][j] = a[i][j] + b[i][j]
    return answer


# 다른 코드 1
# 이 코드 좋다.
# zip(): 리스트 2개를 동시에 for문 돌릴 때 쓰기.
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer


# 다른 코드 2
# zip(*zip(a,b)): a,b를 zip 했다가 다시 unzip
# https://docs.python.org/ko/3/library/functions.html?highlight=zip#zip
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]


print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))