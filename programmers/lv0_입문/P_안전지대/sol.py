# 내 코드
# 풀이방법
# 1. list out of range 신경쓰지 않기 위해, (n+2) X (n+2) 크기의 빈 matrix 생성
# 2. board에서 1 등장시 mat에서 9개칸을 모두 1로 변경
# 3. matrix에서 테두리 라인이 아닌 0의 개수 도출 

def solution(board):
    n = len(board)
    mat = [[0]*(n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                mat[i][j] = 1
                mat[i][j+1] = 1
                mat[i][j+2] = 1
                mat[i+1][j] = 1
                mat[i+1][j+1] = 1
                mat[i+1][j+2] = 1
                mat[i+2][j] = 1
                mat[i+2][j+1] = 1
                mat[i+2][j+2] = 1

    count = 0
    for i in range(n+2):
        for j in range(n+2):
            if 0<i<n+1 and 0<j<n+1 and mat[i][j] == 0:
                count += 1
    
    return count


# 다른 코드
# 다시 볼 것...
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board): 
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))