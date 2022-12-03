# # 1065번 - 한수
# def is_hansu(N):
#     if N < 100:
#         return True
#     elif N < 1000:
#         hundreds = N//100
#         tens = N % 100 // 10
#         ones = N % 10
#         if hundreds - tens == tens - ones:
#             return True
#         else:
#             return False
#     elif N == 1000:
#         return False
#     else:
#         print('error')
#         return 0


# def count_hansu(N):
#     count = 0
#     for i in range(1, N+1):
#         if is_hansu(i):
#             count += 1
#     return count

# result = count_hansu(int(input()))
# print(result)

# # 4673번 - 셀프 넘버

# def d(n):
#     new_n = n
#     for num in str(n):
#         new_n += int(num)
#     return new_n

# all_numbers = []
# for i in range(1, 10001):
#     all_numbers.append(i)

# 한줄 쓰기
# all_numbers = [x for x in range(1,10001)]

# for i in range(1, 10001):
#     not_a_self_number = d(i)
#     if not_a_self_number in all_numbers:
#         all_numbers.remove(not_a_self_number)

# for number in all_numbers:
#     print(number)




# list = []

# def d(n):
#     n = n+ n//10 + n%10
#     return n
    
# for i in range(1, 100):
#     if  d(i) < 100:
#         list.append(d(i))

# set_1 = set(list)

# list100 = []

# for i in range(1, 100):
#     list100.append(i)

# set_2 = set(list100)

# self_num = sorted(set_2 - set_1)

# for i in self_num:
#     print(i)



# #15596

# n = int(input())
# a = list(map(int, input().split()))

# def sum():
#     sum_all=0
#     for i in a:
#         sum_all +=i
#     return(sum_all)

# print(sum())

# #15596번 한줄 작성

# def solve(a):
#     return sum(a)