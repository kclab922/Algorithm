# 내 풀이
def solution(age):
    answer = ''
    for num in str(age):
        if num == '0':
            answer += 'a'
        elif num == '1':
            answer += 'b'
        elif num == '2':
            answer += 'c'
        elif num == '3':
            answer += 'd'
        elif num == '4':
            answer += 'e'
        elif num == '5':
            answer += 'f'
        elif num == '6':
            answer += 'g'
        elif num == '7':
            answer += 'h'
        elif num == '8':
            answer += 'i'
        elif num == '9':
            answer += 'j'
    return answer
    
# 다른 풀이1
def solution(age):
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age

# 다른 풀이2
def solution(age):
    answer = ''
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for char in str(age):
        for i in range(1, 10):
            if int(char) == i:
                answer += lst[i]
    return answer


print(solution(23))
print(solution(51))
print(solution(100))