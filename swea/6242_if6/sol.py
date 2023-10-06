# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.


# 1번째 해결법
blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A' : 0,
    'O' : 0,
    'B' : 0,
    'AB': 0,
}

for blood in blood_list:
    # print(blood)
    blood_dict[blood] += 1

print(blood_dict)


########### 응용(리스트에 다른 데이터가 추가되어도 코드수정 없이 운용 가능)

location_list = ['서울', '부산', '부산', '서울', '대전', '광주', '제주']

location_dict = {
    '서울': 1 #첫번쨰로 등장하는 경우 00: 1
}

for location in location_list:

    if location in location_dict.keys():
        location_dict[location] += 1
    else:
        location_dict[location] = 1
                      # key       #value
print(location_dict)