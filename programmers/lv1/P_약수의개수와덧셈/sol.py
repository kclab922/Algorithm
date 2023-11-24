# 내 코드
# 전체구조: l부터 r까지 각 수의 약수를 구하고 => 약수 개수가 짝수면 더하고, 홀수면 빼기
def solution(l, r):
    answer = 0
    for i in range(l, r+1):
        yaksu = []
        for j in range(1, i+1):
            if i%j == 0:
                yaksu.append(i)
        if len(yaksu) % 2:
            answer-=i
        else:
            answer+=i
    return answer


# 다른 코드
# 제곱근이 정수인 수 => 약수의 개수가 홀수!
# 예) 4 => (1,4) (2,2) (4,1): 제곱근으로 이루어진 약수가 하나 껴 있으므로
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer



print(solution(13, 17))
print(solution(24, 27))