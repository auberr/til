# 최소 공배수 (Least Common Mutliple)
def lcm(a, b):
    for i in range(max(a, b), a*b+1):
        if i % a == 0 and i % b == 0:
            return i

a, b = 8, 12

import math
math.lcm(a, b)


# 최대 공약수 (Greatest Common Divisor)
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

a, b = 8, 12

import math
math.gcd(a, b)

# num= int(input("수?"))

# for i in range(1, num+1):
#     if num % i == 0:
#         # 약수임
#         print(i, end=' ')


# def getMyDivisor(n):
#     divisorsList = []
#     for i in range(1, int(n**1/2) +1):
#         if (n % i == 0):
#             divisorsList.append(i)
#             if ((i**2) != n):
#                 divisorsList.append( n // i)
    
#     divisorsList.sort()
#     return divisorsList

# def get_division(n):
#     data = []
    
#     for i in range(1, n+1):
#         if n % i == 0:
#             data.append(i)
#     return data

# print(get_division(8))


# def get_division(n):
#     data = []
    
#     for i in range(1, n //2 +1):
#         if n % i == 0:
#             data.append(i)
#     data.append(n)
#     return data

# print(get_division(8))


# def get_division(n):
#     front = []
#     back = []
    
#     for i in range(1, int(n** (1/2))+1):
#         if n % i  == 0:
#             front.append(i)
#             if i != n//i:
#                 back.append(n//i)
#     return front+back[::-1]

# print(get_division(8))

