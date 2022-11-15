def solution(n):
    answer = 0
    minimum = n
    for i in range(1, n):
        if n % i == 1:
            if i < minimum:
                minimum = i
    answer = minimum
    return answer


solution(12)