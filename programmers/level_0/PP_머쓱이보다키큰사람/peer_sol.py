# 풀이1
# A.append(B): A에다 B추가
# .index(A): A의 인덱스 출력 

def solution(array, height):
    array.append(height)
    # [149, 180, 192, 170, 167]
    # [180, 120, 140, 190]    

    array.sort(reverse = True)
    # [192, 180, 170, 167, 149]
    # [190, 180, 140, 120]

    return array.index(height)

print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))



# 풀이2
def solution(array, height):
    return sum(1 for i in array if i > height)

print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))


