# 내 코드
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



# 다른 코드 (효율성 이슈 해결)
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
