def solution(s):
    answer = 0
    eng_list = ["zero", "one", "two","three","four","five","six","seven","eight","nine"]
    for i in eng_list:
        if i in s:
            s = s.replace(i, str(eng_list.index(i)))
    answer = int(s)
    return answer

print(solution("1zerotwozero3"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
