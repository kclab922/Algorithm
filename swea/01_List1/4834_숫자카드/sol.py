# # 내 풀이

# import sys
# sys.stdin = open('input.txt')

# T = int(input())


# for tc in range(1, T+1):

#     N = int(input())
#     counter = [0 for i in range(10)]

#     numbers = list(map(int, input()))
    
#     for number in numbers:
#         counter[int(number)] += 1

#         counter_max = 0



# 선생님 풀이

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 카드 장수, numbers: 카드 배열

    N = int(input())
    numbers = input()

    counter = [0 for i in range(10)]  #(list comprehension)
    # counter = [0] * 10 (list concatenation)

    for number in numbers:
        counter[int(number)] += 1
    
    card_count = 0
    card_number = 0

    for idx, value in enumerate(counter): 
    #enumerate: 인덱스에는 숫자번호, 밸류에는 몇 장인지 기록됨
        if card_count <= value:
            card_count = value
            card_number = idx

    print(f'#{tc} {card_number} {card_count}')







   
    
   







# print(f'#{tc}' {card_many} {card_count})