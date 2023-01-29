def find_min_num(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min

print(find_min_num([1, 2, 3, 4, 5, 6, 8]))

def find_max_num_index(arr):
    index = 0
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            index = i
    return index

print(find_max_num_index([1, 2, 3, 4, 5, 6, 8]))        

def find_max_num(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max

print(find_max_num([1, 2, 3, 4, 5, 6, 8]))