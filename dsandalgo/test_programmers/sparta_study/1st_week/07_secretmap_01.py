#zip 함수
#https://www.youtube.com/watch?v=GXlcx7H0GP4
#https://www.youtube.com/watch?v=BjJPjv_gcqA

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        # print(bin(a1))
        # print(bin(a2))
        # print(bin(a1|a2))
        a = str(bin(a1 | a2))[2:]
        a = '0' * (n-len(a)) + a
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        answer.append(a)
    return answer
        

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))