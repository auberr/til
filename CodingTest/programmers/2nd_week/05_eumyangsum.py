def solution(absolutes, signs):
    answer = 123456789
    sum = 0
    for i in range(len(signs)):
        print(signs[i])
        if signs[i] == True:
            sum+=absolutes[i]
        if signs[i] == False:
            sum-=absolutes[i]
            
    print(sum)
    return answer

solution([4,7,12], [True,False,True])
solution([1,2,3], [False,False,True])
