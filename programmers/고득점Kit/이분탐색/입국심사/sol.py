#1. 가능한 소요시간의 범위를 start부터 end까지 설정.
#2. 심사 완료한 사람 수가 n이 될 때의 '소요시간'을 target으로 찾는 것.

def solution(n, times):
    answer = 0
    start, end = 1, max(times)* n   # 1초~120초
    
    while start <= end:     # 28초 > 27초
        mid = (start + end) // 2    # 현재 mid초 - 1~120초(60초) => 1~59초(30초) => 1~30초(15초) => 16~30초(23초) => 24~30초(27초) => 28초~30초(29초) => 28초
        
        count = 0   # 심사완료된 사람 수 누적
        for time in times:      # [7, 10]
            count += mid // time    # mid초일 때, 각 심사대(time)에서 통과시킨 사람의 수 - 8명 => 4+3=7명 => 2+1=3명 => 3+2=5명 => 3+2=5명 => 4+2=6명 => 4+2=6명
            if count > n:   # 어차피 n명까지만 심사하면 되므로, count가 n을 넘어가는 순간 for문 멈춰
                break 
        
        if count >= n:  # 심사완료된 인원이 n보다 많거나 같은 경우 - 8명 => 7명 => 6명 => 6명
            end = mid - 1       # end = 59초 => 29초 => 28초 => 27초
            answer = mid        # answer = 60초 => 30초 => 29초 => 28초
        else:   # 심사완료된 인원이 n보다 적은 경우 => 3명 => 5명 => 5명
            start = mid + 1     # mid초+1초를 시작으로 다시 돌자 => 16초 => 24초 => 28초
        
    return answer



print(solution(6, [7, 10]))