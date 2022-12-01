list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

my_function = lambda a, b: a+b
result = map(my_function, list1, list2)
print(list(result))


add = lambda x, y : x + y
print(add(1,2))

product_xy = []
for x in [1, 2, 3]:
    for y in [2, 4, 6]:
        product_xy.append(x * y)
print(product_xy)
        
product_xy = [x * y for x in [1, 2, 3] for y in [2, 4, 6]]
print(product_xy)

[n for n in range(1, 31)
 if n % 2 ==0 
 if n % 5 ==0]

[x for x in range(10)]

[x * x for x in range(10)]

[x for x in range(10) if x % 2 == 0]

[x for x in range(10) if x % 2 == 1]

[x for x in range(10) if x % 2 == 0]

[x for x in range(10) if x % 2 == 1]

ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x>=19, ages))
print('성년 리스트:', adult_ages)

ages = [34, 39, 20, 18, 13, 54]
print('성년 리스트:', [x for x in ages if x >= 19])



# print(range(10))
# print(list(range(10)))

# print([x for x in range(10)])

# print([x+10 for x in range(10)])

# a = [1,2,3,4,5,6,7]
# a = list(map(lambda x: x**2, a))
# print(a)

# a = [1,2,3,4,5,6,7]
# a = [x**2 for x in a]
# print(a)

# a = [x**2 for x in range(1,8)]
# print(a)


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

