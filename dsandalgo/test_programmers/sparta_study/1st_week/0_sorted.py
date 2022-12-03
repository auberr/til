# sorted

# sorted 는 배열 자체를 바꾸지 않음
arr = [5, 8, 1, 2, 4, 9, 3, 7, 6]
print("sorted data: ", sorted(arr))
print("input data: ", arr)

# sort()
# sort 는 배열 자체를 정렬
arr = [5, 8, 1, 2, 4, 9, 3, 7, 6]
arr.sort()
print("input data: ", arr)

# key 를 기준으로 정렬하기
arr = [('Smith', 95), ('John', 78), ('Paul', 87)]
res = sorted(arr, key = lambda x: x[1])
print(res)