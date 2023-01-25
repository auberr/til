from functools import cmp_to_key

def compare(a, b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return b[1] - a[1]

def solution(N, stages):
    answer = []
    total = len(stages)
    fails = []

    users = [0 for _ in range(N+1)]
    
    for s in stages:
        users[s-1] += 1

    for i in range(N):
        if users[i] == 0:
            fails.append((i+1, 0))
        else:
            fails.append((i+1, users[i] / total))
            total -= users[i]

    for f in sorted(fails, key=cmp_to_key(compare)):
        answer.append(f[0])
    
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

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