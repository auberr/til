arr = list(range(10))
print(arr)

# arr[A:B:C] 의 의미는 index A부터 index B 까지 C의 간격으로 배열을 만들어라
# A 가 None 이면 처음부터 / B 가 None 이면 할수 있는데 까지 (C 가 양수이면 마지막 index까지 C 가 음수이면 첫 index 까지)
# C 가 None 이면 한칸 간격으로

arr_n_n_2 = arr[::2] # 처음부터 끝까지 두칸 간격으로
print(arr_n_n_2)

arr_1_n_2 = arr[1::2] # index 1부터 끝까지 두칸 간격으로
print(arr_1_n_2)

arr_n_n_m1 = arr[::-1]
print(arr_n_n_m1)

arr_n_n_m2 = arr[::-2]
print(arr_n_n_m2)

arr_3_n_m1 = arr[3::-1]
print(arr_3_n_m1)

arr_1_6_2 = arr[1:6:2]
print(arr_1_6_2)