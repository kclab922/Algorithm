# 나의 풀이
# 1. 오름차순된 array를 num으로 반복문
# 2. num-n의 절대값들로 리스트 li 만들기
# 3. 'li원소 중 최솟값'의 인덱스를 오름차순된 array의 인덱스에 넣어 원소 값 도출

def solution(array, n):    
    li = []
    for num in sorted(array):
        li.append(abs(num-n))
    return sorted(array)[li.index(min(li))]

# 다른 풀이
# .sort(lambda ..)
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    return array[0]

print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))