def solution(n):
    a = [x for x in range(1, n+1) if n% x == 1][0]
    return a


print(solution(10))
print(solution(12))


def solution(n):
    answer = 0
    x = []
    for i in range(1, n):
        if n % i == 1:
            x.append(i)
    
    answer = x[0]

    return answer
