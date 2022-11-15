def solution(n):
    answer = 0
    answer_list =[]
    for i in str(n):
        answer_list.append(int(i))
    print(answer_list)
    new_answer = []
    for i in answer_list:
        new_answer.append(i)
    print(new_answer)
    return answer

solution(118372)
