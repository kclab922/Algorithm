def solution (keyinput, board):
    now = [0, 0]

    for key in keyinput:
        if key == 'left':
            now = [now[0]-1, now[1]]
        elif key == 'right':
            now = [now[0]+1, now[1]] 
        elif key == 'up':
            now = [now[0], now[1]+1]
        elif key == 'down':
            now = [now[0], now[1]-1]
        
        if now[0] < -(board[0]//2):
            now[0] = -(board[0]//2)          
        elif now[0] > board[0]//2:
            now[0] = (board[0]//2)  
        elif now[1] < -(board[1]//2):
            now[1] = -(board[1]//2)
        elif now[1] > (board[1]//2):
            now[1] = (board[1]//2)

    return now

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))
