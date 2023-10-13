import sys
sys.stdin = open('input.txt')

T = int(input())  # 5 가져옴

# 각 숫자가 몇장인지 세어주기

for tc in range(1, T+1):
    numbers = input()

    # counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = [0 for i in range(10)]

    for number in numbers:
        counter[int(number)] +=1

    # print(counter)


    # 연속or같은 숫자인지 확인

    idx = 0
    is_babygin = 0

    while idx < len(counter):
        # 1. triplet인지 검증
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
        
        # 2. run인지 검증 (나를 기준으로 오른쪽으로 3개를 볼거야)
        if idx < len(counter) - 2: 
        # 맨 뒤 2개(8,9,10 / 9,10,11)는 연속3개를 만들 수 없으므로
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                is_babygin +=1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1

        idx += 1

    if is_babygin == 2:
        print(True)
    else:
        print(False)