# 내 풀이 
# 1. 기본값을 2로 설정
# 2. dict의 각 단어들 속에 spell의 각 글자들이 있는지 검토
# 3. 있으면 count에 +1
# 4. count가 spell의 글자 수보다 많아지면 1 출력
# 5. **이때 count는 dict 속 단어가 바뀔때마다 리셋해줘야 하므로, 중간에 초기화

def solution(spell, dic):
    answer = 2
    for word in dic:
        count = 0
        for char in spell:
            if char in word:
                count += 1
                if count >= len(spell):
                    answer = 1                            
    return answer

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))