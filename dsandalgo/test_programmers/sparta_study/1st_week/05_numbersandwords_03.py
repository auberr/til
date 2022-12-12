def solution(s):
    answer = s
    num_list = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for i in num_list:
        if i in s:
            answer = answer.replace(i, num_list[i])
    return int(answer)

# def solution(s):
#     answer = 0
#     num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     answer = str(s)
#     for i in num_list:
#         if i in s:
#             print(i)
#             print(str(num_list.index(i)))
#             answer = answer.replace(i, str(num_list.index(i)))
#     return answer

print(solution("one4seveneight"))

