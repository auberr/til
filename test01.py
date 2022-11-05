def solution(mylist):
    answer = mylist[0]
    list=[]
    for i in mylist:
        list.append(len(i))
    print(list)
    return answer

mylist = [[1, 2], [3, 4], [5]]

solution(mylist)


# def solution(denum1, num1, denum2, num2):
#     answer = []
#     if num1 < num2:
#         if num2 % num1 == 0:
#             answer = [denum1*(num2//num1)+denum2, num2]
#         elif num2 % num1 !=0:
#             answer = [denum1*num2+denum2*num1, num2*num1]

#     if num1 > num2:
#         if num1 % num2 == 0:
#             answer = [denum2*(num1//num2)+denum1, num1]
#         elif num1 % num2 !=0:
#             answer = [denum2*num1+denum1*num2, num1*num2]

#     print(answer)
#     return answer

# solution(10,3,5,6)

