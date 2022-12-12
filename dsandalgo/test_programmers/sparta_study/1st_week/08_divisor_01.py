def solution(left, right):
    answer = 0
    divisor = []
    divisor_left = []
    for j in range(2, left+1):
        for k in range(2, j):
            print(j, k)
            if j % k == 0:
                divisor_left.append(k)
        
    print(divisor_left)
        
    
    for i in range(left, right+1):
        pass
    return answer

print(solution(13, 17))