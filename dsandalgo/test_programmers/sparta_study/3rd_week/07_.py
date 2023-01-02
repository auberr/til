def solution(s):
    answer = True
    count_left = 0
    count_right = 0
    for i in range(0, len(s)):
        if i == 0:
            if s[i] == ")":
                return False
        elif i+1 == len(s):
            if s[i] == "(":
                return False
        else:
            if s[i] == "(":
                count_left+=1
            elif s[i] == ")":
                count_right+=1
    if count_left != count_right:
        return False
    return answer

solution("()()")

# a-1 b-1 
# c -1 c-2  / c-3 사례

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print(solution("()(())"))