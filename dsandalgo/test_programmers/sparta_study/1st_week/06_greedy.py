reserve = [1, 2, 4, 5]
lost = [1, 3, 5, 7, 8, 9]

reserve_del = set(reserve) - set(lost)
lost_del = set(lost) - set(reserve)

print(reserve_del)
print(lost_del)

for i in reserve_del:
    if i-1 in lost_del:
        lost_del.remove(i-1)
    elif i+1 in lost_del:
        lost_del.remove(i+1)

print(reserve_del)
print(lost_del)


def solution(n, lost, reserve):
    reserve_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)

    for i in reserve_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)

    return n - len(lost_del)

print(solution(5, [2,4], [1,3,5]))

# numbers = [1 for x in range(5)]
# print(numbers)

# def solution(n, lost, reserve):
#     temp = [1 for _ in range(n+2)]
#     print(temp)
#     temp[0]=0
#     temp[-1]=0
#     for lo in lost:
#         temp[lo] = 0
    
#     print(temp)

#     for re in reserve:
#         if temp[re] == 0:
#             temp[re] = 1
#             continue
#         temp[re] = 2
    
#     print(temp)

#     for i in range(1, n+1):
#         if temp[i] == 0:
#             if temp[i-1] == 2:
#                 temp[i-1] -= 1
#                 temp[i] = 1
#             elif temp[i+1] == 2:
#                 temp[i+1] -= 1
#                 temp[i] = 1
#     return sum([1 for x in temp if x != 0])


# print(solution(5, [2,4], [1,3,5]))