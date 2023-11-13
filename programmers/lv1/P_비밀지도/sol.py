# 내 코드
# 1. arr1, arr2의 각 원소를 이진수로 바꾸어 같은 자릿수끼리 더하기
#   - bin(): arr1, arr2의 각 원소를 이진수로 (이때 str상태)
#   - [2:]: bin 썼을 때 앞에 붙는 Ob 제거 
#   - int(): 현재 str 상태이므로 int화
#   - zip(): 같은 자릿수끼리 더하기
# 2. 이진수를 원소로 리스트 l 생성 (이때 각 원소의 길이는 제각각)
# 3. replace사용을 위해 str화 하여 list로 만들고 for문 돌리기
# 4. 이때 길이가 n자리가 안 되는 원소는 앞에 모자라는만큼 0 붙여주기
# 5. 각 숫자를 ' ', '#'로 replace해 answer에 더해주기

def solution(n, arr1, arr2):
    l=[]
    answer = []

    for a, b in zip(arr1, arr2):
        l.append(int(bin(a)[2:]) + int(bin(b)[2:]))

    for i in list(map(str, l)):
        if len(i) < n:
            i = '0'*(n-len(i)) + i
        i = i.replace('0', ' ')
        i = i.replace('1', '#')
        i = i.replace('2', '#')
        answer.append(i)
    return answer


# 다른 코드
# 나와 접근방식이 동일하나, 함수/메소드 더 공격적으로 활용
# bin(i|j): i와 j의 합집합(or) ex) bin(0b1101 | 0b1001) => '0b1101'
# str.rjust(n, '0'): (전체자리숫자, 공백 있을 경우 공백 대체 문자)
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
