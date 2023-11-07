# 내 풀이
# 중복숫자 없애고 => 각 숫자별 개수 리스트 만들기 => 최빈값의 인덱스를 활용
# tc1: {1, 2, 3, 4} => [1, 1, 3, 1] => [1, 2, 3, 4][2] = 3
# tc2: {1, 2} => [2, 2] => 최댓값 2가 여러개 => -1 

def solution(array):
    l = []
    for n in set(array):
        l.append(array.count(n))
    if l.count(max(l)) >= 2:
        return -1
    return [*set(array)][l.index(max(l))]


# 다른 풀이
# 숫자 하나씩 돌아가며 삭제 => 마지막에 남는 애가 최빈값 
# .remove(): list method
# for문 반복시 원본에 뭔가를 씌우면, 이는 복사본으로 처리됨 -> 원본이 손상되어도 복사본은 유지

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))