def solution(num, hand):
    answer = ''
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for i in range(4):
        for j in range(3):
            if j == 0:
                answer += 'L'
            elif j == 2:
                answer += 'R'
            else:
                if i == 0
    return 


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))