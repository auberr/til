# Q.
# 1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.

# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.

# 문제의 번호별 조건에 대한 입력 예시와 출력
# Ex 1)
# abc 	# a1/b1/c1

# Ex 2-1)
# aaabbbc	# a3/b3/c1

# Ex 2-2)
# abbbc	# a1/b3/c1

# Ex 3-1)
# ahhhhz	# a1/h4/z1

# Ex 3-2)
# acccdeee	# a1/c3/d1/e3


def summarize_string(input_str):
    # 이 부분을 채워보세요!
    sum = ''
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    count=0
    new_list = []
    
    for i in range(0, len(input_str)):
        if input_str[i] in list:
            count+=1
            new_list.append(input_str[i])
            new_list.append(count)
            if input_str[i] != input_str[i-1]:
                count=0
            
    print(new_list)
                
            
        
    # 1. for문으로 input_str 을 돈다.
    # 2. 알파벳에 숫자를 더한다.
    # 3. 없으면 pass 한다.
    
    return sum    


input_str = "acccdeee"

print(summarize_string(input_str))



