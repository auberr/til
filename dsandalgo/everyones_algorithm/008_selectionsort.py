# def find_min_idx(a):
#     n = len(a)
#     min_idx = 0
#     for i in range(1, n):
#         if a[i] < a[min_idx]:
#             min_idx = i
#     return min_idx

# def sel_sort(a):
#     result = []
#     while a:
#         min_idx = find_min_idx(a)
#         value = a.pop(min_idx)
#         result.append(value)
#     return result

# d=[2,4,5,1,3]
# print(sel_sort(d))

def select_sort_ascending(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[i]:
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]
                print(a[i], a[min_idx])


d=[2, 4, 5, 1, 3]
print(select_sort_ascending(d))
print(d)



def select_sort_descending(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] > a[i]:
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]
                print(a[i], a[min_idx])


d=[2, 4, 5, 1, 3]
print(select_sort_descending(d))
print(d)