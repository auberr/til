def solution(denum1, num1, denum2, num2):
    answer = []
    # 1. 분모끼리 곱하고 해서 더함
    bunja = denum1 * num2 + denum2 * num1
    bunmo = num1 * num2
    # 2. 분모 분자 최대 공약수를 구함
    if bunja > bunmo:
        min = bunmo
    else:
        min = bunja
        
    for i in range(min, 0, -1):
        if bunja % i == 0 and bunmo % i == 0:
            gcd = i
            break
        
    # 3. 분모 분자를 최대 공약수로 나눔
    bunja = int(bunja / gcd)
    bunmo = int(bunmo / gcd)

    # 4. 분자, 분모를 answer 배열에 담아줌
    answer.append(bunja)
    answer.append(bunmo)
    
    return answer

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))


