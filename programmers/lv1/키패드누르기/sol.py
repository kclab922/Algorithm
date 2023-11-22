def distance(start, goal):
    pad = {
        1: [0, 0],
        2: [1, 0],
        3: [2, 0],
        4: [0, 1],
        5: [1, 1],
        6: [2, 1],
        7: [0, 2],
        8: [1, 2],
        9: [2, 2],
        '*': [0, 3],
        0: [1, 3],
        '#': [2, 3],
    }

    a1, b1 = pad[start]
    a2, b2 = pad[goal]

    return abs(a1-a2) + abs(b1-b2)



def solution(num, hand):
    answer = ''
    left = '*'
    right = '#'

    for i in num:
        if i in [1, 4, 7]:
            answer += 'L'
            left = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right = i
        else:
            if distance(left, i) < distance(right, i):
                answer += 'L'
                left = i
            elif distance(right, i) < distance(left, i):
                answer += 'R'
                right = i
            else:
                if hand == 'left':
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
    return answer
            



print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))