from collections import Counter
def solution(partipant, completion):
    # 1. particpant 의 count를 구한다.
    part_counter = Counter(partipant)
    print(type(part_counter))
    print(part_counter)
    # 2. completion 의 count를 구한다.
    comp_counter = Counter(completion)
    
    # 3. 둘의 차를 구하고, key를 읽어온다.
    answer = part_counter - comp_counter
    print(answer)
    print(answer.keys())
    print(list(answer.keys()))
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    #1. participant list 의 hash 를 구하고 hash 값을 더한다
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    print(hashDict)
    print(sumHash)
    # 2. completion list의 hash를 빼준다.
    for comp in completion:
        sumHash -= hash(comp)
    
    print(sumHash)
    print(hashDict[sumHash])
    return 

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))



def solution(participant, completion):
    # 1. 두 리스트를 sorting
    participant.sort()
    completion.sort()
    
    # 2. completion list의 length 만큼 돌면서 particpatn 를 비교
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    # 3. 다 돌아도 없을 경우에는 마지막 주자
    return participant[len(participant)- 1]
    
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])

