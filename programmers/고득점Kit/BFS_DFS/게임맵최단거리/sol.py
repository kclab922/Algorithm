# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
#     x, y, count = 0, 0, 0

#     while :
    
#         if maps[n-1][m] == 0 and maps[n][m-1] == 0 and maps[n-1][m-1] == 0:
#             return -1
#         elif:
            

  
from collections import deque

def bfs(start, maps):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    queue = deque()
    queue.append(start)
    while queue:
        y, x, count = queue.popleft()
        maps[y][x] = 0
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx

            if (ny == len(maps)-1) and (nx == len(maps[0])-1):
                return count+1

            elif (0 <= ny < len(maps)) and (0 <= nx < len(maps[0])) and (maps[ny][nx] == 1):
                maps[ny][nx] = 0
                queue.append((ny, nx, count+1))

    return -1


def solution(maps):
    return bfs((0,0,1), maps)



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
