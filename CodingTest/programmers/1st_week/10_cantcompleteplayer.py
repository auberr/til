def solution(participant, completion):
    answer = ''
    for i in completion:        
        participant.remove(i)
    answer = participant[0]
    return answer


# def solution(participant, completion):
#     answer = ''
#     for i in completion:
#         participant.remove(i)
#     answer = participant[0]
#     return answer

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])


# def solution(participant, completion):
#     answer = ''
#     for i in participant:
#         if i not in completion:
#             answer = i

#         elif i in completion:
#             if completion == []:
#                 answer = i
#             else:
#                 completion.remove(i)          
#     return answer

# solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

# solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])