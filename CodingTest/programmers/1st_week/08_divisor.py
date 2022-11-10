def solution(left, right):
    answer = 0
    divisorsList = []
    divisorsList_plus = []
    divisorsList_minus = []

    between_num =[]
    for i in range(left, right+1):
        between_num.append(i)

    for j in between_num:
        divisorsList=[]
        for k in range(1, j+1):
            if j % k==0:
                divisorsList.append(k)
        if len(divisorsList)%2==0:
            divisorsList_plus.append(j)
        elif len(divisorsList)%2==1:
            divisorsList_minus.append(j)
    
    print(divisorsList_minus)
    print(divisorsList_plus)

    sum = 0
    for i in divisorsList_minus:
        sum-=i
    for i in divisorsList_plus:
        sum+=i
    answer=sum
    print(answer)



        # for j in between_num:
        #     for k in range(1, j+1):
        #         if k % 1 == 0:
        #             divisorsList.append(k)
        #     print(divisorsList)
        # if len(divisorsList) % 2 == 1:
        #     divisorsList_minus.append(j)
        # elif len(divisorsList) % 2 == 0:
        #     divisorsList_plus.append(j)


    # sum = 0
    # for i in divisorsList_plus:
    #     sum+=i

    # print(divisorsList_minus)
    # print(divisorsList_plus)

    # for i in divisorsList_minus:
    #     sum-=i

    # answer=sum
    # print(answer)
    # return answer

    


    # if left - right != 0:
    #     for i in range(1, left+1)
    # for i in range(1, left+1):
    #     if left % i == 0 :
    #         divisorsList_left.append(i)
    # for j in range(1, right+1):
    #     if right % j == 0:
    #         divisorsList_right.append(j)
    # print(divisorsList_left, divisorsList_right)
    # print(len(divisorsList_left), len(divisorsList_right))
    # if len(divisorsList_left) % 2 == 1 and len(divisorsList_right) % 2:


solution(13, 17)