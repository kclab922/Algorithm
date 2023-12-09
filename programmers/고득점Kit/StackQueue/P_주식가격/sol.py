# 내 코드 
# 1. 마지막 초는 무조건 0이므로, 0~3 인덱스까지 4개만 계산하면 됨.
# 2. sec: 몇초 뒤 가격이 떨어지는지. 답 리스트에 들어갈 원소. 바로 다음에 떨어져도 1초로 계산되므로 기본값은 1.
# 3. 해당 인덱스 i와 그 다음 인덱스 j를 비교. 
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        sec = 1
        j = i+1
        while j <= len(prices)-2 and prices[i] <= prices[j]:
            j += 1
            sec += 1
        answer.append(sec)
    answer.append(0)
    return answer




# 다른 코드 1 (stack/queue 활용한 정석풀이 => 시간복잡도 최저)
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer



# 다른 코드 2 (시간복잡도 애매하나 내 거보단 낫다!)
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer




print(solution([1, 2, 3, 2, 3]))