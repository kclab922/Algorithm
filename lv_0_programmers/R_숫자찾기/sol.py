# 내 풀이
def solution(num, k):
    # str(): 숫자는 반복이 안 되므로, 문자열로 바꾸어 for문 돌림 => 2, 9, 1, 8, 3
    for n in str(num):
        if int(n) == k:
            # '자리 수'를 도출하기 위해 index 활용. 
            # list(), map(): index 사용 위해서 map을 이용하여 숫자를 하나씩 리스트화 
            # str(): map을 쓰려면 iterable한 원소가 들어와야 하므로 숫자를 문자화         
            # 리스트를 만든 후 원소가 k와 같으면 해당 인덱스에 1을 더해 출력(인덱스는 0부터 시작하므로)
            return  list(map(int, str(num))).index(k) + 1
    return -1

# 다른 풀이
def solution(num, k):
    # enumerate(iterable): (인덱스, 원소)를 튜플 형태로 출력 
    for i, n in enumerate(str(num)):
        # 원소가 k와 같으면 해당 인덱스에 1을 더해 출력
        if str(k) == n:
            return i + 1
    return -1

print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))