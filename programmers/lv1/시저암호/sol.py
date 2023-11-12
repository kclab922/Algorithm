def solution(s, n):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = ''
    for i in s:
        if i.isupper():
            i = i.lower()
            answer += a[a.index(i) - 26 + n].upper()
        elif i == ' ':
            answer += ' '
        else:
            answer += a[a.index(i) - 26 + n]


    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))