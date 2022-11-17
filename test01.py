import queue

data = queue.Queue()
print(type(data))

data.put(2)
data.put(5)
data.put(8)

print(data.get())
print(data.get())
print(data.get())

from collections import deque

#deque 생성
queue = deque()

#append # 오른쪽에 데이터 추가

queue.append(3) # deque([3])
queue.append(5) # deque([3, 5])
queue.append(7) # deque([3, 5, 7])

# appendleft # 왼쪽에 데이터 추가
queue.appendleft(2) # deque([2, 3, 5, 7])
queue.appendleft(4) # deque([4, 2, 3, 5, 7])

# pop 
# 오른쪽에서 데이터 삭제
queue.pop() # 7
queue.pop() # 5

# popleft # 왼쪽에서 데이터 삭제
queue.popleft() #4
queue.popleft() #2

queue # deque([3])

print(queue)


# stack = []

# stack.append(2)
# stack.append(5)
# stack.append(8)

# print("stack:", stack)

# print("첫번째 pop")
# print(stack.pop())
# print(stack)

# print(len('1234425'))

# super = 'supermanman'

# print(super[0])

# def solution(my_string):
#     answer=''
#     for i in my_string:
#         if i.isupper() == True:
#             answer+=i.lower()
#         if i.islower() == True:
#             answer+=i.upper()
#     print(answer)
#     return answer


# solution("cccCCC")


# def solution(my_string):
#     answer = ''
#     nonelist =[]
#     for i in range(len(my_string)):
#         nonelist.append(my_string[i])
#     print(nonelist)
#     newlist = []
#     for i in nonelist:
#         if i.isupper() == True:
#             newlist.append(i.lower())
#         if i.islower() == True:
#             newlist.append(i.upper())
#     print(newlist)
#     for i in newlist:
#         answer+=i
#     print(answer)
#     return answer

# solution("cccCCC")

# def solution(mylist):
#     answer = mylist[0]
#     list=[]
#     for i in mylist:
#         list.append(len(i))
#     print(list)
#     return answer

# mylist = [[1, 2], [3, 4], [5]]

# solution(mylist)


# def solution(denum1, num1, denum2, num2):
#     answer = []
#     if num1 < num2:
#         if num2 % num1 == 0:
#             answer = [denum1*(num2//num1)+denum2, num2]
#         elif num2 % num1 !=0:
#             answer = [denum1*num2+denum2*num1, num2*num1]

#     if num1 > num2:
#         if num1 % num2 == 0:
#             answer = [denum2*(num1//num2)+denum1, num1]
#         elif num1 % num2 !=0:
#             answer = [denum2*num1+denum1*num2, num1*num2]

#     print(answer)
#     return answer

# solution(10,3,5,6)

