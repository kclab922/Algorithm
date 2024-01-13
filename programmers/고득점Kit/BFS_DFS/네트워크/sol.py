def dfs(i, computers, visited):
    visited[i] = 1 # i번째 노드에 방문한 것이므로 True로 바꿔줌.
    for a, b in enumerate(computers[i]): # b가 1이면 a는 i번째 노드와 연결된 노드, b가 0이면 a와 i는 연결 안 되어 있으므로 상관없음.
        if b==1 and not visited[a]: # b가 1이면 a는 i번째 노드와 연결된 노드인데, a를 아직 방문 안했다면?
            dfs(a, computers, visited) # i와의 연결노드인 a도 방문해! 재귀 타고타고 a와 연결된 노드들도 쭉쭉 방문.

def solution(n, computers):
    visited = [0] * n  # n=노드의 개수. 일단 3개의 모든 노드에 방문하지 않은 상태.
    count = 0

    for i in range(n): # 각 노드에 모두 방문해야 하므로 for문.
        if not visited[i]: # i번째 노드의 방문상태가 0이라면:
            dfs(i, computers, visited) # 방문 고고
            count += 1 # 방문했다는 건 일단 네트워크 하나가 늘어난 것이므로 cout +1
    
    return count 

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))