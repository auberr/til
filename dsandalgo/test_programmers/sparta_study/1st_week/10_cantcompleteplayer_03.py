def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant)-1]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])

solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])