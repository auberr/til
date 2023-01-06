def solution(d, budget):
    answer = 0
    # 1. 부서별로 신청한 금액이 있는 d 를 정렬한다.
    for i in range(len(d)):
        for j in range(i, len(d)):
            if d[i] > d[j]:
                temp = d[j]
                d[j] = d[i]
                d[i] = temp
    
    # 2. budget에서 d를 순서대로 하나씩 뺀다. 몇개나 뺐는지 수를 센다.
    count = 0
    for i in d:
        if budget >= i:
            budget = budget - i
            count+=1
        else:
            break
    
    answer = count
    
    return answer

print(solution([1,3,2,5,4], 9))