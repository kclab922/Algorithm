# 풀이1
def solution(my_string, letter):
    for char in my_string:
        if char == letter:
            my_string = my_string.replace(char, '')
    return my_string

# 풀이2
def solution(my_string, letter):
    return my_string.replace(letter, '')

print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))