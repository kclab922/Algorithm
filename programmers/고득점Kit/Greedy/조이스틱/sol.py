# def solution(name):
#     alpha = [chr(x) for x in range(65, 91)]
#     # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#     myL =[]
#     for char in name:
#         alphaIndex = alpha.index(char)
#         if alphaIndex < 13:
#             myL.append(alphaIndex)
#         else:
#             myL.append(abs(alphaIndex-26))
#     print(sum(myL))
    # [9, 4, 9, 12, 4, 13]
    # [9, 0, 13]
    # [9, 0, 1]

    # now = 0
    # answer = myL[0]
    # visited = [0]
    # length = len(name)
    
    # while len(visited) < length:
    #     myL2 = myL
    #     for i in range(1, length):
    #         if myL[i] == 0:
    #             myL[i] = 14+11
    #         elif (myL[i] != 0) and (i != now) and (i not in visited):
    #             if (abs(now-i) < length/2):
    #                 myL2[i] += abs(now-i)
    #             else:
    #                 myL2[i] += now+length-i
    #     now = myL2.index(min(myL2))
    #     answer += myL2[now]
    #     visited.append(now)
    #     myL[now] = 14+11
    # return answer




# def solution(name):
#     alpha = [chr(x) for x in range(65, 91)]
#     # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M' // 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#     answer = 0
#     for char in name:
#         alphaIdx = alpha.index(char)
#         if alphaIdx < 13:
#             answer += alphaIdx
#         else:
#             answer += abs(alphaIdx-26)
    
#     if name[1] == 'A' or name[-1] == 'A':
#         return answer + len(name)-2 
#     else:
#         return answer + len(name)-1


def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 1. 기존, 2. 연속된 A의 왼쪽시작 방식, 3. 연속된 A의 오른쪽시작 방식 비교 및 갱신
        # for문 돌면서 왼쪽으로 갈지 오른쪽으로 갈지 매번 체크를 한다.
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move

    return answer


print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZ"))