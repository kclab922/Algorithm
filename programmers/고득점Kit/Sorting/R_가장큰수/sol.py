# 내 코드
# 1. if문: 모든 숫자가 0인 경우 0을 리턴해야 함. 그런데 이는 전체 원소를 확인해야 하므로 시간복잡도 상승 => any함수 사용. (from 프로세스)
# 2. str으로 바꾼 이유: int 그대로 쓸 경우 원소 숫자크기 전체를 기준으로 정렬되는데, str으로 바꿀 경우 숫자를 앞자릿수부터 하나씩 기준으로 정렬.
# 3. *4: *4 없이 할 경우, 30과 3 중 3이 무조건 뒤쪽. 3과 0을 또 비교하려면 3 복제 필요. (from 알파벳-숫자 변환 문제)
#    최대숫자가 1000이므로, 한 자릿수도 넉넉히 네 자릿수로 만들어줌. 
def solution(numbers):
    if any(num > 0 for num in numbers):
        numbers.sort(key=lambda x: str(x)*4, reverse=True)
        numbers = ''.join(list(map(str, numbers)))  
        return numbers
    else:
        return '0'
    
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0]))