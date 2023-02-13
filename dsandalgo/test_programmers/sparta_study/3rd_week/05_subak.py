def solution(n):
    answer = ''
    for i in range(1, n+1):
        if i % 2 == 1:
            answer+='수'
        elif i % 2 == 0:
            answer+='박'
    return answer

print(solution(3))
print(solution(4))


# def solution(n):
#     answer = ''
#     name = '수박'
    
#     count = 0
#     a_list=[]
#     while True:
#         count+=1
        
#         if count > n:
#             for i in range(len(n)):
#                 a_list.append(name[i-1])
#             print(a_list)
            
#         elif count < n:
#             temp = count % 2 
#             for i in range(n):
#                 a_list.append(name[i-1])
#             print(a_list)
            
#         elif count == n:
#             break
            
#     return answer

# solution(3)

