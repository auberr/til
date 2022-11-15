def solution(n, arr1, arr2):
    answer = []
    return answer


# format(숫자, 'b')

# print(bin(1))
# print(bin(1)[2:])
# print(bin(1)[2:].zfill(3))


def solution(n, arr1, arr2):
    answer = []
    # arr1 = [9, 20, 28, 18, 11]
    # arr2 = [30, 1, 21, 17, 28]
    # n= 5

    answer = [''] *n
    print(answer)
    for i in range(len(arr1)):
        bin1 = bin(arr1[i])[2:].zfill(n)
        bin2 = bin(arr2[i])[2:].zfill(n)    
        # print(bin1)
        # print(bin2)
        for j in range(n):
            # or 연산하기
            # 모두 0 일때 말고는 다 1
            if bin1[j] == '0' and bin2[j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'
    print(answer)

    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])

# def solution1(n, arr1, arr2):
#     answer = ['']*n
#     for i in range(len(arr1)):
#         bin1 = bin(arr1[i])[2:].zfill(n)
#         bin2 = bin(arr2[i])[2:].zfill(n)
#         for j in range(n):
#             if bin1[j] == '0' and bin2[j] == '0':
#                 answer[i] += ' '
#             else:
#                 answer[i] += '#'
#     return answer
# solution1(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
