def solution(lines):

    for tc in range(len(lines)):

        # 겹치는 선분의 길이
        co_lines = 0

        # 각 선분이 지나가는 구간의 정수 배열
        num1 = list(range(int(lines[0][0]), int(lines[0][1])+1))
        num2 = list(range(int(lines[1][0]), int(lines[1][1])+1))
        num3 = list(range(int(lines[2][0]), int(lines[2][1])+1))

        # 중복 구간의 정수 배열 리스트
        num1num2 = list(set(num1).intersection(num2)) 
        num1num3 = list(set(num1).intersection(num3))
        num2num3 = list(set(num2).intersection(num3))
        num1num2num3 = list(set(num1num2).intersection(num3))

        # 경우의 수 총 10가지
        # 선분이 중복된다 = 중첩 구간 리스트의 밸류 개수가 2 이상이다
        # 중첩 구간의 길이 = 중첩 구간 리스트의 각 밸류값은 각각 점이므로, 전체 밸류 개수 -1

        # 선분12 중첩
        if len(num1num2) >= 2:
            co_lines += len(num1num2)-1
            # 선분23 중첩
            if len(num2num3) >= 2:
                co_lines += len(num2num3)-1
                # 선분123 중첩 제외 
                if len(num1num2num3) >= 2:
                        co_lines -= len(num1num2num3) - 1
                # 선분13 중첩
                if len(num1num3) >= 2:
                    co_lines += len(num1num3)-1
                    # 선분123 중첩 제외
                    if len(num1num2num3) >= 2:
                        co_lines -= len(num1num2num3) - 1

            # 선분12 중첩X
            else:
                # 선분13 중첩
                if len(num1num3) >= 2:
                    co_lines += len(num1num3)-1

        # 선분12 중첩X
        else:
            if len(num2num3) >= 2:
                co_lines += len(num2num3)-1
                if len(num1num3) >= 2:
                    co_lines += len(num1num3)-1
            else:
                if len(num1num3) >= 2:
                    co_lines += len(num1num3)-1
        
    return co_lines

print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))