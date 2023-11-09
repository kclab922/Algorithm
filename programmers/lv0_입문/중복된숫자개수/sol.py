# 풀이1
def solution(array, n):
    return array.count(n)

# 풀이2
# def solution(array, n):
#     count = 0
#     for num in array:
#         if n == num:
#             count += 1
#     return count


print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))
