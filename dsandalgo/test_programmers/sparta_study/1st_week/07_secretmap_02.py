def solution(n, arr1, arr2):
    answer = []
    sum = []
    for i in range(n):
        sum.append(bin(arr1[i]|arr2[i])[2:])
    
    new_sum = []
    for i in sum:
        i = i.replace('1', '#')
        i = i.replace('0', ' ')
        new_sum.append(i)

    print(new_sum)
    answer = new_sum
    return answer



print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))