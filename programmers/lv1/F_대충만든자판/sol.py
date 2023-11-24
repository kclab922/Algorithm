# 내 코드
# 전체구조: 목표 속 첫번째 문자열의 첫번쨰 글자부터(eg.'A') 내 자판으로 도출시킬 수 있는지 하나씩 검토
#          => 예를 들어, 'B'로 검토하는 경우 먼저 1번 키에 있으므로 두 번 누른다고 저장
#          => 1번 키 검토 완료 후 2번 키로 넘어갔을 때, B를 더 빨리 쓸 수 있으므로 한 번 누른다고 바꿔줌
#          => 이렇게 글자 하나하나 살펴보다가, 한 글자라도 내 자판에 없으면 그 즉시 -1 도출하고 다음 문자열로 넘어갈 것.

def solution(keymap, targets):
    answer = []
    for w in targets:
        total_press = 0
        for c in w:
            min_press = 101
            for k in keymap:
                if 0 < k.find(c)+1 < min_press:
                    min_press = k.find(c)+1
            if min_press == 101:
                total_press = -1
                break

            total_press += min_press

        answer.append(total_press)
    return answer



# 다른 코드 (딕셔너리로 시간복잡도 감소)
def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            if ch in hs:
                hs[ch] = min(i + 1, hs[ch])  
            else:
                hs[ch] = i + 1

    for t in targets:
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer





print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
