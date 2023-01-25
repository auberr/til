def solution(nums):
    

    def checkPrime(num):
        for j in range(2, num):
            if num % j == 0:
                return False
        return True

    answer = 0    

    sum=0
    number_set = set()
    # 1. 배열 에서 3개의 항목을 뽑는것
    for i in nums:
        sum+=i
        nums.pop(i)
        for j in nums:
            sum+=j
            nums.pop(j)
            for k in nums:
                sum+=k
                nums.pop(k)
                number_set.add(sum)
    
    print(number_set)

    for i in number_set:
        if checkPrime(i) == True:
            print(i, '이수는 소수')
            answer +=1
        
    
    # 2. 배열에서 뽑은 세개를 더해보는 것

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
