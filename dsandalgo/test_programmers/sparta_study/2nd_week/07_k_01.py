def solution(array, commands):
    answer = []
    # 1. array 를 i 에서 j 까지 자른다.    
    for i in commands:
        new = array[i[0]-1:i[1]]
        for j in range(len(new)):
            for k in range(j, len(new)):
                if new[j] > new[k]:
                    temp = new[j]
                    new[j] = new[k]
                    new[k] = temp

        answer.append(new[i[2]-1])
                        
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))