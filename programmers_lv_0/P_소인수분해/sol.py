# 처음에 2번으로 작성했다가, 같은 코드구조가 반복됨을 발견하고 이를 개선하기 위해 함수를 나누어 설정

# 내 코드 1 
# 풀이구조
# 1. insu(n): n의 인수를 도출하는 함수 설정 
# 2. solution(n): insu(n)의 원소 i들 중 소수(= 2 이상인 insu(i)가 1개인 수)만 도출 
# (범위: 1은 어차피 소수가 아니므로 insu()에서부터 배제)
# tc1: insu(12) = [2, 3, 4, 6, 12] 
#      각 원소의 인수 (1 제외) - 2: 2 / 3: 3 / 4: 2, 4 / 6: 2, 3 / 12: 2, 3, 4, 6, 12 
#      이 중 개수가 1개인 [2, 3]만 소수이므로 도출 

def insu(n):   
    return [m for m in range(2, n+1) if n % m == 0]

def solution(n):   
    return [i for i in insu(n) if len(insu(i))==1]


# 내 코드 2
# 풀이구조
# 1. n의 인수 목록 insu 도출
# 2. insu의 원소들 중 소수(1을 제외한 인수가 1개뿐인 수)만 모아서 최종 도출 

def solution(n):   
    insu = []
    answer = []
    
    for m in range(2, n+1):
        if n % m == 0:
            insu.append(m)

    for i in insu:
        l = []
        for j in range(2, i+1):
            if i % j == 0:
                l.append(j)
        if len(l) == 1:
            answer.append(i)

    return answer



# 다른 코드 (시간단축)
# 2부터 시작해서 n을 나눌 수 있을 때까지 나누고, 그 다음 3으로 나누고.. 굿.
# 실제 내가 소인수분해를 진행하는 방법에서 아이디어 얻을 것.
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer

print(solution(12))
print(solution(17))
print(solution(420))