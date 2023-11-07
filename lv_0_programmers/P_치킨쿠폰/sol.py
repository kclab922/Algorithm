# 내 코드
# 풀이과정
# 1. '쿠폰'과 '서비스'를 변수로 이용 (쿠폰 기본값 = chicken: 첫 번째 쿠폰 개수는 chicken 개수와 같으므로 이렇게 시작)
# 2. 쿠폰 개수를 10으로 나누어 => 몫은 서비스에 누적 / 몫과 나머지를 더해 쿠폰 개수 도출 (서비스 개수만큼 쿠폰이 나오므로)
# 3. 쿠폰 개수가 10개 이상인 동안은 추가 서비스가 발생하므로, 이 과정을 계속 반복 
# 4. 쿠폰 개수가 9개 이하로 떨어지면 더이상의 추가 서비스는 없으므로 중단
# divmod 호진님 헌정 문제

def solution(chicken):
    coupon = chicken
    service = 0

    while coupon >= 10:
        a, b = divmod(coupon, 10)
        service += a
        coupon = a + b
    
    return service


# 참고 코드 1
# 서비스 개수는 10%의 10%의 10%의 10%...를 계속 더해가는 과정이므로! + int 씌워서 정수만 추출
def solution(chicken):
    return int(chicken*0.11111111111)

# 참고 코드 2
def solution(chicken):
    return (max(chicken,1)-1)//9

print(solution(100))
print(solution(1081))