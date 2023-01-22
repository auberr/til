def solution(N, stages):
    answer = []
    list_stages = []
    for i in range(N):
        list_stages.append(0)
        
    print(list_stages)
    
    for i in range(0, len(stages)):
        print(stages[i])
        for j in range(1, N+1):
            if stages[i] == j:
                list_stages[]
            
    print(list_stages)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))