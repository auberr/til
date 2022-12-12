def solution(n):
    answer = 0
    n = list(str(n))
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] < n[j]:
                temp = n[j]
                n[j] = n[i]
                n[i] = temp
    print(n)
    a = ''
    a = a.join(n)
    print(a)
    answer=int(a)
    return answer

solution(118372)

