# 1081 주문
# 쿠폰 1081 => 서비스 108 / 쿠폰 1
# 쿠폰 108 => 서비스 10 / 쿠폰 8
# 쿠폰 10 => 서비스 1 / 쿠폰 0
# 쿠폰 1 => 서비스 0 / 쿠폰 1 


def solution(chicken):
    s_sum = chicken // 10 # 108
    c_sum = chicken % 10  # 1
    service = chicken // 10 # 108
    coupon = chicken % 10  # 1

    while service >= 0:
        for _ in range(chicken//10 + 1):
            service = service // 10 # 10
            s_sum += service
            coupon = service % 10 # 8
            c_sum += coupon
            # if c_sum >= 10:
            #     service += c_sum // 10
            break

    return s_sum

print(solution(100))
print(solution(1081))