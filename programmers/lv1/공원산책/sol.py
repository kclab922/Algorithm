def solution(park, routes):
    now = [0, 0]
    d = {'N': [-1,0], 'W': [0,-1], 'E': [0,1], 'S': [1,0]}

    for i, p in enumerate(park):
        if 'S' in p:
            now = [i, p.index('S')]
            break

    for r in routes:
        op, n = r[0], int(r[2])
        x, y = d[op][0], d[op][1]
        count = 0
        temp = [now[0], now[1]]

        if 0 <= now[0]+(x*n) < len(park) and 0 <= now[1]+(y*n) < len(park[0]):
            while count < n:
                if park[temp[0]+x][temp[1]+y] == 'X':
                    break
                else:            
                    temp = [temp[0]+x, temp[1]+y]
                    count += 1
            if count == n:
                now = temp

    return now

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))