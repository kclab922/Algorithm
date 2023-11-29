# 내 코드
def solution(park, routes):
    now = [0, 0]
    d = {'S': [1,0], 'E': [0,1], 'N': [-1,0], 'W': [0,-1]}

    for i, p in enumerate(park):
        if 'S' in p:
            now = [i, p.index('S')]
            break

    for r in routes:
        NEWS, n = r[0], int(r[2])
        xm, ym = d[NEWS][0], d[NEWS][1]
        if 0 <= now[0]+(xm*n) < len(park) and 0 <= now[1]+(ym*n) < len(park[0]):
            count = 0
            while count < n:
                if park[now[0]+xm][now[1]+ym] == 'X':
                    break
                else:            
                    now = [now[0]+xm, now[1]+ym]
                    count += 1
            if count != n:
                now = [now[0]-(xm*count), now[1]-(ym*count)]

    return now


# 다른 코드
def solution(park, routes):
    h = len(park)
    w = len(park[0])
    x,y = 0,0
    
    nav = {
        'S': [1,0],
        'N':[-1,0],
        'W': [0,-1],
        'E':[0,1]
    }
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x = i
                y = j
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        flag = 0
        step_x = x
        step_y = y
        for i in range(1,distance+1):
            step_x += nav[direction][0]
            step_y += nav[direction][1]
            
            if step_x >= h or step_x <= -1 or step_y >= w or step_y <= -1 or park[step_x][step_y] == 'X':
                flag = 1
                break
            
        if(flag == 0):
            x += nav[direction][0] * distance
            y += nav[direction][1] * distance
    
    answer = [x,y]
    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))