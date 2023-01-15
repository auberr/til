def same_group(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            answer.append([arr[i], arr[j]])
    
    return answer

print(same_group(["Tom", "Jerry", "Mike"]))

# def same_name(arr):
#     same_name_list = []
#     n = len(arr)
#     for i in range(0, n):
#         for j in range(i+1, len(arr)):
#             print(i, j)
#             if arr[i] == arr[j]:
#                 same_name_list.append(arr[i])
#     return same_name_list

# print(same_name(["Tom", "Jerry", "Mike", "Tom"]))