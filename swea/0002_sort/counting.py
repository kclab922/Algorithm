# 이런 식으로 작동하는구나만 알고 넘어가면 됨. 실제 문제 풀때는 sort 함수 사용.
# 원리만 이해하고 설명 가능하면 됨.

my_list = [1, 5, 2, 8, 6, 4, 3, 6, 1, 1]

counter = [0 for i in range(10)]

for num in my_list:
    counter[num] +=1

# print(counter)

result = []

for value, count in enumerate(counter):  
    # print(value, count) # 인덱스 번호와 밸류값을 좌우로 해서 프린트
    for i in range(count): 
        result.append(value)
    
print(result)