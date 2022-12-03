#1157

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input().upper()

max_alphabet = ''
max_count = 0

for alphabet in alphabets:
    n = word.count(alphabet)
    if n > max_count:
        max_count = n
        max_alphabet = alphabet
    elif n == max_count:
        max_alphabet = '?'
    else:
        continue

print(max_alphabet)
    



# 10809번

# alphabets = 'abcdefghijklmnopqrstuvwxyz'

# word = input()

# for alphabet in alphabets:
#     try:
#         print(word.index(alphabet), end=' ')
#     except:
#         print('-1', end=' ')


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


# # 4344

# T = int(input())

# for _ in range(T):
#     scores = list(map(int, input().split()))
#     sum_score = 0
#     num_people = scores[0]
#     for i in range(1, num_people+1):
#         sum_score += scores[i]
#     avg_score = sum_score / num_people

#     above_avg = 0
#     for i in range(1, num_people+1):
#         if scores[i] > avg_score:
#             above_avg += 1
    
#     print(f"{above_avg/num_people*100:.3f}%")


# # 다른 풀이 방법

# T = int(input())

# for _ in range(T):
#     scores = list(map(int, input().split()))
#     num_people = scores.pop(0)
#     avg_score = sum(scores) / num_people

#     above_avg = 0
#     for i in range(num_people):
#         if scores[i] > avg_score:
#             above_avg += 1

#     print(f"{above_avg/num_people*100:.3f}%")

# # pop_tutorial

# my_list = ['뭐', '이런','값들이', '있습니다']

# my_list.pop()
# my_list.pop()
# my_list.pop()
# print(my_list)


# # 8958

# T = int(input())

# for _ in range(T):
#     answers = input()
#     total_score = 0
#     point = 1
#     for answer in answers:
#         if answers == 'O':
#             total_score += point
#             point += 1
#         else:
#             point = 1
#     print(total_score)



# 2562

# num_list = []

# for i in range(9):
#     num_list.append(int(input()))

#     max_num = max(num_list)
#     index = num_list.index(max_num)


# print(max_num)
# print(index+1)

# # 1110
# original_num = input()

# if len(original_num) == 1:
#     original_num = "0" + original_num

# current_num = original_num
# count = 0
# while True:
#     sum_num = int(current_num[0]) + int(current_num[1])
#     sum_num = str(sum_num)
#     current_num = current_num[-1] + sum_num[-1]
#     count += 1
#     if current_num == original_num:
#         print(count)
#         break

# 15552 

# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     A, B = map(int, sys.stdin.readline().split())
#     print(A+B)


# ######오류 ##########

# T = int(input())

# for _ in range(T):
#     A, B = map(int, input().split())
#     print(A+B)


# # 10871 X 보다 작은 수

# N, X = map(int, input().split())

# my_list = list(map(int, input().split()))

# for number in my_list:
#     if number < X:
#         print(number, end=' ')


# # 다른 방법 - 공백이 없음 #
# #########################

# result_list = []
# for number in my_list:
#     if number < X:
#         result_list.append(str(number))

# print(' '.join(result_list))


# ####################