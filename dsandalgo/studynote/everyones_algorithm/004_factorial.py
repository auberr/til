def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(factorial(10))
print(factorial(5))

def fact(n):
    if n <=1:
        return 1
    return n * fact(n-1)

print(fact(10))
print(fact(5))

def sum_recur(n):
    if n <= 1:
        return 1
    return n + sum_recur(n-1)

print(sum_recur(10))


# def find_max_idx(a):
#     n = len(a)-1
#     max_idx = 0
#     if a[n] > a[n-1]:
#         max_idx = a[n]
#         return find_max_idx(a-1)
#     elif a[n-1] < a[n]:
#         max_idx = a[n-1]
#         return find_max_idx(a-1)
#     return find_max_idx(a-1)

# v = [17, 92, 18, 33, 58, 7, 33 ,42]
# print(find_max_idx(v))

def find_max(a, n):
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]
    
v = [17, 92, 18, 33, 58, 7, 33 ,42]
print(find_max(v, len(v)))