# 내 풀이
# 풀이구조: 로그인 성공 시 login 
#          로그인 실패 시 1) 아이디가 일치하면 wrong pw  
#                        2) 아니면 fail

def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    else:
        for i in range(len(db)):
            if id_pw[0] == db[i][0]: 
                return 'wrong pw'
    return 'fail'


# 다른 풀이
# dict(list) : {'rardss': '123', 'yyoom': '1234', 'meosseugi': '1234'}
# a := b 의 의미: a = b 그리고 a   
# dict.get(key): value 

def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))