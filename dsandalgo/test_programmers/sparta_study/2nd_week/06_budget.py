def solution(d, budget):
    answer = 0
    for i in range(len(d)-1):
        for j in range(i+1, len(d)):
            print(i, j)
            if d[i] > d[j]:
                temp = d[i]
                d[i] = d[j]
                d[j] = temp

    print(d)    
    sum=0
    cnt=0
    for i in d:
        sum+=i
        cnt+=1
        if sum > budget:
            sum-=i
            cnt-=1
            break
    
    print(cnt)
    answer = cnt
    return answer

solution([1,3,2,5,4], 9)
solution([2,2,3,3], 10)