def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == a[i]:
            count[0] += 1
        elif answers[i] == b[i]:
            count[1] += 1
        elif answers[i] == c[i]:
            count[2] += 1 
    
    print(count)

    max = 0

    for i in range(len(count)):
        if count[i] > max:
            max = count[i]
            higher = i
    
    print(max)
    

    return answer


solution([1,2,3,4,5])
solution([1,3,2,4,2])