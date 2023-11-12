# 내 코드
# 1. 오름차순 정렬된 d를 i로 for문 반복 
#    (예산이 적은 부서를 우선지원해줘야 최대한 많은 부서의 물품을 구매 가능하므로)
# 2. 예산이 i보다 크거나 같으면 => budget에서 해당 예산 빼고, count에 +1
def solution(d, budget):
    count = 0
    for i in sorted(d):
        if budget >= i:
            budget -= i
            count += 1
    return count


# 다른 코드 
# 발상은 좋으나 효율성 문제 발생 예상. 
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))