# 내 코드
def solution(num, total):
    for i in range(int(total/num) - num, total+1):
        count = 0
        for j in range(num):
            count += i+j
            if count == total:
                return [i+j for j in range(num)]
        

# 다른 코드 1
# 어떻게 이런 코드를 짜게 됐는지 수학적 사고 과정을 모르겠음
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]


# 다른 코드 2
# 어떻게 이런 코드를 짜게 됐는지 수학적 사고 과정을 모르겠음
# range에도 sum() 적용 가능하군
def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start_num = diff//num
    answer = [i+1+start_num for i in range(num)]
    return answer


print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))