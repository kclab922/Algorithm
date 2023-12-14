# 내 코드
# 1. 딕셔너리 형성: {'headgear': 2, 'eyewear': 1}
# 2. 경우의 수: (각 종류가 0개~최댓값인 경우의 수) - (모두 0개인 경우) => (3*2) - (1)

def solution(clothes):
    
    d = {}
    for _, c in clothes:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    answer = 1
    for _, v in d.items():
        answer *= v+1

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))