# 풀이구조:
# 1. Babbling 속 단어b가 words 속 단어 w를 포함하고 있으면 => w를 0으로 replace
# 2. b의 모든 글자가 숫자로 바뀌면 => count +1

# ** 이때 공란이 아닌 숫자로 바꾸는 이유: 
# 공란으로 바꿀 경우 tc1 "wyeoo" -> ye 지우면 -> 떨어져있던 글자들이 붙어 woo가 되어 지워지므로.
# 숫자로 바꿔주면 글자들 사이에 숫자가 껴있으므로, 글자가 모두 지워진다면 결국 숫자만 남음.

def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    count = 0
    for b in babbling:
        for w in words:        
            if w in b:
                b = b.replace(w, '0')
                if b.isdigit():
                    count += 1
    return count


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))