# def solution(participant, completion):
#     answer = ''
#     for i in completion:        
#         participant.remove(i)
#     answer = participant[0]
#     return answer


# def solution(participant, completion):
#     answer = ''
#     for i in completion:
#         participant.remove(i)
#     answer = participant[0]
#     return answer

def solution(participant, completion):
    temp  = {}
    for i in participant:
        if i in temp:
            temp[i]+=1
        else:
            temp[i]=1
    for i in completion:
        if temp[i]==1:
            del temp[i]
        else:
            temp[i] -=1
    return list(temp.keys())[0]


import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))


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

a = 'a'
b = 'b'
c = 'c'
d = 'a'

print(hash(a))
print(hash(b))
print(hash(c))
print(hash(d))