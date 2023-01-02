# 재귀 (recursive)
# 자기 자신을 호출 하는 것

## 재귀 함수 (recursive function)
## 자기 자신을 호출하는 함수

arr =[7, 3, 2, 9]

def sum(arr, accu):
    if (len(arr) == 0): return accu
    return sum(arr, accu + arr.pop())

result = sum(arr, 0)
print('result =>', result)

# n = int(input())
# def factorial(n):
#     if n <=1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(n))
# print(factorial(10))