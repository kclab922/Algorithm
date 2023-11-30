def solution(band, health, attacks):
    bandTime, healAmount, healAdd = band[0], band[1], band[2]
    now = health
    
    for i in range(len(attacks)):
        now -= attacks[i][1]
        if now <= 0:
            return -1
        else:
            if i <= len(attacks)-2:
                between = attacks[i+1][0]-attacks[i][0]-1
                if bandTime > between:
                    now += healAmount * between
                else:
                    now += (healAmount * between) + (healAdd * (between//bandTime))
            if now > health:
                now = health

    return now

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))