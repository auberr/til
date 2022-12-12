def solution(citations):
    answer = 0
    # 1. 정렬
    for i in range(len(citations)):
        for j in range(i+1, len(citations)):
            if citations[i] > citations[j]:
                temp = citations[j]
                citations[j] = citations[i]
                citations[i] = temp
    print(citations)


    # 2. h 번 이상 인용 -> h 편 이상 | 나머지 h 번 이하 인용 
    for i in citations:
        # i 번 이상 인용
        if i >= 0:
            
        # i 편 이상

        

    return sum(citations)/len(citations)

print(solution([3, 0, 6, 1, 5]))