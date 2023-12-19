# 내 코드
def solution(nums):
    myD = {}
    for n in nums:
        myD[n] = myD.get(n, 0) + 1    # {3: 3, 2: 3}

    return min(len(nums)//2, len(myD.keys()))


# 다른 코드
# 딕셔너리 안 쓰고 set으로!
def solution(nums):
    return min(len(nums)//2, len(set(nums)))

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))