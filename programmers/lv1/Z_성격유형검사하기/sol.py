# 내 코드
# 시간복잡도 완화를 위해 딕셔너리와 짧은 for문을 활용 => 최대범위까지 돌아가는 for문의 개수를 1개로 줄여봄.

# 풀이과정
# 0. 전체구조: (문단 단위 구분) 성격유형별로 0점을 기본점수로 설정 => 각 유형별 점수 누적계산 => 경쟁군 비교하여 우위성향 도출 
# 1문단. 전체 성격유형을 각각 key로, 해당 유형의 점수 value로 딕셔너리 생성 / 기본점수 0점 설정
# 2문단. 선택지 척도 choices를 기준으로 for문 돌림 
#    => 점수 올려줄 성격유형을 도출하여 survey 인덱스로 접근 
#    => 해당 성격유형을 key값으로 하는 점수 value값에 점수 더해주기
# 3문단. 한 지표 내의 경쟁하는 2개 유형씩 묶어서 for문 돌림
#    => 점수가 큰 쪽을 answer에 더하기 / 같으면 정렬해서 0번 인덱스를 answer에

def solution(survey, choices):
    answer = ''

    score = {}
    for i in 'RTCFJMAN':
        score[i] = 0
    
    for i in range(len(survey)):
        if choices[i] <= 3:
            score[survey[i][0]] += 4 - choices[i]
        elif choices[i] >= 5:
            score[survey[i][1]] += choices[i] - 4
        
    for i in ['RT', 'CF', 'JM', 'AN']:
        if score[i[0]] > score[i[1]]:
            answer += i[0]
        elif score[i[0]] < score[i[1]]:
            answer += i[1]
        else:
            answer += sorted(i)[0]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))


테스트 1 〉	 통과 (0.01ms, 10.1MB)
테스트 2 〉	 통과 (0.02ms, 10.2MB)
테스트 3 〉	 통과 (0.03ms, 10.3MB)
테스트 4 〉	 통과 (0.01ms, 10.2MB)
테스트 5 〉	 통과 (0.01ms, 10.3MB)
테스트 6 〉	 통과 (0.01ms, 10.2MB)
테스트 7 〉	 통과 (0.02ms, 10.2MB)
테스트 8 〉	 통과 (0.02ms, 10.3MB)
테스트 9 〉	 통과 (0.02ms, 10.3MB)
테스트 10 〉 통과 (0.03ms, 10.2MB)
테스트 11 〉 통과 (0.04ms, 10.3MB)
테스트 12 〉 통과 (0.07ms, 10.2MB)
테스트 13 〉 통과 (0.15ms, 10.1MB)
테스트 14 〉 통과 (0.32ms, 10.3MB)
테스트 15 〉 통과 (0.28ms, 10.2MB)
테스트 16 〉 통과 (0.29ms, 10.4MB)
테스트 17 〉 통과 (0.18ms, 10.3MB)
테스트 18 〉 통과 (0.29ms, 10.2MB)
테스트 19 〉 통과 (0.32ms, 10.2MB)
테스트 20 〉 통과 (0.35ms, 10.3MB)

