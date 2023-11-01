# 내 풀이
# 1. 문자밀기의 모든 경우의 수(=글자길이만큼) 반복 돌리기 
# 2. A==B인 순간 => 바로 answer 반환 + for문 중단
# 3. A!=B인 경우 => 한 칸 밀고 answer+1 => for문 계속 진행
# 4. for문이 중간에 안 멈추고 끝까지 돌면(=A==b 불가능) => -1 반환

def solution(A, B):
    count = 0
    for _ in range(len(A)):
        if A == B:
            return count
            break
        else:
            A = A[-1] + A[:-1]
            count += 1

    return -1


# 다른 풀이
# .find(a) - 찾는 문자가 존재 한다면 해당 위치의 index를 반환
#          - 찾는 문자가 존재 하지 않는다면 -1 을 반환
#          - 만약 찾는 문자나 문자열이 여러개 있다면 맨 처음 찾은 문자의 index를 반환
solution=lambda a,b:(b*2).find(a)


print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))
