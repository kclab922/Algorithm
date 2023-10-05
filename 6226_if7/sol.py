
# 내 풀이
#for n in range(1, 201):
    #if n % 7 == 0 and n % 5 != 0:
        #print(n)
    
numbers = range(1, 201)

result = []

for number in numbers:
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))

print(','.join(result))
