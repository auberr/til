def solution(numbers):
    answer = 0
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in number_list:
        if i not in numbers:
            answer+=i
    return answer

print(solution([1,2,3,4,6,7,8,0]))

def solution(numbers):
    answer =0
    for i in range(1, 10):
        if i not in numbers:
            answer+=i
    return answer
print(solution([1,2,3,4,6,7,8,0]))

def solution(numbers):
    return sum([i for i in range(1, 10) if i not in numbers])

print(solution([1,2,3,4,6,7,8,0]))

def solution(numbers):
    return sum(range(1, 10)) - sum(numbers)

print(solution([1,2,3,4,6,7,8,0]))

solution  = lambda x: sum(range(10)) - sum(x)
print(solution([1,2,3,4,6,7,8,0]))