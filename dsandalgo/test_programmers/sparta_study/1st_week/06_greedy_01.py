# def solution(n, lost, reserve):
#     answer = 0
#     for i in reserve:
#         if i-1 == lost[0]:
#             del lost[0]
#             del reserve


#     for j in lost:
#         print(j)

#     for k in 

#     return answer


def solution(n, lost, reserve):
    answer = 0
    student = [0] * (n + 2)

    for r in reserve:
        student[r] += 1
    for l in lost:
        student[l] -= 1

    for i in range(1, n+1):
        if student[i]>0:
            front = i -1
            back = i +1
            if student[front]<0:
                student[i]-=1
                student[front]+=1
            elif student[back]<0:
                student[i]-=1
                student[back]+=1

    answer = 0
    for i in range(1, n+1):
        if student[i] >= 0:
            answer+=1
    return answer


def solution(n, lost, reserve):
    reserve_only = set(reserve)-set(lost)
    lost_only = set(lost)- set(reserve)

    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1

        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
    
    return n - len(lost_only)

solution(5, [2, 4], [1, 3, 5])