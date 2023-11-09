# 풀이1
# tip: 딕셔너리 이용해보기

def solution(price):
    discount_rates = {
        500000: 0.8, 
        300000: 0.9,
        100000: 0.95,
        0: 1,
    }
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price*discount_rate)

print(solution(150000))
print(solution(580000))