def solution(n):
    answer = 0
    n = list(str(n))
    # 정수를 배열로
    for i in range(0, len(n)): # 0에서 5까지
        for j in range(i, len(n)):
            if n[i] < n[j]:
                temp = n[i]
                n[i] = n[j]
                n[j] = temp

            print(f"{i}번 반복{n}")
    return answer
solution(118372)


# def solution(n):
#     answer = 0
#     answer_list =[]
#     for i in str(n):
#         answer_list.append(int(i))
#     print(answer_list)
#     new_answer = []
#     for i in answer_list:
#         new_answer.append(i)
#     print(new_answer)
#     return answer

# solution(118372)
