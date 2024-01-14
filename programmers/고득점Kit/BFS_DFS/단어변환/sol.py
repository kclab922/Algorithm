# dfs
from collections import deque

def solution(begin, target, words):
    if target not in words: # 타겟이 워드에 아예 없을시 밑에서 while문이 계속 돌 수 있으므로 먼저 조건 설정.
        return 0  

    queue = deque()
    queue.append([begin, 0])
    visited = [0] * len(words) # 각 단어를 방문해야하므로, 단어 개수만큼 방문여부 만들어줌.

    while queue:
        word, count = queue.popleft() # 큐에서 빼다가 각각 현재글자, 총 몇단계를 거쳤는지에 할당
        
        if word == target: # 이때 현재글자가 타겟과 같다면
            return count # 그대로 몇단계 거쳐왔는지 답을 출력!
        
        for i in range(len(words)): # 현재 단어와 비교하기 위해 words 원소들을 돌아야하므로, 단어 개수만큼 for문.
            difference = 0 # words를 돌며, 현재 단어와 비교할마다 차이나는 글자수 세어주기
            if not visited[i]: # i번째 원소에 아직 방문을 안 했다면, 아래 방법으로 방문하자.
                for j in range(len(word)): # 여기서 word는 현재단어. 현재단어를 한 글자씩 쪼개면서 words속 단어들과 비교.
                    if word[j] != words[i][j]: # 만약 현재단어의 j번째 글자가, words의 i번째(위에서 이미 지정됨) 단어의 j번째 글자와 다르다면
                        difference += 1 # 차이나는 글자수에 +1
                if difference == 1: # j for문이 돌아서 현재단어와 words속 단어 하나를 비교했는데, 차이나는 글자 수가 1이라면
                    visited[i] # 해당 단어는 방문처리!
                    queue.append([words[i], count+1]) # 그리고 현재 단어를 해당 단어로 바꿔주고, 한 단계를 더 거친 것이므로 count+1 해서 큐에 넣어주자.
          

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))