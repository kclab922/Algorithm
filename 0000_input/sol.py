import sys
sys.stdin = open('input.txt') 
# stdin : standard input

TC = int(input())
# TC : Test Case
# 인풋을 integer형태로 바꿔줌

# print(TC)
# error : EOF : end of file >> 저장 안 된 경우



# 좀 더 긴 데이터 받기

# numbers는 여기서 아직 글자데이터 string임. 
# 이를 리스트로 바꿔줘야 함. 

# 1. 1차원 리스트 input 받기
# 이를 위해 먼저 12345각각 쪼개줘야 함
numbers = input().split()
# print(numbers)
# print(type(numbers))

# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다.')

numbers = list(map(int, input().split()))
numbers = list(map(int, ['1', '2', '3', '4', '5']))
numbers = list([1, 2, 3, 4, 5])
print(numbers)

for number in numbers:
    if number % 2 == 1:
        print(f'{number}은 홀수입니다.')

# 2차원리스트는 나중에