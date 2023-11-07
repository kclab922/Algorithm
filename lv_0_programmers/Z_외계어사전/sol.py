# 풀이구조: 
# 1. dic의 각 단어 속에 spell의 각 알파벳이 있는지 검토 
# 2. 있으면 count에 +1 
# 3. count가 spell의 원소 수와 같거나 많아지면 조건 부합 => 1 출력
# **이때 count는 dict 속 단어가 바뀔때마다 리셋해줘야 하므로, 중간에 초기화

def solution(spell, dic):
    for word in dic:
        count = 0
        for char in spell:
            if char in word:
                count += 1
                if count >= len(spell):
                    return 1                       
    return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))