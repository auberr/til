# 문제가 길때의 팁
# 문제에서 주어진 변수가 많을 때는 반드시 주석으로
# 1. 각 변수의 뜻
# 2. 구해야 하는 값


# N = 전체 스테이지의 개수
# stages = 게임을 이용하는 사용자가 멈춰 있는 스테이지 번호 배열


# len(stages) = 전체 사용자 수

# 전체 사용자 수
# 해당 스테이지를 클리어한 사람
# 해당 스테이지에서 막힌 사람

# -> 전부 stages 에서 도출할 수 있다.


# 구해야하는 것 = 실패율이 높은 스테이지 번호부터 내림차순 배열

# 문제 풀기
# 1. 스테이지별 실패을 구하기
# 2. 실패율이 높은 스테이지부터 내림차순 정렬
# ( 실패율을 내림차순 하는 것이 아니다 )

# 1. 스테이지별 실패율을 구해보자


def solution(N, stages):
    answer = []
    total = len(stages)

    #실패율 구하기
    stage_ppl = []

    for i in range(1, N+1):
        # 현재 스테이지에 도착한 인원
        num = stages.count(i)
        if num == 0:
            stage_ppl.append(0)
        else:
            stage_ppl.append(num/total)
        # 다음 스테이지로 넘어가는 인원이 이전 스테이지 시작인원과 다름
        # 5명이 스테이지에 들어왔어도 3명이 클라이얹트면 3명부터 시작
        total -= stages.count(i)

    # 실패율을 기준으로 내림차순 정렬
    # 실패율 자체가 아니라
    # 실패율에 해당하는 스테이지를 출력하기!
    for i in range(N):
        # 현재 가장 큰 값의 인덱스를 구해서
        pop_idx = stage_ppl.index(max(stage_ppl))
        # 그 스테이지 (인덱스 + i ) append
        answer.append(pop_idx + 1)
        stage_ppl[pop_idx] = -1
        
    return answer
    













# 내가 시도해본 내용

# # 1. 정렬
# # 2. ~N 까지 각 stg에 맞는 배열로 만듬
# # 3. 배열을 하나더 만듬
# # 4. 1:1 매칭으로 배열을 하나 더 만듬
# # 5. value key 식으로 연동?
# # 6. value 값으로 정렬
# # 7. 정렬한 값에서 key를 추출

# def solution(N, stages):
#     answer = []

#     stage_list = []
#     all_list = []

#     for i in range(N):
#         stage_list.append(0)
#         all_list.append(0)
  
#     for stage in stages:
#         # print(stage, ' 이것은 stage')
#         for i in range(0, stage-1):
#             # print(i, ' 이것은 i')
#             # if i+1 == N:
#             #     stage_list[i] -=1    
#             stage_list[i] +=1

#     for stage in stages:
#         if stage > N:
#             stage-=1
#             for j in range(0, stage):
#                 all_list[j] +=1
#         else:
#             for j in range(0, stage):
#                 all_list[j] +=1

#     # print(stage_list)
#     # print(all_list)

#     failrate = []
#     failrate_index = []
#     for i in range(0, N):
#         failrate.append(1-stage_list[i]/all_list[i])
#         failrate_index.append([1-stage_list[i]/all_list[i], i])

#     a= sorted(failrate, reverse=True)
#     print(a)

#     for i in range(len(a)):
#         answer.append(failrate.index(a[i])+1)
#         failrate[failrate.index(a[i])] = 2

#     return answer


# def solution(N, stages):
#     k = len(stages)
#     s = []
#     for i in range(1, N+1):
#         c = 0
#         for j in range(len(stages)):
#             if stages[j] == i:
#                 c+=1
#         if c== 0:
#             s.append(0)
#         else:
#             s.append(c/k)
#         k = k -c
#     a = sorted(s, reverse=True)
#     answer = []
#     for i in range(len(a)):
#         answer.append(s.index(a[i])+1)
#         s[s.index(a[i])]=2

#     return answer


# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# print(solution(4, [4,4,4,4,4]))



# def solution(N, stages):
#     answer = []
#     list_stages = []
#     for i in range(N):
#         list_stages.append(0)
        
#     print(list_stages)
    
#     for i in range(0, len(stages)):
#         print(stages[i])
#         for j in range(1, N+1):
#             if stages[i] == j:
#                 list_stages[]
            
#     print(list_stages)
#     return answer

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
