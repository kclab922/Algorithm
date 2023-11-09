# 내 풀이
def solution(order):
    count_clab = 0
    for num in str(order):
        if num == '3': 
            count_clab += 1
        if num == '6':
            count_clab += 1
        if num == '9':
            count_clab += 1

    return count_clab

# 다른 풀이
# tip: str에 .count()함수를 쓸 수 있군.
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')

print(solution(3))
print(solution(29423))