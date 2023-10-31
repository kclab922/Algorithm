# 내 풀이
# 'num의 각 문자열 원소'가 그 인덱스값과 정확히 일치하는 점을 활용
# ex) input 문자열 속'zero' => num에서 'zero'의 인덱스값으로 바꿔주면 됨. 
def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        numbers = numbers.replace(num[i], str(i))
    return int(numbers)


# 다른 풀이 1.
# 내 풀이와 같은 맥락
# tip: enumerate() => (인덱스, '원소') 출력
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

# 다른 풀이 2.
#  for k in dict.keys()
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])
    return int(numbers)

print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))