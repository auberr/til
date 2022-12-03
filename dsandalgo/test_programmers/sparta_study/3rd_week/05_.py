def solution(n):
    answer = ''
    name = '수박'
    
    count = 0
    a_list=[]
    while True:
        count+=1
        
        if count > n:
            for i in range(len(n)):
                a_list.append(name[i])
            print(a_list)
            
        elif count < n:
            temp = count % 2 
            for i in range(n):
                a_list.append(name[i])
            print(a_list)
            
        elif count == n:
            break
            
    return answer

solution(3)

