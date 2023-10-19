import sys
sys.stdin = open('input.txt')

T = int(input())
target = ''

for tc in range(1, T+1):
    letters = list(input())
    
    for i in range(len(letters)-1):
        if letters[i] == letters[i+1]:
            target = letters[i] + letters[i+1]
            letters.pop(t)
        else:
            break

    print(letters)


