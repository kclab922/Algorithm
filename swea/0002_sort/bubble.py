# 이런 식으로 작동하는구나만 알고 넘어가면 됨. 실제 문제 풀때는 sort 함수 사용.
# 원리만 이해하고 설명 가능하면 됨.


my_list = [1, 5, 2, 8, 6, 4, 3, 6, 1, 1]


for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        # print(left, right)
        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

