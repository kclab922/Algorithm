def solution(num, hand):
    answer = ''
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    l = [1, 4, 7]
    r = [3, 6, 9]
    m = [2, 5, 8, 0]

    mydict = {}

    for n in num:
        if n in l:
            mydict[n] = 'L'
        elif n in r:
            mydict[n] = 'R'
        elif n == 2:


    return pad.index(3)


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))