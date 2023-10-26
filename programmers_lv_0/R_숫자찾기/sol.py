# 내 풀이
def solution(num, k):
    # str(): 숫자는 반복이 안 되므로, 문자열로 바꾸어 for문 돌림
    for n in str(num):
        if int(n) == k:
            # 자리 수를 도출하기 위해 index 사용. > index 사용 위해서는 숫자를 하나씩 리스트화 해야함. 
            answer = list(map(int, str(num))).index(k) + 1
            break
        else:
            answer = -1
    return answer

print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))