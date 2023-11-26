def solution(wp):
    answer = [51, 51, 0, 0]
    for i in range(len(wp)):
        for j in range(len(wp[i])):
            if wp[i][j] == '#':
                if i < answer[0]:
                    answer[0] = i
                if j < answer[1]:
                    answer[1] = j
                if i+1 > answer[2]:
                    answer[2] = i+1
                if j+1 > answer[3]:
                    answer[3] = j+1
    return answer

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))