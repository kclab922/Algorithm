# 내 풀이
def solution(n):
    answer = 0
    for num in range(1, n+1):
        count = 0
        for number in range(1, num+1):
            if num % number == 0:
                count += 1
        if count >= 3:
            answer += 1
    return answer

#  다른 풀이
def solution(n):
    output = 0
    # 어차피 1~3 중 합성수 없으므로 4부터 반복 
    for i in range(4, n + 1): 
        # (1,i)(i,1)는 기본 포함되므로 약수는 2부터 반복
        for j in range(2, int(i ** 0.5) + 1): 
            if i % j == 0:
                # (1,i)(i,1) + (j,i//j),(i//j,j) or (j,j) 이므로
                output += 1 
                break
    return output

print(solution(10))
print(solution(15))