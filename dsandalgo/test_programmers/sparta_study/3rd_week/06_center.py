def solution(s):
    answer = ''
    # 단어 길이 체크
    len_s = len(s)
    # 단어 길이 짝수 인지
    if len_s % 2 == 0:
        # 짝수이면 전체의 반 번째 와 +1을 한 반환
        new_len_s = len_s //2
        answer = s[new_len_s-1]+s[new_len_s]

    # 단어 길이 홀수 인지
    if len_s % 2 == 1:
        # 홀수이면 전체의 반으로 나눈 몫에서 +1을 한 번째 반환
        new_len_s = (len_s //2)
        answer = s[new_len_s]
    
    return answer

print(solution("abcde"))

print(solution("qwer"))