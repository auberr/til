# 4344
C = int(input())

for _ in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt+=1
    rate = cnt/nums[0]*100
    print(f'{rate:.3f}%')




# 8958
# N = int(input())

# for _ in range(N):
#     score = 0
#     ox = list(input())
#     sum_score= 0

#     for i in ox:
#         if i == 'O':
#             score += 1
#             sum_score+= score
#         else:
#             score=0
    
#     print(sum_score)



# for i in ox:
    


# 1546
# N = int(input())
# nums = list(map(int, input().split()))
# max = max(nums)
# new_nums = []
# sum = 0

# for i in nums[0: ]:
#     new_nums.append(i/max*100)

# for i in new_nums:
#     sum = sum + i

# avg = sum/N
# print(avg)






# 3052
# nums = []

# for i in range(10):
#     num = int(input())
#     num42 = num%42
#     nums.append(num42)

# print(len(set(nums)))

#2562

# nums = []

# for i in range(9):
#     a = int(input())
#     nums.append(a)

#     max = nums[0]

#     for i in nums[0: ]:
#         if i > max:
#             max = i

#     max_index = nums.index(max)
    

# print(max)
# print(max_index+1)



# #10818

# N = int(input())
# nums = list(map(int, input().split()))

# max = nums[0]
# min = nums[0]

# for i in nums[0:]:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
    
# print(min, max)

    