# def solution(left, right):
#     answer = 0
#     divisorsList = []
#     divisorsList_plus = []
#     divisorsList_minus = []

#     between_num =[]
#     for i in range(left, right+1):
#         between_num.append(i)

#     for j in between_num:
#         divisorsList=[]
#         for k in range(1, j+1):
#             if j % k==0:
#                 divisorsList.append(k)
#         if len(divisorsList)%2==0:
#             divisorsList_plus.append(j)
#         elif len(divisorsList)%2==1:
#             divisorsList_minus.append(j)
    
#     print(divisorsList_minus)
#     print(divisorsList_plus)

#     sum = 0
#     for i in divisorsList_minus:
#         sum-=i
#     for i in divisorsList_plus:
#         sum+=i
#     answer=sum
#     print(answer)



#         # for j in between_num:
#         #     for k in range(1, j+1):
#         #         if k % 1 == 0:
#         #             divisorsList.append(k)
#         #     print(divisorsList)
#         # if len(divisorsList) % 2 == 1:
#         #     divisorsList_minus.append(j)
#         # elif len(divisorsList) % 2 == 0:
#         #     divisorsList_plus.append(j)


#     # sum = 0
#     # for i in divisorsList_plus:
#     #     sum+=i

#     # print(divisorsList_minus)
#     # print(divisorsList_plus)

#     # for i in divisorsList_minus:
#     #     sum-=i

#     # answer=sum
#     # print(answer)
#     # return answer

    


#     # if left - right != 0:
#     #     for i in range(1, left+1)
#     # for i in range(1, left+1):
#     #     if left % i == 0 :
#     #         divisorsList_left.append(i)
#     # for j in range(1, right+1):
#     #     if right % j == 0:
#     #         divisorsList_right.append(j)
#     # print(divisorsList_left, divisorsList_right)
#     # print(len(divisorsList_left), len(divisorsList_right))
#     # if len(divisorsList_left) % 2 == 1 and len(divisorsList_right) % 2:


# solution(13, 17)


# # cnt = 0 
# # a = 4
# # for i in range(1, a+1):
# #     if a % i == 0 :
# #         cnt += 1
# # print(cnt)

# # cnt = 0
# # a = 4
# # for i in range(1, a+1):
# #     if a % i == 0:
# #         cnt+=1
# #     print("약수 개수", cnt)

# def solution(left, right):
#     answer = 0
#     for num in range(left, right+1):
#         cnt=0
#         for i in range(1, num+1):
#             if num % i == 0:
#                 cnt+=1
#         if cnt % 2 == 0:
#             answer += num
#         else :
#             answer -= num
#     return answer


# left 와 right 에 두 숫자가 주어진다.
# 단 left < right 
# left와 right 사이의 평균을 영문으로 바꾼 함수를 만들어라.(단 소숫점 무시)

def solution(left, right):
    answer = 0
    sum = 0
    for num in range(left, right+1):
        sum+=num
    print(sum)
    avg = int(sum / (right-left+1))
    print(avg)
    print(str(avg))
    
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    new_avg = str(avg)
    for i in arr:
        new_avg = new_avg.replace(str(arr.index(i)), i)
    print(new_avg)

solution(2, 5)
