def solution(num):
    answer = 0
    count = 0
    
    if num == 1:
        answer = 0
        return answer
        
    while True:
        
        if count >= 500:
            answer = -1
            break
        elif count < 500:
            count+=1
            if num % 2 == 0:
                num = num / 2
            
            elif num % 2 == 1:
                num = num * 3 + 1
            
            if num == 1:
                answer = count
                break
            
    return answer

print(solution(6))
print(solution(16))
print(solution(626331))