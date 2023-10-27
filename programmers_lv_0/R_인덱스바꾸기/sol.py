# 내 풀이
# swap 이용
def solution(my_string, num1, num2):
    li = list(my_string)
    li[num1], li[num2] = li[num2], li[num1]
    return ''.join(li)


# 다른 풀이
# 흥미로웠다.
def solution(my_string, num1, num2):
    [a, b] = sorted([num1, num2])
    return my_string[0:a] + my_string[b] + my_string[a+1:b] + my_string[a] + my_string[b+1:]
           # 0부터 a-1까지 -> a 자리에 b -> a+1부터 b-1까지 -> b 자리에 a -> b+1부터 끝까지


print(solution("hello", 1, 2))
print(solution("I love you"	, 3, 6))