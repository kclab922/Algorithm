# 내 풀이
def solution(array):
    return ''.join(map(str, array)).count('7')

# 다른 풀이
def solution(array):
    return str(array).count('7')
    
print(solution([7, 77, 17]))
print(solution([10, 29]))