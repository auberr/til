def solution(a, b):
    answer = 0
    if a == b :
        answer = a
    elif a < b:
        for i in range(a, b+1):
            answer+=i
    elif a > b:
        for i in range(b, a+1):
            answer+=i
    return answer

solution(3, 5)

a = 5
b = 1
print(range(a, b+1))
print(type(range(a, b+1)))