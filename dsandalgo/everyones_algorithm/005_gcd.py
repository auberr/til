# def gcd(a, b):
#     cd_list = []
#     if a > b:
#         for i in range(b+1, 2, -1):
#             if a % i == 0 and b % i ==0:
#                 return i
#     elif a < b:
#         for i in range(a+1, 2, -1):
#             if a % i == 0 and b % i ==0:
#                 return i

# print(gcd(5, 15))


# def gcd(a, b):
#     cd_list = []
#     if a > b:
#         for i in range(2, b+1):
#             if a % i == 0 and b % i ==0:
#                 cd_list.append(i)
#     elif a < b:
#         for i in range(2, a+1):
#             if a % i == 0 and b % i ==0:
#                 cd_list.append(i)

#     return max(cd_list)

# print(gcd(5, 15))


# def gcd2(a, b):
#     i = min(a, b)
#     while True:
#         if a % i and b % i ==0:
#             return i
#         i = i-1

def fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))

