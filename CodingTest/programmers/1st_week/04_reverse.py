def solution(n):
    answer = []
    n_list = n.split()
    print(answer)
    for i in range(len(n)):
        answer.insert(0, n_list[0][i])
        print(answer)
    return answer

solution('12345')