def solution(n):
    answer = []
    n_list = str(n).split()
    print(n_list)
    for i in range(len(str(n))):
        answer.insert(0, int(n_list[0][i]))
    return answer

solution(12345)