# def solution(keymap, targets):
#     answer = []
    # for i in range(len(targets)):
    #     total_press = 0
    #     for j in range(len(targets[i])):

#             min_press = 10000
#             for k in keymap:
#                 if -1 < k.find(targets[i][j]) < min_press-1:
#                     min_press = k.find(targets[i][j])+1
#             if min_press == 10000:
#                 return [-1]
#             total_press += min_press

#         answer.append(total_press)
#     return answer


def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        total_press = 0
        for j in range(len(targets[i])):

            min_press = 100000
            for k in keymap:
                if -1 < k.find(targets[i][j]) < min_press-1:
                    min_press = k.find(targets[i][j])+1
                else:
                    continue
            if min_press == 100000:
                return [-1]
            total_press += min_press

        answer.append(total_press)
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
