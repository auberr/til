# 1. 정렬
# 2. ~N 까지 각 stg에 맞는 배열로 만듬
# 3. 배열을 하나더 만듬
# 4. 1:1 매칭으로 배열을 하나 더 만듬
# 5. value key 식으로 연동?
# 6. value 값으로 정렬
# 7. 정렬한 값에서 key를 추출

def solution(N, stages):
    answer = []

    stage_list = []
    all_list = []

    for i in range(N):
        stage_list.append(0)
        all_list.append(0)
  
    for stage in stages:
        # print(stage, ' 이것은 stage')
        for i in range(0, stage-1):
            # print(i, ' 이것은 i')
            # if i+1 == N:
            #     stage_list[i] -=1    
            stage_list[i] +=1

    for stage in stages:
        if stage > N:
            stage-=1
            for j in range(0, stage):
                all_list[j] +=1
        else:
            for j in range(0, stage):
                all_list[j] +=1

    # print(stage_list)
    # print(all_list)

    failrate = []
    failrate_index = []
    for i in range(0, N):
        failrate.append(1-stage_list[i]/all_list[i])
        failrate_index.append([1-stage_list[i]/all_list[i], i])

    
    a= sorted(failrate, reverse=True)
    print(a)

    for i in range(len(a)):
        answer.append(failrate.index(a[i])+1)
        failrate[failrate.index(a[i])] = 2

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

print(solution(4, [4,4,4,4,4]))