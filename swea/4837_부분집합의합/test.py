# 모든 부분집합의 개수 구하기

numbers = list(range(1, 5))

n = len(numbers)

for i in range(1<<n):
    # 1<<n = 10000(b) = 16 = 2**4

    # print(i)

    temp = [] # 모든 부분집합 찾기
    for j in range(n):
        # print(i, bin(i), bin(1<<j))
        if i & (1<<j):
            # 여기서 T가 나온다는 건 해당 자리에 1이 있다는 것
            temp.append(numbers[j])
        print(temp)
