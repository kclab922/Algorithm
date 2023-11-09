# 평행: 두 직선의 기울기(y증가량/x증가량)가 같음
# 1. 한 직선의 기울기를 구하는 함수 inc 설정
# 2. dots에서 서로 다른 2개 점을 고르고 => 기울기 같으면 1, 다르면 0  


# 내 코드

def inc(dot1, dot2):
    return (dot1[1]-dot2[1])/(dot1[0]-dot2[0])

def solution(dots):
    for i in dots:
        for j in dots:
            if i!=j:
                a = inc(i, j) 
                d = dots[:]
                d.remove(i)
                d.remove(j)
                b = inc(d[0], d[1])
                if a == b:
                    return 1

    return 0


# 다른 코드
# 경우의 수 3개 모두 나열
# 코드 쓰는 법 참고!
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
