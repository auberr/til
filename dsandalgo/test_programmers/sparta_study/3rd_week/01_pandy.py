def solution(s):
    answer = True
    s_list = []
    
    for i in range(len(s)):
        s_list.append(s[i])
    
    y_count = 0
    p_count = 0
    
    for i in s_list:
        if i == 'p' or i == 'P':
            p_count+=1
        elif i == 'y' or i == 'Y':
            y_count+=1
            
    print(p_count)
    print(y_count)
    
    if p_count == y_count:
        answer = True
    elif p_count == 0 and y_count==0:
        answer = True
    else:
        answer = False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(answer)
    

    return answer

solution('Pyy')