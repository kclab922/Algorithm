def solution(keymap, targets):
    answer = []
    for words in targets:
        total_press = 0
        for char in words:

            min_press = 101
            for k in keymap:
                if char in k:
                    min_press = min(k.index(char)+1, min_press)
            if min_press == 101:
                return [-1]

            total_press += min_press

        answer.append(total_press)
    return answer






print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
