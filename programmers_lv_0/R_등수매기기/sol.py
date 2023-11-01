# 내 풀이
# 1. 평균 도출: 입력값을 행렬로 볼 때 열은 영/수 점수로 각각 정해져있으므로 고정하고, 행만 반복 돌리며 평균값 리스트 도출 ([75.0, 70.0, 55.0, 65.0])
# 2. 등수 도출: 평균 리스트의 각 원소를 반복 돌리며, 내림차순 정렬시의 인덱스를 활용하여 등수 도출

def solution(score):
    average = []
    rank = []

    # 1. 평균 도출
    for i in range(len(score)):
        average.append((score[i][0] + score[i][1]) / 2)
    
    # 2. 등수 도출
    for a in average: 
        rank.append(sorted(average, reverse=True).index(a) + 1)

    return rank


# 다른 풀이
# 굳이 평균값 안 구하고, 영수 점수 합계만 이용해도 됨.
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))