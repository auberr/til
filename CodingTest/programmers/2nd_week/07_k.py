def solution(array, commands):
    answer = []
    a = array[commands[0][0]-1:commands[0][1]]
    # for i in range(len(a)-1):
    #     for j in range(i, len(a)):
    #         if a[i] > a[j]:
    #             temp = a[i]
    #             a[i] = a[j]
    #             a[j] = temp
    # print(a[commands[0][2]-1])

    # b = array[commands[1][0]-1:commands[1][1]]
    # for i in range(len(b)-1):
    #     for j in range(i, len(b)):
    #         if b[i] > b[j]:
    #             temp = b[i]
    #             b[i] = b[j]
    #             b[j] = temp
    # print(b[commands[1][2]-1])

    for i in range(len(commands)):
        a = array[commands[i][0]-1:commands[i][1]]
        print(a)
        for j in range(len(a)-1):
            for k in range(j, len(a)):
                if a[j] > a[k]:
                    temp = a[j]
                    a[j] = a[k]
                    a[k] = temp
        
        answer.append(a[commands[i][2]-1])
    
    print(answer)

            
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
