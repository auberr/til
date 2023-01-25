def solution(s):
    answer = True
    
    count_p = 0
    count_y = 0
    
    for i in s:
        if i == 'p':
            count_p +=1
        elif i == 'P':
            count_p +=1
        elif i == 'y':
            count_y+=1
        elif i == 'Y':
            count_y+=1

    if count_p == count_y :
        return True
    else:
        return False


    return True

print(solution("pPoooyY"))
print(solution("Pyy"))