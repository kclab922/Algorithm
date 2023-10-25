# 풀이1
# 이해값1. `.replace(old, new)`: 문자열 메소드!
# 이해값2. 문자열에서 특정문자 지울 때는 replace 사용하자.
# 이해값3. 문자열 메소드는 원본을 바꾸지 못함
#          >> replace만 하면 원본은 계속 'bus'그대로...
#          >> my_string = my_string.replace() 형태로 써야!
def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in vowels:
        my_string = my_string.replace(char, '')
    return my_string


# 풀이2 
# 모음이 아니면 걔네 모아서 출력
# Q. 이걸 풀어서 쓰면 어떻게 될까?
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])



print(solution("bus"))
print(solution("nice to meet you"))

