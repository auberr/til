arr = [1,2,3,4,5]
print(arr[-1])


def sum_square(n):
    answer = 0
    for i in range(1, n+1):
        answer += i*i
    return answer

print(sum_square(10))

def sum_n(n):
    return n * (n+1) // 2

print(sum_n(10))
print(sum_n(100))

def sums(n):
    answer = 0
    for i in range(1, n+1):
        answer+=i
    return answer

print(sums(10))