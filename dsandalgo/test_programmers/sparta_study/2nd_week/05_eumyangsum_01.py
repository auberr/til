def solution(absolutes, signs):
    answer = 0
    for num in range(len(absolutes)):
        if signs[num] is True:
            answer+=absolutes[num]
        elif signs[num] is False:
            answer-=absolutes[num]
    return answer

print(solution([4,7,12], [True,False,True]))