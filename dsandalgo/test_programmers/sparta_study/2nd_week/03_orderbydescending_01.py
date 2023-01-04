def solution(n):
    answer = 0
    list_n = []
    for i in str(n):
        list_n.append(i)
    
    for i in range(len(list_n)):
        for j in range(i, len(list_n)):
            if int(list_n[i]) < int(list_n[j]):
                temp = list_n[i]
                list_n[i] = list_n[j]
                list_n[j] = temp

    num1 = ''.join(list_n)

    answer = int(num1)
    return answer

solution(118372)