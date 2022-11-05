# 1110

N = int(input())
num = N
cycle = 0

while True:
    a = num % 10
    b = num // 10
    c = (a + b) % 10
    num = (a * 10) + c
    cycle= cycle+1

    if num == N:
        break

print(cycle)


    






# N = int(input())
# cyc = 1

# while True:
#     if N < 10:
#         A = 0
#         B = N %10
        

#         if A+B >= 10:
#             C= (A+B)%10
#             newN = B*10 +C
#             print(newN)
#             cyc=+1
#             print(cyc)

#             if newN == N:
#                 break


#         else :
#             C = A+B
#             newN = B * 10 + C
#             print(newN)
#             cyc=+1
#             print(cyc)


#             if newN == N:
#                 break


#     else:
#         A = N // 10
#         B = N %10

#         if A+B >= 10:
#             C= (A+B)%10
#             newN = B*10 +C
#             print(newN)
#             cyc=+1
#             print(cyc)
        

#         else :
#             C = A+B
#             newN = B * 10 + C
#             print(newN)
#             cyc=+1
#             print(cyc)

#             if newN == 68:
#                 print(newN)

        





# N =  str((int(str(N)[1]))) + str((int(str(N)[0])+int(str(N)[1])))

# print(N)



# 10951

# A, B = map(int, input().split())

# while True:
#     try:
#         C = A+B
#         print(C)
#         A, B = map(int, input().split())

#     except :
#         break
        





# # 10952 A + B - 5

# A, B = map(int, input().split())

# while True:
#     if int(A+B) == int(0):
#         break
#     else:
#         C = A+B
#         print(C)
#         A, B = map(int, input().split())





# 10871 X 보다 작은 수
# N, X = map(int, input().split())

# A = list(map(int, input().split()))

# result = str()

# for i in range(N):
#     if A[i] < X:
#         result = result+str(A[i])+' '

# print(result)


# #2439 별 찍기 - 2
# N = int(input())

# star = 0

# for i in range(N):
#     star = ' '*(N-i-1)+'*'*(i+1)
#     print(star)


# #2438 별 찍기 - 1
# N = int(input())

# star = 0

# for i in range(N):
#     star = '*'*(i+1)
#     print(star)


# 11022 A+B - 8
# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     print(f'Case #{i+1}: {a} + {b} = {a+b}')


# 11021 A+B - 7

# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     print(f'Case #{i+1}: {a+b}')



#15552 빠른 A+B

# t = int(input())

# for i in range(t):
#     a, b = map(int, input().split())
#     print(a+b)


# import sys

# sys.stdin.readline

# t = int(sys.stdin.readline())

# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)


#25304 영수증

# x = int(input())
# n = int(input())

# receipt = 0

# for i in range(n):
#     a, b = map(int, input().split())
#     receipt = receipt +a*b


# if receipt == x:
#     print('Yes')
# else:
#     print('No')
    



#8393 합

# n = int(input())

# result = 0

# for i in range(n+1):
#     result = result+i

# print(result)


#10950 A+B-3
# t = int(input())

# for i in range(t):
#     a, b = map(int, input().split())
#     print(a+b)




# #2739번 구구단

# a = int(input())

# for i in range(1, 10): print(f'{a} * {i} = {a * i}')

