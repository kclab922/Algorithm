# 처음에 3번으로 작성했다가, 같은 코드구조가 반복됨을 발견하고 이를 개선하기 위해 함수 여러 개 설정

# 내 코드 1 
# 풀이구조
# 1. insu(): 인수를 도출하는 함수 설정 (범위: 1은 어차피 소수가 아니므로 여기서부터 배제)
# 2. solution(): n의 인수 i들 중 소수(= 2 이상인 i의 인수가 1개인 수) 도출 
# tc1: insu(12) = [2, 3, 4, 6, 12] 
#      각 원소의 인수 (1 제외) - 2: 2 / 3: 3 / 4: 2, 4 / 6: 2, 3 / 12: 2, 3, 4, 6, 12 
#      이 중 개수가 1개인 [2, 3]만 소수이므로 도출 

def insu(n):   
    return [m for m in range(2, n+1) if n % m == 0]

def solution(n):   
    return [i for i in insu(n) if len(insu(i))==1]



# 내 코드 2
# 풀이구조
# 1. 소수여부 판단하는 함수 설정
# 2. n의 인수 i 중 '소수'만 도출

def sosu(n):
    l = []
    for i in range(2, n+1):
        if n%i == 0:
            l.append(i)
    return True if len(l) == 1 else False

def solution(n):
    return [i for i in range(2, n+1) if n%i == 0 and sosu(i)]


# 내 코드 3
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